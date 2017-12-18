import json
import csv

from game.rules.settings import *
from game.rules.ships import *
from game.rules.weapons import *
from game.rules.cards import *
from game.rules.objects import *
from game.rules.buffs import *


class RulesError(RuntimeError):
    pass


def get_card(key: str) -> dict:
    card = cards.get(key, None)
    if card is None:
        raise RulesError('No such card: {0}'.format(key))
    return card


def get_buff(key: str) -> dict:
    buff = buffs.get(key, None)
    if buff is None:
        raise RulesError('No such buff: {0}'.format(key))
    return buff


def get_object(key: str) -> dict:
    e = objects.get(key, None)
    if e is None:
        raise RulesError('No such entity: {0}'.format(key))
    return e


def get_ship(key: str) -> dict:
    e = ships.get(key, None)
    if e is None:
        raise RulesError('No such ship: {0}'.format(key))
    return e


def get_weapon(key: str) -> dict:
    w = weapons.get(key, None)
    if w is None:
        raise RulesError('No such weapon: {0}'.format(key))
    return w


def get_gb():
    return {
        Section.CARDS: cards,
        Section.BUFFS: buffs,
        Section.OBJECTS: objects,
        Section.SHIPS: ships,
        Section.WEAPONS: weapons
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
                del o[Effect.TARGET]
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
                      Card.FULL_NAME,
                      Card.TYPE,
                      Card.DECK,
                      p(Card.ACTION_OFFENSE, Card.DESCRIPTION),
                      p(Card.ACTION_OFFENSE, Card.FLAVOR),
                      p(Card.ACTION_OFFENSE, Card.COST),
                      p(Card.ACTION_OFFENSE, Card.EFFECTS, '0', Effect.TARGET),
                      p(Card.ACTION_OFFENSE, Card.EFFECTS, '0', 'effect'),
                      p(Card.ACTION_OFFENSE, Card.EFFECTS, '1', Effect.TARGET),
                      p(Card.ACTION_OFFENSE, Card.EFFECTS, '1', 'effect'),
                      p(Card.ACTION_OFFENSE, Card.EFFECTS, '2', Effect.TARGET),
                      p(Card.ACTION_OFFENSE, Card.EFFECTS, '2', 'effect'),
                      p(Card.ACTION_OFFENSE, Card.EFFECTS, '3', Effect.TARGET),
                      p(Card.ACTION_OFFENSE, Card.EFFECTS, '3', 'effect'),
                      p(Card.ACTION_OFFENSE, Card.EFFECTS, '4', Effect.TARGET),
                      p(Card.ACTION_OFFENSE, Card.EFFECTS, '4', 'effect'),
                      p(Card.ACTION_DEFENSE, Card.DESCRIPTION),
                      p(Card.ACTION_DEFENSE, Card.FLAVOR),
                      p(Card.ACTION_DEFENSE, Card.COST),
                      p(Card.ACTION_DEFENSE, Card.EFFECTS, '0', Effect.TARGET),
                      p(Card.ACTION_DEFENSE, Card.EFFECTS, '0', 'effect'),
                      p(Card.ACTION_DEFENSE, Card.EFFECTS, '1', Effect.TARGET),
                      p(Card.ACTION_DEFENSE, Card.EFFECTS, '1', 'effect'),
                      p(Card.ACTION_DEFENSE, Card.EFFECTS, '2', Effect.TARGET),
                      p(Card.ACTION_DEFENSE, Card.EFFECTS, '2', 'effect'),
                      p(Card.ACTION_DEFENSE, Card.EFFECTS, '3', Effect.TARGET),
                      p(Card.ACTION_DEFENSE, Card.EFFECTS, '3', 'effect'),
                      p(Card.ACTION_DEFENSE, Card.EFFECTS, '4', Effect.TARGET),
                      p(Card.ACTION_DEFENSE, Card.EFFECTS, '4', 'effect'),
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
