# SETTINGS
BOARD_SIZE = 6
INITIAL_A_POSITION = 1
INITIAL_B_POSITION = 5
INITIAL_CARDS = 4
WEAPON_CARDS_EACH = 2
SHIP_CARDS_EACH = 2
EVENT_CARDS_FROM_POOL = 10

# Sections
SECTION_SHIPS = 'ships'
SECTION_BUFFS = 'buffs'
SECTION_WEAPONS = 'weapons'
SECTION_CARDS = 'cards'


# Player actions
ACTION_PLAY_CARD = 'play_card'
ACTION_FIRE_WEAPON = 'fire_weapon'
ACTION_END_TURN = 'end_turn'


# COMMON KEYS
P_TYPE = 'type'
P_VALUE = 'value'
P_TARGET = 'target'

# TARGETS
TARGET_ALL = 'all'
TARGET_ALL_EXCEPT = 'all_except'
TARGET_SELF = 'self'
TARGET_ENEMY = 'enemy'
TARGET_MAX_HEALTH = 'max_health'
TARGET_MAX_ENERGY = 'max_energy'
TARGET_FORWARD = 'forward'
TARGET_BACKWARD = 'backward'
TARGET_FORWARD_PIERCE = 'forward_pierce'
TARGET_BACKWARD_PIERCE = 'backward_pierce'

# EFFECTS
EFFECT_TYPE_DAMAGE = 'damage'
EFFECT_TYPE_EDAMAGE = 'edamage'
EFFECT_TYPE_HEAL = 'heal'
EFFECT_TYPE_EHEAL = 'eheal'
EFFECT_TYPE_POSITION = 'position'
EFFECT_TYPE_DISARM = 'disarm'
EFFECT_TYPE_ARM = 'arm'
EFFECT_TYPE_MUTE = 'mute'
EFFECT_TYPE_UNMUTE = 'unmute'
EFFECT_TYPE_LOCK_POSITION = 'lock_position'
EFFECT_TYPE_UNLOCK_POSITION = 'unlock_position'
EFFECT_TYPE_REDUCE_CARDCOST = 'reduce_cardcost'
EFFECT_TYPE_ADD_CARDCOST = 'add_cardcost'
EFFECT_TYPE_DRAW_CARD = 'draw_card'
EFFECT_TYPE_DROP_CARD = 'drop_card'
EFFECT_TYPE_GAIN_CARD = 'gain_card'
EFFECT_TYPE_DAMAGE_REDUCE = 'damage_reduce'
EFFECT_TYPE_DAMAGE_ADD = 'damage_add'
EFFECT_TYPE_ENERGYGAIN_REDUCE = 'energygain_reduce'
EFFECT_TYPE_ENERGYGAIN_ADD = 'energygain_add'
EFFECT_TYPE_SPAWN = 'spawn'
EFFECT_TYPE_DESTROY = 'destroy'
EFFECT_TYPE_APPLY_BUFF = 'apply_buff'
EFFECT_TYPE_REMOVE_BUFF = 'remove_buff'

# Effect properties
P_EFFECT_TYPE = P_TYPE
P_EFFECT_VALUE = P_VALUE
P_EFFECT_TARGET = P_TARGET
P_EFFECT_RANGE = 'range'
P_EFFECT_RANGE_MOD = 'range_mod'
P_EFFECT_SPAWN_POSITION = 'spawn_position'


# Cases
CASE_COLLIDE = 'collide'
CASE_DRAW_CARD = 'draw_card'
CASE_PLAY_CARD = 'play_card'

# Event properties
P_CASE_ARG = 'arg'
P_CASE_EFFECTS = 'effects'


# Ship properties
P_SHIP_HP = 'hp'
P_SHIP_MAX_ENERGY = 'max_energy'
P_SHIP_ENERGY_PER_TURN = 'energy_per_turn'
P_SHIP_CARDS = 'cards'


ships = {
    'ship1': {
        P_SHIP_HP: 20,
        P_SHIP_MAX_ENERGY: 20,
        P_SHIP_ENERGY_PER_TURN: 1,
        P_SHIP_CARDS: ['card1', 'card2', 'card3'],
    },
}


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

weapons = {
    'mg': {
        P_WEAPON_FULL_NAME: 'Machine gun',
        P_WEAPON_CARDS: ['card1', 'card2', 'card3'],
        P_WEAPON_ACTION_OFFENSE: {
            P_WEAPON_DESCRIPTION: 'Just a machine gun attack',
            P_WEAPON_COST: 2,
            P_WEAPON_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
            ]
        },
        P_WEAPON_ACTION_DEFENSE: {
            P_WEAPON_DESCRIPTION: 'Just a machine gun attack shooting backwards',
            P_WEAPON_COST: 2,
            P_WEAPON_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
            ]
        }
    }
}


# Entities properties
P_ENTITY_FULL_NAME = 'full_name'
P_ENTITY_DESCRIPTION = 'description'
P_ENTITY_EVENTS = 'events'
P_ENTITY_SPEED = 'speed'


entities = {
    'c4': {
        P_ENTITY_FULL_NAME: 'Flying c4',
        P_ENTITY_SPEED: -1,
        P_ENTITY_EVENTS: {
            CASE_PLAY_CARD: {
                P_CASE_ARG: 'detonate',
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                        P_EFFECT_TARGET: TARGET_ALL,
                        P_EFFECT_RANGE: 0,
                        P_EFFECT_VALUE: 5
                    }
                ]
            }
        },
    },
    'mine': {
        P_ENTITY_FULL_NAME: 'Flying mine',
        P_ENTITY_SPEED: -1,
        P_ENTITY_EVENTS: {
            CASE_COLLIDE: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                        P_EFFECT_TARGET: TARGET_ALL,
                        P_EFFECT_RANGE: 0,
                        P_EFFECT_VALUE: 5
                    }
                ]
            }
        },
    }
}


# Buff properties
P_BUFF_FULL_NAME = 'full_name'
P_BUFF_DESCRIPTION = 'description'
P_BUFF_DURATION = 'duration'
P_BUFF_ON_TURN_EFFECTS = 'turn_effects'
P_BUFF_ON_APPLY_EFFECTS = 'apply_effects'
P_BUFF_ON_REMOVE_EFFECTS = 'remove_effects'


buffs = {
    'mute': {
        P_BUFF_FULL_NAME: 'Mute',
        P_BUFF_DESCRIPTION: 'Mutes a target for 1 turn',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_MUTE,
            }
        ],
        P_BUFF_ON_TURN_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE,
            }
        ],
    },
}


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
P_CARD_TARGET = P_TARGET
P_CARD_COST = 'cost'
P_CARD_FULL_NAME = 'full_name'
P_CARD_DESCRIPTION = 'description'
P_CARD_EFFECTS = 'effects'


cards = {
    'some': {
        P_CARD_FULL_NAME: 'IMBA Card',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Some card description',
            P_CARD_COST: 5,
            P_CARD_TARGET: TARGET_ENEMY,
            P_CARD_EFFECTS: [

            ]
        },
        P_CARD_ACTION_DEFENSE: {

        }
    }
}
