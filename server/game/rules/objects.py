from game.rules.settings import *

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
    'EMP': {
        P_OBJECT_FULL_NAME: 'EMP',
        P_OBJECT_DESCRIPTION: 'A flying electromagnetic grenade',
        P_OBJECT_CASES: {
            CASE_PLAY_CARD: {
                P_CASE_ARG: 'detonate EMP',
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
                        P_EFFECT_VALUE: 2
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
                        P_EFFECT_VALUE: 2
                    },
                ]
            }
        },
    },
    'Birds': {
        P_OBJECT_FULL_NAME: 'A flock of birds',
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
            }
        },
    }
}
