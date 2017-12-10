from game.rules.settings import *

buffs = {
    'mute': {
        P_BUFF_FULL_NAME: 'Mute',
        P_BUFF_DESCRIPTION: 'Target cannot use ship cards',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_MUTE,
                P_EFFECT_TARGET: TARGET_SELF,
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_UNMUTE,
                P_EFFECT_TARGET: TARGET_SELF
            }
        ],
    },
    'disarm': {
        P_BUFF_FULL_NAME: 'Mute',
        P_BUFF_DESCRIPTION: 'Target cannot use weapon cards',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DISARM,
                P_EFFECT_TARGET: TARGET_SELF
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ARM,
                P_EFFECT_TARGET: TARGET_SELF
            }
        ],
    },
    'lock_position': {
        P_BUFF_FULL_NAME: 'Lock position',
        P_BUFF_DESCRIPTION: 'Target cannot move or be moved',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_LOCK_POSITION,
                P_EFFECT_TARGET: TARGET_SELF
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_UNLOCK_POSITION,
                P_EFFECT_TARGET: TARGET_SELF
            }
        ],
    },
    'energygain_reduce1': {
        P_BUFF_FULL_NAME: 'Reduce energy gain',
        P_BUFF_DESCRIPTION: 'Energy gain reduced by 1',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'energygain_reduce2': {
        P_BUFF_FULL_NAME: 'Reduce energy gain',
        P_BUFF_DESCRIPTION: 'Energy gain reduced by 2',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'energygain_add1': {
        P_BUFF_FULL_NAME: 'Increase energy gain',
        P_BUFF_DESCRIPTION: 'Energy gain increased by 1',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'energygain_add2': {
        P_BUFF_FULL_NAME: 'Increase energy gain',
        P_BUFF_DESCRIPTION: 'Energy gain increased by 2',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'cardcost_reduce1': {
        P_BUFF_FULL_NAME: 'Reduce card cost',
        P_BUFF_DESCRIPTION: 'Card cost reduced by 1',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_REDUCE_CARDCOST,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ADD_CARDCOST,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'cardcost_reduce2': {
        P_BUFF_FULL_NAME: 'Reduce card cost',
        P_BUFF_DESCRIPTION: 'Card cost reduced by 2',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_REDUCE_CARDCOST,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ADD_CARDCOST,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'damage_reduce1': {
        P_BUFF_FULL_NAME: 'Reduce damage',
        P_BUFF_DESCRIPTION: 'Damage output reduced by 1',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'damage_reduce2': {
        P_BUFF_FULL_NAME: 'Reduce damage',
        P_BUFF_DESCRIPTION: 'Damage output reduced by 2',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'damage_add1': {
        P_BUFF_FULL_NAME: 'Increase damage',
        P_BUFF_DESCRIPTION: 'Damage output increased by 1',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'damage_add2': {
        P_BUFF_FULL_NAME: 'Increase damage',
        P_BUFF_DESCRIPTION: 'Damage output increased by 2',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'on_fire': {
        P_BUFF_FULL_NAME: 'You are burning!',
        P_BUFF_DESCRIPTION: 'You lose 2 HP per turn',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [],
        P_BUFF_ON_ROUND_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                P_EFFECT_TARGET: TARGET_SELF,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ADD_CARDCOST,
                P_EFFECT_TARGET: TARGET_SELF
            }
        ],
    },
    'lightning_rod': {
        P_BUFF_FULL_NAME: 'Lightning Rod',
        P_BUFF_DESCRIPTION: 'Bla bla bla',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [],
        P_BUFF_CASES: {
            CASE_PLAY_CARD: {
                P_CASE_EFFECTS: [
                    {
                        P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                        P_EFFECT_TARGET: TARGET_SELF,
                        P_EFFECT_VALUE: 1
                    }
                ]
            }
        }
    },
    'destroy': {
        P_BUFF_FULL_NAME: 'Destroy',
        P_BUFF_DESCRIPTION: 'Destroys the object after some time',
        P_BUFF_DURATION: 3,
        P_BUFF_ON_APPLY_EFFECTS: [],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DESTROY,
                P_EFFECT_TARGET: TARGET_SELF,
            }
        ],
    },
}
