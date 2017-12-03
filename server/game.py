import connection
import uuid
import logging
import random

from protocol import *
from rules import *

SIDE_A = 'a'
SIDE_B = 'b'


class GameError(RuntimeError):
    """
        Game logic error
    """
    pass


class Player(object):
    def __init__(self, channel):
        self._channel = channel  # type: connection.ClientChannel
        self._is_registered = False
        self._name = None
        self._id = str(uuid.uuid4())
        self.in_queue = False
        self.in_game = False
        self.ship = None
        self.weapon = None

        # Proxy events
        self.on_message = self._channel.on_message
        self.on_disconnect = self._channel.on_disconnect

        self.on_message.append(self._on_message)

    def _on_message(self, message):
        if message is None:
            return

        if not self.in_game:
            if message.domain == MESSAGE_DOMAIN_LOBBY:
                if message.head == MESSAGE_HEAD_START_QUEUE and not self.in_queue:
                    if message.body.get('ship', None) is None or message.body.get('weapon', None) is None:
                        self.send(LobbyMessage(MESSAGE_HEAD_ERROR, status='ship and weapon are not selected'))
                        return
                    self.set_ship(message.body.get('ship'))
                    self.set_weapon(message.body.get('weapon'))
                    self.in_queue = True
                    self.send(LobbyMessage(MESSAGE_HEAD_ACK, status='queue started'))
                elif message.head == MESSAGE_HEAD_STOP_QUEUE and self.in_queue:
                    self.in_queue = False
                    self.send(LobbyMessage(MESSAGE_HEAD_ACK, status='queue stopped'))

    def set_ship(self, ship):
        if ship not in ships:
            err = 'Unknown ship: {0}'.format(ship)
            self.send(GameMessage(MESSAGE_HEAD_ERROR, status=err))
            raise RuntimeError(err)
        self.ship = ship

    def set_weapon(self, weapon):
        if weapon not in weapons:
            self.send(GameMessage(MESSAGE_HEAD_ERROR, status='unknown weapon'))
            raise RuntimeError('Unknown weapon')
        self.weapon = weapon

    def send(self, message):
        if self._channel.is_active:
            self._channel.send_message(message)


class Entity(object):
    def effect_handler(self, event_name):
        def decorator(fn):
            def wrapper(*args, **kwargs):
                fn(*args, **kwargs)
            return wrapper
        self._handlers[event_name] = decorator
        return decorator

    def __init__(self, *args, **kwargs):
        self.id = -1
        self.energy = 0
        self.max_energy = 10
        self.energy_gain = 0
        self.hp = 10
        self.buffs = []
        self.position = 0
        self.name = None
        self.armed = False
        self.muted = False
        self.locked = False
        self.damage_mod = 0
        self.buffable = False
        self.side = None


class PlayerEntity(Entity):
    def __init__(self, side, ship, weapon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.side = side

        if side == SIDE_A:
            self.position = INITIAL_A_POSITION
            self.name = 'player_a'
            self.id = 0
        else:
            self.position = INITIAL_B_POSITION
            self.name = 'player_b'
            self.id = 1

        self.ship_name = ship
        self.weapon_name = weapon
        self.armed = True
        self.buffable = True

        self.deck = []
        self.hand = []

        for i in range(INITIAL_CARDS):
            self.hand.append(self.draw_from_deck())

        self.build_deck()

    def build_deck(self):
        event_cards = []

        # weapon and ship cards to deck
        for card_key, card in cards.items():
            if hasattr(card, 'ship') and card['ship'] == self.ship_name:
                for i in range(SHIP_CARDS_EACH):
                    self.deck.append(card_key)
            if hasattr(card, 'weapon') and card['weapon'] == self.weapon_name:
                for i in range(WEAPON_CARDS_EACH):
                    self.deck.append(card_key)
            if card.get('deck', False) and card[P_TYPE] == CARD_TYPE_EVENT:
                event_cards.append(card_key)

        self.deck += random.sample(event_cards, EVENT_CARDS_FROM_POOL)

    def draw_from_deck(self):
        if len(self.deck) > 0:
            card = random.sample(self.deck, 1)[0]
            self.deck.remove(card)
            return card


class GameBase(object):
    def __init__(self, player_a, player_b):
        self.id = str(uuid.uuid4())
        self.logger = logging.getLogger('Game:{0}'.format(self.id))
        self.player_a = player_a  # type: Player
        self.player_b = player_b  # type: Player
        self.player_a.in_game = True
        self.player_b.in_game = True

        self.player_a_entity = PlayerEntity(SIDE_A, player_a.ship, player_a.weapon)
        self.player_b_entity = PlayerEntity(SIDE_B, player_b.ship, player_b.weapon)
        self.turn = SIDE_A

        # Subscribe to player messages
        self.player_a.on_message.append(self._on_player_a_message)
        self.player_b.on_message.append(self._on_player_b_message)
        self.player_a.on_disconnect.append(self._on_player_a_disconnect)
        self.player_b.on_disconnect.append(self._on_player_b_disconnect)

        # Send that the game is started
        self.player_a.send(GameMessage(MESSAGE_HEAD_HELLO,
                                       status='started',
                                       id=self.id,
                                       side=SIDE_A,
                                       state=self.get_state(SIDE_A)))
        self.player_b.send(GameMessage(MESSAGE_HEAD_HELLO,
                                       status='started',
                                       id=self.id,
                                       side=SIDE_B,
                                       state=self.get_state(SIDE_B)))

        self.is_active = True

    def get_player_state(self, player):
        if player == self.player_a:
            return self.player_a_entity
        if player == self.player_b:
            return self.player_b_entity
        return None

    def _validate_message(self, player, message):
        if message is None:
            return False

        if message.domain != MESSAGE_DOMAIN_GAME:
            self.logger.warning('Expected game message: {0}'.format(message))
            return False

        if message.game_id != self.id:
            self.logger.warning('Wrong game id: {0}'.format(message))
            player.send(GameMessage(MESSAGE_HEAD_ERROR, status='wrong game id'))
            return False

        if message.head == MESSAGE_HEAD_ACTION:
            if self.get_player_state(player).side != self.turn:
                self.logger.warning('Not your turn: {0}'.format(message))
                player.send(GameMessage(MESSAGE_HEAD_ERROR, status='not your turn'))
                return False
        return True

    def _on_player_a_message(self, message):
        if self._validate_message(self.player_a, message):
            return self._on_game_message(message, self.player_a_entity)

    def _on_player_b_message(self, message):
        if self._validate_message(self.player_b, message):
            return self._on_game_message(message, self.player_b_entity)

    def _on_player_a_disconnect(self, channel):
        self.player_b.send(GameMessage(MESSAGE_HEAD_PLAYER_LEFT, status='opponent disconnected'))
        self.end(interrupted=True)

    def _on_player_b_disconnect(self, channel):
        self.player_a.send(GameMessage(MESSAGE_HEAD_PLAYER_LEFT, status='opponent disconnected'))
        self.end(interrupted=True)

    def _on_game_message(self, message, entity):
        pass

    def notify(self, message, entity=None):
        if entity is None or entity == self.player_a_entity:
            self.player_a.send(message)
        if entity is None or entity == self.player_b_entity:
            self.player_b.send(message)

    def end_turn(self):
        if self.turn == SIDE_A:
            new_turn = SIDE_B
        else:
            new_turn = SIDE_A

        self.player_a.send(GameMessage(MESSAGE_HEAD_TURN,
                                       status='turn',
                                       turn=new_turn,
                                       state=self.get_state(SIDE_A)))
        self.player_b.send(GameMessage(MESSAGE_HEAD_TURN,
                                       status='turn',
                                       turn=new_turn,
                                       state=self.get_state(SIDE_B)))

    def get_state(self, only_for=None):
        return {}

    def end(self, interrupted=False):
        self.logger.info('Finished interrupted={0}'.format(interrupted))
        self.player_a.send(GameMessage(MESSAGE_HEAD_ENDED, status='finished', interrupted=interrupted))
        self.player_b.send(GameMessage(MESSAGE_HEAD_ENDED, status='finished', interrupted=interrupted))

        # Unsubscribe
        self.player_a.on_message.remove(self._on_player_a_message)
        self.player_b.on_message.remove(self._on_player_b_message)
        self.player_a.on_disconnect.remove(self._on_player_a_disconnect)
        self.player_b.on_disconnect.remove(self._on_player_b_disconnect)

        self.player_a.in_game = False
        self.player_b.in_game = False

        self.is_active = False

    def is_player(self, entity):
        if entity == self.player_a_entity:
            return True
        if entity == self.player_b_entity:
            return True
        return False


class CardGame(GameBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.objects = []
        self._last_entity_id = 1
        self.board_size = BOARD_SIZE

    def _on_game_message(self, message, entity):
        try:
            if message.head == MESSAGE_HEAD_ACTION:
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

    def play_card(self, card_name, entity):
        card = get_card(card_name)
        if card_name not in entity.hand:
            raise GameError('Card is not in hand: {0}'.format(card_name))
        if self.is_offense(entity):
            card_action = P_CARD_ACTION_OFFENSE
        else:
            card_action = P_CARD_ACTION_DEFENSE
        # if not offense or defense, then use SAME
        card_core = card.get(card_action, card.get(P_CARD_ACTION_SAME, None))
        if card_core is None:
            raise GameError('Card cannot be played: {0}'.format(card_name))
        cost = card_core.get(P_CARD_COST, 0)
        if cost > entity.energy:
            raise GameError('Not enough energy: {0}'.format(card_name))
        self.entity_modify_energy(entity, -cost)
        self.apply_effects(card_core.get(P_CARD_EFFECTS, []), entity)
        self.test_case(CASE_PLAY_CARD, card_name)

    def fire_weapon(self, entity):
        if not entity.armed:
            raise GameError('Not armed: {0}'.format(entity))
        if self.is_offense(entity):
            action_key = P_WEAPON_ACTION_OFFENSE
        else:
            action_key = P_WEAPON_ACTION_DEFENSE
        w = get_weapon(entity.weapon_name)
        w_core = w.get(action_key, w.get(P_WEAPON_ACTION_SAME))
        cost = w_core.get(P_WEAPON_COST, 0)
        self.entity_modify_energy(entity, -cost)
        self.apply_effects(w_core.get(P_WEAPON_EFFECTS, []), entity)

    def player_end_turn(self, entity):
        self.end_turn()
        if self.turn == SIDE_A:
            self.end_round()

    def end_round(self):
        for e in self.get_all_objects():
            self.test_case(CASE_ROUND_END, e)
            for buff_name, duration in e.buffs:
                d = duration - 1
                if d <= 0:
                    self.entity_remove_buff(e, buff_name)
                else:
                    buff = get_buff(buff_name)
                    self.apply_effects(buff.get(P_BUFF_ON_ROUND_EFFECTS, []), e)
                    raise NotImplementedError()

        for e in self.get_all_objects():
            self.test_case(CASE_ROUND_START, e)

            if e.energy > e.max_energy:
                e.energy = e.max_energy
                self.entity_modify_hp(e, -1)
                self.test_case(CASE_OVERLOAD, e, e.name)

    def apply_effects(self, effects, entity):
        for effect in effects:
            targets = self.get_targets(effect.get(P_EFFECT_TARGET), entity=entity)
            for e in targets:
                # e type: Entity
                self.apply_effect(e, effect)

    def apply_effect(self, entity, effect):
        """
        @type:entity: Entity
        """
        etype = effect.get(P_EFFECT_TYPE, None)
        evalue = effect.get(P_EFFECT_VALUE, None)
        if etype is None:
            raise GameError('Effect has no type: {0}'.format(effect))

        if evalue is None and etype not in EFFECTS_WITHOUT_VALUE:
            raise GameError('Effect has no value: {0}'.format(effect))

        if effect == EFFECT_TYPE_DAMAGE:
            # TODO: RANGES AND MODIFIERS
            self.entity_modify_hp(entity, -evalue)
        if effect == EFFECT_TYPE_HEAL:
            self.entity_modify_hp(entity, evalue)
        if effect == EFFECT_TYPE_EDAMAGE:
            self.entity_modify_energy(entity, -evalue)
        if effect == EFFECT_TYPE_EHEAL:
            self.entity_modify_energy(entity, evalue)
        if effect == EFFECT_TYPE_MOVE:
            self.entity_move(entity, evalue)
        if effect == EFFECT_TYPE_DISARM:
            entity.armed = False
        if effect == EFFECT_TYPE_ARM:
            entity.armed = True
        if effect == EFFECT_TYPE_MUTE:
            entity.muted = True
        if effect == EFFECT_TYPE_UNMUTE:
            entity.muted = False
        if effect == EFFECT_TYPE_LOCK_POSITION:
            entity.locked = True
        if effect == EFFECT_TYPE_UNLOCK_POSITION:
            entity.locked = False
        if effect == EFFECT_TYPE_ADD_CARDCOST:
            self.change_card_cost(entity, effect.get(P_EFFECT_CARD_TYPE), evalue)
        if effect == EFFECT_TYPE_REDUCE_CARDCOST:
            self.change_card_cost(entity, effect.get(P_EFFECT_CARD_TYPE), -evalue)
        if effect == EFFECT_TYPE_DRAW_CARD:
            self.entity_draw_card(entity)
        if effect == EFFECT_TYPE_DAMAGE_ADD:
            entity.damage_mod += evalue
        if effect == EFFECT_TYPE_DAMAGE_REDUCE:
            entity.damage_mod -= evalue
        if effect == EFFECT_TYPE_ENERGYGAIN_ADD:
            # TODO: CAN BE NEGATIVE?
            entity.energy_gain += evalue
        if effect == EFFECT_TYPE_ENERGYGAIN_REDUCE:
            # TODO: CAN BE NEGATIVE?
            entity.energy_gain = max(entity.energy_gain - evalue, 0)
        if effect == EFFECT_TYPE_SPAWN:
            self.entity_spawn(entity, evalue, effect.get(P_EFFECT_SPAWN_POSITION))
        if effect == EFFECT_TYPE_APPLY_BUFF:
            self.entity_apply_buff(entity, evalue)
        if effect == EFFECT_TYPE_REMOVE_BUFF:
            self.entity_apply_buff(entity, evalue)

        self.notify(GameMessage(MESSAGE_HEAD_ACTION, status='effect', entity=entity, effect=effect))

    def entity_apply_buff(self, entity, buff_name):
        if entity.buffable:
            buff = get_buff(buff_name)
            # It will renew if the buff is existed
            entity.buffs[buff_name] = buff.get(P_BUFF_DURATION)
            self.apply_effects(buff.get(P_BUFF_ON_APPLY_EFFECTS, []), entity)

    def entity_remove_buff(self, entity, buff_name):
        if buff_name in entity.buffs:
            buff = get_buff(buff_name)
            del entity.buffs[buff_name]
            self.apply_effects(buff.get(P_BUFF_ON_REMOVE_EFFECTS, []), entity)

    def change_card_cost(self, entity, card_type, amount):
        if not self.is_player(entity):
            raise GameError('Non-player entities does not have cards: {0}'.format(card_type))
        raise NotImplementedError()

    def entity_spawn(self, entity, name, spawn_position):
        if name not in objects:
            raise GameError('No such entity: {0}'.format(name))
        e = Entity()
        e.name = name
        e.position = max(min(spawn_position + entity.position, self.board_size), 0)
        self._last_entity_id += 1
        e.id = self._last_entity_id
        self.objects.append(e)

    def entity_draw_card(self, entity):
        if not self.is_player(entity):
            raise GameError('Non-player entities cannot draw card: {0}'.format(effect))
        if len(entity.deck) > 0:
            card_name = entity.draw_from_deck()
            entity.hand.append(card_name)
            self.test_case(CASE_DRAW_CARD, entity, card_name)

    def entity_drop_card(self, entity):
        if not self.is_player(entity):
            raise GameError('Non-player entities cannot draw card: {0}'.format(effect))
        if len(entity.hand) > 0:
            card_to_drop = random.sample(entity.hand, 1)[0]
            entity.hand.remove(card_to_drop)
            self.test_case(CASE_DROP_CARD, entity, card_to_drop)

    def entity_move(self, entity, amount):
        if entity.locked:
            # TODO: HOW!!!!!!!!!!!!!
            return

        old_pos = entity.position
        entity.position += amount
        entity.position = max(min(entity.position, self.board_size), 0)

        self.test_case(CASE_COLLIDE, entity, entity.position)

        # Swap players
        if self.is_player(old_pos):
            enemy = self.get_enemy(entity)
            if enemy.position == entity.position:
                self.entity_move(enemy, -amount)

    def entity_modify_hp(self, entity, amount):
        entity.hp += amount
        entity.hp = max(entity.hp, 0)
        if entity.hp == 0:
            if not self.is_player(entity):
                self.test_case(CASE_DESTOYED, entity, entity.name)
                self.objects.remove(entity)
            else:
                self.end()

    def entity_modify_energy(self, entity, amount):
        entity.energy += amount
        entity.energy = max(entity.energy, 0)

    def test_case(self, case, entity, arg=None):
        if case == CASE_COLLIDE:
            for entity in self.get_entities_at(arg):
                self.proc_case(case, arg, entity)
        raise GameError('Unknown case: {0}'.format(case))

    def proc_case(self, case, arg, entity):
        raise NotImplementedError()

    def is_offense(self, entity):
        if not self.is_player(entity):
            return None

        if entity == self.player_a_entity:
            return self.player_a_entity.position < \
                   self.player_b_entity.position
        else:
            return self.player_b_entity.position < \
                   self.player_a_entity.position

    def get_enemy(self, entity):
        if not self.is_player(entity):
            return None
        if entity == self.player_a_entity:
            return self.player_b_entity
        else:
            return self.player_a_entity

    def get_targets(self, target, entity):
        if target == TARGET_SELF:
            return [entity]
        if target == TARGET_ENEMIES:
            enemy = self.get_enemy(entity)
            if enemy is not None:
                return [enemy]
            return [enemy]
        if target == TARGET_ALL:
            return [self.player_a_entity, self.player_b_entity] + self.objects
        if target == TARGET_ALL_EXCEPT_SELF:
            return [self.get_enemy(entity)] + self.objects
        if target == TARGET_MAX_ENERGY:
            enemy = self.get_enemy(entity)
            if enemy is None:
                return []
            if enemy.energy > entity.erengy:
                return [enemy]
            else:
                return [entity]
        if target == TARGET_MAX_HEALTH:
            enemy = self.get_enemy(entity)
            if enemy is None:
                return []
            if enemy.hp > entity.hp:
                return [enemy]
            else:
                return [entity]
        if target in [TARGET_FORWARD, TARGET_FORWARD_PIERCE]:
            if entity.position == self.board_size - 1:
                return []
            found = []
            for pos in range(entity.position + 1, self.board_size):
                found += self.get_entities_at(pos)
                if target == TARGET_BACKWARD and len(found) > 0:
                    return [found[0]]
            return found
        if target in [TARGET_BACKWARD, TARGET_BACKWARD_PIERCE]:
            if entity.position == 0:
                return []
            found = []
            for pos in reversed(range(0, entity.position - 1)):
                found += self.get_entities_at(pos)
                if target == TARGET_BACKWARD and len(found) > 0:
                    return [found[0]]
            return found
        raise GameError('Unknown target: {0}'.format(target))

    def get_entities_at(self, position):
        if position not in range(self.board_size):
            return []
        found = []
        if self.player_a_entity.position == position:
            found.append(self.player_a_entity)
        if self.player_b_entity.position == position:
            found.append(self.player_b_entity)
        for e in self.objects:
            if e.position == position:
                found.append(e)
        return found

    def get_all_objects(self):
        return [self.player_a_entity, self.player_b_entity] + self.objects

    def get_state(self, only_for=None):
        state = {
            SIDE_A: self.get_player_state(self.player_a).__dict__,
            SIDE_B: self.get_player_state(self.player_b).__dict__,
        }
        if only_for == SIDE_A:
            del state[SIDE_B]
        if only_for == SIDE_B:
            del state[SIDE_A]
        return state


def create(player_a, player_b):
    return CardGame(player_a, player_b)


def get_card(key):
    card = cards.get(key, None)
    if card is None:
        raise GameError('No such card: {0}'.format(key))
    return card


def get_buff(key):
    buff = buffs.get(key, None)
    if buff is None:
        raise GameError('No such buff: {0}'.format(key))
    return buff


def get_entity(key):
    e = objects.get(key, None)
    if e is None:
        raise GameError('No such entity: {0}'.format(key))
    return e


def get_weapon(key):
    w = weapons.get(key, None)
    if w is None:
        raise GameError('No such weapon: {0}'.format(key))
    return w
