from enum import Enum, unique


@unique
class Side(Enum):
    A = 'a'
    B = 'b'


@unique
class GameStateProtocol(Enum):
    ID = 'id'
    TURN = 'turn'
    OBJECTS = 'objects'


@unique
class BuffStateProtocol(Enum):
    NAME = 'name',
    DURATION = 'duration'


@unique
class CardStateProtocol(Enum):
    NAME = 'name',
    COST_OFFENSE = 'cost_offense'
    COST_DEFENSE = 'cost_defense'


@unique
class EntityStateProtocol(Enum):
    ID = 'id'
    NAME = 'name'
    POSITION = 'position'
    SIDE = 'side'
    HP = 'hp'
    ENERGY = 'energy'
    MAX_ENERGY = 'max_energy'
    ENERGY_GAIN = 'energy_gain'
    BUFFS = 'buffs'
    MUTED = 'muted'
    ARMED = 'armed'
    LOCKED = 'locked'
    DAMAGE_MOD = 'damage_mod'
    BUFFABLE = 'buffable'
    IS_PLAYER = 'is_player'


@unique
class PlayerEntityProtocol(Enum):
    SHIP_NAME = 'ship_name'
    WEAPON_NAME = 'weapon_name'
    HAND = 'hand'
    DECK = 'deck'
    CARDS_IN_HAND = 'hand_cards'
    CARDS_IN_DECK = 'deck_cards'
