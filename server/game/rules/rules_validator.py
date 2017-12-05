from game.rules import *


TYPE_CARD_KEY = 'card_key'

TARGETS = [
    TARGET_SELF,
    TARGET_ALL,
    TARGET_ALL_EXCEPT_SELF,
    TARGET_ALL_ENEMIES,
    TARGET_ALL_ALLIES,
    TARGET_ALL_SHIPS,
    TARGET_ENEMY_SHIP,
    TARGET_ALLY_SHIP,
    TARGET_MAX_HEALTH,
    TARGET_MIN_HEALTH,
    TARGET_MAX_ENERGY,
    TARGET_FORWARD,
    TARGET_FORWARD_ALLY,
    TARGET_FORWARD_ENEMY,
    TARGET_FORWARD_PIERCE,
    TARGET_BACKWARD,
    TARGET_BACKWARD_ALLY,
    TARGET_BACKWARD_ENEMY,
    TARGET_BACKWARD_PIERCE,
]
EFFECT_TYPES = [
    EFFECT_TYPE_DAMAGE,
    EFFECT_TYPE_EDAMAGE,
    EFFECT_TYPE_HEAL,
    EFFECT_TYPE_EHEAL,
    EFFECT_TYPE_MOVE,
    EFFECT_TYPE_DISARM,
    EFFECT_TYPE_ARM,
    EFFECT_TYPE_MUTE,
    EFFECT_TYPE_UNMUTE,
    EFFECT_TYPE_LOCK_POSITION,
    EFFECT_TYPE_UNLOCK_POSITION,
    EFFECT_TYPE_REDUCE_CARDCOST,
    EFFECT_TYPE_ADD_CARDCOST,
    EFFECT_TYPE_DRAW_CARD,
    EFFECT_TYPE_DROP_CARD_OF_TYPE,
    EFFECT_TYPE_REMOVE_CARD,
    EFFECT_TYPE_GAIN_CARD,
    EFFECT_TYPE_DAMAGE_REDUCE,
    EFFECT_TYPE_DAMAGE_ADD,
    EFFECT_TYPE_ENERGYGAIN_REDUCE,
    EFFECT_TYPE_ENERGYGAIN_ADD,
    EFFECT_TYPE_SPAWN,
    EFFECT_TYPE_DESTROY,
    EFFECT_TYPE_APPLY_BUFF,
    EFFECT_TYPE_REMOVE_BUFF,
    EFFECT_TYPE_ENERGY_TEST,
    EFFECT_TYPE_SPECIAL_SWAP,
    EFFECT_TYPE_OFFENSE_APPROACH,
]
CARD_TYPES = [
    CARD_TYPE_SHIP,
    CARD_TYPE_EVENT,
    CARD_TYPE_WEAPON
]
CASES = [
    CASE_COLLIDE,
    CASE_DRAW_CARD,
    CASE_PLAY_CARD,
    CASE_DROP_CARD,
    CASE_DESTROYED,
    CASE_OVERLOAD,
    CASE_ROUND_END,
    CASE_ROUND_START,
]


class PrintColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ValidationResult(object):
    def __init__(self, is_valid, message, obj, param, val):
        self.is_valid = is_valid
        self.message = message
        self.obj = obj
        self.param = param
        self.val = val
        self.inner_results = []

    def print(self, indent=0, hide_valid=True):
        is_valid = self.is_valid
        for i in self.inner_results:
            if not i.is_valid:
                is_valid = False

        if is_valid and hide_valid:
            return
        prefix = ''
        for i in range(indent):
            prefix += '\t'
        if is_valid:
            print(prefix + PrintColors.OKGREEN + 'Result: OK' + PrintColors.ENDC)
        else:
            print(prefix + PrintColors.FAIL + self.message + PrintColors.ENDC)
        print(prefix + 'Object: {0}'.format(self.obj))
        print(prefix + 'Param: {0}'.format(self.param))
        print(prefix + 'Value: {0}'.format(self.val))
        print()

        for inner_res in self.inner_results:
            inner_res.print(indent + 1, hide_valid)


class Validator(object):
    def validate(self, obj, param, val):
        raise NotImplementedError


class In(Validator):
    def __init__(self, values):
        self.values = values

    def validate(self, obj, param, val):
        return ValidationResult(val in self.values,
                                'Value should be one of these: {0}'.format(self.values),
                                obj, param, val)


class NotIn(Validator):
    def __init__(self, values):
        self.values = values

    def validate(self, obj, param, val):
        return ValidationResult(val not in self.values,
                                'Value should NOT be one of these: {0}'.format(self.values),
                                obj, param, val)


class NoParam(Validator):
    def __init__(self, param):
        self.param = param

    def validate(self, obj, param, val):
        return ValidationResult(self.param not in obj,
                                'Object should NOT have param: {0}'.format(self.param),
                                obj, param, val)


class HasParam(Validator):
    def __init__(self, param):
        self.param = param

    def validate(self, obj, param, val):
        return ValidationResult(self.param in obj,
                                'Object should have param: {0}'.format(self.param),
                                obj, param, val)


class StrNotEmpty(Validator):
    def validate(self, obj, param, val):
        return ValidationResult(val != '',
                                'Empty string',
                                obj, param, val)


class Type(Validator):
    def __init__(self, *types):
        self.types = types

    def validate(self, obj, param, val):
        return ValidationResult(type(val) in self.types,
                                'Value should be one of types: {0}'.format(self.types),
                                obj, param, val)


class ParamIs(Validator):
    def __init__(self, param, validator):
        self.param = param
        self.validator = validator

    def validate(self, obj, param, val):
        return self.validator.validate(obj, self.param, val)


class ValidateListItems(Validator):
    def __init__(self, validator):
        self.validator = validator

    def validate(self, obj, param, val):
        valid = True
        inner = []
        for i, v in enumerate(val):
            inner_res = self.validator.validate(val, i, v)
            inner.append(inner_res)
            if not inner_res.is_valid:
                valid = False
        res = ValidationResult(valid, 'Schema check', obj, param, val)
        res.inner_results = inner
        return res


class SchemaForEachElementInList(ValidateListItems):
    def __init__(self, schema_desc):
        super().__init__(Schema(schema_desc))


class SchemaForEachElementInDict(Validator):
    def __init__(self, schema_desc, keys_validator=None):
        self.schema = Schema(schema_desc)
        self.keys_validator = keys_validator

    def validate(self, obj, param, val):
        valid = True
        inner = []
        for key in val:
            if self.keys_validator is not None:
                inner_res = self.keys_validator.validate(val, key, key)
                inner.append(inner_res)
                if inner_res.is_valid:
                    valid = False

            v = val[key]
            inner_res = self.schema.validate(val, key, v)
            inner.append(inner_res)
            if not inner_res.is_valid:
                valid = False
        res = ValidationResult(valid, 'Schema check', obj, param, val)
        res.inner_results = inner
        return res


class Schema(Validator):
    def __init__(self, schema):
        self.schema = schema

    def validate(self, obj, param, val):
        inner = []
        valid = True
        o = val
        for field in o:
            if field not in self.schema[SCHEMA_FIELDS]:
                if self.schema[SCHEMA_ONLY_THESE_FIELDS]:
                    inner_res = ValidationResult(False, 'Unexpected field: {0}'.format(field), obj, param, val)
                    inner.append(inner_res)
                    valid = False
        for field_name in self.schema[SCHEMA_FIELDS]:
            if field_name in o:
                validators = self.schema[SCHEMA_FIELDS][field_name].get(SCHEMA_VALIDATORS, [])
                for v in validators:
                    try:
                        res = v.validate(o, field_name, o[field_name])
                        inner.append(res)
                        if not res.is_valid:
                            valid = False
                    except Exception as err:
                        print('Validator exception: {0}'.format(err))
            else:
                if self.schema[SCHEMA_FIELDS][field_name][SCHEMA_REQUIRED]:
                    inner_res = ValidationResult(False, 'Missing required field: {0}'.format(field_name), obj, param, val)
                    inner.append(inner_res)
                    valid = False
        res = ValidationResult(valid, 'Schema check', obj, param, val)
        res.inner_results = inner
        return res


SCHEMA_FIELDS = 'fields'
SCHEMA_VALIDATORS = 'validators'
SCHEMA_REQUIRED = 'required'
SCHEMA_SCHEMA = 'schema'
SCHEMA_ONLY_THESE_FIELDS = 'field_check'

effect_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_EFFECT_TYPE: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str), In(EFFECT_TYPES)]
        },
        P_EFFECT_TARGET: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str), In(TARGETS)]
        },
        P_EFFECT_VALUE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str, int)]
        },
        P_EFFECT_RANGE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str, int)]
        },
        P_EFFECT_RANGE_MOD: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        P_EFFECT_SPAWN_POSITION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(int), ParamIs(P_EFFECT_TYPE, In([EFFECT_TYPE_SPAWN]))]
        },
        P_EFFECT_CARD_TYPE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str),
                                In(cards),
                                ParamIs(P_EFFECT_TYPE, In([EFFECT_TYPE_REDUCE_CARDCOST, EFFECT_TYPE_ADD_CARDCOST]))]
        },
        P_EFFECT_BUFF_DURATION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(int), ParamIs(P_EFFECT_TYPE, In([EFFECT_TYPE_APPLY_BUFF]))]
        },
    }
}

card_action_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_CARD_DESCRIPTION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str), StrNotEmpty()]
        },
        P_CARD_COST: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        P_CARD_EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        }
    }
}

card_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_CARD_FULL_NAME: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        P_CARD_TYPE: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str), In(CARD_TYPES)]
        },
        P_CARD_DECK: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(bool)]
        },
        P_CARD_ACTION_OFFENSE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                HasParam(P_CARD_ACTION_DEFENSE),
                                NoParam(P_CARD_ACTION_SAME),
                                Schema(card_action_schema)]
        },
        P_CARD_ACTION_DEFENSE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                HasParam(P_CARD_ACTION_OFFENSE),
                                NoParam(P_CARD_ACTION_SAME),
                                Schema(card_action_schema)]
        },
        P_CARD_ACTION_SAME: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                NoParam(P_CARD_ACTION_DEFENSE),
                                NoParam(P_CARD_ACTION_OFFENSE),
                                Schema(card_action_schema)]
        },
    }
}

case_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_CASE_ARG: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        P_CASE_EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        },
    }
}

buff_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_BUFF_FULL_NAME: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        P_BUFF_DESCRIPTION: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        P_BUFF_DURATION: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        P_BUFF_ON_APPLY_EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        },
        P_BUFF_ON_ROUND_EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        },
        P_BUFF_ON_REMOVE_EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        },
        P_BUFF_CASES: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict), SchemaForEachElementInDict(case_schema, keys_validator=In(CASES))]
        },
    }
}


object_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_OBJECT_FULL_NAME: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        P_OBJECT_DESCRIPTION: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        P_OBJECT_CASES: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict), SchemaForEachElementInDict(case_schema, keys_validator=In(CASES))]
        },
    }
}


ship_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_SHIP_HP: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        P_SHIP_MAX_ENERGY: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        P_SHIP_ENERGY_PER_TURN: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        P_SHIP_CARDS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), ValidateListItems(In(cards))]
        },
    }
}


weapon_action_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_WEAPON_DESCRIPTION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str), StrNotEmpty()]
        },
        P_WEAPON_COST: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        P_WEAPON_EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        }
    }
}


weapon_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_WEAPON_FULL_NAME: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        P_WEAPON_CARDS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), ValidateListItems(In(cards))]
        },
        P_WEAPON_ACTION_OFFENSE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                HasParam(P_WEAPON_ACTION_DEFENSE),
                                NoParam(P_WEAPON_ACTION_SAME),
                                Schema(card_action_schema)]
        },
        P_WEAPON_ACTION_DEFENSE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                HasParam(P_WEAPON_ACTION_OFFENSE),
                                NoParam(P_WEAPON_ACTION_SAME),
                                Schema(card_action_schema)]
        },
        P_WEAPON_ACTION_SAME: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                NoParam(P_WEAPON_ACTION_DEFENSE),
                                NoParam(P_WEAPON_ACTION_OFFENSE),
                                Schema(card_action_schema)]
        },
    }
}


if __name__ == '__main__':
    print('Checking cards...')
    cards_validation = SchemaForEachElementInDict(card_schema).validate(None, None, cards)
    cards_validation.print()
    if cards_validation.is_valid:
        print(PrintColors.OKGREEN + 'No errors, cool!' + PrintColors.ENDC)

    print('Checking buffs...')
    buffs_validation = SchemaForEachElementInDict(buff_schema).validate(None, None, buffs)
    buffs_validation.print()
    if buffs_validation.is_valid:
        print(PrintColors.OKGREEN + 'No errors, cool!' + PrintColors.ENDC)

    print('Checking objects...')
    objects_validation = SchemaForEachElementInDict(object_schema).validate(None, None, objects)
    objects_validation.print()
    if objects_validation.is_valid:
        print(PrintColors.OKGREEN + 'No errors, cool!' + PrintColors.ENDC)

    print('Checking ships...')
    ships_validation = SchemaForEachElementInDict(ship_schema).validate(None, None, ships)
    ships_validation.print()
    if ships_validation.is_valid:
        print(PrintColors.OKGREEN + 'No errors, cool!' + PrintColors.ENDC)

    print('Checking weapons...')
    weapons_validation = SchemaForEachElementInDict(weapon_schema).validate(None, None, weapons)
    weapons_validation.print()
    if weapons_validation.is_valid:
        print(PrintColors.OKGREEN + 'No errors, cool!' + PrintColors.ENDC)

