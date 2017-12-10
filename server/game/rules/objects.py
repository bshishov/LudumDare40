from game.rules.settings import *

objects = {
    'bomb': {
        P_OBJECT_FULL_NAME: 'Bomb',
        P_OBJECT_DESCRIPTION: 'Just a flying c4',
        P_OBJECT_HP: 3,
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
    'emp': {
        P_OBJECT_FULL_NAME: 'EMP',
        P_OBJECT_DESCRIPTION: 'A flying electromagnetic grenade',
        P_OBJECT_HP: 3,
        P_OBJECT_CASES: {
            CASE_PLAY_CARD: {
                P_CASE_ARG: 'detonate_emp',
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                        P_EFFECT_TARGET: TARGET_ALL,
                        P_EFFECT_VALUE: 2
                    },
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_EDAMAGE,
                        P_EFFECT_TARGET: TARGET_ALL,
                        P_EFFECT_VALUE: 6
                    },
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_MUTE,
                        P_EFFECT_TARGET: TARGET_ALL
                    },
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DESTROY,
                        P_EFFECT_TARGET: TARGET_SELF
                    }
                ]
            },
            CASE_ROUND_END: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                        P_EFFECT_TARGET: TARGET_SELF,
                        P_EFFECT_VALUE: -1,
                    }
                ]
            }
        },
    },
    'mine': {
        P_OBJECT_FULL_NAME: 'Flying mine',
        P_OBJECT_DESCRIPTION: 'A flying landmine',
        P_OBJECT_HP: 3,
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
    'adrone': {
        P_OBJECT_FULL_NAME: 'Wingdrone',
        P_OBJECT_DESCRIPTION: 'Simple attacking drone',
        P_OBJECT_HP: 3,
        P_OBJECT_CASES: {
            CASE_SPAWNED: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                        P_EFFECT_TARGET: TARGET_SELF,
                        P_EFFECT_VALUE: 'destroy',
                        P_EFFECT_BUFF_DURATION: 3
                    },
                ]
            },
            CASE_ROUND_END: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                        P_EFFECT_TARGET: TARGET_ALL_ENEMIES,
                        P_EFFECT_VALUE: 2
                    },
                ]
            }
        },
    },
    'hdrone': {
        P_OBJECT_FULL_NAME: 'Helper drone',
        P_OBJECT_DESCRIPTION: 'Simple healing drone',
        P_OBJECT_HP: 3,
        P_OBJECT_CASES: {
            CASE_SPAWNED: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                        P_EFFECT_TARGET: TARGET_SELF,
                        P_EFFECT_VALUE: 'destroy',
                        P_EFFECT_BUFF_DURATION: 3
                    },
                ]
            },
            CASE_ROUND_END: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_HEAL,
                        P_EFFECT_TARGET: TARGET_ALLY_SHIP,
                        P_EFFECT_VALUE: 2
                    },
                ]
            }
        },
    },
    'birds': {
        P_OBJECT_FULL_NAME: 'Birds!',
        P_OBJECT_DESCRIPTION: 'A flock of birds',
        P_OBJECT_HP: 3,
        P_OBJECT_CASES: {
            CASE_COLLIDE: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                        P_EFFECT_TARGET: TARGET_ALL,
                        P_EFFECT_RANGE: 0,
                        P_EFFECT_VALUE: 2
                    },
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
    'debris': {
        P_OBJECT_FULL_NAME: 'Debris',
        P_OBJECT_DESCRIPTION: 'Chunks of metal blown away from your ship',
        P_OBJECT_HP: 3,
        P_OBJECT_CASES: {
            CASE_SPAWNED: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                        P_EFFECT_TARGET: TARGET_SELF,
                        P_EFFECT_VALUE: 'destroy',
                        P_EFFECT_BUFF_DURATION: 2
                    },
                ]
            },
            CASE_COLLIDE: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                        P_EFFECT_TARGET: TARGET_ALL_EXCEPT_SELF,
                        P_EFFECT_RANGE: 2,
                        P_EFFECT_VALUE: 3
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
    'wgenerator': {
        P_OBJECT_FULL_NAME: 'Wind generator',
        P_OBJECT_DESCRIPTION: 'It pushes everyone backwards',
        P_OBJECT_HP: 3,
        P_OBJECT_CASES: {
            CASE_SPAWNED: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_APPLY_BUFF,
                        P_EFFECT_TARGET: TARGET_SELF,
                        P_EFFECT_VALUE: 'destroy',
                        P_EFFECT_BUFF_DURATION: 3
                    },
                ]
            },
            CASE_COLLIDE: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_MOVE,
                        P_EFFECT_TARGET: TARGET_ALL,
                        P_EFFECT_RANGE: 1,
                        P_EFFECT_VALUE: -1
                    }
                ]
            },
        },
    }
}
