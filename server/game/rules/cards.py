from game.rules.settings import *

cards = {
    'Fire all': {
        P_CARD_FULL_NAME: 'Fire all weapons',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Fire all weapons and deal 6 damage + range modifier',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 6,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Fire all weapons in blank and move yourself back by 1 position, '
                                'dealing 1 damage to yourself and 3 to opponent + range modifier',
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
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }
            ]
        }
    },
    'Hamstring': {
        P_CARD_FULL_NAME: 'Hamstring',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Aim for the wings and deal 3 damage + range modifier,'
                                ' also restricting the enemy movement for 2 turns',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'lock_position2'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Aim for the engines, dealing 2 damage '
                                '+ range modifier and move enemy back by 1 position',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
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
            P_CARD_DESCRIPTION: 'Fire incendiary bullets, dealing 3 damage + range modifier and'
                                'put the enemy on fire, dealing 1 damage per turn for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'on fire'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Shoot tracer bullets in your enemies windshield,'
                                ' blinding them and reducing damage by 1 for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage1_reduce2'
                }
            ]
        }
    },
    'Leak': {
        P_CARD_FULL_NAME: 'Cause a leak',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Shoot the enemies tanks, dealing 2 damage + range modifier'
                                'moving them back by 1 position and causing them to get 1 less energy for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'energygain2_reduce1'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Shoot the enemies tanks, causing them to get 1 less energy for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'energygain2_reduce1'
                }
            ]
        }
    },
    'Bomb': {
        P_CARD_FULL_NAME: 'Bomb',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Drop a bomb behind and detonate it instantly to give '
                                'you a boost. You take 2 damage and move forward by 2 positions',
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
            P_CARD_DESCRIPTION: 'Drop a bomb, that will fly towards your enemy and get'
                                ' a "Detonate" card, that deals damage to all objects in a small radius',
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
            P_CARD_DESCRIPTION: 'Detonate the bomb, dealing 6 damage to everyone near it',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Detonate the bomb, dealing 6 damage to everyone near it',
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
            P_CARD_DESCRIPTION: 'Let your weapon cool for a while. Draw a card. '
                                'You can\'t use weapon cards for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm2'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Let your weapon cool for a while. Draw a card. '
                                'You can\'t use weapon cards for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm2'
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
            P_CARD_DESCRIPTION: 'Aim for a weak spot and deal 3 damage + range modifier, 2 energy damage'
                                ' and forbid enemy to use ship cards for 2 turns',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_EDAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute2'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Strike precisely through windshield and deal 2 damage + '
                                'range modifier. Enemy deals 1 damage less for turn.',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,

                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage1_reduce1'
                }
            ]
        }

    },
    'Scorch': {
        P_CARD_FULL_NAME: 'Scorch this feathers',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Scorch the inflammable parts of the ship, dealing 1 damage + range modifier'
                                ', 2 energy damage and make it burn, dealing 1 damage for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
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
            P_CARD_DESCRIPTION: 'Boil the clouds before you, dealing 2 damage to everyone'
                                ' and forbidding every player to play weapon cards for 1 turn',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm1'
                },
            ]
        }

    },
    'Redirect': {
        P_CARD_FULL_NAME: 'Redirect energy',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Redirect your energy from weapons to ship. Regain the ability to use ship cards and '
                                'forbid yourself to use weapon cards. Draw a card',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm1'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Redirect your energy from weapons to ship. Regain the ability to use ship cards and '
                                'forbid yourself to use weapon cards. Draw a card',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE,
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm1'
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
            P_CARD_DESCRIPTION: 'Detonate the EMP in proximity to own ship, gaining 10 energy.'
                                ' You can\'t use weapon cards for 1 round',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_EHEAL,
                    P_EFFECT_VALUE: 10
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm1'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Drop an EMP, that flies to enemy and gain the card "Detonate EMP"'
                                ', that allows you to deal massive energy damage to enemy ship',
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
            P_CARD_DESCRIPTION: 'Detonate EMP, dealing 2 damage, 6 energy damage '
                                'and prohibiting them to use ship cards for 1 turn',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Detonate EMP, dealing 2 damage, 6 energy damage '
                                'and prohibiting them to use ship cards for 1 turn',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                            ]
        }
    },
    'Charging': {
        P_CARD_FULL_NAME: 'Chargin\' ma laser!',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You charge your weapon to deal 8 damage + '
                                'range modifier on command. You can\'t use weapon for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm2'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'Fire!'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You charge your weapon to deal 8 damage + '
                                'range modifier on command. You can\'t use weapon for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm2'
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
            P_CARD_DESCRIPTION: 'You release the charge and deal 8 damage + range modifier, 4 energy damage to everyone'
                                ' in front of you and move by 1 position backwards',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 8,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
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
            P_CARD_DESCRIPTION: 'You release the charge and deal 6 damage + range modifier, 2 energy damage to everyone'
                                ' behind you and move by 1 position forward',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 6,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
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
            P_CARD_DESCRIPTION: 'Prepare yourself for battle. You can\'t use weapons for 2 rounds,'
                                ' but increase your damage by 2 for 3 rounds and draw a card',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm2'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage3_add2'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Prepare yourself for battle. You can\'t use weapons for 2 rounds,'
                                ' but increase your damage by 2 for 3 rounds and draw a card',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm2'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage3_add2'
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
            P_CARD_DESCRIPTION: 'Deal 1 damage + range modifier, pooling your enemy closer',
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
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Deal 1 damage + range modifier, pooling your enemy closer',
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
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }
            ]
        }

    },
    'Lighting rod': {
        P_CARD_FULL_NAME: 'Lighting rod',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Shoot your enemy in the reactor, causing them to take 1 damage for every attempt to '
                                'play ship or weapon card. Deal 2 damage + range modifier',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Lightning rod'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Shoot your enemy in the reactor, causing them to take 1 damage for every attempt to '
                                'play ship or weapon card. Deal 2 damage + range modifier',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'lightning_rod'
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }
            ]
        }

    },
    'Impale': {
        P_CARD_FULL_NAME: 'Impale',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Impale all enemies in front of you, dealing 3 damage + range modifier'
                                ', move them forward by 1 position and forbid to use ship cards for 1 turn',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute1'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Impale all enemies behind of you, dealing 2 damage + range modifier'
                                ' and move them backwards by 1 position',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD_PIERCE,
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
            P_CARD_DESCRIPTION: 'Shoot the enemy with electrified harpoon, decrease their energy gain by 2 for 2 turns '
                                'and increase yours equally. Deal 1 damage + range modifiers and 3 energy damage.',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_EDAMAGE,
                    P_EFFECT_VALUE: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'energygain2_reduce2'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'energygain2_add2'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Electrocute the enemy\'s reactor, forbidding them to use ship and weapon cards for 1 '
                                'turn. Deal 3 damage + range modifier and draw a card.',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm1'
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute1'
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
            P_CARD_DESCRIPTION: 'Shoot a harpoon with a rope, moving enemy further and '
                                'forbidding both of you from moving for 1 turn. Deal 3 damage + range modifier',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL_SHIPS,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'lock_position1'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Shoot a harpoon with a rope, moving enemy further and '
                                'forbidding both of you from moving for 1 turn. Deal 3 damage + range modifier',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 3,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL_SHIPS,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'lock_position1'
                }
            ]
        }

    },
    'Grab': {
        P_CARD_FULL_NAME: 'That\'s mine',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You tear off a vital part of enemy ship, dealing 5 damage + range modifier and '
                                'forbidding them to play weapon and ship cards. Enemy gets a "Fix it!" card '
                                'to handle this situation',
            P_CARD_COST: 8,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 5,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'Fix it!'
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm2'
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute2'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You tear off a "Spare part" from enemy ship, dealing 4 damage + range modifier and'
                                ' draw a card. You can use "Spare part" card to heal yourself',
            P_CARD_COST: 8,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 4,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
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
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Fix it right now! Returns you the ability to play all cards',
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
            P_CARD_DESCRIPTION: 'Fix it right now! Returns you the ability to play all cards',
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
        }

    },
    'Spare': {
        P_CARD_FULL_NAME: 'Spare part!',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Use it to quickly fix your ship and get 4 HP',
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
            P_CARD_DESCRIPTION: 'Use it to quickly fix your ship and get 4 HP',
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
            P_CARD_DESCRIPTION: 'Use the ship\'s special reserve to power up your weapon. '
                                'Increase all damage by 1 for this turn',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage1_add1'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Use the ship\'s special reserve to power up your armor. '
                                'Decrease enemy ship damage by 1 for 2 turns',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage2_reduce1'
                },
            ]
        }

    },
    'Ram': {
        P_CARD_FULL_NAME: 'Ram',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Ram yourself into everything in front of you. Deal 4 damage + range modifier,'
                                ' take 2 damage and move forward by 1 position',
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
                    P_EFFECT_VALUE: 4,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Ram yourself into everything behind you. Deal 4 damage + range modifier,'
                                ' take 2 damage and move backwards by 1 position',
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
                    P_EFFECT_TARGET: TARGET_BACKWARD_PIERCE,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 4,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
            ]
        }

    },
    'EBoost': {
        P_CARD_FULL_NAME: 'Energy boost',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Sacrifice ship integrity to get 2 energy. Take 1 damage',
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
            P_CARD_DESCRIPTION: 'Sacrifice ship integrity to get 2 energy. Take 1 damage',
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
            P_CARD_DESCRIPTION: 'Turn off all the ship systems. You can\'t play ship and weapon cards, move back by 2 '
                                'positions, but also draw a card and increase energy gain by 2 for 2 rounds',
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
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'energygain2_add2'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm1'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MUTE,
                    P_EFFECT_VALUE: 1
                },

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Turn off all the ship systems. You can\'t play ship and weapon cards, move back by 2 positions'
                                ', but also draw a card and increase energy gain by 2 for 2 rounds',
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
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'energygain2_add2'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm1'
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
            P_CARD_DESCRIPTION: 'You take a vantage point. Move 1 forward, regain the ability to play weapon cards and '
                                'reduce card cost for 1 turn',
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
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'cardcost_reduce1'
                },

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You take a sudden turn, regain the ability to play weapon cards, move backwards,'
                                ' reduce card cost for 1 turn and deal 2 damage + range modifier to anyone behind',
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
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'cardcost1_reduce1'
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }
            ]
        }

    },
    'Barrel': {
        P_CARD_FULL_NAME: 'Barrel roll',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You do a barrel roll and safely move 1 forward, deal 1 damage + range modifier'
                                ' and draw a card',
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
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You do a barrel roll and safely move 1 forward, deal 1 damage + range modifier'
                                ' and draw a card',
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
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }
            ]
        }

    },
    'missile': {
        P_CARD_FULL_NAME: 'Hardpoint missile',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You fire a missile, pushing enemy away by 1 position and'
                                'dealing 3 damage',
            P_CARD_COST: 2,
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
            P_CARD_DESCRIPTION: 'You fire a missile forward, exploding it in distance.'
                                ' No one can use weapon cards for 1 turn',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm1'
                },
            ]
        }

    },
    'Wingdrone': {
        P_CARD_FULL_NAME: 'Wingdrone',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Summon an attack drone behind you. It will attack enemy in front of you for 3 turns',
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
            P_CARD_DESCRIPTION: 'Summon an attack drone behind you. It will attack enemy in front of you for 3 turns',
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
            P_CARD_DESCRIPTION: 'You shoot out a floating mine in 2 positions in front of you. Anyone colliding with'
                                ' it will take 5 damage',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'mine'
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You shoot out a floating mine in 2 positions behind you. Anyone colliding with'
                                ' it will take 5 damage',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'mine'
                }
            ]
        }

    },
    'Healdrone': {
        P_CARD_FULL_NAME: 'Little Drone Helper',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You summon a healing drone behind you. It will heal you for 3 turns',
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
            P_CARD_DESCRIPTION: 'You summon a healing drone behind you. It will heal you for 3 turns',
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
            P_CARD_DESCRIPTION: 'You release energy from reactor and draw 2 cards. '
                                'Energy gain reduced by 2 for 2 rounds.',
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
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'energygain2_reduce2'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You release energy from reactor and draw 2 cards. '
                                'Energy gain reduced by 2 for 2 rounds.',
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
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'energygain2_reduce2'
                },
            ]
        }

    },
    'Core': {
        P_CARD_FULL_NAME: 'Power to the core',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You redirect the energy from weapons to reactor. '
                                'Your damage and card cost reduced for 2 turns',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'cardcost_reduce2'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage2_reduce1'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You redirect the energy from weapons to reactor. '
                                'Your damage and card cost reduced for 2 turns',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'cardcost_reduce2'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage2_reduce1'
                },
            ]
        }

    },
    'Sandstorm': {
        P_CARD_FULL_NAME: 'Sandstorm',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Sudden sandstorm strikes the enemy ship for 2 damage',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Sudden sandstorm pushes your enemy on your'
                                ' position and you take a position behind them. Everyone takes 2 damage',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPECIAL_SWAP
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                }
            ]
        }

    },
    'Thunder': {
        P_CARD_FULL_NAME: 'Thunder and Lightning',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Thunderbolt is attracted to energy. Ship with higher energy takes 2 damage',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_MAX_ENERGY,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Thunderbolt is attracted to energy. Ship with higher energy takes 2 damage',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_MAX_ENERGY,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                }
            ]
        }

    },
    'Tornado': {
        P_CARD_FULL_NAME: 'Tornado',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Tornado brings chaos and ships clash in the eye of the storm. Ship with less HP takes '
                                '2 damage. You move 3 positions forward and enemy moves 3 positions back.',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_MIN_HEALTH,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL_ALLIES,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL_ENEMIES,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -3
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Tornado brings chaos and ships clash in the eye of the storm. Ship with less HP takes '
                                '2 damage. You move 3 positions backwards and enemy moves 3 positions forward.',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_MIN_HEALTH,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL_ENEMIES,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL_ALLIES,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -3
                }
            ]
        }

    },
    'Sidewind': {
        P_CARD_FULL_NAME: 'Sidewind',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'It\'s hard enough to control the ship when sidewind strikes,'
                                ' so no shooting for 1 round. Both of you can\'t use weapon cards',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm1'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'It\'s hard enough to control the ship when sidewind strikes,'
                                ' so no shooting for 1 round. Both of you can\'t use weapon cards',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm1'
                },
            ]
        }
    },
    'Wingman': {
        P_CARD_FULL_NAME: 'Wingman\'s help',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Ally shows up to help you finish the prey. Damage increased by 2 for this turn',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage1_add2'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Ally shows up to help you deal with a pursuing enemy. They deal 3 damage to enemy ship',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
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
            P_CARD_DESCRIPTION: 'Solar flare blinds everyone who looks at it. Gladly, you wear your glasses. '
                                'Everyone\'s but yours damage reduced by 2 for 1 round.',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_EXCEPT_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage1_reduce2'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Solar flare blinds everyone who looks at it. Gladly, you wear your glasses. '
                                'Everyone\'s but yours damage reduced by 2 for 1 round.',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_EXCEPT_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage1_reduce2'
                },
            ]
        }
    },
    'Meteor': {
        P_CARD_FULL_NAME: 'Meteor shower',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Sometimes a hull full of holes is convenient - rocks just fly right through it!'
                                'Ship with most health takes 2 damage',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_MAX_HEALTH,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Sometimes a hull full of holes is convenient - rocks just fly right through it!'
                                'Ship with most health takes 2 damage',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_MAX_HEALTH,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                }
            ]
        }
    },
    'Geomagnetic': {
        P_CARD_FULL_NAME: 'Geomagnetic storm',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'The geomagnetic interference hits you hard. Everyone takes 10 energy damage. '
                                'When energy ends you take HP damage instead',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_SHIPS,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGY_TEST
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'The geomagnetic interference hits you hard. Everyone takes 10 energy damage. '
                                'When energy ends you take HP damage instead',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_SHIPS,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGY_TEST
                }
            ]
        }
    },
    'Fog': {
        P_CARD_FULL_NAME: 'Fog',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'It\'s hard to track your position in fog. '
                                'Attacker takes a position right behind a defender',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_OFFENSE_APPROACH
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'It\'s hard to track your position in fog. '
                                'Attacker takes a position right behind a defender',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_OFFENSE_APPROACH
                }
            ]
        }
    },
    'Bursts': {
        P_CARD_FULL_NAME: 'Energy microbursts',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'It\'s good to have a spare energy, right? Right?!'
                                ' Everyone gets 4 energy, but can\'t play weapon and ship cards',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_EHEAL,
                    P_EFFECT_VALUE: 4
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm1'
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute1'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'It\'s good to have a spare energy, right? Right?!'
                                ' Everyone gets 4 energy, but can\'t play weapon and ship cards',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_EHEAL,
                    P_EFFECT_VALUE: 4
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'Disarm1'
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute1'
                },
            ]
        }
    },
    'Birds': {
        P_CARD_FULL_NAME: 'Bird flock',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Birds move from the north and deal 2 damage to everyone on the same position as them',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'Birds'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Birds move from the north and deal 2 damage to everyone on the same position as them',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'Birds'
                }
            ]
        }
    },
    'Headwind': {
        P_CARD_FULL_NAME: 'Headwind',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Headwind moves you 1 position back',
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
            P_CARD_DESCRIPTION: 'Headwind moves you 1 position back',
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
            P_CARD_DESCRIPTION: 'Tailwind moves you 1 position forward',
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
            P_CARD_DESCRIPTION: 'Tailwind moves you 1 position forward',
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
