from game.rules.settings import *

weapons = {
    'mg': {
        Weapon.FULL_NAME: 'Machine gun',
        Weapon.CARDS: ['fire_all', 'hamstring', 'irounds', 'leak', 'bomb', 'detonate', 'cool'],
        Weapon.ACTION_OFFENSE: {
            Weapon.DESCRIPTION: 'Deals 2 damage',
            # This sturdy machine gun has seen thousands of battles and you are more than likely not her first.

            Weapon.COST: 2,
            Weapon.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 2,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
            ]
        },
        Weapon.ACTION_DEFENSE: {
            Weapon.DESCRIPTION: 'Deals 1 damage.',

            Weapon.COST: 2,
            Weapon.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
            ]
        }
    },
    'laser': {
        Weapon.FULL_NAME: 'Laser',
        Weapon.CARDS: ['snipe', 'scorch', 'redirect', 'emp', 'detonate_emp', 'charging', 'fire', 'hold_fire'],
        Weapon.ACTION_OFFENSE: {
            Weapon.DESCRIPTION: 'Deals 1 damage to hp and energy.',
            #                                ' This revolutionary invention brings glory'
            #                                ' to its makers and death for all the infidels.'
            #                                ' In style. '
            Weapon.COST: 2,
            Weapon.EFFECTS: [
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
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                }
            ]
        },
        Weapon.ACTION_DEFENSE: {
            Weapon.DESCRIPTION: 'Deals 1 damage to hp and energy',
            Weapon.COST: 2,
            Weapon.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.EDAMAGE,
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                }
            ]
        }
    },
    'harpoon': {
        Weapon.FULL_NAME: 'Harpoon',
        Weapon.CARDS: ['grapple', 'lighting_rod', 'impale', 'electrocute', 'still', 'grab', 'fix', 'spare'],
        Weapon.ACTION_OFFENSE: {
            Weapon.DESCRIPTION: 'Deals 1 damage',
            # We used to hunt with those for sky creatures,
            # but now it seeks a different prey.
            Weapon.COST: 2,
            Weapon.EFFECTS: [
                {
                    Effect.TARGET: Target.FORWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
            ]
        },
        Weapon.ACTION_DEFENSE: {
            Weapon.DESCRIPTION: 'Deals 1 damage',
            Weapon.COST: 2,
            Weapon.EFFECTS: [
                {
                    Effect.TARGET: Target.BACKWARD,
                    Effect.TYPE: EffectType.DAMAGE,
                    Effect.VALUE: 1,
                    Effect.RANGE: 3,
                    Effect.RANGE_MOD: 1,
                },
            ]
        }
    }
}
