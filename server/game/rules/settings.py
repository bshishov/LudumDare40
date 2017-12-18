from enum import Enum, unique

# SETTINGS
BOARD_SIZE = 6
INITIAL_A_POSITION = 4
INITIAL_B_POSITION = 1
INITIAL_CARDS = 4
WEAPON_CARDS_EACH = 2
SHIP_CARDS_EACH = 2
EVENT_CARDS_FROM_POOL = 6
MAX_EVENT_CARDS_OF_EACH_TYPE = 2


@unique
class Section(Enum):
    SHIPS = 'ships'
    BUFFS = 'buffs'
    WEAPONS = 'weapons'
    CARDS = 'cards'
    OBJECTS = 'objects'


@unique
class PlayerAction(Enum):
    PLAY_CARD = 'play_card'
    FIRE_WEAPON = 'fire_weapon'
    END_TURN = 'end_turn'
    CHEAT_TAKE_CARD = 'take_card'


@unique
class Target(Enum):
    SELF = 'self'
    ALL = 'all'
    ALL_EXCEPT_SELF = 'all_except'
    ALL_ENEMIES = 'all_enemies'
    ALL_ALLIES = 'all_allies'
    ALL_SHIPS = 'all_ships'
    ENEMY_SHIP = 'enemy_ship'
    ALLY_SHIP = 'ally_ship'
    MAX_HEALTH = 'max_health'
    MIN_HEALTH = 'min_health'
    MAX_ENERGY = 'max_energy'
    FORWARD = 'forward'
    FORWARD_ALLY = 'forward_ally'
    FORWARD_ENEMY = 'forward_enemy'
    FORWARD_PIERCE = 'forward_pierce'
    BACKWARD = 'backward'
    BACKWARD_ALLY = 'backward_ally'
    BACKWARD_ENEMY = 'backward_enemy'
    BACKWARD_PIERCE = 'backward_pierce'


@unique
class EffectType(Enum):
    DAMAGE = 'damage'
    EDAMAGE = 'edamage'
    HEAL = 'heal'
    EHEAL = 'eheal'
    MOVE = 'position'
    DISARM = 'disarm'
    ARM = 'arm'
    MUTE = 'mute'
    UNMUTE = 'unmute'
    LOCK_POSITION = 'lock_position'
    UNLOCK_POSITION = 'unlock_position'
    REDUCE_CARDCOST = 'reduce_cardcost'
    ADD_CARDCOST = 'add_cardcost'
    DRAW_CARD = 'draw_card'
    DROP_CARD_OF_TYPE = 'drop_card'
    REMOVE_CARD = 'remove_card'
    GAIN_CARD = 'gain_card'
    DAMAGE_REDUCE = 'damage_reduce'
    DAMAGE_ADD = 'damage_add'
    ENERGYGAIN_REDUCE = 'energygain_reduce'
    ENERGYGAIN_ADD = 'energygain_add'
    SPAWN = 'spawn'
    DESTROY = 'destroy'
    APPLY_BUFF = 'apply_buff'
    REMOVE_BUFF = 'remove_buff'
    ENERGY_TEST = 'energy_test'

    # Speacial effects
    SPECIAL_SWAP = 'special_swap'
    OFFENSE_APPROACH = 'approach'


@unique
class Effect(Enum):
    """
        Effect properties
    """
    TYPE = 'type'
    VALUE = 'value'
    TARGET = 'target'
    RANGE = 'range'
    RANGE_MOD = 'range_mod'
    SPAWN_POSITION = 'spawn_position'
    CARD_TYPE = 'card_type'
    BUFF_DURATION = 'buff_duration'


@unique
class CaseType(Enum):
    COLLIDE = 'collide'
    DRAW_CARD = 'draw_card'
    PLAY_CARD = 'play_card'
    DROP_CARD = 'drop_card'
    DESTROYED = 'entity_destroyed'
    OVERLOAD = 'entity_overload'
    ROUND_END = 'turn_end'
    ROUND_START = 'turn_start'
    SPAWNED = 'spawned'


@unique
class Case(Enum):
    ARG = 'arg'
    EFFECTS = 'effects'
    SOURCE_TARGET = 'source_target'


@unique
class Weapon(Enum):
    # Weapon properties
    DESCRIPTION = 'description'
    FULL_NAME = 'full_name'
    COST = 'cost'
    EFFECT = 'effect'
    CARDS = 'cards'
    ACTION_OFFENSE = 'offense'
    ACTION_DEFENSE = 'defense'
    ACTION_SAME = 'same'
    TARGET = 'target'
    EFFECTS = 'effects'


@unique
class Ship(Enum):
    # Ship properties
    HP = 'hp'
    MAX_ENERGY = 'max_energy'
    ENERGY_PER_TURN = 'energy_per_turn'
    CARDS = 'cards'


@unique
class Entity(Enum):
    # Entities properties
    FULL_NAME = 'full_name'
    DESCRIPTION = 'description'
    HP = 'hp'
    CASES = 'cases'


@unique
class Buff(Enum):
    """
        Buff properties
    """
    FULL_NAME = 'full_name'
    DESCRIPTION = 'description'
    DURATION = 'duration'
    ON_ROUND_EFFECTS = 'turn_effects'
    ON_APPLY_EFFECTS = 'apply_effects'
    ON_REMOVE_EFFECTS = 'remove_effects'
    CASES = 'cases'


@unique
class CardType(Enum):
    EVENT = 'event'
    SHIP = 'ship'
    WEAPON = 'weapon'


@unique
class Card(Enum):
    """
        Card properties
    """
    ACTION_OFFENSE = 'offense'
    ACTION_DEFENSE = 'defense'
    ACTION_SAME = 'same'
    DECK = 'deck'
    TYPE = 'type'
    COST = 'cost'
    FULL_NAME = 'full_name'
    DESCRIPTION = 'description'
    FLAVOR = 'flavor'
    EFFECTS = 'effects'
