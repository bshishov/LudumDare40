from game.rules.settings import *

ships = {
    'tank': {
        P_SHIP_HP: 30,
        P_SHIP_MAX_ENERGY: 14,
        P_SHIP_ENERGY_PER_TURN: 5,
        P_SHIP_CARDS: ['power', 'ram', 'eboost', 'stop'],
    },
    'fighter': {
        P_SHIP_HP: 20,
        P_SHIP_MAX_ENERGY: 20,
        P_SHIP_ENERGY_PER_TURN: 4,
        P_SHIP_CARDS: ['tab', 'barrel', 'missile', 'wingdrone'],
    },
    'scout': {
        P_SHIP_HP: 25,
        P_SHIP_MAX_ENERGY: 18,
        P_SHIP_ENERGY_PER_TURN: 6,
        P_SHIP_CARDS: ['mine', 'healdrone', 'reactor', 'core'],
    },
}
