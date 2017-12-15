import random
from typing import List, Dict

from game.rules import *
from game.base import *
from game.types import EntityStateType


def select_cards(deck: List[str], amount: int, max_of_each: int) -> List[str]:
    if amount > len(deck) * max_of_each:
        raise RuntimeError('Impossible to select so many cards')
    selected = {}
    total = 0
    while total < amount:
        # get random card
        card = deck[random.randint(0, len(deck) - 1)]
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


def is_allies(e1: EntityStateType, e2: EntityStateType) -> bool:
    return e1.side == e2.side


def is_enemies(e1: EntityStateType, e2: EntityStateType) -> bool:
    return e1.side != e2.side


def get_card(key: str) -> Dict:
    card = cards.get(key, None)
    if card is None:
        raise GameError('No such card: {0}'.format(key))
    return card


def get_buff(key: str) -> Dict:
    buff = buffs.get(key, None)
    if buff is None:
        raise GameError('No such buff: {0}'.format(key))
    return buff


def get_object(key: str) -> Dict:
    e = objects.get(key, None)
    if e is None:
        raise GameError('No such entity: {0}'.format(key))
    return e


def get_ship(key: str) -> Dict:
    e = ships.get(key, None)
    if e is None:
        raise GameError('No such ship: {0}'.format(key))
    return e


def get_weapon(key: str) -> Dict:
    w = weapons.get(key, None)
    if w is None:
        raise GameError('No such weapon: {0}'.format(key))
    return w


def filter_side(entities: List[EntityStateType], side: str) -> List[EntityStateType]:
    return [e for e in entities if e.side == side]


def filter_enemy(entities: List[EntityStateType], entity: EntityStateType) -> List[EntityStateType]:
    return [e for e in entities if is_enemies(entity, e)]


def filter_ally(entities: List[EntityStateType], entity: EntityStateType) -> List[EntityStateType]:
    return [e for e in entities if is_allies(entity, e)]


def filter_ship(entities: List[EntityStateType], is_ship: bool=True) -> List[EntityStateType]:
    return [e for e in entities if hasattr(e, 'ship_name') == is_ship]


def filter_position(entities: List[EntityStateType], pos: int) -> List[EntityStateType]:
    return [e for e in entities if e.position == pos]


def filter_position_range(entities: List[EntityStateType], fr: int, to: int) -> List[EntityStateType]:
    return [e for e in entities if e.position in range(min(fr, to), max(fr, to) + 1)]


def filter_direction(entities: List[EntityStateType], start: int, direction: int=+1, pierce: bool=True) -> List[EntityStateType]:
    es = filter_position_range(entities, start, start + direction * 10)
    if not pierce and len(es) > 0:
        return [es[0], ]
    else:
        return es


def filter_exclude(entities: List[EntityStateType], entity: EntityStateType) -> List[EntityStateType]:
    return [e for e in entities if e != entity]
