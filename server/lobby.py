import threading
import logging
import time

from protocol import *
import game.base
import game.card_game
from game.rules import get_gb


MATCHMAKING_DELAY = 10  # seconds
GAME_CHECK_DELAY = 10  # seconds


class Lobby(object):
    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._players = {}
        self._players_lock = threading.Lock()
        self._games = []

        self._game_thread = threading.Thread(target=self.game_worker)
        self._matchmaking_thread = threading.Thread(target=self.matchmaking_worker)

        self._game_thread.start()
        self._matchmaking_thread.start()

    def on_client_connect(self, channel):
        # channel:type
        player = game.base.Player(channel)  # type: game.base.Player
        with self._players_lock:
            self._players[channel] = player
        player.send(LobbyMessage(MSG_SRV_HELLO, status='Welcome',
                                 version=VERSION,
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
            time.sleep(MATCHMAKING_DELAY)
            with self._players_lock:
                queued_players = [p for channel, p in self._players.items() if p.in_queue]
                if len(queued_players) > 0:
                    self._logger.debug('Matchmaking: {0} players in queue'.format(len(queued_players)))

                if len(queued_players) >= 2:
                    self.init_game(queued_players[0], queued_players[1])

    def init_game(self, player_a, player_b):
        g = None
        try:
            # Stop player queues
            player_a.stop_queue()
            player_b.stop_queue()

            self._logger.debug('Creating game for players: A:{0} B:{1}'.format(player_a, player_b))
            g = game.card_game.create(player_a, player_b)

            # Send that the game is started
            player_a.send(LobbyMessage(MSG_SRV_QUEUE_GAME_CREATED,
                                       status='Game created',
                                       game_id=g.id))
            player_b.send(LobbyMessage(MSG_SRV_QUEUE_GAME_CREATED,
                                       status='Game created',
                                       game_id=g.id))

        except Exception as err:
            player_a.send(LobbyMessage(MSG_SRV_ERROR, status='Failed to create a game', err=str(err)))
            player_b.send(LobbyMessage(MSG_SRV_ERROR, status='Failed to create a game', err=str(err)))
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
