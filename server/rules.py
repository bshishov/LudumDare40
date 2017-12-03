# SETTINGS
BOARD_SIZE = 6
INITIAL_A_POSITION = 1
INITIAL_B_POSITION = 4
INITIAL_CARDS = 4
WEAPON_CARDS_EACH = 2
SHIP_CARDS_EACH = 2
EVENT_CARDS_FROM_POOL = 0

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

EFFECTS_WITHOUT_VALUE = [
    EFFECT_TYPE_DRAW_CARD,
    EFFECT_TYPE_DROP_CARD,
    EFFECT_TYPE_LOCK_POSITION,
    EFFECT_TYPE_UNLOCK_POSITION,
    EFFECT_TYPE_MUTE,
    EFFECT_TYPE_UNMUTE,
    EFFECT_TYPE_ARM,
    EFFECT_TYPE_DISARM,
    EFFECT_TYPE_DESTROY,
]

# Effect properties
P_EFFECT_TYPE = P_TYPE
P_EFFECT_VALUE = P_VALUE
P_EFFECT_TARGET = P_TARGET
P_EFFECT_RANGE = 'range'
P_EFFECT_RANGE_MOD = 'range_mod'
P_EFFECT_SPAWN_POSITION = 'spawn_position'
P_EFFECT_CARD_TYPE = 'card_type'


# Cases
CASE_COLLIDE = 'collide'
CASE_DRAW_CARD = 'draw_card'
CASE_PLAY_CARD = 'play_card'
CASE_DROP_CARD = 'drop_card'
CASE_DESTOYED = 'entity_destroyed'
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
P_OBJECT_FULL_NAME = 'full_name'
P_OBJECT_DESCRIPTION = 'description'
P_OBJECT_CASES = 'cases'


objects = {
    'Bomb': {
        P_OBJECT_FULL_NAME: 'Bomb',
        P_OBJECT_DESCRIPTION: 'Just a flying c4',
        P_OBJECT_CASES: {
            CASE_PLAY_CARD: {
                P_CASE_ARG: 'detonate',
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                        P_EFFECT_TARGET: TARGET_ALL,
                        P_EFFECT_VALUE: 5
                    }
                ]
            },
            CASE_ROUND_END: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                        P_EFFECT_TARGET: TARGET_SELF,
                        P_EFFECT_VALUE: -1
                    }
                ]
            }
        },
    },
    'mine': {
        P_OBJECT_FULL_NAME: 'Flying mine',
        P_OBJECT_CASES: {
            CASE_COLLIDE: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                        P_EFFECT_TARGET: TARGET_ALL,
                        P_EFFECT_RANGE: 0,
                        P_EFFECT_VALUE: 5
                    }
                ]
            },
            CASE_ROUND_END: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                        P_EFFECT_TARGET: TARGET_SELF,
                        P_EFFECT_VALUE: -1
                    },
                ]
            }
        },
    },
    'ADrone': {
        P_OBJECT_FULL_NAME: 'Simple attacking drone',
        P_OBJECT_CASES: {
            CASE_ROUND_END: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                        P_EFFECT_TARGET: TARGET_ALL_ENEMIES,
                        P_EFFECT_VALUE: 3
                    },
                ]
            }
        },
    },
    'HDrone': {
        P_OBJECT_FULL_NAME: 'Simple healing drone',
        P_OBJECT_CASES: {
            CASE_ROUND_END: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_HEAL,
                        P_EFFECT_TARGET: TARGET_ALLY_SHIP,
                        P_EFFECT_VALUE: 3
                    },
                ]
            }
        },
    }
}


# Buff properties
P_BUFF_FULL_NAME = 'full_name'
P_BUFF_DESCRIPTION = 'description'
P_BUFF_DURATION = 'duration'
P_BUFF_ON_ROUND_EFFECTS = 'turn_effects'
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
        P_BUFF_ON_ROUND_EFFECTS: [],
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
P_CARD_COST = 'cost'
P_CARD_FULL_NAME = 'full_name'
P_CARD_DESCRIPTION = 'description'
P_CARD_EFFECTS = 'effects'


cards = {
    'Fire all': {
        P_CARD_FULL_NAME: 'Fire all weapons',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Fire all offense description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 6,
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Fire all defense description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1,
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                }
            ]
        }
    },
    'Hamstring': {
        P_CARD_FULL_NAME: 'Hamstring',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Hamstring card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_LOCK_POSITION
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Some card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                }
            ]
        }
    },
    'IRrounds': {
        P_CARD_FULL_NAME: 'Incendiary rounds',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Incendiary card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'on fire'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Incendiary card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }
    },
    'Leak': {
        P_CARD_FULL_NAME: 'Cause a leak',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Leak  card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Leak card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }
    },
    'Bomb': {
        P_CARD_FULL_NAME: 'Bomb',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Bomb  card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Bomb card description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'Bomb'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'Detonate'
                }
            ]
        }

    },
    'Detonate': {
        P_CARD_FULL_NAME: 'Detonate Bomb',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Detonate Bomb card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Bomb card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                            ]
        }
    },
    'Cool': {
        P_CARD_FULL_NAME: 'Cool the gun',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Cool card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Cool card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        }

    },
    'Snipe': {
        P_CARD_FULL_NAME: 'Precise shot',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Cool card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_EDAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_MUTE
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Cool card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                    P_EFFECT_VALUE: 1
                },
            ]
        }

    },
    'Scorch': {
        P_CARD_FULL_NAME: 'Scorch this feathers',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Scorch card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_EDAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'on fire'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Scorch card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
            ]
        }

    },
    'Redirect': {
        P_CARD_FULL_NAME: 'Redirect energy this feathers',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Scorch card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Scorch card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        }

    },
    'EMP': {
        P_CARD_FULL_NAME: 'EMP',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'EMP card description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_EHEAL,
                    P_EFFECT_VALUE: 10
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Scorch card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'EMP'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'Detonate EMP'
                }
            ]
        }

    },
    'Detonate EMP': {
        P_CARD_FULL_NAME: 'Detonate EMP',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Detonate EMP card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Detonate EMP card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                            ]
        }
    },
    'Charging': {
        P_CARD_FULL_NAME: 'Charging my laser',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'laser card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'Fire!'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'laser card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'Fire!'
                }
            ]
        }

    },
    'Fire!': {
        P_CARD_FULL_NAME: 'Fire!',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Fire! card description',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 8
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_EDAMAGE,
                    P_EFFECT_VALUE: 4
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Fire! card description',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 6
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_EDAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }

    },
    'Hold fire': {
        P_CARD_FULL_NAME: 'Hold fire',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Hold fire card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Hold fire card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        }

    },
    'Grapple': {
        P_CARD_FULL_NAME: 'Grapple',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Grapple card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Grapple card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }

    },
    'Lighting rod': {
        P_CARD_FULL_NAME: 'Lighting rod',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Lighting rod card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Lightning rod'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Lighting rod card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                }
            ]
        }

    },
    'Impale': {
        P_CARD_FULL_NAME: 'Impale',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Impale card description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_MUTE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Impale card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                },
            ]
        }

    },
    'Electrocute': {
        P_CARD_FULL_NAME: 'Electrocute',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Electrocute card description',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_EDAMAGE,
                    P_EFFECT_VALUE: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                    P_EFFECT_VALUE: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Electrocute card description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_MUTE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        }

    },
    'Still': {
        P_CARD_FULL_NAME: 'Hold still',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Hold still card description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_LOCK_POSITION,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Hold still card description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_LOCK_POSITION,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                }
            ]
        }

    },
    'Grab': {
        P_CARD_FULL_NAME: 'That\'s mine',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'That\'s mine card description',
            P_CARD_COST: 8,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 5
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'Fix it!'
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_MUTE,
                    P_EFFECT_VALUE: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'That\'s mine card description',
            P_CARD_COST: 8,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 4
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'Spare part'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        }

    },
    'Fix': {
        P_CARD_FULL_NAME: 'Fix it!',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Fix it! card description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_ARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {

        }

    },
    'Spare': {
        P_CARD_FULL_NAME: 'Spare part!',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Spare card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_HEAL,
                    P_EFFECT_VALUE: 4
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Spare card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_HEAL,
                    P_EFFECT_VALUE: 4
                }
            ]
        }

    },
    'Power': {
        P_CARD_FULL_NAME: 'Power up',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Power card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Power card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_ENEMIES,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }

    },
    'Ram': {
        P_CARD_FULL_NAME: 'Ram',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Ram card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 4
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Ram card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 4
                },
            ]
        }

    },
    'EBoost': {
        P_CARD_FULL_NAME: 'Energy boost',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'EBoost card description',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_EHEAL,
                    P_EFFECT_VALUE: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'EBoost card description',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_EHEAL,
                    P_EFFECT_VALUE: 2
                }
            ]
        }

    },
    'Stop': {
        P_CARD_FULL_NAME: 'Full stop',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Stop card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                    P_EFFECT_VALUE: 4
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MUTE,
                    P_EFFECT_VALUE: 1
                },

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Stop card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                    P_EFFECT_VALUE: 4
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MUTE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }

    },
    'TaB': {
        P_CARD_FULL_NAME: 'Turn and burn',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'TaB card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_ARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_REDUCE_CARDCOST,
                    P_EFFECT_VALUE: 1
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'TaB card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_ARM
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_REDUCE_CARDCOST,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                }
            ]
        }

    },
    'Barrel': {
        P_CARD_FULL_NAME: 'Barrel roll',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Barrel card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Barrel card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }

    },
    'missile': {
        P_CARD_FULL_NAME: 'Hardpoint missile',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'missile card description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'missile card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM,
                    P_EFFECT_VALUE: 1
                }
            ]
        }

    },
    'Wingdrone': {
        P_CARD_FULL_NAME: 'Wingdrone',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Wingdrone card description',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'ADrone'
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Wingdrone card description',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'ADrone'
                }
            ]
        }

    },
    'Mine': {
        P_CARD_FULL_NAME: 'Floating mine',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Mine card description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'Mine'
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Mine card description',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'Mine'
                }
            ]
        }

    },
    'Healdrone': {
        P_CARD_FULL_NAME: 'Little Drone Helper',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Healdrone card description',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'HDrone'
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Healdrone card description',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'HDrone'
                }
            ]
        }

    },
    'Reactor': {
        P_CARD_FULL_NAME: 'Cool the reactor',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Reactor card description',
            P_CARD_COST: 6,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                    P_EFFECT_VALUE: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Reactor card description',
            P_CARD_COST: 6,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                    P_EFFECT_VALUE: 2
                }
            ]
        }

    },
    'Core': {
        P_CARD_FULL_NAME: 'Power to the core',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Core card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_REDUCE_CARDCOST,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Core card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_REDUCE_CARDCOST,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }

    },
    'Sandstorm': {
        P_CARD_FULL_NAME: 'Sandstorm',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Sandstorm card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Sandstorm card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [

            ]
        }

    },
    'Thunder': {
        P_CARD_FULL_NAME: 'Thunder and Lightning',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Thunder card description',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Thunder card description',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [

            ]
        }

    },
    'Tornado': {
        P_CARD_FULL_NAME: 'Tornado',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Tornado card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Tornado card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [

            ]
        }

    },
    'Sidewind': {
        P_CARD_FULL_NAME: 'Sidewind',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Sidewind card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Sidewind card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                 {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                 }
            ]
        }
    },
    'Wingman': {
        P_CARD_FULL_NAME: 'Wingman\'s help',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Sidewind card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                    P_EFFECT_VALUE: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Sidewind card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD_ENEMY,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3
                }
            ]
        }
    },
    'Flare': {
        P_CARD_FULL_NAME: 'Solar flare',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'flare card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_ENEMIES,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                    P_EFFECT_VALUE: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'flare card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_ENEMIES,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                    P_EFFECT_VALUE: 2
                }
            ]
        }
    },
    'Meteor shower': {
        P_CARD_FULL_NAME: 'Solar flare',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'flare card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {


                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'flare card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {


                }
            ]
        }
    },
    'Geomagnetic': {
        P_CARD_FULL_NAME: 'Geomagnetic storm',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Geomagnetic card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {


                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Geomagnetic card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {


                }
            ]
        }
    },
    'Fog': {
        P_CARD_FULL_NAME: 'Fog',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Fog card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {


                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Fog card description',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {


                }
            ]
        }
    },
    'Bursts': {
        P_CARD_FULL_NAME: 'Energy microbursts',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Bursts card description',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_EHEAL,
                    P_EFFECT_VALUE: 4
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_MUTE
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Bursts card description',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_EHEAL,
                    P_EFFECT_VALUE: 4
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_DISARM
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_MUTE
                }
            ]
        }
    },
    'Birds': {
        P_CARD_FULL_NAME: 'Bird flock',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Birds card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'birds'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Birds card description',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'birds'
                }
            ]
        }
    },
    'Headwind': {
        P_CARD_FULL_NAME: 'Headwind',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Headwind card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Headwind card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                }
            ]
        }
    },
    'Tailwind': {
        P_CARD_FULL_NAME: 'Tailwind',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Tailwind card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Tailwind card description',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }
    }

}
