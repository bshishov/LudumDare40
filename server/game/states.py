import random
from typing import List, Optional

from framework.game import GameError
from game.rules import *
from game.utils import select_cards
import network.protocol as proto


__all__ = ['BuffState', 'CardState', 'EntityState', 'PlayerEntityState']


class BuffState(object):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def get_state(self) -> proto.BuffState:
        state = proto.BuffState()
        state.duration = self.duration
        state.name = self.name
        return state


class CardState(object):
    def __init__(self, name):
        if name not in cards:
            raise GameError('No such card: {0}'.format(name))

        self.name = name

        card = get_card(self.name)
        card_offense_core = card.get(Card.ACTION_OFFENSE, card.get(Card.ACTION_SAME))
        card_defense_core = card.get(Card.ACTION_OFFENSE, card.get(Card.ACTION_SAME))
        self.cost_offense = card_offense_core.get(Card.COST)
        self.cost_defense = card_defense_core.get(Card.COST)

    @property
    def type(self) -> str:
        card = get_card(self.name)
        return card.get(Card.TYPE)

    def get_state(self) -> proto.CardState:
        state = proto.CardState()
        state.name = self.name
        state.cost_offense = self.cost_offense
        state.cost_defense = self.cost_defense
        return state


class EntityState(object):
    def __init__(self, *args, **kwargs):
        self.id = -1
        self.energy = 0
        self.max_energy = 10
        self.energy_gain = 0
        self.hp = 3
        self.buffs = []  # type: List[BuffState]
        self.position = 0
        self.name = None
        self.armed = False
        self.muted = False
        self.locked = False
        self.damage_mod = 0
        self.buffable = True
        self.side = None
        self.is_player = False

    def get_buff(self, buff_name, default=None) -> BuffState:
        for b in self.buffs:
            if b.name == buff_name:
                return b
        return default

    def get_state(self) -> proto.EntityState:
        state = proto.EntityState()
        state.id = self.id
        state.side = self.side
        state.hp = self.hp
        state.name = self.name
        state.energy = self.energy
        state.energy_gain = self.energy_gain
        state.max_energy = self.max_energy
        state.muted = self.muted
        state.armed = self.armed
        state.locked = self.locked
        state.damage_mod = self.damage_mod
        state.buffable = self.buffable
        state.is_player = self.is_player
        state.position = self.position

        for b in self.buffs:
            state.buffs.append(b.get_state())

        return state


class PlayerEntityState(EntityState):
    def __init__(self, side, prefs: proto.CliQueuePreferences, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.side = side

        if side == proto.Side.A:
            self.position = INITIAL_A_POSITION
            self.name = 'player_a'
            self.id = 0
        else:
            self.position = INITIAL_B_POSITION
            self.name = 'player_b'
            self.id = 1

        self.is_player = True

        ship_name = prefs.ship
        weapon_name = prefs.weapon

        self.ship_name = ship_name
        self.weapon_name = weapon_name
        self.armed = True
        self.buffable = True

        ship = get_ship(ship_name)
        self.hp = ship.get(Ship.HP)
        self.max_energy = ship.get(Ship.MAX_ENERGY)
        self.energy_gain = ship.get(Ship.ENERGY_PER_TURN)

        self.deck = []  # type: List[str]
        self.hand = []  # type: List[CardState]

        self.build_deck()

    def get_card_in_hand(self, card_name, default=None) -> Optional[CardState]:
        for c in self.hand:
            if c.name == card_name:
                return c
        return default

    def build_deck(self):
        ship = get_ship(self.ship_name)
        ship_cards = ship.get(Ship.CARDS, [])
        for c_name in ship_cards:
            card = get_card(c_name)
            in_deck = card.get(Card.DECK, True)
            if in_deck:
                self.deck += [c_name, ] * SHIP_CARDS_EACH

        weapon = get_weapon(self.weapon_name)
        weapon_cards = weapon.get(Weapon.CARDS, [])

        for c_name in weapon_cards:
            card = get_card(c_name)
            in_deck = card.get(Card.DECK, True)
            if in_deck:
                self.deck += [c_name, ] * WEAPON_CARDS_EACH

        event_cards = []
        for card_key, card in cards.items():
            if card.get(Card.DECK, False) and card[Card.TYPE] == CardType.EVENT:
                event_cards.append(card_key)

        self.deck += select_cards(event_cards, EVENT_CARDS_FROM_POOL, MAX_EVENT_CARDS_OF_EACH_TYPE)
        random.shuffle(self.deck)

    def draw_from_deck(self) -> Optional[CardState]:
        if len(self.deck) > 0:
            card_name = random.sample(self.deck, 1)[0]
            self.deck.remove(card_name)
            return CardState(card_name)
        return None

    def get_state(self, hide_hand=False) -> proto.EntityState:
        state = super().get_state()

        state.weapon_name = self.weapon_name
        state.ship_name = self.ship_name

        state.hand_cards = len(self.hand)
        state.deck_cards = len(self.deck)

        if not hide_hand:
            for c in self.hand:
                state.hand.append(c.get_state())

        return state
