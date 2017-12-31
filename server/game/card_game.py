from typing import Optional

from framework.game import *
import network.protocol_tools as proto
from utils import set_interval

from game.effects import EffectHandler
from game.rules import *
from game.states import *
from game.target_filters import *


__all__ = ['CardGame', ]


class CardGame(GameBase):
    def __init__(self, player_a: Player, player_b: Player):
        super().__init__(players=[player_a, player_b])

        self.player_a = player_a
        self.player_b = player_b
        self.player_a_entity = PlayerEntityState(proto.Side.A, self.player_a.queue_args)
        self.player_b_entity = PlayerEntityState(proto.Side.B, self.player_b.queue_args)

        self.objects = []  # type: List[EntityState]
        self.board_size = BOARD_SIZE
        self.effect_handler = EffectHandler(self)
        self._last_entity_id = 1

        self.cheats_enabled = True

    def begin(self):
        super().begin()
        set_interval(1, self.draw_initial_cards)
        set_interval(3, self.start_round)

    def draw_initial_cards(self):
        for i in range(INITIAL_CARDS):
            self.effect_handler.draw_card(None, self.player_a_entity)
            self.effect_handler.draw_card(None, self.player_b_entity)

    def on_player_message(self, player: Player, message: proto.Message):
        if player is self.player_a:
            self.on_game_message(message, self.player_a_entity)
        elif player is self.player_a:
            self.on_game_message(message, self.player_b_entity)

    def on_game_message(self, message: proto.Message, player_entity: PlayerEntityState):
        try:
            if message.head == proto.Head.CLI_GAME_ACTION:
                if self.turn != player_entity.side:
                    raise GameError('Not your turn')

                action = proto.get_message_body(message).action
                if action is None:
                    raise GameError('Cannot interpret game action')
                else:
                    self.do_player_action(player_entity, action)
            else:
                raise GameError('Not-action game message')
        except GameError as err:
            msg = 'Game error: {0}'.format(err)
            self.logger.warning(msg)
            self.notify_entity(player_entity, proto.Head.SRV_ERROR, status=msg)

    def do_player_action(self, player_entity: PlayerEntityState, action: dict):
        action_type = PlayerActionType(action['type'])
        if action_type == PlayerActionType.PLAY_CARD:
            self.play_card(player_entity, action['card'])
        elif action_type == PlayerActionType.FIRE_WEAPON:
            self.fire_weapon(player_entity)
        elif action_type == PlayerActionType.END_TURN:
            self.player_end_turn(player_entity)
        elif action_type == PlayerActionType.CHEAT_TAKE_CARD:
            if self.cheats_enabled:
                self.effect_handler.gain_card(None, player_entity, action['card'])
            else:
                raise GameError('Cheating: {0}'.format(action))
        else:
            raise GameError('Unknown action: {0}'.format(action))

    def play_card(self, player_state: PlayerEntityState, card_name: str):
        if player_state.muted:
            raise GameError('You are muted')

        card = get_card(card_name)
        card_state = player_state.get_card_in_hand(card_name, None)
        if card_state is None:
            raise GameError('Card is not in hand: {0}'.format(card_name))
        if self.is_offense(player_state):
            card_action = card.get(Card.ACTION_OFFENSE, card.get(Card.ACTION_SAME, None))
            cost = card_state.cost_offense
        else:
            card_action = card.get(Card.ACTION_DEFENSE, card.get(Card.ACTION_SAME, None))
            cost = card_state.cost_defense
        if card_action is None:
            raise GameError('Card does not have any actions: {0}'.format(card_name))
        if cost > player_state.energy:
            raise GameError('Not enough energy to play card: {0}'.format(card_name))

        # Play card
        self.effect_handler.remove_card(None, player_state, card_name)
        self.effect_handler.energy_damage(None, player_state, cost)
        self.effect_handler.apply_effects(player_state, card_action.get(Card.EFFECTS, []))
        self.invoke_case(player_state, CaseType.PLAY_CARD, card_name)

    def fire_weapon(self, player_state: PlayerEntityState):
        if not player_state.armed:
            raise GameError('You are not armed')

        w = get_weapon(player_state.weapon_name)
        if self.is_offense(player_state):
            w_action = w.get(Weapon.ACTION_OFFENSE, w.get(Weapon.ACTION_SAME, None))
        else:
            w_action = w.get(Weapon.ACTION_DEFENSE, w.get(Weapon.ACTION_SAME, None))
        if w_action is None:
            raise GameError('Weapon does not have actions: {0}'.format(player_state.weapon_name))
        cost = w_action.get(Weapon.COST, 0)
        if cost > player_state.energy:
            raise GameError('Not enough energy to shoot: {0}'.format(player_state.weapon_name))
        self.effect_handler.energy_damage(None, player_state, cost)
        self.effect_handler.apply_effects(player_state, w_action.get(Weapon.EFFECTS, []))

    def player_end_turn(self, player_state: PlayerEntityState):
        if self.turn == proto.Side.B:
            self.end_round()
        self.end_turn()
        if self.turn == proto.Side.A:
            self.start_round()

    def end_round(self):
        self.invoke_case_global(CaseType.ROUND_END)

        # Process buffs
        for entity_state in self.get_all_entities():
            for buff in entity_state.buffs:
                buff.duration -= 1
                if buff.duration <= 0:
                    self.effect_handler.remove_buff(None, entity_state, buff.name)
                else:
                    buff = get_buff(buff.name)
                    self.effect_handler.apply_effects(entity_state, buff.get(Buff.ON_ROUND_EFFECTS, []))

        self.effect_handler.draw_card(None, self.player_a_entity)
        self.effect_handler.draw_card(None, self.player_b_entity)

    def start_round(self):
        self.invoke_case_global(CaseType.ROUND_START)

        # Process energy
        for entity_state in self.get_all_entities():
            self.effect_handler.energy_heal(None, entity_state, entity_state.energy_gain)
            if entity_state.energy > entity_state.max_energy:
                entity_state.energy = entity_state.max_energy
                self.effect_handler.damage(None, entity_state, 1)
                self.invoke_case(entity_state, CaseType.OVERLOAD, entity_state.name)

    def invoke_case_global(self, case: CaseType, arg=None):
        for e in self.get_all_entities():  # type: EntityState
            self.invoke_case(e, case, arg)

    def invoke_case(self, target_entity: EntityState, case: CaseType, arg=None):
        # Cases in buffs
        for b in target_entity.buffs:
            buff = get_buff(b.name)
            cases = buff.get(Buff.CASES, {})
            case = cases.get(case, None)
            if case is None:
                continue
            case_arg = case.get(Case.ARG, None)
            if case_arg is None or case_arg == arg:
                self.effect_handler.apply_effects(target_entity, case.get(Case.EFFECTS, []))

        # Cases in objects
        if not self.is_player(target_entity):
            obj = get_object(target_entity.name)
            cases = obj.get(Entity.CASES, {})
            case = cases.get(case, None)
            if case is None:
                return
            case_arg = case.get(Case.ARG, None)
            if case_arg is None or case_arg == arg:
                self.effect_handler.apply_effects(target_entity, case.get(Case.EFFECTS, []))

    def is_offense(self, entity: EntityState) -> Optional[bool]:
        if not self.is_player(entity):
            return None

        if entity == self.player_a_entity:
            return self.player_a_entity.position < self.player_b_entity.position
        else:
            return self.player_b_entity.position < self.player_a_entity.position

    def get_enemy_ship(self, entity: EntityState) -> Optional[EntityState]:
        if entity.side == proto.Side.A:
            return self.player_b_entity
        if entity.side == proto.Side.B:
            return self.player_a_entity
        return None

    def get_targets(self, entity: EntityState, target: str, target_range: int=10) -> List[EntityState]:
        es = self.get_targets_no_range(entity, target)
        return filter_position_range(es, entity.position - target_range, entity.position + target_range)

    def get_targets_no_range(self, entity: EntityState, target: str) -> List[EntityState]:
        if target == Target.SELF:
            return [entity, ]

        if target == Target.ALL:
            return self.get_all_entities()

        if target == Target.ALL_EXCEPT_SELF:
            return filter_exclude(self.get_all_entities(), entity)

        if target == Target.ALL_ENEMIES:
            return filter_enemy(self.get_all_entities(), entity)

        if target == Target.ALL_ALLIES:
            return filter_ally(self.get_all_entities(), entity)

        if target == Target.ALL_SHIPS:
            return filter_ship(self.get_all_entities())

        if target == Target.ENEMY_SHIP:
            return filter_enemy(filter_ship(self.get_all_entities()), entity)

        if target == Target.ALLY_SHIP:
            return filter_ally(filter_ship(self.get_all_entities()), entity)

        if target == Target.FORWARD:
            return filter_direction(self.get_all_entities(),
                                    entity.position + 1,
                                    direction=+1, pierce=False)

        if target == Target.FORWARD_ALLY:
            return filter_direction(filter_ally(self.get_all_entities(), entity),
                                    entity.position + 1,
                                    direction=+1, pierce=False)

        if target == Target.FORWARD_ENEMY:
            return filter_direction(filter_enemy(self.get_all_entities(), entity),
                                    entity.position + 1,
                                    direction=+1, pierce=False)

        if target == Target.FORWARD_PIERCE:
            return filter_direction(self.get_all_entities(),
                                    entity.position - 1,
                                    direction=-1, pierce=True)

        if target == Target.BACKWARD:
            return filter_direction(self.get_all_entities(),
                                    entity.position - 1,
                                    direction=-1, pierce=False)

        if target == Target.BACKWARD_ALLY:
            return filter_direction(filter_ally(self.get_all_entities(), entity),
                                    entity.position - 1,
                                    direction=-1, pierce=False)

        if target == Target.BACKWARD_ENEMY:
            return filter_direction(filter_enemy(self.get_all_entities(), entity),
                                    entity.position - 1,
                                    direction=-1, pierce=False)

        if target == Target.BACKWARD_PIERCE:
            return filter_direction(self.get_all_entities(),
                                    entity.position - 1,
                                    direction=-1, pierce=True)

        if target == Target.MAX_ENERGY:
            enemy = self.get_enemy_ship(entity)
            if enemy is None:
                return []
            if enemy.energy > entity.energy:
                return [enemy, ]
            else:
                return [entity, ]

        if target == Target.MAX_HEALTH:
            enemy = self.get_enemy_ship(entity)
            if enemy is None:
                return []
            if enemy.hp > entity.hp:
                return [enemy, ]
            else:
                return [entity, ]

        if target == Target.MIN_HEALTH:
            enemy = self.get_enemy_ship(entity)
            if enemy is None:
                return []
            if enemy.hp < entity.hp:
                return [enemy, ]
            else:
                return [entity, ]

        raise GameError('Unknown target: {0}'.format(target))

    def get_entities_at(self, position: int):
        return filter_position(self.get_all_entities(), position)

    def get_all_entities(self) -> List[EntityState]:
        return [self.player_a_entity, self.player_b_entity] + self.objects

    def get_state(self, perspective_player: Player=None) -> proto.GameState:
        hide_hand_a = perspective_player != self.player_a
        hide_hand_b = perspective_player != self.player_b

        state = {
            #Side.A: self.get_player_state(self.player_a, hide_hand=hide_hand_a),
            #Side.B: self.get_player_state(self.player_b, hide_hand=hide_hand_b),
            GameStateProtocol.OBJECTS: [s.get_state() for s in self.objects],
            GameStateProtocol.TURN: self.turn,
        }
        return state

    def get_player_state(self, player: Player, hide_hand: bool=False) -> dict:
        if player == self.player_a:
            return self.player_a_entity.get_state(hide_hand=hide_hand)
        if player == self.player_b:
            return self.player_b_entity.get_state(hide_hand=hide_hand)
        return {}

    def is_player(self, entity: EntityState) -> bool:
        if entity == self.player_a_entity:
            return True
        if entity == self.player_b_entity:
            return True
        return False

    def notify_entity(self, entity: EntityState, *args, **kwargs):
        if entity is None:
            self.notify_players(*args, **kwargs)
            return

        if entity == self.player_a_entity:
            self.notify_player(self.player_a, *args, **kwargs)

        if entity == self.player_b_entity:
            self.notify_player(self.player_b, *args, **kwargs)
