from game.rules import *
from validation import *


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
EFFECTS_WITHOUT_VALUE = [
    EFFECT_TYPE_DISARM,
    EFFECT_TYPE_ARM,
    EFFECT_TYPE_MUTE,
    EFFECT_TYPE_UNMUTE,
    EFFECT_TYPE_LOCK_POSITION,
    EFFECT_TYPE_UNLOCK_POSITION,
    EFFECT_TYPE_DESTROY,
    EFFECT_TYPE_DRAW_CARD,
    EFFECT_TYPE_SPECIAL_SWAP,
    EFFECT_TYPE_OFFENSE_APPROACH,
]


DESCRIPTION_MAX_LEN = 90
FLAVOR_MAX_LEN = 150
ID_PATTERN = '^[a-z0-9_]+$'


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
            SCHEMA_VALIDATORS: [
                Type(str, int),
                IfConditionValid(ParamValid(P_EFFECT_TYPE, In([EFFECT_TYPE_APPLY_BUFF, EFFECT_TYPE_REMOVE_BUFF])), In(buffs)),
                IfConditionValid(ParamValid(P_EFFECT_TYPE, Exact(EFFECT_TYPE_SPAWN)), In(objects)),
                IfConditionValid(ParamValid(P_EFFECT_TYPE, In([EFFECT_TYPE_GAIN_CARD, EFFECT_TYPE_REMOVE_CARD])), In(cards)),
                IfConditionValid(ParamValid(P_EFFECT_TYPE, Exact(EFFECT_TYPE_DROP_CARD_OF_TYPE)), In(CARD_TYPES)),
                IfConditionValid(ParamValid(P_EFFECT_TYPE, In(EFFECTS_WITHOUT_VALUE)), NoParam(P_EFFECT_VALUE)),
            ]
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
            SCHEMA_VALIDATORS: [Type(int), ParamValid(P_EFFECT_TYPE, In([EFFECT_TYPE_SPAWN]))]
        },
        P_EFFECT_CARD_TYPE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str),
                                In(cards),
                                ParamValid(P_EFFECT_TYPE, In([EFFECT_TYPE_REDUCE_CARDCOST, EFFECT_TYPE_ADD_CARDCOST])),
                                StrMatchRe('[a-z0-9]+')]
        },
        P_EFFECT_BUFF_DURATION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(int), ParamValid(P_EFFECT_TYPE, Exact(EFFECT_TYPE_APPLY_BUFF))]
        },
    }
}

card_action_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_CARD_DESCRIPTION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str), StrNotEmpty(), StrShortenThan(DESCRIPTION_MAX_LEN)]
        },
        P_CARD_FLAVOR: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str), StrNotEmpty(), StrShortenThan(FLAVOR_MAX_LEN)]
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
            SCHEMA_VALIDATORS: [Type(str), StrShortenThan(DESCRIPTION_MAX_LEN)]
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
            SCHEMA_VALIDATORS: [Type(dict),
                                ValidSchemaDictValues(case_schema),
                                ValidDictKeys(In(CASES))]
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
            SCHEMA_VALIDATORS: [Type(str), StrShortenThan(DESCRIPTION_MAX_LEN)]
        },
        P_OBJECT_CASES: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                ValidSchemaDictValues(case_schema),
                                ValidDictKeys(In(CASES))]
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
            SCHEMA_VALIDATORS: [Type(list), ValidListItems(In(cards))]
        },
    }
}

weapon_action_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        P_WEAPON_DESCRIPTION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str), StrNotEmpty(), StrShortenThan(DESCRIPTION_MAX_LEN)]
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
            SCHEMA_VALIDATORS: [Type(list), ValidListItems(In(cards))]
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

db_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        SECTION_CARDS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [
                Type(dict),
                ValidDictKeys(StrMatchRe(ID_PATTERN)),
                ValidSchemaDictValues(card_schema)
            ]
        },
        SECTION_SHIPS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [
                Type(dict),
                ValidDictKeys(StrMatchRe(ID_PATTERN)),
                ValidSchemaDictValues(ship_schema)
            ]
        },
        SECTION_OBJECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [
                Type(dict),
                ValidDictKeys(StrMatchRe(ID_PATTERN)),
                ValidSchemaDictValues(object_schema)
            ]
        },
        SECTION_BUFFS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [
                Type(dict),
                ValidDictKeys(StrMatchRe(ID_PATTERN)),
                ValidSchemaDictValues(buff_schema)
            ]
        },
        SECTION_WEAPONS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [
                Type(dict),
                ValidDictKeys(StrMatchRe(ID_PATTERN)),
                ValidSchemaDictValues(weapon_schema)
            ]
        },
    }
}

if __name__ == '__main__':
    print('Checking db...')
    res = Schema(db_schema).validate(None, None, get_gb())
    res.print_endpoint()
    if res.is_valid:
        print(PrintColors.OKGREEN + 'No errors, cool!' + PrintColors.ENDC)
