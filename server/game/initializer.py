from typing import List

from framework.game import Player, GameBase
from framework.lobby import GameInitializer
from game.card_game import CardGame


class CardGameInitializer(GameInitializer):
    def select_players(self, queued_players: List[Player]) -> List[Player]:
        if len(queued_players) >= 2:
            return [queued_players[0], queued_players[1]]
        return []

    def create_game(self, players: List[Player]) -> GameBase:
        return CardGame(players[0], players[1])
