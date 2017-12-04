from typing import List, Dict

from protocol import *
from rules import *
from game_base import *
from game_states import *
from game_effects import EffectHandler

from utils import set_interval


class CardGame(GameBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.player_a_entity = PlayerState(SIDE_A, self.player_a.args)
        self.player_b_entity = PlayerState(SIDE_B, self.player_b.args)

        self.objects = []  # type: List[EntityState]
        self.board_size = BOARD_SIZE
        self.effect_handler = EffectHandler(self)
        self._last_entity_id = 1

    def begin(self):
        super().begin()
        set_interval(1, self.draw_initial_cards)
        set_interval(4, self.start_round)

    def draw_initial_cards(self):
        for i in range(INITIAL_CARDS):
            self.effect_handler.effect_draw_card(self.player_a_entity)
            self.effect_handler.effect_draw_card(self.player_b_entity)

    def on_player_a_message(self, message):
        self._on_game_message(message, self.player_a_entity)

    def on_player_b_message(self, message):
        self._on_game_message(message, self.player_b_entity)

    def _on_game_message(self, message, entity):
        try:
            if message.head == MESSAGE_HEAD_ACTION:
                if self.turn != entity.side:
                    raise GameError('Not your turn')

                action = message.body.get('action', None)
                if action is None:
                    raise GameError('Cannot interpret game action')
                self._do_player_action(action, entity)
            else:
                raise GameError('Not-action game message')
        except GameError as err:
            msg = 'Game error: {0}'.format(err)
            self.logger.warning(msg)
            self.notify(GameMessage(MESSAGE_HEAD_ERROR, status=msg), entity)

    def _do_player_action(self, action, entity):
        action_type = action['type']
        if action_type == ACTION_PLAY_CARD:
            self.play_card(action['card'], entity)
        elif action_type == ACTION_FIRE_WEAPON:
            self.fire_weapon(entity)
        elif action_type == ACTION_END_TURN:
            self.player_end_turn(entity)
        else:
            raise GameError('Unknown action: {0}'.format(action))

    def play_card(self, card_name, player_state):
        """
            @type card_name: str
            @type player_state: PlayerState
        """
        card = get_card(card_name)
        card_state = player_state.get_card_in_hand(card_name, None)
        if card_state is None:
            raise GameError('Card is not in hand: {0}'.format(card_name))
        if self.is_offense(player_state):
            card_action = card.get(P_CARD_ACTION_OFFENSE, card.get(P_CARD_ACTION_SAME, None))
            cost = card_state.cost_offense
        else:
            card_action = card.get(P_CARD_ACTION_DEFENSE, card.get(P_CARD_ACTION_SAME, None))
            cost = card_state.cost_defense
        if card_action is None:
            raise GameError('Card does not have any actions: {0}'.format(card_name))
        if cost > player_state.energy:
            raise GameError('Not enough energy: {0}'.format(card_name))

        # Play card
        self.effect_handler.effect_remove_card(player_state, card_name)
        self.effect_handler.effect_edamage(player_state, cost)
        self.effect_handler.apply_effects(player_state, card_action.get(P_CARD_EFFECTS, []))
        self.invoke_case(player_state, CASE_PLAY_CARD, card_name)

    def fire_weapon(self, player_state):
        """
            @type player_state: PlayerState
        """
        if not player_state.armed:
            raise GameError('Not armed: {0}'.format(player_state))
        w = get_weapon(player_state.weapon_name)
        if self.is_offense(player_state):
            w_action = w.get(P_WEAPON_ACTION_OFFENSE, w.get(P_WEAPON_ACTION_SAME, None))
        else:
            w_action = w.get(P_WEAPON_ACTION_DEFENSE, w.get(P_WEAPON_ACTION_SAME, None))
        if w_action is None:
            raise GameError('Weapon does not have actions: {0}'.format(player_state.weapon_name))
        cost = w_action.get(P_WEAPON_COST, 0)
        if cost > player_state.energy:
            raise GameError('Not enough energy to shoot: {0}'.format(player_state.weapon_name))
        self.effect_handler.effect_edamage(player_state, cost)
        self.effect_handler.apply_effects(player_state, w_action.get(P_WEAPON_EFFECTS, []))

    def player_end_turn(self, player_state):
        """
            @type player_state: PlayerState
        """
        if self.turn == SIDE_B:
            self.end_round()
        self.end_turn()
        if self.turn == SIDE_A:
            self.start_round()

    def end_round(self):
        # Process buffs
        for entity_state in self.get_all_entities():
            self.invoke_case_global(CASE_ROUND_END)
            for buff in entity_state.buffs:
                d = buff.duration - 1
                if d <= 0:
                    self.effect_handler.effect_remove_buff(entity_state, buff.name)
                else:
                    buff = get_buff(buff.name)
                    self.effect_handler.apply_effects(entity_state, buff.get(P_BUFF_ON_ROUND_EFFECTS, []))

    def start_round(self):
        # Process energy
        for entity_state in self.get_all_entities():
            self.invoke_case_global(CASE_ROUND_START)
            self.effect_handler.effect_eheal(entity_state, entity_state.energy_gain)
            if entity_state.energy > entity_state.max_energy:
                entity_state.energy = entity_state.max_energy
                self.effect_handler.effect_damage(entity_state, 1)
                self.invoke_case(entity_state, CASE_OVERLOAD, entity_state.name)

    def invoke_case_global(self, case, arg=None):
        for e in self.get_all_entities():  # type: EntityState
            self.invoke_case(e, case, arg)

    def invoke_case(self, entity, case, arg):
        # Cases in buffs
        for b in entity.buffs:  # type: BuffState
            buff = get_buff(b.name)
            cases = buff.get(P_BUFF_CASES, {})
            case = cases.get(case, None)
            if case is None:
                continue
            case_arg = case.get(P_CASE_ARG, None)
            if case_arg is None or case_arg == arg:
                self.effect_handler.apply_effects(entity, case.get(P_CASE_EFFECTS, []))

        # Cases in objects
        if not self.is_player(entity):
            obj = get_object(entity.name)
            cases = obj.get(P_OBJECT_CASES, {})
            case = cases.get(case, None)
            if case is None:
                return
            case_arg = case.get(P_CASE_ARG, None)
            if case_arg is None or case_arg == arg:
                self.effect_handler.apply_effects(entity, case.get(P_CASE_EFFECTS, []))

    def is_offense(self, entity):
        if not self.is_player(entity):
            return None

        if entity == self.player_a_entity:
            return self.player_a_entity.position < \
                   self.player_b_entity.position
        else:
            return self.player_b_entity.position < \
                   self.player_a_entity.position

    def get_enemy_ship(self, entity):
        if entity.side == SIDE_A:
            return self.player_b_entity
        if entity.side == SIDE_B:
            return self.player_a_entity
        return None

    def get_enemies(self, entity):
        enemies = []
        for e in self.get_all_entities():
            if e != entity and is_enemies(entity, e):
                enemies.append(e)
        return enemies

    def get_allies(self, entity):
        enemies = []
        for e in self.get_all_entities():
            if e != entity and is_allies(entity, e):
                enemies.append(e)
        return enemies

    def get_targets(self, entity, target, target_range=10):
        es = self.get_targets_no_range(entity, target)
        return filter_position_range(es, entity.position - target_range, entity.position + target_range)

    def get_targets_no_range(self, entity, target):
        if target == TARGET_SELF:
            return [entity, ]

        if target == TARGET_ALL:
            return self.get_all_entities()

        if target == TARGET_ALL_EXCEPT_SELF:
            return filter_exclude(self.get_all_entities(), entity)

        if target == TARGET_ALL_ENEMIES:
            return filter_enemy(self.get_all_entities(), entity)

        if target == TARGET_ALL_ALLIES:
            return filter_ally(self.get_all_entities(), entity)

        if target == TARGET_ALL_SHIPS:
            return filter_ship(self.get_all_entities())

        if target == TARGET_ENEMY_SHIP:
            return filter_enemy(filter_ship(self.get_all_entities()), entity)

        if target == TARGET_ALLY_SHIP:
            return filter_ally(filter_ship(self.get_all_entities()), entity)

        if target == TARGET_FORWARD:
            return filter_direction(self.get_all_entities(),
                                    entity.position + 1,
                                    direction=+1, pierce=False)

        if target == TARGET_FORWARD_ALLY:
            return filter_direction(filter_ally(self.get_all_entities(), entity),
                                    entity.position + 1,
                                    direction=+1, pierce=False)

        if target == TARGET_FORWARD_ENEMY:
            return filter_direction(filter_enemy(self.get_all_entities(), entity),
                                    entity.position + 1,
                                    direction=+1, pierce=False)

        if target == TARGET_FORWARD_PIERCE:
            return filter_direction(self.get_all_entities(),
                                    entity.position - 1,
                                    direction=-1, pierce=True)

        if target == TARGET_BACKWARD:
            return filter_direction(self.get_all_entities(),
                                    entity.position - 1,
                                    direction=-1, pierce=False)

        if target == TARGET_BACKWARD_ALLY:
            return filter_direction(filter_ally(self.get_all_entities(), entity),
                                    entity.position - 1,
                                    direction=-1, pierce=False)

        if target == TARGET_BACKWARD_ENEMY:
            return filter_direction(filter_enemy(self.get_all_entities(), entity),
                                    entity.position - 1,
                                    direction=-1, pierce=False)

        if target == TARGET_BACKWARD_PIERCE:
            return filter_direction(self.get_all_entities(),
                                    entity.position - 1,
                                    direction=-1, pierce=True)

        if target == TARGET_MAX_ENERGY:
            enemy = self.get_enemy_ship(entity)
            if enemy is None:
                return []
            if enemy.energy > entity.erengy:
                return [enemy, ]
            else:
                return [entity, ]

        if target == TARGET_MAX_HEALTH:
            enemy = self.get_enemy_ship(entity)
            if enemy is None:
                return []
            if enemy.hp > entity.hp:
                return [enemy, ]
            else:
                return [entity, ]

        if target == TARGET_MIN_HEALTH:
            enemy = self.get_enemy_ship(entity)
            if enemy is None:
                return []
            if enemy.hp < entity.hp:
                return [enemy, ]
            else:
                return [entity, ]

        raise GameError('Unknown target: {0}'.format(target))

    def get_entities_at(self, position):
        return filter_position(self.get_all_entities(), position)

    def get_all_entities(self):
        """
            :rtype: list[EntityState]
        """
        return [self.player_a_entity, self.player_b_entity] + self.objects  # type: List[EntityState]

    def get_state(self, only_for=None):
        state = {
            SIDE_A: self.get_player_state(self.player_a),
            SIDE_B: self.get_player_state(self.player_b),
        }
        if only_for == SIDE_A:
            del state[SIDE_B]
        if only_for == SIDE_B:
            del state[SIDE_A]
        return state

    def get_player_state(self, player):
        if player == self.player_a:
            return self.player_a_entity.get_state()
        if player == self.player_b:
            return self.player_b_entity.get_state()
        return None

    def is_player(self, entity):
        if entity == self.player_a_entity:
            return True
        if entity == self.player_b_entity:
            return True
        return False

    def notify(self, message, entity=None):
        if entity is None or entity == self.player_a_entity:
            self.player_a.send(message)
        if entity is None or entity == self.player_b_entity:
            self.player_b.send(message)


def create(player_a, player_b):
    return CardGame(player_a, player_b)



