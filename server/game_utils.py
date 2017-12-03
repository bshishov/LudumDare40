import random
from rules import *
from game_base import *


def select_cards(x, amount, max_of_each):
    if amount > len(x) * max_of_each:
        raise RuntimeError('Impossible to select so many cards')
    selected = {}
    total = 0
    while total < amount:
        # get random card
        card = x[random.randint(0, len(x) - 1)]
        if card not in selected:
            selected[card] = 1
            total += 1
        else:
            if selected[card] >= max_of_each:
                continue
            selected[card] += 1
            total += 1
    flat = []
    for c, n in selected.items():
        for i in range(n):
            flat.append(c)
    return flat


def is_allies(e1, e2):
    return e1.side == e2.side


def is_enemies(e1, e2):
    return e1.side != e2.side


def get_card(key):
    card = cards.get(key, None)
    if card is None:
        raise GameError('No such card: {0}'.format(key))
    return card


def get_buff(key):
    buff = buffs.get(key, None)
    if buff is None:
        raise GameError('No such buff: {0}'.format(key))
    return buff


def get_object(key):
    e = objects.get(key, None)
    if e is None:
        raise GameError('No such entity: {0}'.format(key))
    return e


def get_ship(key):
    e = ships.get(key, None)
    if e is None:
        raise GameError('No such ship: {0}'.format(key))
    return e


def get_weapon(key):
    w = weapons.get(key, None)
    if w is None:
        raise GameError('No such weapon: {0}'.format(key))
    return w


def filter_side(entities, side):
    """
        @type entities: List[EntityState]
        @type side: str
    """
    return [e for e in entities if e.side == side]


def filter_enemy(entities, entity):
    """
        @type entities: List[EntityState]
        @type entity: EntityState
    """
    return [e for e in entities if is_enemies(entity, e)]


def filter_ally(entities, entity):
    """
        @type entities: List[EntityState]
        @type entity: EntityState
    """
    return [e for e in entities if is_allies(entity, e)]


def filter_ship(entities, is_ship=True):
    """
        @type entities: List[EntityState]
        @type is_ship: bool
    """
    return [e for e in entities if hasattr(e, 'ship_name') == is_ship]


def filter_position(entities, pos):
    """
        @type entities: List[EntityState]
        @type pos: int
    """
    return [e for e in entities if e.position == pos]


def filter_position_range(entities, fr, to):
    """
        @type entities: List[EntityState]
        @type fr: int
        @type to: int
    """
    return [e for e in entities if e.position in range(min(fr, to), max(fr, to) + 1)]


def filter_direction(entities, start, direction=+1, pierce=True):
    """
        @type entities: List[EntityState]
        @type start: int
        @type direction: int
        @type pierce: bool
    """
    es = filter_position_range(entities, start, start + direction * 10)
    if not pierce and len(es) > 0:
        return [es[0], ]
    else:
        return es


def filter_exclude(entities, entity):
    """
        @type entities: List[EntityState]
        @type entity: EntityState
    """
    return [e for e in entities if e != entity]

import collections


def todict(obj):
  """
  Recursively convert a Python object graph to sequences (lists)
  and mappings (dicts) of primitives (bool, int, float, string, ...)
  """
  if isinstance(obj, str):
    return obj
  elif isinstance(obj, dict):
    return dict((key, todict(val)) for key, val in obj.items())
  elif isinstance(obj, collections.Iterable):
    return [todict(val) for val in obj]
  elif hasattr(obj, '__dict__'):
    return todict(vars(obj))
  elif hasattr(obj, '__slots__'):
    return todict(dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__')))
  return obj