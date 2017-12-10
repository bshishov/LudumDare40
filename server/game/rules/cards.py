from game.rules.settings import *

cards = {
    'fire_all': {
        P_CARD_FULL_NAME: 'Fire all weapons',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Fire all weapons and deal 6 base dmg',
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
            P_CARD_DESCRIPTION: 'Fire all weapons in blank. Move yourself backwards by 1, take 1 dmg and deal 4 base dmg',
            P_CARD_COST: 3,
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
                    P_EFFECT_VALUE: 4,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }
            ]
        }
    },
    'hamstring': {
        P_CARD_FULL_NAME: 'Hamstring',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Aim for the wings and deal 3 base dmg. Lock enemy position for 2 turns',
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
                    P_EFFECT_VALUE: 'lock_position',
                    P_EFFECT_BUFF_DURATION: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Aim for the engines, dealing 2 base dmg and move enemy back by 1 position',
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
    'irounds': {
        P_CARD_FULL_NAME: 'Incendiary rounds',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 3 base dmg and put the enemy on fire, dealing 2 damage per turn for 2 turns',
            P_CARD_COST: 4,
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
                    P_EFFECT_VALUE: 'on_fire',
                    P_EFFECT_BUFF_DURATION: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Blind your enemy and reduce their damage by 1 for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage_reduce1',
                    P_EFFECT_BUFF_DURATION: 2
                }
            ]
        }
    },
    'leak': {
        P_CARD_FULL_NAME: 'Cause a leak',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 2 base dmg, move enemy back by 1 and cause them to get 1 less energy for 2 turns',
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
                    P_EFFECT_VALUE: 'energygain_reduce1',
                    P_EFFECT_BUFF_DURATION: 2
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
                    P_EFFECT_VALUE: 'energygain_reduce1',
                    P_EFFECT_BUFF_DURATION: 2
                }
            ]
        }
    },
    'bomb': {
        P_CARD_FULL_NAME: 'Bomb',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Take 2 dmg and move forward by 2',
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
            P_CARD_DESCRIPTION: 'Drop a bomb to detonate it later and deal damage to all objects in a small radius',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'bomb'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'detonate'
                }
            ]
        }

    },
    'detonate': {
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
    'cool': {
        P_CARD_FULL_NAME: 'Cool the gun',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Draw a card. disarm yourself for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Draw a card. disarm yourself for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        }

    },
    'snipe': {
        P_CARD_FULL_NAME: 'Precise shot',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 3 base dmg, 2 energy dmg and mute enemy for 2 turns',
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
                    P_EFFECT_VALUE: 'mute',
                    P_EFFECT_BUFF_DURATION: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Deal 2 base dmg. Enemy deals 1 dmg less for 1 turn.',
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
                    P_EFFECT_VALUE: 'damage_reduce1',
                    P_EFFECT_BUFF_DURATION: 1
                }
            ]
        }

    },
    'scorch': {
        P_CARD_FULL_NAME: 'Scorch this feathers',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 1 base dmg, 2 energy dmg and make enemy burn, dealing 1 dmg for 2 turns',
            P_CARD_COST: 4,
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
                    P_EFFECT_TYPE: EFFECT_TYPE_EDAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'on_fire'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Deal 2 dmg and disarm everyone for 1 turn',
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
                    P_EFFECT_VALUE: 'disarm'
                },
            ]
        }

    },
    'redirect': {
        P_CARD_FULL_NAME: 'Redirect energy',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Unmute and disarm yourself. Draw a card',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Unmute and disarm yourself. Draw a card',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE,
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        }

    },
    'emp': {
        P_CARD_FULL_NAME: 'EMP',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Detonate the EMP in proximity to own ship, gaining 10 energy. disarm (self) for 1 round',
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
                    P_EFFECT_VALUE: 'disarm'
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Drop an EMP, detonate it later to deal massive energy damage to enemy ship',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'emp',
                    P_EFFECT_SPAWN_POSITION: -1
                },

                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'detonate_emp'
                }
            ]
        }

    },
    'detonate_emp': {
        P_CARD_FULL_NAME: 'Detonate EMP',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Detonate EMP, deal 2 damage, 6 energy damage and mute them for 1 turn',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Detonate EMP, deal 2 damage, 6 energy damage and mute them for 1 turn',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                            ]
        }
    },
    'charging': {
        P_CARD_FULL_NAME: 'Chargin\' ma laser!',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You charge your weapon to deal 8 base damage on command. disarm (self) for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'fire'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You charge your weapon to deal 6 base damage on command. disarm (self) for 2 turns',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_GAIN_CARD,
                    P_EFFECT_VALUE: 'fire'
                }
            ]
        }

    },
    'fire': {
        P_CARD_FULL_NAME: 'Fire!',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 8 base dmg. 4 energy damage to everyone afore you and move by 1 position backwards',
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
            P_CARD_DESCRIPTION: 'Deal 6 base dmg, 2 energy damage to everyone behind you and move by 1 position forward',
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
    'hold_fire': {
        P_CARD_FULL_NAME: 'Hold fire',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'disarm yourself fo 2 turns but increase your damage by 2 for 3 rounds and draw a card',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage_add2',
                    P_EFFECT_BUFF_DURATION: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'disarm yourself fo 2 turns but increase your damage by 2 for 3 rounds and draw a card',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage_add2',
                    P_EFFECT_BUFF_DURATION: 3
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        }

    },
    'grapple': {
        P_CARD_FULL_NAME: 'Grapple',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 1 base dmg., pooling your enemy closer',
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
            P_CARD_DESCRIPTION: 'Deal 1 base dmg., pooling your enemy closer',
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
    'lighting_rod': {
        P_CARD_FULL_NAME: 'Lighting rod',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 2 base dmg and make your opponent take 2 damage when they play cards for 1 turn',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'lightning_rod'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Deal 2 base dmg and make your opponent take 2 damage when they play cards for 1 turn',
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
    'impale': {
        P_CARD_FULL_NAME: 'Impale',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 3 base dmg to anyone afore you, move them forward by 1 and apply mute for 1 turn',
            P_CARD_COST: 3,
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
                    P_EFFECT_VALUE: 'mute',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Impale all enemies behind you, dealing 2 base dmg and move them backwards by 1',
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
    'electrocute': {
        P_CARD_FULL_NAME: 'Electrocute',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Reduce enemy\'s energy gain by 2 and add it to yours. Deal 1 base dmg and 3 energy dmg.',
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
                    P_EFFECT_VALUE: 'energygain_reduce2',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'energygain_add2',
                    P_EFFECT_BUFF_DURATION: 2
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'disarm and mute your enemy for 1 turn. Deal 3 base dmg. and draw a card.',
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
                    P_EFFECT_VALUE: 'disarm'
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute',
                    P_EFFECT_BUFF_DURATION: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        }

    },
    'still': {
        P_CARD_FULL_NAME: 'Hold still',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 3 base dmg, move enemy further and lock both ships\' positions',
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
                    P_EFFECT_VALUE: 'lock_position',
                    P_EFFECT_BUFF_DURATION: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Deal 3 base dmg, move enemy further and lock both ships\' positions',
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
                    P_EFFECT_VALUE: 'lock_position',
                    P_EFFECT_BUFF_DURATION: 1
                }
            ]
        }

    },
    'grab': {
        P_CARD_FULL_NAME: 'That\'s mine',
        P_CARD_TYPE: CARD_TYPE_WEAPON,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 5 base dmg., disarm and mute your enemy. Enemy gets a "Fix it!" card',
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
                    P_EFFECT_VALUE: 'fix'
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute',
                    P_EFFECT_BUFF_DURATION: 2
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Deal 4 base dmg, draw a card. Gain "Spare part" card, that heals you when played',
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
                    P_EFFECT_VALUE: 'spare'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                }
            ]
        }

    },
    'fix': {
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
    'spare': {
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
    'power': {
        P_CARD_FULL_NAME: 'Power up',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Increase your damage by 1 for this turn',
            P_CARD_FLAVOR: 'Use the ship\'s special reserve to power up your weapon.',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage_add1',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Decrease enemy ship damage by 1 for 2 turns',
            P_CARD_FLAVOR: 'Use the ship\'s special reserve to power up your armor.',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage_reduce1',
                    P_EFFECT_BUFF_DURATION: 2
                },
            ]
        }

    },
    'ram': {
        P_CARD_FULL_NAME: 'Ram',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 4 base dmg., take 2 damage and move forward by 1 position',
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
            P_CARD_DESCRIPTION: 'Deal 4 base dmg., take 2 damage and move backwards by 1 position',
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
    'eboost': {
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
    'stop': {
        P_CARD_FULL_NAME: 'Full stop',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'disarm and mute, move back by 2. Draw a card and increase energy gain by 2 for 2 rounds',
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
                    P_EFFECT_VALUE: 'energygain_add2',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute',
                    P_EFFECT_BUFF_DURATION: 1
                },

            ]
        },

        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'disarm and mute, move back by 2. Draw a card and increase energy gain by 2 for 2 rounds',
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
                    P_EFFECT_VALUE: 'energygain_add2',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute',
                    P_EFFECT_BUFF_DURATION: 1
                }
            ]
        }

    },
    'explode': {
        P_CARD_FULL_NAME: 'Explode',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Take 2 dmg, draw a card. Created debris deals 3 damage to everyone in it\'s radius',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_BUFF_DURATION: 'debris'
                }

            ]
        },

        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Take 2 dmg, draw a card. Created debris deals 3 damage to everyone in it\'s radius',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_BUFF_DURATION: 'debris'
                }
            ]
        }

    },
    'armoffense': {
        P_CARD_FULL_NAME: 'Armored offense',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'For 4 rounds you will move forward 1 position per turn',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'marcho'
                }
            ]
        },

        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'For 4 rounds you will move backwards 1 position per turn',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'marchd'
                }
            ]
        }

    },

    'tab': {
        P_CARD_FULL_NAME: 'Turn and burn',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You take a vantage point. Move 1 forward, rearm and reduce card cost for 1 turn',
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
                    P_EFFECT_VALUE: 'cardcost_reduce1',
                    P_EFFECT_BUFF_DURATION: 1
                },

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Rearm, move back, reduce card cost for 1 turn and deal 2 base dmg. to anyone behind',
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
                    P_EFFECT_VALUE: 'cardcost_reduce1',
                    P_EFFECT_BUFF_DURATION: 1
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
    'barrel': {
        P_CARD_FULL_NAME: 'Barrel roll',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You do a barrel roll and safely move 1 forward, deal 1 base dmg. and draw a card',
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
            P_CARD_DESCRIPTION: 'You do a barrel roll and safely move 1 forward, deal 1 base dmg. and draw a card',
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
            P_CARD_DESCRIPTION: 'You fire a missile, pushing enemy away by 1 position and dealing 3 damage',
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
            P_CARD_DESCRIPTION: 'You fire a missile, exploding it in distance. No one can use weapon cards for 1 turn',
            P_CARD_COST: 1,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        }

    },
    'wingdrone': {
        P_CARD_FULL_NAME: 'Wingdrone',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Summon an attack drone behind you. It will attack enemy in front of you for 3 turns',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'adrone'
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Summon an attack drone behind you. It will attack enemy in front of you for 3 turns',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'adrone'
                }
            ]
        }

    },
    'maneuver': {
        P_CARD_FULL_NAME: 'Offensive maneuver',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You deal 1 base damage, move forward and deal 1 base damage again',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                },
            ]
        },

        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You deal 1 base damage, move backwards and deal 1 base damage again',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                },
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                },
            ]
        }

    },
    'sonic': {
        P_CARD_FULL_NAME: 'Sonic boost',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You drop random ship card, move forward by 2 and deny enemy from moving fo 1 turn',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DROP_CARD_OF_TYPE,
                    P_EFFECT_VALUE: 'ship'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'lock_position',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        },

        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You drop random ship card, move forward by 2 and deny enemy from moving fo 1 turn',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DROP_CARD_OF_TYPE,
                    P_EFFECT_VALUE: 'ship'
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'lock_position',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        }

    },
    'mine': {
        P_CARD_FULL_NAME: 'Floating mine',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Place a floating mine in 2 positions in front of you. Mine deals 5 damage on collide.',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'mine'
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Place a floating mine in 2 positions behind you. Mine deals 5 damage on collide.',
            P_CARD_COST: 4,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'mine'
                }
            ]
        }

    },
    'healdrone': {
        P_CARD_FULL_NAME: 'Little Drone Helper',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'You summon a healing drone behind you. It will heal you for 3 turns',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'hdrone'
                }

            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'You summon a healing drone behind you. It will heal you for 3 turns',
            P_CARD_COST: 5,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'hdrone'
                }
            ]
        }

    },
    'reactor': {
        P_CARD_FULL_NAME: 'Cool the reactor',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Draw 2 cards. Energy gain reduced by 2 for 2 rounds.',
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
                    P_EFFECT_VALUE: 'energygain_reduce2',
                    P_EFFECT_BUFF_DURATION: 2
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Draw 2 cards. Energy gain reduced by 2 for 2 rounds.',
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
                    P_EFFECT_VALUE: 'energygain_reduce2',
                    P_EFFECT_BUFF_DURATION: 2
                },
            ]
        }

    },
    'core': {
        P_CARD_FULL_NAME: 'Power to the core',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Damage reduced by 2. Card cost reduced by 2',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'cardcost_reduce2',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage_reduce2',
                    P_EFFECT_BUFF_DURATION: 2
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Damage reduced by 2. Card cost reduced by 2',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'cardcost_reduce2',
                    P_EFFECT_BUFF_DURATION: 2
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage_reduce2',
                    P_EFFECT_BUFF_DURATION: 2
                },
            ]
        }

    },
    'closer': {
        P_CARD_FULL_NAME: 'Get closer',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Move 1 forward and draw a card',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },

        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Move 1 backwards and draw a card',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_DRAW_CARD
                },
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                }
            ]
        }
    },
    'wgenerator': {
        P_CARD_FULL_NAME: 'Wind generator',
        P_CARD_TYPE: CARD_TYPE_SHIP,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Spawn a wind generator behind enemy ship that pushes everyone in a small radius backwards',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'wgenerator',
                    P_EFFECT_SPAWN_POSITION: -1
                }
            ]
        },

        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Spawn a wind generator before enemy ship that pushes everyone in a small radius backwards',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'wgenerator',
                    P_EFFECT_SPAWN_POSITION: 1
                }
            ]
        }
    },
    'sandstorm': {
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
            P_CARD_DESCRIPTION: 'Enemy takes your position. You move 1 position back. Everyone takes 2 damage',
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
    'thunder': {
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
    'tornado': {
        P_CARD_FULL_NAME: 'Tornado',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Ship with less HP takes 2 dmg. You move forward by 3 and enemy moves backwards by 3.',
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
            P_CARD_DESCRIPTION: 'Ship with less HP takes 2 dmg. You move forward by 3 and enemy moves backwards by 3.',
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
    'sidewind': {
        P_CARD_FULL_NAME: 'Sidewind',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Everyone is disarmed for 1 turn.',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Everyone is disarmed for 1 turn.',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        }
    },
    'wingman': {
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
                    P_EFFECT_VALUE: 'damage_add2',
                    P_EFFECT_BUFF_DURATION: 1
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
    'flare': {
        P_CARD_FULL_NAME: 'Solar flare',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Everyone but you deals a reduced by 2 dmg for 1 round.',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_EXCEPT_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage_reduce2',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Everyone but you deals a reduced by 2 dmg for 1 round.',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_EXCEPT_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'damage_reduce2',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        }
    },
    'meteor': {
        P_CARD_FULL_NAME: 'Meteor shower',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Ship with most health takes 2 damage',
            P_CARD_FLAVOR: 'Sometimes a hull full of holes is convenient - rocks just fly right through it!',
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
            P_CARD_DESCRIPTION: 'Ship with most health takes 2 damage',
            P_CARD_FLAVOR: 'Sometimes a hull full of holes is convenient - rocks just fly right through it!',
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
    'geomagnetic': {
        P_CARD_FULL_NAME: 'Geomagnetic storm',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Everyone takes 10 energy damage. When energy ends you take HP damage instead',
            P_CARD_FLAVOR: 'The geomagnetic interference hits you hard.',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_SHIPS,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGY_TEST
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Everyone takes 10 energy damage. When energy ends you take HP damage instead',
            P_CARD_FLAVOR: 'The geomagnetic interference hits you hard.',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL_SHIPS,
                    P_EFFECT_TYPE: EFFECT_TYPE_ENERGY_TEST
                }
            ]
        }
    },
    'fog': {
        P_CARD_FULL_NAME: 'Fog',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Attacker takes a position right behind a defender',
            P_CARD_FLAVOR: 'It\'s hard to track your position in fog.',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_OFFENSE_APPROACH
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Attacker takes a position right behind a defender',
            P_CARD_FLAVOR: 'It\'s hard to track your position in fog.',
            P_CARD_COST: 2,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_OFFENSE_APPROACH
                }
            ]
        }
    },
    'bursts': {
        P_CARD_FULL_NAME: 'Energy microbursts',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Everyone gets 4 energy, but can\'t play weapon and ship cards',
            P_CARD_FLAVOR: 'It\'s good to have a spare energy, right? Right?!',
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
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Everyone gets 4 energy, but can\'t play weapon and ship cards',
            P_CARD_FLAVOR: 'It\'s good to have a spare energy, right? Right?!',
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
                    P_EFFECT_VALUE: 'disarm',
                    P_EFFECT_BUFF_DURATION: 1
                },
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute',
                    P_EFFECT_BUFF_DURATION: 1
                },
            ]
        }
    },
    'birds': {
        P_CARD_FULL_NAME: 'Bird flock',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: True,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Birds move from the north and deal 2 dmg. to everyone on the same position as them',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'birds'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Birds move from the south and deal 2 dmg. to everyone on the same position as them',
            P_CARD_COST: 3,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_SPAWN,
                    P_EFFECT_VALUE: 'birds'
                }
            ]
        }
    },
    'headwind': {
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
    'tailwind': {
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

    # CHEAT CARDS

    ,
    'cheat_dmg_enship': {
        P_CARD_FULL_NAME: 'cheat_dmg_enship',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 1 dmg to enemy ship',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Deal 1 dmg to enemy ship',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }
    },
    'cheat_dmg_first': {
        P_CARD_FULL_NAME: 'cheat_dmg_first',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Deal 1 dmg forward',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Deal 1 dmg backward',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }
    },
    'cheat_move_fwd': {
        P_CARD_FULL_NAME: 'cheat_move_fwd',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Move forward by 1',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Move forward by 1',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: 1
                }
            ]
        }
    },
    'cheat_move_bwd': {
        P_CARD_FULL_NAME: 'cheat_move_bwd',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Move back by 1',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Move back by 1',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                    P_EFFECT_VALUE: -1
                }
            ]
        }
    },
    'cheat_disarm': {
        P_CARD_FULL_NAME: 'cheat_disarm',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Disarm enemy',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Disarm enemy',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'disarm'
                }
            ]
        }
    },
    'cheat_arm': {
        P_CARD_FULL_NAME: 'cheat_arm',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Arm self',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_ARM
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Arm self',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_ARM
                }
            ]
        }
    },
    'cheat_mute': {
        P_CARD_FULL_NAME: 'cheat_mute',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Mute enemy',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute'
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Mute enemy',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ALL,
                    P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                    P_EFFECT_VALUE: 'mute'
                }
            ]
        }
    },
    'cheat_unmute': {
        P_CARD_FULL_NAME: 'cheat_unmute',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Unmute self',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Unmute self',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_ENEMY_SHIP,
                    P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE
                }
            ]
        }
    },
    'cheat_heal': {
        P_CARD_FULL_NAME: 'cheat_heal',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Heal yourself',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_HEAL,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Heal yourself',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_HEAL,
                    P_EFFECT_VALUE: 1
                }
            ]
        }
    },
    'cheat_energy': {
        P_CARD_FULL_NAME: 'cheat_energy',
        P_CARD_TYPE: CARD_TYPE_EVENT,
        P_CARD_DECK: False,
        P_CARD_ACTION_OFFENSE: {
            P_CARD_DESCRIPTION: 'Give yourself energy',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_EHEAL,
                    P_EFFECT_VALUE: 1
                }
            ]
        },
        P_CARD_ACTION_DEFENSE: {
            P_CARD_DESCRIPTION: 'Give yourself energy',
            P_CARD_COST: 0,
            P_CARD_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_SELF,
                    P_EFFECT_TYPE: EFFECT_TYPE_EHEAL,
                    P_EFFECT_VALUE: 1
                }
            ]
        }
    }
}
