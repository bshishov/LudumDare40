from game.rules.settings import *

weapons = {
    'mg': {
        P_WEAPON_FULL_NAME: 'Machine gun',
        P_WEAPON_CARDS: ['Fire all', 'Hamstring', 'IRrounds', 'Leak', 'Bomb', 'Detonate', 'Cool'],
        P_WEAPON_ACTION_OFFENSE: {
            P_WEAPON_DESCRIPTION: 'This sturdy machine gun has seen thousands of '
                                  'battles and you are more than likely not her first. Deals 2 damage.',
            P_WEAPON_COST: 2,
            P_WEAPON_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 2,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
            ]
        },
        P_WEAPON_ACTION_DEFENSE: {
            P_WEAPON_DESCRIPTION: 'This sturdy machine gun has seen thousands of '
                                  'battles and you are more than likely not her first. Deals 1 damage.',
            P_WEAPON_COST: 2,
            P_WEAPON_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
            ]
        }
    },
    'laser': {
        P_WEAPON_FULL_NAME: 'Laser',
        P_WEAPON_CARDS: ['Snipe', 'Scorch', 'Redirect', 'EMP', 'Detonate EMP', 'Charging', 'Fire!', 'Hold fire'],
        P_WEAPON_ACTION_OFFENSE: {
            P_WEAPON_DESCRIPTION: 'This revolutionary invention brings glory'
                                  ' to its makers and death for all the infidels. '
                                  'In style. Deals 1 damage to hp and energy.',
            P_WEAPON_COST: 2,
            P_WEAPON_EFFECTS: [
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
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }
            ]
        },
        P_WEAPON_ACTION_DEFENSE: {
            P_WEAPON_DESCRIPTION: 'This revolutionary invention brings glory'
                                  ' to its makers and death for all the infidels.'
                                  ' In style. Deals 1 damage to hp and energy.',
            P_WEAPON_COST: 2,
            P_WEAPON_EFFECTS: [
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
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                }
            ]
        }
    },
    'harpoon': {
        P_WEAPON_FULL_NAME: 'Harpoon',
        P_WEAPON_CARDS: ['Grapple', 'Lighting rod', 'Impale', 'Electrocute', 'Still', 'Grab', 'Fix', 'Spare'],
        P_WEAPON_ACTION_OFFENSE: {
            P_WEAPON_DESCRIPTION: 'We used to hunt with those for sky creatures,'
                                  ' but now it seeks a different prey. Deals 1 damage.',
            P_WEAPON_COST: 2,
            P_WEAPON_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_FORWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
            ]
        },
        P_WEAPON_ACTION_DEFENSE: {
            P_WEAPON_DESCRIPTION: 'We used to hunt with those for sky creatures,'
                                  ' but now it seeks a different prey. Deals 1 damage.',
            P_WEAPON_COST: 2,
            P_WEAPON_EFFECTS: [
                {
                    P_EFFECT_TARGET: TARGET_BACKWARD,
                    P_EFFECT_TYPE: EFFECT_TYPE_DAMAGE,
                    P_EFFECT_VALUE: 1,
                    P_EFFECT_RANGE: 3,
                    P_EFFECT_RANGE_MOD: 1,
                },
            ]
        }
    }
}
