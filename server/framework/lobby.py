import logging
import threading
import time
from typing import List

from framework.game import *
from network import *

MATCHMAKING_DELAY = 10  # seconds
GAME_CHECK_DELAY = 10  # seconds


__all__ = ['GameInitializer', 'Lobby', ]


class GameInitializer(object):
    def select_players(self, queued_players: List[Player]) -> List[Player]:
        raise NotImplementedError

    def create_game(self, players: List[Player]) -> GameBase:
        raise NotImplementedError


class Lobby(object):
    def __init__(self, initializers: List[GameInitializer]):
        self._initializers = initializers

        self._logger = logging.getLogger(self.__class__.__name__)
        self._players = {}
        self._players_lock = threading.Lock()
        self._games = []

        self._game_thread = threading.Thread(target=self.game_worker)
        self._matchmaking_thread = threading.Thread(target=self.matchmaking_worker)

        self._game_thread.start()
        self._matchmaking_thread.start()

    def on_client_connect(self, channel: ClientChannel):
        player = Player(channel)  # type: Player
        with self._players_lock:
            self._players[channel] = player
        player.send(LobbyMessage(MessageHead.SRV_HELLO, status='Welcome',
                                 version=PROTOCOL_VERSION,
                                 players=len(self._players)))
        self._logger.info('Player connected')

    def on_client_disconnect(self, channel):
        with self._players_lock:
            if channel in self._players:
                del self._players[channel]
        self._logger.info('Player disconnected')

    def run(self):
        self._game_thread = threading.Thread(target=self.game_worker)
        self._matchmaking_thread = threading.Thread(target=self.matchmaking_worker)

    def matchmaking_worker(self):
        self._logger.info('Matchmaking started')
        while True:
            with self._players_lock:
                queued_players = [player for channel, player in self._players.items() if player.in_queue]

            self._logger.debug('Matchmaking: {0} players in queue'.format(len(queued_players)))

            if len(queued_players) <= 0:
                time.sleep(MATCHMAKING_DELAY)

            for initializer in self._initializers:
                players = initializer.select_players(queued_players)
                if players is not None and len(players) > 0:
                    self.init_game(initializer, players)

    def init_game(self, initializer, players):
        g = None
        try:
            for player in players:
                player.stop_queue()

            self._logger.debug('Creating game for players: {0}'.format(players))
            g = initializer.create_game(players)

            for player in players:
                # Send that the game is started
                player.send(LobbyMessage(MessageHead.SRV_QUEUE_GAME_CREATED, status='Game created', game_id=g.id))

        except Exception as err:
            for player in players:
                player.send(LobbyMessage(MessageHead.SRV_ERROR, status='Failed to create a game', err=str(err)))
                player.send(LobbyMessage(MessageHead.SRV_ERROR, status='Failed to create a game', err=str(err)))
            self._logger.debug('Failed to create a game: {0}'.format(str(err)))
            if g is not None:
                g.close()
                self._logger.debug('Closing game')
                del g
        if g is not None and g.is_active:
            g.begin()
            self._games.append(g)
            self._logger.debug('Game started')

    def game_worker(self):
        while True:
            time.sleep(GAME_CHECK_DELAY)
            games_to_remove = []
            # Collect non-active games
            for g in self._games:
                if not g.is_active:
                    games_to_remove.append(g)

            # Remove non-active games
            for g in games_to_remove:
                g.close()
                self._games.remove(g)
                self._logger.debug('Removed game: {0}'.format(g))
                del g
