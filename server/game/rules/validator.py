from game.rules import *
from utils.validation import *


TARGETS = list(Target)
EFFECT_TYPES = list(EffectType)
CARD_TYPES = list(CardType)
CASES = list(CaseType)

EFFECTS_WITHOUT_VALUE = [
    EffectType.DISARM,
    EffectType.ARM,
    EffectType.MUTE,
    EffectType.UNMUTE,
    EffectType.LOCK_POSITION,
    EffectType.UNLOCK_POSITION,
    EffectType.DESTROY,
    EffectType.DRAW_CARD,
    EffectType.SPECIAL_SWAP,
    EffectType.OFFENSE_APPROACH,
]


DESCRIPTION_MAX_LEN = 90
FLAVOR_MAX_LEN = 150
ID_PATTERN = '^[a-z0-9_]+$'


effect_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        Effect.TYPE: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(EffectType), In(EFFECT_TYPES)]
        },
        Effect.TARGET: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(Target), In(TARGETS)]
        },
        Effect.VALUE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [
                Type(str, int, CardType),
                IfConditionValid(ParamValid(Effect.TYPE, In([EffectType.APPLY_BUFF, EffectType.REMOVE_BUFF])), In(buffs)),
                IfConditionValid(ParamValid(Effect.TYPE, Exact(EffectType.SPAWN)), In(objects)),
                IfConditionValid(ParamValid(Effect.TYPE, In([EffectType.GAIN_CARD, EffectType.REMOVE_CARD])), In(cards)),
                IfConditionValid(ParamValid(Effect.TYPE, Exact(EffectType.DROP_CARD_OF_TYPE)), Type(CardType)),
                IfConditionValid(ParamValid(Effect.TYPE, In(EFFECTS_WITHOUT_VALUE)), NoParam(Effect.VALUE)),
            ]
        },
        Effect.RANGE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str, int)]
        },
        Effect.RANGE_MOD: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        Effect.SPAWN_POSITION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(int), ParamValid(Effect.TYPE, In([EffectType.SPAWN]))]
        },
        Effect.CARD_TYPE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(CardType),
                                In(cards),
                                ParamValid(Effect.TYPE, In([EffectType.REDUCE_CARDCOST, EffectType.ADD_CARDCOST])),
                                StrMatchRe('[a-z0-9]+')]
        },
        Effect.BUFF_DURATION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(int), ParamValid(Effect.TYPE, Exact(EffectType.APPLY_BUFF))]
        },
    }
}

card_action_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        Card.DESCRIPTION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str), StrNotEmpty(), StrShortenThan(DESCRIPTION_MAX_LEN)]
        },
        Card.FLAVOR: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str), StrNotEmpty(), StrShortenThan(FLAVOR_MAX_LEN)]
        },
        Card.COST: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        Card.EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        }
    }
}

card_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        Card.FULL_NAME: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        Card.TYPE: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(CardType), In(CARD_TYPES)]
        },
        Card.DECK: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(bool)]
        },
        Card.ACTION_OFFENSE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                HasParam(Card.ACTION_DEFENSE),
                                NoParam(Card.ACTION_SAME),
                                Schema(card_action_schema)]
        },
        Card.ACTION_DEFENSE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                HasParam(Card.ACTION_OFFENSE),
                                NoParam(Card.ACTION_SAME),
                                Schema(card_action_schema)]
        },
        Card.ACTION_SAME: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                NoParam(Card.ACTION_DEFENSE),
                                NoParam(Card.ACTION_OFFENSE),
                                Schema(card_action_schema)]
        },
    }
}

case_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        Case.SOURCE_TARGET: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(Target), In(TARGETS)]
        },
        Case.ARG: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str), IfConditionValid(Exact(CaseType.PLAY_CARD), In(cards))]
        },
        Case.EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        },
    }
}

buff_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        Buff.FULL_NAME: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        Buff.DESCRIPTION: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str), StrShortenThan(DESCRIPTION_MAX_LEN)]
        },
        Buff.DURATION: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        Buff.ON_APPLY_EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        },
        Buff.ON_ROUND_EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        },
        Buff.ON_REMOVE_EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        },
        Buff.CASES: {
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
        Entity.FULL_NAME: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        Entity.DESCRIPTION: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str), StrShortenThan(DESCRIPTION_MAX_LEN)]
        },
        Entity.HP: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        Entity.CASES: {
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
        Ship.HP: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        Ship.MAX_ENERGY: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        Ship.ENERGY_PER_TURN: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        Ship.CARDS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), ValidListItems(In(cards))]
        },
    }
}

weapon_action_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        Weapon.DESCRIPTION: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(str), StrNotEmpty(), StrShortenThan(DESCRIPTION_MAX_LEN)]
        },
        Weapon.COST: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(int)]
        },
        Weapon.EFFECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), SchemaForEachElementInList(effect_schema)]
        }
    }
}

weapon_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        Weapon.FULL_NAME: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(str)]
        },
        Weapon.CARDS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [Type(list), ValidListItems(In(cards))]
        },
        Weapon.ACTION_OFFENSE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                HasParam(Weapon.ACTION_DEFENSE),
                                NoParam(Weapon.ACTION_SAME),
                                Schema(weapon_action_schema)]
        },
        Weapon.ACTION_DEFENSE: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                HasParam(Weapon.ACTION_OFFENSE),
                                NoParam(Weapon.ACTION_SAME),
                                Schema(weapon_action_schema)]
        },
        Weapon.ACTION_SAME: {
            SCHEMA_REQUIRED: False,
            SCHEMA_VALIDATORS: [Type(dict),
                                NoParam(Weapon.ACTION_DEFENSE),
                                NoParam(Weapon.ACTION_OFFENSE),
                                Schema(weapon_action_schema)]
        },
    }
}

db_schema = {
    SCHEMA_ONLY_THESE_FIELDS: True,
    SCHEMA_FIELDS: {
        Section.CARDS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [
                Type(dict),
                ValidDictKeys(StrMatchRe(ID_PATTERN)),
                ValidSchemaDictValues(card_schema)
            ]
        },
        Section.SHIPS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [
                Type(dict),
                ValidDictKeys(StrMatchRe(ID_PATTERN)),
                ValidSchemaDictValues(ship_schema)
            ]
        },
        Section.OBJECTS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [
                Type(dict),
                ValidDictKeys(StrMatchRe(ID_PATTERN)),
                ValidSchemaDictValues(object_schema)
            ]
        },
        Section.BUFFS: {
            SCHEMA_REQUIRED: True,
            SCHEMA_VALIDATORS: [
                Type(dict),
                ValidDictKeys(StrMatchRe(ID_PATTERN)),
                ValidSchemaDictValues(buff_schema)
            ]
        },
        Section.WEAPONS: {
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
