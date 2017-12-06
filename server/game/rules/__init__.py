from game.rules.settings import *
from game.rules.ships import *
from game.rules.weapons import *
from game.rules.cards import *
from game.rules.objects import *
from game.rules.buffs import *


def get_gb():
    return {
        SECTION_CARDS: cards,
        SECTION_BUFFS: buffs,
        SECTION_OBJECTS: objects,
        SECTION_SHIPS: ships,
        SECTION_WEAPONS: weapons
    }
