from game.rules.settings import *

buffs = {
    'mute1': {
        P_BUFF_FULL_NAME: 'Mute',
        P_BUFF_DESCRIPTION: 'Target cannot use ship cards for 1 round',
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
    'mute2': {
        P_BUFF_FULL_NAME: 'Mute',
        P_BUFF_DESCRIPTION: 'Target cannot use ship cards for 2 rounds',
        P_BUFF_DURATION: 2,
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
    'Disarm1': {
        P_BUFF_FULL_NAME: 'Mute',
        P_BUFF_DESCRIPTION: 'Target cannot use weapon cards for 1 round',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DISARM,
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ARM,
            }
        ],
    },
    'Disarm2': {
        P_BUFF_FULL_NAME: 'Mute',
        P_BUFF_DESCRIPTION: 'Target cannot use weapon cards for 2 rounds',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DISARM,
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ARM,
            }
        ],
    },
    'lock_position1': {
        P_BUFF_FULL_NAME: 'Lock position',
        P_BUFF_DESCRIPTION: 'Target cannot move or be moved for 1 round',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_LOCK_POSITION,
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_UNLOCK_POSITION,
            }
        ],
    },
    'lock_position2': {
        P_BUFF_FULL_NAME: 'Lock position',
        P_BUFF_DESCRIPTION: 'Target cannot move or be moved for 2 rounds',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_LOCK_POSITION,
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_UNLOCK_POSITION,
            }
        ],
    },
    'energygain1_reduce1': {
        P_BUFF_FULL_NAME: 'Reduce energy gain',
        P_BUFF_DESCRIPTION: 'Energy gain reduced by 1 for 1 turn',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'energygain2_reduce1': {
        P_BUFF_FULL_NAME: 'Reduce energy gain',
        P_BUFF_DESCRIPTION: 'Energy gain reduced by 1 for 2 turns',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'energygain2_reduce2': {
        P_BUFF_FULL_NAME: 'Reduce energy gain',
        P_BUFF_DESCRIPTION: 'Energy gain reduced by 2 for 2 turns',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'energygain1_add1': {
        P_BUFF_FULL_NAME: 'Increase energy gain',
        P_BUFF_DESCRIPTION: 'Energy gain increased by 1 for 1 turn',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'energygain2_add1': {
        P_BUFF_FULL_NAME: 'Increase energy gain',
        P_BUFF_DESCRIPTION: 'Energy gain increased by 1 for 2 turns',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'energygain2_add2': {
        P_BUFF_FULL_NAME: 'Increase energy gain',
        P_BUFF_DESCRIPTION: 'Energy gain increased by 2 for 2 turns',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_ADD,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ENERGYGAIN_REDUCE,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'cardcost_reduce1': {
        P_BUFF_FULL_NAME: 'Reduce card cost',
        P_BUFF_DESCRIPTION: 'Card cost reduced by 1 for 1 turn',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_REDUCE_CARDCOST,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ADD_CARDCOST,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'cardcost_reduce2': {
        P_BUFF_FULL_NAME: 'Reduce card cost',
        P_BUFF_DESCRIPTION: 'Card cost reduced by 1 for 2 turns',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_REDUCE_CARDCOST,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_ADD_CARDCOST,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'damage1_reduce1': {
        P_BUFF_FULL_NAME: 'Reduce damage',
        P_BUFF_DESCRIPTION: 'Damage output reduced by 1 for 1 turn',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'damage2_reduce1': {
        P_BUFF_FULL_NAME: 'Reduce damage',
        P_BUFF_DESCRIPTION: 'Damage output reduced by 1 for 2 turns',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_VALUE: 1
            }
        ]
    },
    'damage1_reduce2': {
        P_BUFF_FULL_NAME: 'Reduce damage',
        P_BUFF_DESCRIPTION: 'Damage output reduced by 2 for 1 turn',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'damage2_reduce2': {
        P_BUFF_FULL_NAME: 'Reduce damage',
        P_BUFF_DESCRIPTION: 'Damage output reduced by 2 for 2 turns',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_VALUE: 2
            }
        ],
    },

    'damage1_add1': {
        P_BUFF_FULL_NAME: 'Increase damage',
        P_BUFF_DESCRIPTION: 'Damage output increased by 1 for 1 turns',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'damage2_add1': {
        P_BUFF_FULL_NAME: 'Increase damage',
        P_BUFF_DESCRIPTION: 'Damage output increased by 1 for 2 turns',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_VALUE: 1
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_VALUE: 1
            }
        ],
    },
    'damage1_add2': {
        P_BUFF_FULL_NAME: 'Increase damage',
        P_BUFF_DESCRIPTION: 'Damage output increased by 2 for 1 turns',
        P_BUFF_DURATION: 1,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'damage2_add2': {
        P_BUFF_FULL_NAME: 'Increase damage',
        P_BUFF_DESCRIPTION: 'Damage output increased by 2 for 2 turns',
        P_BUFF_DURATION: 2,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'damage3_add2': {
        P_BUFF_FULL_NAME: 'Increase damage',
        P_BUFF_DESCRIPTION: 'Damage output increased by 2 for 3 turns',
        P_BUFF_DURATION: 3,
        P_BUFF_ON_APPLY_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_ADD,
                P_EFFECT_VALUE: 2
            }
        ],
        P_BUFF_ON_ROUND_EFFECTS: [],
        P_BUFF_ON_REMOVE_EFFECTS: [
            {
                P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE_REDUCE,
                P_EFFECT_VALUE: 2
            }
        ],
    },
    'on fire': {
        P_BUFF_FULL_NAME: 'You are burning!',
        P_BUFF_DESCRIPTION: 'You lose 2 HP per turn for 2 turns',
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
    }
}
