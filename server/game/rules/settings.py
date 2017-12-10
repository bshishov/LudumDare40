# SETTINGS
BOARD_SIZE = 6
INITIAL_A_POSITION = 4
INITIAL_B_POSITION = 1
INITIAL_CARDS = 4
WEAPON_CARDS_EACH = 2
SHIP_CARDS_EACH = 2
EVENT_CARDS_FROM_POOL = 6
MAX_EVENT_CARDS_OF_EACH_TYPE = 2

# Sections
SECTION_SHIPS = 'ships'
SECTION_BUFFS = 'buffs'
SECTION_WEAPONS = 'weapons'
SECTION_CARDS = 'cards'
SECTION_OBJECTS = 'objects'

# Player actions
ACTION_PLAY_CARD = 'play_card'
ACTION_FIRE_WEAPON = 'fire_weapon'
ACTION_END_TURN = 'end_turn'

# COMMON KEYS
P_TYPE = 'type'
P_VALUE = 'value'
P_TARGET = 'target'

""" 
    ===============================================  
                        TARGETS 
    ===============================================
"""
TARGET_SELF = 'self'
# All
TARGET_ALL = 'all'
TARGET_ALL_EXCEPT_SELF = 'all_except'
TARGET_ALL_ENEMIES = 'all_enemies'
TARGET_ALL_ALLIES = 'all_allies'
TARGET_ALL_SHIPS = 'all_ships'

# Separate ships and objects
TARGET_ENEMY_SHIP = 'enemy_ship'
TARGET_ALLY_SHIP = 'ally_ship'

# Special
TARGET_MAX_HEALTH = 'max_health'
TARGET_MIN_HEALTH = 'min_health'
TARGET_MAX_ENERGY = 'max_energy'

# Directional
TARGET_FORWARD = 'forward'
TARGET_FORWARD_ALLY = 'forward_ally'
TARGET_FORWARD_ENEMY = 'forward_enemy'
TARGET_FORWARD_PIERCE = 'forward_pierce'
TARGET_BACKWARD = 'backward'
TARGET_BACKWARD_ALLY = 'backward_ally'
TARGET_BACKWARD_ENEMY = 'backward_enemy'
TARGET_BACKWARD_PIERCE = 'backward_pierce'
""" ===============================================  """

# EFFECTS
EFFECT_TYPE_DAMAGE = 'damage'
EFFECT_TYPE_EDAMAGE = 'edamage'
EFFECT_TYPE_HEAL = 'heal'
EFFECT_TYPE_EHEAL = 'eheal'
EFFECT_TYPE_MOVE = 'position'
EFFECT_TYPE_DISARM = 'disarm'
EFFECT_TYPE_ARM = 'arm'
EFFECT_TYPE_MUTE = 'mute'
EFFECT_TYPE_UNMUTE = 'unmute'
EFFECT_TYPE_LOCK_POSITION = 'lock_position'
EFFECT_TYPE_UNLOCK_POSITION = 'unlock_position'
EFFECT_TYPE_REDUCE_CARDCOST = 'reduce_cardcost'
EFFECT_TYPE_ADD_CARDCOST = 'add_cardcost'
EFFECT_TYPE_DRAW_CARD = 'draw_card'
EFFECT_TYPE_DROP_CARD_OF_TYPE = 'drop_card'
EFFECT_TYPE_REMOVE_CARD = 'remove_card'
EFFECT_TYPE_GAIN_CARD = 'gain_card'
EFFECT_TYPE_DAMAGE_REDUCE = 'damage_reduce'
EFFECT_TYPE_DAMAGE_ADD = 'damage_add'
EFFECT_TYPE_ENERGYGAIN_REDUCE = 'energygain_reduce'
EFFECT_TYPE_ENERGYGAIN_ADD = 'energygain_add'
EFFECT_TYPE_SPAWN = 'spawn'
EFFECT_TYPE_DESTROY = 'destroy'
EFFECT_TYPE_APPLY_BUFF = 'apply_buff'
EFFECT_TYPE_REMOVE_BUFF = 'remove_buff'
EFFECT_TYPE_ENERGY_TEST = 'energy_test'

# Speacial effects
EFFECT_TYPE_SPECIAL_SWAP = 'special_swap'
EFFECT_TYPE_OFFENSE_APPROACH = 'approach'

# Effect properties
P_EFFECT_TYPE = P_TYPE
P_EFFECT_VALUE = P_VALUE
P_EFFECT_TARGET = P_TARGET
P_EFFECT_RANGE = 'range'
P_EFFECT_RANGE_MOD = 'range_mod'
P_EFFECT_SPAWN_POSITION = 'spawn_position'
P_EFFECT_CARD_TYPE = 'card_type'
P_EFFECT_BUFF_DURATION = 'buff_duration'

# Cases
CASE_COLLIDE = 'collide'
CASE_DRAW_CARD = 'draw_card'
CASE_PLAY_CARD = 'play_card'
CASE_DROP_CARD = 'drop_card'
CASE_DESTROYED = 'entity_destroyed'
CASE_OVERLOAD = 'entity_overload'
CASE_ROUND_END = 'turn_end'
CASE_ROUND_START = 'turn_start'

# Event properties
P_CASE_ARG = 'arg'
P_CASE_EFFECTS = 'effects'

# Ship properties
P_SHIP_HP = 'hp'
P_SHIP_MAX_ENERGY = 'max_energy'
P_SHIP_ENERGY_PER_TURN = 'energy_per_turn'
P_SHIP_CARDS = 'cards'

# Weapon properties
P_WEAPON_DESCRIPTION = 'description'
P_WEAPON_FULL_NAME = 'full_name'
P_WEAPON_COST = 'cost'
P_WEAPON_EFFECT = 'effect'
P_WEAPON_CARDS = 'cards'
P_WEAPON_ACTION_OFFENSE = 'offense'
P_WEAPON_ACTION_DEFENSE = 'defense'
P_WEAPON_ACTION_SAME = 'same'
P_WEAPON_TARGET = P_TARGET
P_WEAPON_EFFECTS = 'effects'

# Entities properties
P_OBJECT_FULL_NAME = 'full_name'
P_OBJECT_DESCRIPTION = 'description'
P_OBJECT_CASES = 'cases'

# Buff properties
P_BUFF_FULL_NAME = 'full_name'
P_BUFF_DESCRIPTION = 'description'
P_BUFF_DURATION = 'duration'
P_BUFF_ON_ROUND_EFFECTS = 'turn_effects'
P_BUFF_ON_APPLY_EFFECTS = 'apply_effects'
P_BUFF_ON_REMOVE_EFFECTS = 'remove_effects'
P_BUFF_CASES = 'cases'

# Card type
CARD_TYPE_EVENT = 'event'
CARD_TYPE_SHIP = 'ship'
CARD_TYPE_WEAPON = 'weapon'

# Card properties
P_CARD_ACTION_OFFENSE = 'offense'
P_CARD_ACTION_DEFENSE = 'defense'
P_CARD_ACTION_SAME = 'same'
P_CARD_DECK = 'deck'
P_CARD_TYPE = P_TYPE
P_CARD_COST = 'cost'
P_CARD_FULL_NAME = 'full_name'
P_CARD_DESCRIPTION = 'description'
P_CARD_FLAVOR = 'flavor'
P_CARD_EFFECTS = 'effects'
