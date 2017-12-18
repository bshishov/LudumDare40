from game.rules.settings import *

ships = {
    'tank': {
        Ship.HP: 25,
        Ship.MAX_ENERGY: 8,
        Ship.ENERGY_PER_TURN: 3,
        Ship.CARDS: ['power', 'ram', 'eboost', 'stop'],
    },
    'fighter': {
        Ship.HP: 17,
        Ship.MAX_ENERGY: 12,
        Ship.ENERGY_PER_TURN: 3,
        Ship.CARDS: ['tab', 'barrel', 'missile', 'wingdrone'],
    },
    'scout': {
        Ship.HP: 20,
        Ship.MAX_ENERGY: 10,
        Ship.ENERGY_PER_TURN: 4,
        Ship.CARDS: ['mine', 'healdrone', 'reactor', 'core'],
    },
}
