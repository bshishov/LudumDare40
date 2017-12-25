from game.rules.settings import *

__all__ = ['cards', ]

cards = {
    'fire_all': {
        Card.FULL_NAME: 'Fire all weapons',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Fire all weapons and deal 6 base dmg',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD_PIERCE,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 6,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Fire all weapons in blank. Move yourself backwards by 1, take 1 dmg and deal 4 base dmg',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1,
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1,
                },
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 4,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                }
            ]
        }
    },
    'hamstring': {
        Card.FULL_NAME: 'Hamstring',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Aim for the wings and deal 3 base dmg. Lock enemy position for 2 turns',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 3,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'lock_position',
                    Effect.BUFF_DURATION: 2
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Aim for the engines, dealing 2 base dmg and move enemy back by 1 position',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                }
            ]
        }
    },
    'irounds': {
        Card.FULL_NAME: 'Incendiary rounds',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 3 base dmg and put the enemy on fire, dealing 2 damage per turn for 2 turns',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 3,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'on_fire',
                    Effect.BUFF_DURATION: 2
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Blind your enemy and reduce their damage by 1 for 2 turns',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_reduce1',
                    Effect.BUFF_DURATION: 2
                }
            ]
        }
    },
    'leak': {
        Card.FULL_NAME: 'Cause a leak',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 2 base dmg, move enemy back by 1 and cause them to get 1 less energy for 2 turns',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'energygain_reduce1',
                    Effect.BUFF_DURATION: 2
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Shoot the enemies tanks, causing them to get 1 less energy for 2 turns',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'energygain_reduce1',
                    Effect.BUFF_DURATION: 2
                }
            ]
        }
    },
    'bomb': {
        Card.FULL_NAME: 'Bomb',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Take 2 dmg and move forward by 2',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Drop a bomb to detonate it later and deal damage to all objects in a small radius',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'bomb',
                    Effect.SPAWN_POSITION: -1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.GAIN_CARD,
                    Effect.VALUE: 'detonate'
                }
            ]
        }

    },
    'detonate': {
        Card.FULL_NAME: 'Detonate Bomb',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Detonate the bomb, dealing 6 damage to everyone near it',
            Card.COST: 1,
            Card.EFFECTS: [
                            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Detonate the bomb, dealing 6 damage to everyone near it',
            Card.COST: 1,
            Card.EFFECTS: [
                            ]
        }
    },
    'cool': {
        Card.FULL_NAME: 'Cool the gun',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Draw a card. disarm yourself for 2 turns',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Draw a card. disarm yourself for 2 turns',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                }
            ]
        }

    },
    'snipe': {
        Card.FULL_NAME: 'Precise shot',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 3 base dmg, 2 energy dmg and mute enemy for 2 turns',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 3,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.EDAMAGE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'mute',
                    Effect.BUFF_DURATION: 2
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Deal 2 base dmg. Enemy deals 1 dmg less for 1 turn.',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,

                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_reduce1',
                    Effect.BUFF_DURATION: 1
                }
            ]
        }

    },
    'scorch': {
        Card.FULL_NAME: 'Scorch this feathers',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 1 base dmg, 2 energy dmg and make enemy burn, dealing 1 dmg for 2 turns',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.EDAMAGE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'on_fire'
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Deal 2 dmg and disarm everyone for 1 turn',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                },
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm'
                },
            ]
        }

    },
    'redirect': {
        Card.FULL_NAME: 'Redirect energy',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Unmute and disarm yourself. Draw a card',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.UNMUTE
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm'
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Unmute and disarm yourself. Draw a card',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.UNMUTE,
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm'
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                }
            ]
        }

    },
    'emp': {
        Card.FULL_NAME: 'EMP',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Detonate the EMP in proximity to own ship, gaining 10 energy. disarm (self) for 1 round',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.EHEAL,
                    Effect.VALUE: 10
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm'
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Drop an EMP, detonate it later to deal massive energy damage to enemy ship',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'emp',
                    Effect.SPAWN_POSITION: -1
                },

                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.GAIN_CARD,
                    Effect.VALUE: 'detonate_emp'
                }
            ]
        }

    },
    'detonate_emp': {
        Card.FULL_NAME: 'Detonate EMP',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Detonate EMP, deal 2 damage, 6 energy damage and mute them for 1 turn',
            Card.COST: 1,
            Card.EFFECTS: [
                            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Detonate EMP, deal 2 damage, 6 energy damage and mute them for 1 turn',
            Card.COST: 1,
            Card.EFFECTS: [
                            ]
        }
    },
    'charging': {
        Card.FULL_NAME: 'Chargin\' ma laser!',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'You charge your weapon to deal 8 base damage on command. disarm (self) for 2 turns',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.GAIN_CARD,
                    Effect.VALUE: 'fire'
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'You charge your weapon to deal 6 base damage on command. disarm (self) for 2 turns',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.GAIN_CARD,
                    Effect.VALUE: 'fire'
                }
            ]
        }

    },
    'fire': {
        Card.FULL_NAME: 'Fire!',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 8 base dmg. 4 energy damage to everyone afore you and move by 1 position backwards',
            Card.COST: 5,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD_PIERCE,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 8,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.FORWARD_PIERCE,
                    Effect.TYPE: EffectType.EDAMAGE,
                    Effect.VALUE: 4
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Deal 6 base dmg, 2 energy damage to everyone behind you and move by 1 position forward',
            Card.COST: 5,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD_PIERCE,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 6,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.BACKWARD_PIERCE,
                    Effect.TYPE: EffectType.EDAMAGE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                }
            ]
        }

    },
    'hold_fire': {
        Card.FULL_NAME: 'Hold fire',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'disarm yourself fo 2 turns but increase your damage by 2 for 3 rounds and draw a card',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_add2',
                    Effect.BUFF_DURATION: 3
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'disarm yourself fo 2 turns but increase your damage by 2 for 3 rounds and draw a card',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_add2',
                    Effect.BUFF_DURATION: 3
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                }
            ]
        }

    },
    'grapple': {
        Card.FULL_NAME: 'Grapple',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 1 base dmg., pooling your enemy closer',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Deal 1 base dmg., pooling your enemy closer',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                }
            ]
        }

    },
    'lighting_rod': {
        Card.FULL_NAME: 'Lighting rod',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 2 base dmg and make your opponent take 2 damage when they play cards for 1 turn',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'lightning_rod'
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Deal 2 base dmg and make your opponent take 2 damage when they play cards for 1 turn',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'lightning_rod'
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                }
            ]
        }

    },
    'impale': {
        Card.FULL_NAME: 'Impale',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 3 base dmg to anyone afore you, move them forward by 1 and apply mute for 1 turn',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD_PIERCE,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 3,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.FORWARD_PIERCE,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.FORWARD_PIERCE,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'mute',
                    Effect.BUFF_DURATION: 1
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Impale all enemies behind you, dealing 2 base dmg and move them backwards by 1',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD_PIERCE,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.BACKWARD_PIERCE,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                },
            ]
        }

    },
    'electrocute': {
        Card.FULL_NAME: 'Electrocute',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Reduce enemy\'s energy gain by 2 and add it to yours. Deal 1 base dmg and 3 energy dmg.',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.EDAMAGE,
                    Effect.VALUE: 3
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'energygain_reduce2',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'energygain_add2',
                    Effect.BUFF_DURATION: 2
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'disarm and mute your enemy for 1 turn. Deal 3 base dmg. and draw a card.',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 3,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm'
                },
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'mute',
                    Effect.BUFF_DURATION: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                }
            ]
        }

    },
    'still': {
        Card.FULL_NAME: 'Hold still',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 3 base dmg, move enemy further and lock both ships\' positions',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 3,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.ALL_SHIPS,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'lock_position',
                    Effect.BUFF_DURATION: 1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Deal 3 base dmg, move enemy further and lock both ships\' positions',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 3,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                },
                {
                    Effect.TARGET: Target.ALL_SHIPS,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'lock_position',
                    Effect.BUFF_DURATION: 1
                }
            ]
        }

    },
    'grab': {
        Card.FULL_NAME: 'That\'s mine',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 5 base dmg., disarm and mute your enemy. Enemy gets a "Fix it!" card',
            Card.COST: 8,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 5,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.GAIN_CARD,
                    Effect.VALUE: 'fix'
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'mute',
                    Effect.BUFF_DURATION: 2
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Deal 4 base dmg, draw a card. Gain "Spare part" card, that heals you when played',
            Card.COST: 8,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 4,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.GAIN_CARD,
                    Effect.VALUE: 'spare'
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                }
            ]
        }

    },
    'fix': {
        Card.FULL_NAME: 'Fix it!',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Fix it right now! Returns you the ability to play all cards',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.ARM
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.UNMUTE
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Fix it right now! Returns you the ability to play all cards',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.ARM
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.UNMUTE
                }
            ]
        }

    },
    'spare': {
        Card.FULL_NAME: 'Spare part!',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Use it to quickly fix your ship and get 4 HP',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.HEAL,
                    Effect.VALUE: 4
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Use it to quickly fix your ship and get 4 HP',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.HEAL,
                    Effect.VALUE: 4
                }
            ]
        }

    },
    'power': {
        Card.FULL_NAME: 'Power up',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Increase your damage by 1 for this turn',
            Card.FLAVOR: 'Use the ship\'s special reserve to power up your weapon.',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_add1',
                    Effect.BUFF_DURATION: 1
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Decrease enemy ship damage by 1 for 2 turns',
            Card.FLAVOR: 'Use the ship\'s special reserve to power up your armor.',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_reduce1',
                    Effect.BUFF_DURATION: 2
                },
            ]
        }

    },
    'ram': {
        Card.FULL_NAME: 'Ram',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 4 base dmg., take 2 damage and move forward by 1 position',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.FORWARD_PIERCE,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 4,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Deal 4 base dmg., take 2 damage and move backwards by 1 position',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.BACKWARD_PIERCE,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                },
                {
                    Effect.TARGET: Target.BACKWARD_PIERCE,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 4,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
            ]
        }

    },
    'eboost': {
        Card.FULL_NAME: 'Energy boost',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Sacrifice ship integrity to get 2 energy. Take 1 damage',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.EHEAL,
                    Effect.VALUE: 2
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Sacrifice ship integrity to get 2 energy. Take 1 damage',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.EHEAL,
                    Effect.VALUE: 2
                }
            ]
        }

    },
    'stop': {
        Card.FULL_NAME: 'Full stop',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'disarm and mute, move back by 2. Draw a card and increase energy gain by 2 for 2 rounds',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'energygain_add2',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'mute',
                    Effect.BUFF_DURATION: 1
                },

            ]
        },

        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'disarm and mute, move back by 2. Draw a card and increase energy gain by 2 for 2 rounds',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'energygain_add2',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'mute',
                    Effect.BUFF_DURATION: 1
                }
            ]
        }

    },
    'explode': {
        Card.FULL_NAME: 'Explode',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Take 2 dmg, draw a card. Created debris deals 3 damage to everyone in it\'s radius',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'debris'
                }

            ]
        },

        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Take 2 dmg, draw a card. Created debris deals 3 damage to everyone in it\'s radius',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'debris'
                }
            ]
        }

    },
    'armoffense': {
        Card.FULL_NAME: 'Armored offense',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'For 4 rounds you will move forward 1 position per turn',
            Card.COST: 5,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'marcho'
                }
            ]
        },

        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'For 4 rounds you will move backwards 1 position per turn',
            Card.COST: 5,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'marchd'
                }
            ]
        }

    },

    'tab': {
        Card.FULL_NAME: 'Turn and burn',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'You take a vantage point. Move 1 forward, rearm and reduce card cost for 1 turn',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.ARM
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'cardcost_reduce1',
                    Effect.BUFF_DURATION: 1
                },

            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Rearm, move back, reduce card cost for 1 turn and deal 2 base dmg. to anyone behind',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.ARM
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'cardcost_reduce1',
                    Effect.BUFF_DURATION: 1
                },
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                }
            ]
        }

    },
    'barrel': {
        Card.FULL_NAME: 'Barrel roll',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'You do a barrel roll and safely move 1 forward, deal 1 base dmg. and draw a card',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                }

            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'You do a barrel roll and safely move 1 forward, deal 1 base dmg. and draw a card',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                }
            ]
        }

    },
    'missile': {
        Card.FULL_NAME: 'Hardpoint missile',
        Card.TYPE: CardType.WEAPON,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'You fire a missile, pushing enemy away by 1 position and dealing 3 damage',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 3
                }

            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'You fire a missile, exploding it in distance. No one can use weapon cards for 1 turn',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 1
                },
            ]
        }

    },
    'wingdrone': {
        Card.FULL_NAME: 'Wingdrone',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Summon an attack drone behind you. It will attack enemy in front of you for 3 turns',
            Card.COST: 5,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'adrone',
                    Effect.SPAWN_POSITION: -1
                }

            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Summon an attack drone behind you. It will attack enemy in front of you for 3 turns',
            Card.COST: 5,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'adrone',
                    Effect.SPAWN_POSITION: -1
                }
            ]
        }

    },
    'maneuver': {
        Card.FULL_NAME: 'Offensive maneuver',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'You deal 1 base damage, move forward and deal 1 base damage again',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1
                },
            ]
        },

        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'You deal 1 base damage, move backwards and deal 1 base damage again',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                },
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1
                },
            ]
        }

    },
    'sonic': {
        Card.FULL_NAME: 'Sonic boost',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'You drop random ship card, move forward by 2 and deny enemy from moving fo 1 turn',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DROP_CARD_OF_TYPE,
                    Effect.VALUE: CardType.SHIP
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'lock_position',
                    Effect.BUFF_DURATION: 1
                },
            ]
        },

        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'You drop random ship card, move forward by 2 and deny enemy from moving fo 1 turn',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DROP_CARD_OF_TYPE,
                    Effect.VALUE: CardType.SHIP
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'lock_position',
                    Effect.BUFF_DURATION: 1
                },
            ]
        }

    },
    'mine': {
        Card.FULL_NAME: 'Floating mine',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Place a floating mine in 2 positions in front of you. Mine deals 5 damage on collide.',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'mine',
                    Effect.SPAWN_POSITION: 2
                }

            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Place a floating mine in 2 positions behind you. Mine deals 5 damage on collide.',
            Card.COST: 4,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'mine',
                    Effect.SPAWN_POSITION: -2
                }
            ]
        }

    },
    'healdrone': {
        Card.FULL_NAME: 'Little Drone Helper',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'You summon a healing drone behind you. It will heal you for 3 turns',
            Card.COST: 5,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'hdrone',
                    Effect.SPAWN_POSITION: -1
                }

            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'You summon a healing drone behind you. It will heal you for 3 turns',
            Card.COST: 5,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'hdrone',
                    Effect.SPAWN_POSITION: -1
                }
            ]
        }

    },
    'reactor': {
        Card.FULL_NAME: 'Cool the reactor',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Draw 2 cards. Energy gain reduced by 2 for 2 rounds.',
            Card.COST: 6,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'energygain_reduce2',
                    Effect.BUFF_DURATION: 2
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Draw 2 cards. Energy gain reduced by 2 for 2 rounds.',
            Card.COST: 6,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'energygain_reduce2',
                    Effect.BUFF_DURATION: 2
                },
            ]
        }

    },
    'core': {
        Card.FULL_NAME: 'Power to the core',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Damage reduced by 2. Card cost reduced by 2',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'cardcost_reduce2',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_reduce2',
                    Effect.BUFF_DURATION: 2
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Damage reduced by 2. Card cost reduced by 2',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'cardcost_reduce2',
                    Effect.BUFF_DURATION: 2
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_reduce2',
                    Effect.BUFF_DURATION: 2
                },
            ]
        }

    },
    'closer': {
        Card.FULL_NAME: 'Get closer',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Move 1 forward and draw a card',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                }
            ]
        },

        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Move 1 backwards and draw a card',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.DRAW_CARD
                },
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                }
            ]
        }
    },
    'wgenerator': {
        Card.FULL_NAME: 'Wind generator',
        Card.TYPE: CardType.SHIP,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Spawn a wind generator behind enemy ship that pushes everyone in a small radius '
                              'backwards',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'wgenerator',
                    Effect.SPAWN_POSITION: -1
                }
            ]
        },

        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Spawn a wind generator before enemy ship that pushes everyone in a small radius '
                              'backwards',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'wgenerator',
                    Effect.SPAWN_POSITION: 1
                }
            ]
        }
    },
    'sandstorm': {
        Card.FULL_NAME: 'Sandstorm',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Sudden sandstorm strikes the enemy ship for 2 damage',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Enemy takes your position. You move 1 position back. Everyone takes 2 damage',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.SPECIAL_SWAP
                },
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                }
            ]
        }

    },
    'thunder': {
        Card.FULL_NAME: 'Thunder and Lightning',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Thunderbolt is attracted to energy. Ship with higher energy takes 2 damage',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.MAX_ENERGY,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Thunderbolt is attracted to energy. Ship with higher energy takes 2 damage',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.MAX_ENERGY,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                }
            ]
        }

    },
    'tornado': {
        Card.FULL_NAME: 'Tornado',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Ship with less HP takes 2 dmg. You move forward by 3 and enemy moves backwards by 3.',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.MIN_HEALTH,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.ALL_ALLIES,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 3
                },
                {
                    Effect.TARGET: Target.ALL_ENEMIES,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -3
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Ship with less HP takes 2 dmg. You move forward by 3 and enemy moves backwards by 3.',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.MIN_HEALTH,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                },
                {
                    Effect.TARGET: Target.ALL_ENEMIES,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 3
                },
                {
                    Effect.TARGET: Target.ALL_ALLIES,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -3
                }
            ]
        }

    },
    'sidewind': {
        Card.FULL_NAME: 'Sidewind',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Everyone is disarmed for 1 turn.',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 1
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Everyone is disarmed for 1 turn.',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 1
                },
            ]
        }
    },
    'wingman': {
        Card.FULL_NAME: 'Wingman\'s help',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Ally shows up to help you finish the prey. Damage increased by 2 for this turn',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_add2',
                    Effect.BUFF_DURATION: 1
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Ally shows up to help you deal with a pursuing enemy. They deal 3 damage to enemy ship',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 3
                }
            ]
        }
    },
    'flare': {
        Card.FULL_NAME: 'Solar flare',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Everyone but you deals a reduced by 2 dmg for 1 round.',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL_EXCEPT_SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_reduce2',
                    Effect.BUFF_DURATION: 1
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Everyone but you deals a reduced by 2 dmg for 1 round.',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL_EXCEPT_SELF,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'damage_reduce2',
                    Effect.BUFF_DURATION: 1
                },
            ]
        }
    },
    'meteor': {
        Card.FULL_NAME: 'Meteor shower',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Ship with most health takes 2 damage',
            Card.FLAVOR: 'Sometimes a hull full of holes is convenient - rocks just fly right through it!',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.MAX_HEALTH,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Ship with most health takes 2 damage',
            Card.FLAVOR: 'Sometimes a hull full of holes is convenient - rocks just fly right through it!',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.MAX_HEALTH,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2
                }
            ]
        }
    },
    'geomagnetic': {
        Card.FULL_NAME: 'Geomagnetic storm',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Everyone takes 10 energy damage. When energy ends you take HP damage instead',
            Card.FLAVOR: 'The geomagnetic interference hits you hard.',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL_SHIPS,
                    Effect.TYPE: EffectType.ENERGY_TEST
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Everyone takes 10 energy damage. When energy ends you take HP damage instead',
            Card.FLAVOR: 'The geomagnetic interference hits you hard.',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL_SHIPS,
                    Effect.TYPE: EffectType.ENERGY_TEST
                }
            ]
        }
    },
    'fog': {
        Card.FULL_NAME: 'Fog',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Attacker takes a position right behind a defender',
            Card.FLAVOR: 'It\'s hard to track your position in fog.',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.OFFENSE_APPROACH
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Attacker takes a position right behind a defender',
            Card.FLAVOR: 'It\'s hard to track your position in fog.',
            Card.COST: 2,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.OFFENSE_APPROACH
                }
            ]
        }
    },
    'bursts': {
        Card.FULL_NAME: 'Energy microbursts',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Everyone gets 4 energy, but can\'t play weapon and ship cards',
            Card.FLAVOR: 'It\'s good to have a spare energy, right? Right?!',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.EHEAL,
                    Effect.VALUE: 4
                },
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 1
                },
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'mute',
                    Effect.BUFF_DURATION: 1
                },
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Everyone gets 4 energy, but can\'t play weapon and ship cards',
            Card.FLAVOR: 'It\'s good to have a spare energy, right? Right?!',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.EHEAL,
                    Effect.VALUE: 4
                },
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm',
                    Effect.BUFF_DURATION: 1
                },
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'mute',
                    Effect.BUFF_DURATION: 1
                },
            ]
        }
    },
    'birds': {
        Card.FULL_NAME: 'Bird flock',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Birds move from the north and deal 2 dmg. to everyone on the same position as them',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'birds'
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Birds move from the south and deal 2 dmg. to everyone on the same position as them',
            Card.COST: 3,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.SPAWN,
                    Effect.VALUE: 'birds'
                }
            ]
        }
    },
    'headwind': {
        Card.FULL_NAME: 'Headwind',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Headwind moves you 1 position back',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Headwind moves you 1 position back',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                }
            ]
        }
    },
    'tailwind': {
        Card.FULL_NAME: 'Tailwind',
        Card.TYPE: CardType.EVENT,
        Card.DECK: True,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Tailwind moves you 1 position forward',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Tailwind moves you 1 position forward',
            Card.COST: 1,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                }
            ]
        }
    },

    # CHEAT CARDS
    'cheat_dmg_enship': {
        Card.FULL_NAME: 'cheat_dmg_enship',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 1 dmg to enemy ship',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Deal 1 dmg to enemy ship',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1
                }
            ]
        }
    },
    'cheat_dmg_first': {
        Card.FULL_NAME: 'cheat_dmg_first',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Deal 1 dmg forward',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Deal 1 dmg backward',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1
                }
            ]
        }
    },
    'cheat_move_fwd': {
        Card.FULL_NAME: 'cheat_move_fwd',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Move forward by 1',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Move forward by 1',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: 1
                }
            ]
        }
    },
    'cheat_move_bwd': {
        Card.FULL_NAME: 'cheat_move_bwd',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Move back by 1',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Move back by 1',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.MOVE,
                    Effect.VALUE: -1
                }
            ]
        }
    },
    'cheat_disarm': {
        Card.FULL_NAME: 'cheat_disarm',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Disarm enemy',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm'
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Disarm enemy',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'disarm'
                }
            ]
        }
    },
    'cheat_arm': {
        Card.FULL_NAME: 'cheat_arm',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Arm self',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.ARM
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Arm self',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.ARM
                }
            ]
        }
    },
    'cheat_mute': {
        Card.FULL_NAME: 'cheat_mute',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Mute enemy',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'mute'
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Mute enemy',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ALL,
                    Effect.TYPE: EffectType.APPLY_BUFF,
                    Effect.VALUE: 'mute'
                }
            ]
        }
    },
    'cheat_unmute': {
        Card.FULL_NAME: 'cheat_unmute',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Unmute self',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.UNMUTE
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Unmute self',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.ENEMY_SHIP,
                    Effect.TYPE: EffectType.UNMUTE
                }
            ]
        }
    },
    'cheat_heal': {
        Card.FULL_NAME: 'cheat_heal',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Heal yourself',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.HEAL,
                    Effect.VALUE: 1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Heal yourself',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.HEAL,
                    Effect.VALUE: 1
                }
            ]
        }
    },
    'cheat_energy': {
        Card.FULL_NAME: 'cheat_energy',
        Card.TYPE: CardType.EVENT,
        Card.DECK: False,
        Card.ACTION_OFFENSE: {
            Card.DESCRIPTION: 'Give yourself energy',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.EHEAL,
                    Effect.VALUE: 1
                }
            ]
        },
        Card.ACTION_DEFENSE: {
            Card.DESCRIPTION: 'Give yourself energy',
            Card.COST: 0,
            Card.EFFECTS: [
                {
                    Effect.TARGET: Target.SELF,
                    Effect.TYPE: EffectType.EHEAL,
                    Effect.VALUE: 1
                }
            ]
        }
    }
}
