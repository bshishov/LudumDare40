import random
from typing import List


__all__ = ['select_cards', 'is_allies', 'is_enemies', 'filter_side', 'filter_enemy', 'filter_ally', 'filter_ship',
           'filter_position', 'filter_position_range', 'filter_direction', 'filter_exclude']


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


