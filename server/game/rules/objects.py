from game.rules.settings import *

objects = {
    'bomb': {
        Entity.FULL_NAME: 'Bomb',
        Entity.DESCRIPTION: 'Just a flying c4',
        Entity.HP: 3,
        Entity.CASES: {
            CaseType.PLAY_CARD: {
                Case.ARG: 'detonate',
                Case.SOURCE_TARGET: Target.ALL_ALLIES,
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.DAMAGE,
                        Effect.TARGET: Target.ALL,
                        Effect.VALUE: 5
                    }
                ]
            },
            CaseType.ROUND_END: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.MOVE,
                        Effect.TARGET: Target.SELF,
                        Effect.VALUE: -1
                    }
                ]
            }
        },
    },
    'emp': {
        Entity.FULL_NAME: 'EMP',
        Entity.DESCRIPTION: 'A flying electromagnetic grenade',
        Entity.HP: 3,
        Entity.CASES: {
            CaseType.PLAY_CARD: {
                Case.ARG: 'detonate_emp',
                Case.SOURCE_TARGET: Target.ALL_ALLIES,
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.DAMAGE,
                        Effect.TARGET: Target.ALL,
                        Effect.VALUE: 2
                    },
                    {
                        Effect.TYPE: EffectType.EDAMAGE,
                        Effect.TARGET: Target.ALL,
                        Effect.VALUE: 6
                    },
                    {
                        Effect.TYPE: EffectType.MUTE,
                        Effect.TARGET: Target.ALL
                    },
                    {
                        Effect.TYPE: EffectType.DESTROY,
                        Effect.TARGET: Target.SELF
                    }
                ]
            },
            CaseType.ROUND_END: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.MOVE,
                        Effect.TARGET: Target.SELF,
                        Effect.VALUE: -1,
                    }
                ]
            }
        },
    },
    'mine': {
        Entity.FULL_NAME: 'Flying mine',
        Entity.DESCRIPTION: 'A flying landmine',
        Entity.HP: 3,
        Entity.CASES: {
            CaseType.COLLIDE: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.DAMAGE,
                        Effect.TARGET: Target.ALL,
                        Effect.RANGE: 0,
                        Effect.VALUE: 5
                    }
                ]
            },

        },
    },
    'adrone': {
        Entity.FULL_NAME: 'Wingdrone',
        Entity.DESCRIPTION: 'Simple attacking drone',
        Entity.HP: 3,
        Entity.CASES: {
            CaseType.SPAWNED: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.APPLY_BUFF,
                        Effect.TARGET: Target.SELF,
                        Effect.VALUE: 'destroy',
                        Effect.BUFF_DURATION: 3
                    },
                ]
            },
            CaseType.ROUND_END: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.DAMAGE,
                        Effect.TARGET: Target.ALL_ENEMIES,
                        Effect.VALUE: 2
                    },
                ]
            }
        },
    },
    'hdrone': {
        Entity.FULL_NAME: 'Helper drone',
        Entity.DESCRIPTION: 'Simple healing drone',
        Entity.HP: 3,
        Entity.CASES: {
            CaseType.SPAWNED: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.APPLY_BUFF,
                        Effect.TARGET: Target.SELF,
                        Effect.VALUE: 'destroy',
                        Effect.BUFF_DURATION: 3
                    },
                ]
            },
            CaseType.ROUND_END: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.HEAL,
                        Effect.TARGET: Target.ALLY_SHIP,
                        Effect.VALUE: 2
                    },
                ]
            }
        },
    },
    'birds': {
        Entity.FULL_NAME: 'Birds!',
        Entity.DESCRIPTION: 'A flock of birds',
        Entity.HP: 3,
        Entity.CASES: {
            CaseType.COLLIDE: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.DAMAGE,
                        Effect.TARGET: Target.ALL,
                        Effect.RANGE: 0,
                        Effect.VALUE: 2
                    },
                ]
            },
            CaseType.ROUND_END: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.MOVE,
                        Effect.TARGET: Target.SELF,
                        Effect.VALUE: -1
                    },
                ]
            }
        },
    },
    'debris': {
        Entity.FULL_NAME: 'Debris',
        Entity.DESCRIPTION: 'Chunks of metal blown away from your ship',
        Entity.HP: 3,
        Entity.CASES: {
            CaseType.SPAWNED: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.APPLY_BUFF,
                        Effect.TARGET: Target.SELF,
                        Effect.VALUE: 'destroy',
                        Effect.BUFF_DURATION: 2
                    },
                ]
            },
            CaseType.COLLIDE: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.DAMAGE,
                        Effect.TARGET: Target.ALL_EXCEPT_SELF,
                        Effect.RANGE: 2,
                        Effect.VALUE: 3
                    }
                ]
            },
            CaseType.ROUND_END: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.MOVE,
                        Effect.TARGET: Target.SELF,
                        Effect.VALUE: -1
                    },
                ]
            }
        },
    },
    'wgenerator': {
        Entity.FULL_NAME: 'Wind generator',
        Entity.DESCRIPTION: 'It pushes everyone backwards',
        Entity.HP: 3,
        Entity.CASES: {
            CaseType.SPAWNED: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.APPLY_BUFF,
                        Effect.TARGET: Target.SELF,
                        Effect.VALUE: 'destroy',
                        Effect.BUFF_DURATION: 3
                    },
                ]
            },
            CaseType.COLLIDE: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.MOVE,
                        Effect.TARGET: Target.ALL,
                        Effect.RANGE: 1,
                        Effect.VALUE: -1
                    }
                ]
            },
        },
    }
}
