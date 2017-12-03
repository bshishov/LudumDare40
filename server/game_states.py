import random

from game_base import *
from rules import *
from game_utils import *


class BuffState(object):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration


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
        return self.__dict__


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

        ship = prefs.get('ship')
        if ship not in ships:
            raise GameError('No such ship: {0}'.format(ship))

        weapon = prefs.get('weapon')
        if weapon not in weapons:
            raise GameError('No such ship: {0}'.format(weapon))

        self.ship_name = ship
        self.weapon_name = weapon
        self.armed = True
        self.buffable = True

        self.deck = [] # type: List[str]
        self.hand = [] # type: List[CardState]

        for i in range(INITIAL_CARDS):
            self.hand.append(self.draw_from_deck())

        self.build_deck()

    def get_card_in_hand(self, card_name, default=None):
        for c in self.hand:
            if c.name == card_name:
                return c
        return default

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

        self.deck += select_cards(event_cards, EVENT_CARDS_FROM_POOL, MAX_EVENT_CARDS_OF_EACH_TYPE)

    def draw_from_deck(self):
        if len(self.deck) > 0:
            card_name = random.sample(self.deck, 1)[0]
            self.deck.remove(card_name)
            return CardState(card_name)