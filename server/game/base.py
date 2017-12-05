import connection
import uuid
import logging

from protocol import *

SIDE_A = 'a'
SIDE_B = 'b'


class GameError(RuntimeError):
    """
        Game logic error
    """

    def __init__(self, message, crucial=True, *args):
        self.crucial = crucial
        super().__init__(message, *args)


class Player(object):
    def __init__(self, channel):
        self._channel = channel  # type: connection.ClientChannel
        self._is_registered = False
        self._name = None
        self._id = str(uuid.uuid4())
        self.in_queue = False
        self.in_game = False
        self.args = None

        # Proxy events
        self.on_message = self._channel.on_message
        self.on_disconnect = self._channel.on_disconnect

        self.on_message.append(self._on_message)

    def _on_message(self, message):
        if message is None:
            return

        if not self.in_game:
            if message.domain == MSG_DOMAIN_LOBBY:
                if message.head == MSG_CLI_QUEUE_START and not self.in_queue:
                    self.args = message.body
                    self.start_queue()
                elif message.head == MSG_CLI_QUEUE_STOP and self.in_queue:
                    self.stop_queue()

    def send(self, message):
        if self._channel.is_active:
            self._channel.send_message(message)

    def start_queue(self):
        if self.in_game:
            return
        self.in_queue = True
        self.send(LobbyMessage(MSG_SRV_QUEUE_STARTED, status='queue started'))

    def stop_queue(self):
        if self.in_game:
            return
        self.in_queue = False
        self.send(LobbyMessage(MSG_SRV_QUEUE_STOPPED, status='queue stopped'))


class GameBase(object):
    def __init__(self, player_a, player_b):
        self.id = str(uuid.uuid4())
        self.is_active = True

        self.logger = logging.getLogger('Game:{0}'.format(self.id))
        self.player_a = player_a  # type: Player
        self.player_b = player_b  # type: Player

        self.turn = SIDE_A

    def begin(self):
        self.player_a.in_game = True
        self.player_b.in_game = True

        # Subscribe to player messages
        self.player_a.on_message.append(self._on_player_a_message)
        self.player_b.on_message.append(self._on_player_b_message)
        self.player_a.on_disconnect.append(self._on_player_a_disconnect)
        self.player_b.on_disconnect.append(self._on_player_b_disconnect)

        # Send that the game is started
        self.notify_player(self.player_a, MSG_SRV_GAME_BEGIN, status='Game begin', side=SIDE_A)
        self.notify_player(self.player_b, MSG_SRV_GAME_BEGIN, status='Game begin', side=SIDE_B)

    def _validate_message(self, player, message):
        if message is None:
            return False

        if message.domain != MSG_DOMAIN_GAME:
            self.logger.warning('Expected game message: {0}'.format(message))
            return False

        if message.body.get(P_MSG_GAME_ID) != self.id:
            self.logger.warning('Wrong game id: {0}'.format(message))
            self.notify_player(player, MSG_SRV_ERROR, status='wrong game id')
            return False
        return True

    def _on_player_a_message(self, message):
        if self._validate_message(self.player_a, message):
            return self.on_player_a_message(message)

    def _on_player_b_message(self, message):
        if self._validate_message(self.player_b, message):
            return self.on_player_b_message(message)

    def on_player_a_message(self, message):
        raise NotImplementedError

    def on_player_b_message(self, message):
        raise NotImplementedError

    def _on_player_a_disconnect(self, channel):
        self.notify_player(self.player_b, MSG_SRV_GAME_PLAYER_LEFT, status='opponent disconnected')
        self.end(interrupted=True)

    def _on_player_b_disconnect(self, channel):
        self.notify_player(self.player_a, MSG_SRV_GAME_PLAYER_LEFT, status='opponent disconnected')
        self.end(interrupted=True)

    def _on_game_message(self, message, entity):
        pass

    def end_turn(self):
        if self.turn == SIDE_A:
            self.turn = SIDE_B
        else:
            self.turn = SIDE_A

        self.notify_players(MSG_SRV_GAME_TURN, status='End of turn', turn=self.turn)

    def get_state(self, perspective_player=None):
        return {}

    def notify_players(self, head, status='', *args, **kwargs):
        self.notify_player(self.player_a, head, status=status, *args, **kwargs)
        self.notify_player(self.player_b, head, status=status, *args, **kwargs)

    def notify_player(self, player, head, status='', *args, **kwargs):
        msg = GameMessage(head,
                          game_id=self.id,
                          status=status,
                          state=self.get_state(perspective_player=player),
                          *args, **kwargs)
        player.send(msg)

    def end(self, interrupted=False):
        self.logger.info('Game finished, interrupted={0}'.format(interrupted))
        try:
            self.notify_player(self.player_a, MSG_SRV_GAME_END,
                               status='finished', interrupted=interrupted)
        except Exception as err:
            self.logger.error(err)

        try:
            self.notify_player(self.player_b, MSG_SRV_GAME_END,
                               status='finished', interrupted=interrupted)
        except Exception as err:
            self.logger.error(err)

        self.is_active = False

    def close(self):
        self.player_a.in_game = False
        self.player_b.in_game = False

        # Unsubscribe
        self.player_a.on_message.remove(self._on_player_a_message)
        self.player_b.on_message.remove(self._on_player_b_message)
        self.player_a.on_disconnect.remove(self._on_player_a_disconnect)
        self.player_b.on_disconnect.remove(self._on_player_b_disconnect)
