import random
from typing import List, Optional

from framework.game import GameError
from game.rules import *
from game.utils import select_cards
from game.protocol import *


__all__ = ['BuffState', 'CardState', 'EntityState', 'PlayerEntityState']


class BuffState(object):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def get_state(self):
        return {
            BuffStateProtocol.NAME: self.name,
            BuffStateProtocol.DURATION: self.duration
        }


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

    def get_state(self) -> dict:
        return {
            CardStateProtocol.NAME: self.name,
            CardStateProtocol.COST_DEFENSE: self.cost_defense,
            CardStateProtocol.COST_OFFENSE: self.cost_offense
        }


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

    def get_state(self) -> {}:
        return {
            EntityStateProtocol.ID: self.id,
            EntityStateProtocol.NAME: self.name,
            EntityStateProtocol.POSITION: self.position,
            EntityStateProtocol.SIDE: self.side,
            EntityStateProtocol.HP: self.hp,
            EntityStateProtocol.ENERGY: self.energy,
            EntityStateProtocol.ENERGY_GAIN: self.energy_gain,
            EntityStateProtocol.MAX_ENERGY: self.max_energy,
            EntityStateProtocol.BUFFABLE: self.buffable,
            EntityStateProtocol.BUFFS: [s.get_state() for s in self.buffs],
            EntityStateProtocol.ARMED: self.armed,
            EntityStateProtocol.MUTED: self.muted,
            EntityStateProtocol.LOCKED: self.locked,
            EntityStateProtocol.IS_PLAYER: self.is_player,
            EntityStateProtocol.DAMAGE_MOD: self.damage_mod,
        }


class PlayerEntityState(EntityState):
    def __init__(self, side, prefs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.side = side

        if side == Side.A:
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

    def get_state(self, hide_hand=False) -> {}:
        state = super().get_state()
        player_state = {
            PlayerEntityProtocol.SHIP_NAME: self.ship_name,
            PlayerEntityProtocol.WEAPON_NAME: self.weapon_name,
            PlayerEntityProtocol.CARDS_IN_DECK: len(self.deck),
            PlayerEntityProtocol.CARDS_IN_HAND: len(self.hand),
            PlayerEntityProtocol.DECK: [],
            PlayerEntityProtocol.HAND: [],
        }
        if not hide_hand:
            player_state[PlayerEntityProtocol.HAND] = [c.get_state() for c in self.hand]
        state.update(player_state)
        return state
