from game.rules.settings import *

weapons = {
    'mg': {
        P_WEAPON_FULL_NAME: 'Machine gun',
        P_WEAPON_CARDS: ['fire_all', 'hamstring', 'irounds', 'leak', 'bomb', 'detonate', 'cool'],
        P_WEAPON_ACTION_OFFENSE: {
            P_WEAPON_DESCRIPTION: 'Deals 2 damage',
        #This sturdy machine gun has seen thousands of battles and you are more than likely not her first.

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
            P_WEAPON_DESCRIPTION: 'Deals 1 damage.',

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
        P_WEAPON_CARDS: ['snipe', 'scorch', 'redirect', 'emp', 'detonate_emp', 'charging', 'fire', 'hold_fire'],
        P_WEAPON_ACTION_OFFENSE: {
            P_WEAPON_DESCRIPTION: 'Deals 1 damage to hp and energy.',
            #                                ' This revolutionary invention brings glory'
            #                                ' to its makers and death for all the infidels.'
            #                                ' In style. '
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
            P_WEAPON_DESCRIPTION: 'Deals 1 damage to hp and energy',
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
        P_WEAPON_CARDS: ['grapple', 'lighting_rod', 'impale', 'electrocute', 'still', 'grab', 'fix', 'spare'],
        P_WEAPON_ACTION_OFFENSE: {
            P_WEAPON_DESCRIPTION: 'Deals 1 damage',  #We used to hunt with those for sky creatures, but now it seeks a different prey.
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
            P_WEAPON_DESCRIPTION: 'Deals 1 damage',
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
