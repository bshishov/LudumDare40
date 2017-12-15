import json
import csv

from game.rules.settings import *
from game.rules.ships import *
from game.rules.weapons import *
from game.rules.cards import *
from game.rules.objects import *
from game.rules.buffs import *


class GameStateProtocol(object):
    P_ID = 'id'
    P_TURN = 'turn'
    P_OBJECTS = 'objects'


class BuffStateProtocol(object):
    P_NAME = 'name',
    P_DURATION = 'duration'


class CardStateProtocol(object):
    P_NAME = 'name',
    P_COST_OFFENSE = 'cost_offense'
    P_COST_DEFENSE = 'cost_defense'


class EntityStateProtocol(object):
    P_ID = 'id'
    P_NAME = 'name'
    P_POSITION = 'position'
    P_SIDE = 'side'
    P_HP = 'hp'
    P_ENERGY = 'energy'
    P_MAX_ENERGY = 'max_energy'
    P_ENERGY_GAIN = 'energy_gain'
    P_BUFFS = 'buffs'
    P_MUTED = 'muted'
    P_ARMED = 'armed'
    P_LOCKED = 'locked'
    P_DAMAGE_MOD = 'damage_mod'
    P_BUFFABLE = 'buffable'
    P_IS_PLAYER = 'is_player'


class PlayerEntityProtocol(object):
    P_SHIP_NAME = 'ship_name'
    P_WEAPON_NAME = 'weapon_name'
    P_HAND = 'hand'
    P_DECK = 'deck'
    P_CARDS_IN_HAND = 'hand_cards'
    P_CARDS_IN_DECK = 'deck_cards'


def get_gb():
    return {
        SECTION_CARDS: cards,
        SECTION_BUFFS: buffs,
        SECTION_OBJECTS: objects,
        SECTION_SHIPS: ships,
        SECTION_WEAPONS: weapons
    }


def export_db(filename):
    data = json.dumps(get_gb(), sort_keys=True, indent=4)
    with open(filename, 'w') as f:
        f.write(data)


def export_cards_to_excel_csv(filename):
    def p(*args) -> str:
        return '/'.join(args)

    def resolve_field(card_key, field):
        if field == 'id':
            return card_key

        c = cards[card_key]

        parts = field.split('/')
        if len(parts) == 1:
            return c.get(field, '--')

        o = c
        for pp in parts:
            if pp in ['0', '1', '2', '3', '4']:
                pp = int(pp)
            if pp == 'effect':
                del o[P_EFFECT_TARGET]
            else:
                try:
                    o = o[pp]
                except KeyError:
                    return '--'
                except IndexError:
                    return '--'
        return o

    def resolve(card_key, fields) -> dict:
        out = {}
        for f in fields:
            out[f] = resolve_field(card_key, f)
        return out

    with open(filename, 'w', newline='') as csv_file:
        fieldnames = ['id',
                      P_CARD_FULL_NAME,
                      P_CARD_TYPE,
                      P_CARD_DECK,
                      p(P_CARD_ACTION_OFFENSE, P_CARD_DESCRIPTION),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_FLAVOR),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_COST),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_EFFECTS, '0', P_EFFECT_TARGET),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_EFFECTS, '0', 'effect'),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_EFFECTS, '1', P_EFFECT_TARGET),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_EFFECTS, '1', 'effect'),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_EFFECTS, '2', P_EFFECT_TARGET),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_EFFECTS, '2', 'effect'),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_EFFECTS, '3', P_EFFECT_TARGET),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_EFFECTS, '3', 'effect'),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_EFFECTS, '4', P_EFFECT_TARGET),
                      p(P_CARD_ACTION_OFFENSE, P_CARD_EFFECTS, '4', 'effect'),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_DESCRIPTION),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_FLAVOR),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_COST),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_EFFECTS, '0', P_EFFECT_TARGET),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_EFFECTS, '0', 'effect'),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_EFFECTS, '1', P_EFFECT_TARGET),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_EFFECTS, '1', 'effect'),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_EFFECTS, '2', P_EFFECT_TARGET),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_EFFECTS, '2', 'effect'),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_EFFECTS, '3', P_EFFECT_TARGET),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_EFFECTS, '3', 'effect'),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_EFFECTS, '4', P_EFFECT_TARGET),
                      p(P_CARD_ACTION_DEFENSE, P_CARD_EFFECTS, '4', 'effect'),
                      ]
        csv_file.write('sep=,\r\n')
        writer = csv.DictWriter(csv_file,
                                dialect='excel',
                                fieldnames=fieldnames,
                                delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for c in cards:
            writer.writerow(resolve(c, fieldnames))


if __name__ == '__main__':
    export_cards_to_excel_csv('cards.csv')
