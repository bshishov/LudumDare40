from typing import List
from game.states import EntityState
from game.rules import *





def is_allies(e1: EntityState, e2: EntityState) -> bool:
    return e1.side == e2.side


def is_enemies(e1: EntityState, e2: EntityState) -> bool:
    return e1.side != e2.side


def filter_side(entities: List[EntityState], side: str) -> List[EntityState]:
    return [e for e in entities if e.side == side]


def filter_enemy(entities: List[EntityState], entity: EntityState) -> List[EntityState]:
    return [e for e in entities if is_enemies(entity, e)]


def filter_ally(entities: List[EntityState], entity: EntityState) -> List[EntityState]:
    return [e for e in entities if is_allies(entity, e)]


def filter_ship(entities: List[EntityState], is_ship: bool=True) -> List[EntityState]:
    return [e for e in entities if hasattr(e, 'ship_name') == is_ship]


def filter_position(entities: List[EntityState], pos: int) -> List[EntityState]:
    return [e for e in entities if e.position == pos]


def filter_position_range(entities: List[EntityState], fr: int, to: int) -> List[EntityState]:
    return [e for e in entities if e.position in range(min(fr, to), max(fr, to) + 1)]


def filter_direction(entities: List[EntityState], start: int, direction: int=+1, pierce: bool=True) -> List[EntityState]:
    es = filter_position_range(entities, start, start + direction * 10)
    if not pierce and len(es) > 0:
        return [es[0], ]
    else:
        return es


def filter_exclude(entities: List[EntityState], entity: EntityState) -> List[EntityState]:
    return [e for e in entities if e != entity]