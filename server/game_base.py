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
            if message.domain == MESSAGE_DOMAIN_LOBBY:
                if message.head == MESSAGE_HEAD_START_QUEUE and not self.in_queue:
                    self.args = message.body
                    self.start_queue()
                elif message.head == MESSAGE_HEAD_STOP_QUEUE and self.in_queue:
                    self.stop_queue()

    def send(self, message):
        if self._channel.is_active:
            self._channel.send_message(message)

    def start_queue(self):
        if self.in_game:
            return
        self.in_queue = True
        self.send(LobbyMessage(MESSAGE_HEAD_ACK, status='queue started'))

    def stop_queue(self):
        if self.in_game:
            return
        self.in_queue = False
        self.send(LobbyMessage(MESSAGE_HEAD_ACK, status='queue stopped'))


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
        self.player_a.send(GameMessage(MESSAGE_HEAD_HELLO,
                                       status='started',
                                       game_id=self.id,
                                       side=SIDE_A,
                                       state=self.get_state(SIDE_A)))
        self.player_b.send(GameMessage(MESSAGE_HEAD_HELLO,
                                       status='started',
                                       game_id=self.id,
                                       side=SIDE_B,
                                       state=self.get_state(SIDE_B)))

    def _validate_message(self, player, message):
        if message is None:
            return False

        if message.domain != MESSAGE_DOMAIN_GAME:
            self.logger.warning('Expected game message: {0}'.format(message))
            return False

        if message.body.get(P_GAME_ID) != self.id:
            self.logger.warning('Wrong game id: {0}'.format(message))
            player.send(GameMessage(MESSAGE_HEAD_ERROR, status='wrong game id'))
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
        self.player_b.send(GameMessage(MESSAGE_HEAD_PLAYER_LEFT, status='opponent disconnected'))
        self.end(interrupted=True)

    def _on_player_b_disconnect(self, channel):
        self.player_a.send(GameMessage(MESSAGE_HEAD_PLAYER_LEFT, status='opponent disconnected'))
        self.end(interrupted=True)

    def _on_game_message(self, message, entity):
        pass

    def end_turn(self):
        if self.turn == SIDE_A:
            self.turn = SIDE_B
        else:
            self.turn = SIDE_A

        self.player_a.send(GameMessage(MESSAGE_HEAD_TURN,
                                       status='turn',
                                       turn=self.turn,
                                       state=self.get_state(SIDE_A)))
        self.player_b.send(GameMessage(MESSAGE_HEAD_TURN,
                                       status='turn',
                                       turn=self.turn,
                                       state=self.get_state(SIDE_B)))

    def get_state(self, only_for=None):
        return {}

    def end(self, interrupted=False):
        self.logger.info('Game finished, interrupted={0}'.format(interrupted))
        try:
            self.player_a.send(GameMessage(MESSAGE_HEAD_ENDED, status='finished', interrupted=interrupted))
        except Exception as err:
            self.logger.error(err)

        try:
            self.player_b.send(GameMessage(MESSAGE_HEAD_ENDED, status='finished', interrupted=interrupted))
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
