import random

from game_base import *
from rules import *
from game_utils import *
from typing import List, Dict

class BuffState(object):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def get_state(self):
        return self.__dict__


class CardState(object):
    def __init__(self, name):
        if name not in cards:
            raise GameError('No such card: {0}'.format(name))

        self.name = name

        card = get_card(self.name)
        card_offense_core = card.get(P_CARD_ACTION_OFFENSE, card.get(P_CARD_ACTION_SAME))
        card_defense_core = card.get(P_CARD_ACTION_OFFENSE, card.get(P_CARD_ACTION_SAME))
        self.cost_offense = card_offense_core.get(P_CARD_COST)
        self.cost_defense = card_defense_core.get(P_CARD_COST)

    @property
    def type(self):
        card = get_card(self.name)
        return card.get(P_CARD_TYPE)

    def get_state(self):
        return self.__dict__


class EntityState(object):
    def __init__(self, *args, **kwargs):
        self.id = -1
        self.energy = 0
        self.max_energy = 10
        self.energy_gain = 0
        self.hp = 10
        self.buffs = []  # type: List[BuffState]
        self.position = 0
        self.name = None
        self.armed = False
        self.muted = False
        self.locked = False
        self.damage_mod = 0
        self.buffable = False
        self.side = None
        self.is_player = False

    def get_buff(self, buff_name, default=None):
        for b in self.buffs:
            if b.name == buff_name:
                return b
        return default

    def get_state(self):
        return todict(self)


class PlayerState(EntityState):
    def __init__(self, side, prefs, *args, **kwargs):
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

        self.is_player = True

        ship_name = prefs.get('ship')
        weapon_name = prefs.get('weapon')

        self.ship_name = ship_name
        self.weapon_name = weapon_name
        self.armed = True
        self.buffable = True

        ship = get_ship(ship_name)
        self.hp = ship.get(P_SHIP_HP)
        self.max_energy = ship.get(P_SHIP_MAX_ENERGY)
        self.energy_gain = ship.get(P_SHIP_ENERGY_PER_TURN)

        self.deck = []  # type: List[str]
        self.hand = []  # type: List[CardState]

        self.build_deck()

    def get_card_in_hand(self, card_name, default=None):
        for c in self.hand:
            if c.name == card_name:
                return c
        return default

    def build_deck(self):
        ship = get_ship(self.ship_name)
        ship_cards = ship.get(P_SHIP_CARDS, [])
        self.deck += ship_cards * SHIP_CARDS_EACH

        weapon = get_weapon(self.weapon_name)
        weapon_cards = weapon.get(P_WEAPON_CARDS, [])
        self.deck += weapon_cards * WEAPON_CARDS_EACH

        event_cards = []
        for card_key, card in cards.items():
            if card.get(P_CARD_DECK, False) and card[P_TYPE] == CARD_TYPE_EVENT:
                event_cards.append(card_key)

        self.deck += select_cards(event_cards, EVENT_CARDS_FROM_POOL, MAX_EVENT_CARDS_OF_EACH_TYPE)
        random.shuffle(self.deck)

    def draw_from_deck(self):
        if len(self.deck) > 0:
            card_name = random.sample(self.deck, 1)[0]
            self.deck.remove(card_name)
            return CardState(card_name)

    def get_state(self, hide_hand=False):
        state = todict(self)
        if 'deck' in state:
            del state['deck']
            state['deck_cards'] = len(self.deck)
        if hide_hand and 'hand' in state:
            del state['hand']
            state['hand_cards'] = len(self.hand)
        return state


