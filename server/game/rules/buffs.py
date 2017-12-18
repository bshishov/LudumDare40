from game.rules.settings import *

buffs = {
    'mute': {
        Buff.FULL_NAME: 'Mute',
        Buff.DESCRIPTION: 'Target cannot use ship cards',
        Buff.DURATION: 1,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.MUTE,
                Effect.TARGET: Target.SELF,
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.UNMUTE,
                Effect.TARGET: Target.SELF
            }
        ],
    },
    'disarm': {
        Buff.FULL_NAME: 'Mute',
        Buff.DESCRIPTION: 'Target cannot use weapon cards',
        Buff.DURATION: 1,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.DISARM,
                Effect.TARGET: Target.SELF
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.ARM,
                Effect.TARGET: Target.SELF
            }
        ],
    },
    'lock_position': {
        Buff.FULL_NAME: 'Lock position',
        Buff.DESCRIPTION: 'Target cannot move or be moved',
        Buff.DURATION: 1,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.LOCK_POSITION,
                Effect.TARGET: Target.SELF
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.UNLOCK_POSITION,
                Effect.TARGET: Target.SELF
            }
        ],
    },
    'energygain_reduce1': {
        Buff.FULL_NAME: 'Reduce energy gain',
        Buff.DESCRIPTION: 'Energy gain reduced by 1',
        Buff.DURATION: 1,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.ENERGYGAIN_REDUCE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.ENERGYGAIN_ADD,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
    },
    'energygain_reduce2': {
        Buff.FULL_NAME: 'Reduce energy gain',
        Buff.DESCRIPTION: 'Energy gain reduced by 2',
        Buff.DURATION: 2,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.ENERGYGAIN_REDUCE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.ENERGYGAIN_ADD,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
    },
    'energygain_add1': {
        Buff.FULL_NAME: 'Increase energy gain',
        Buff.DESCRIPTION: 'Energy gain increased by 1',
        Buff.DURATION: 1,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.ENERGYGAIN_ADD,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.ENERGYGAIN_REDUCE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
    },
    'energygain_add2': {
        Buff.FULL_NAME: 'Increase energy gain',
        Buff.DESCRIPTION: 'Energy gain increased by 2',
        Buff.DURATION: 2,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.ENERGYGAIN_ADD,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.ENERGYGAIN_REDUCE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
    },
    'cardcost_reduce1': {
        Buff.FULL_NAME: 'Reduce card cost',
        Buff.DESCRIPTION: 'Card cost reduced by 1',
        Buff.DURATION: 1,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.REDUCE_CARDCOST,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.ADD_CARDCOST,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
    },
    'cardcost_reduce2': {
        Buff.FULL_NAME: 'Reduce card cost',
        Buff.DESCRIPTION: 'Card cost reduced by 2',
        Buff.DURATION: 2,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.REDUCE_CARDCOST,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.ADD_CARDCOST,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
    },
    'damage_reduce1': {
        Buff.FULL_NAME: 'Reduce damage',
        Buff.DESCRIPTION: 'Damage output reduced by 1',
        Buff.DURATION: 1,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.DAMAGE_REDUCE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.DAMAGE_ADD,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
    },
    'damage_reduce2': {
        Buff.FULL_NAME: 'Reduce damage',
        Buff.DESCRIPTION: 'Damage output reduced by 2',
        Buff.DURATION: 1,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.DAMAGE_REDUCE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.DAMAGE_ADD,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
    },
    'damage_add1': {
        Buff.FULL_NAME: 'Increase damage',
        Buff.DESCRIPTION: 'Damage output increased by 1',
        Buff.DURATION: 1,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.DAMAGE_ADD,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.DAMAGE_REDUCE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
    },
    'damage_add2': {
        Buff.FULL_NAME: 'Increase damage',
        Buff.DESCRIPTION: 'Damage output increased by 2',
        Buff.DURATION: 1,
        Buff.ON_APPLY_EFFECTS: [
            {
                Effect.TYPE: EffectType.DAMAGE_ADD,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.DAMAGE_REDUCE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
    },
    'on_fire': {
        Buff.FULL_NAME: 'You are burning!',
        Buff.DESCRIPTION: 'You lose 2 HP per turn',
        Buff.DURATION: 2,
        Buff.ON_APPLY_EFFECTS: [],
        Buff.ON_ROUND_EFFECTS: [
            {
                Effect.TYPE: EffectType.DAMAGE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 2
            }
        ],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.ADD_CARDCOST,
                Effect.TARGET: Target.SELF
            }
        ],
    },
    'lightning_rod': {
        Buff.FULL_NAME: 'Lightning Rod',
        Buff.DESCRIPTION: 'Bla bla bla',
        Buff.DURATION: 2,
        Buff.ON_APPLY_EFFECTS: [],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [],
        Buff.CASES: {
            CaseType.PLAY_CARD: {
                Case.EFFECTS: [
                    {
                        Effect.TYPE: EffectType.DAMAGE,
                        Effect.TARGET: Target.SELF,
                        Effect.VALUE: 1
                    }
                ]
            }
        }
    },
    'destroy': {
        Buff.FULL_NAME: 'Destroy',
        Buff.DESCRIPTION: 'Destroys the object after some time',
        Buff.DURATION: 3,
        Buff.ON_APPLY_EFFECTS: [],
        Buff.ON_ROUND_EFFECTS: [],
        Buff.ON_REMOVE_EFFECTS: [
            {
                Effect.TYPE: EffectType.DESTROY,
                Effect.TARGET: Target.SELF,
            }
        ],
    },
    'marcho': {
        Buff.FULL_NAME: 'March',
        Buff.DESCRIPTION: 'Each turn you move forward',
        Buff.DURATION: 4,
        Buff.ON_APPLY_EFFECTS: [],
        Buff.ON_ROUND_EFFECTS: [
            {
                Effect.TYPE: EffectType.MOVE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: 1
            }
        ],
        Buff.ON_REMOVE_EFFECTS: [],
    },
    'marchd': {
        Buff.FULL_NAME: 'March',
        Buff.DESCRIPTION: 'Each turn you move backwards',
        Buff.DURATION: 3,
        Buff.ON_APPLY_EFFECTS: [],
        Buff.ON_ROUND_EFFECTS: [
            {
                Effect.TYPE: EffectType.MOVE,
                Effect.TARGET: Target.SELF,
                Effect.VALUE: -1
            }
        ],
        Buff.ON_REMOVE_EFFECTS: [],
    },
}
