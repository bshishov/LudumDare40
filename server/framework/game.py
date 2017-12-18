import logging
import uuid
from typing import List

from network import *
from utils import EventSubscription

__all__ = ['GameError', 'Player', 'GameBase']


class GameError(RuntimeError):
    """
        Game logic error
    """

    def __init__(self, message, crucial=True, *args):
        self.crucial = crucial
        super().__init__(message, *args)


class Player(object):
    def __init__(self, channel):
        self._channel = channel  # type: ClientChannel
        self._is_registered = False
        self._name = None
        self._id = str(uuid.uuid4())  # Unique player identifier
        self.in_queue = False
        self.in_game = False
        self.queue_args = None

        # Proxy events
        self.on_message = EventSubscription()
        self.on_disconnect = EventSubscription()

        self._channel.on_message.append(self._on_message)
        self._channel.on_disconnect.append(self._on_disconnect)

    def _on_message(self, message: Message):
        if message is None:
            return

        if not self.in_game:
            if message.domain == MessageDomain.LOBBY:
                if message.head == MessageHead.CLI_QUEUE_START and not self.in_queue:
                    self.queue_args = message.body
                    self.start_queue()
                elif message.head == MessageHead.CLI_QUEUE_STOP and self.in_queue:
                    self.stop_queue()

        self.on_message(self, message)

    def _on_disconnect(self, channel: ClientChannel):
        self.on_disconnect(self)

    def send(self, message):
        if self._channel.is_active:
            self._channel.send_message(message)

    def start_queue(self):
        if self.in_game:
            return
        self.in_queue = True
        self.send(LobbyMessage(MessageHead.MSG_SRV_QUEUE_STARTED, status='queue started'))

    def stop_queue(self):
        if self.in_game:
            return
        self.in_queue = False
        self.send(LobbyMessage(MessageHead.MSG_SRV_QUEUE_STOPPED, status='queue stopped'))

    def __del__(self):
        self._channel.on_message.remove(self._on_message)
        self._channel.on_disconnect.remove(self._on_message)


class GameBase(object):
    def __init__(self, players: List[Player]):
        self.id = str(uuid.uuid4())
        self.is_active = True

        self.logger = logging.getLogger('Game:{0}'.format(self.id))

        if len(players) == 0:
            raise GameError('Could not create a game, no players specified')

        self.players = players
        self.turn = 0  # index of the player which turn it is

    def begin(self):
        for player in self.players:
            player.in_game = True

            # Subscribe to player messages
            player.on_message.append(self._on_player_message)
            player.on_disconnect.append(self._on_player_disconnect)

        # Send that the game is started
        for side, player in enumerate(self.players):
            self.notify_player(player, MSG_SRV_GAME_BEGIN, status='Game begin', side=side)

    def _validate_message(self, player: Player, message: Message):
        if message is None:
            return False

        if message.domain != MSG_DOMAIN_GAME:
            self.logger.warning('Expected game message: {0}'.format(message))
            return False

        if message.body.get(GameMessageProtocol.P_GAME_ID) != self.id:
            self.logger.warning('Wrong game id: {0}'.format(message))
            self.notify_player(player, MSG_SRV_ERROR, status='wrong game id')
            return False
        return True

    def _on_player_message(self, player: Player, message: Message):
        if self._validate_message(player, message):
            self.on_player_message(player, message)

    def on_player_message(self, player: Player, message: Message):
        raise NotImplementedError

    def _on_player_disconnect(self, player: Player):
        self.notify_players(MSG_SRV_GAME_PLAYER_LEFT, status='Player disconnected', player=player._id)
        self.end(interrupted=True)

    def end_turn(self):
        self.turn = (self.turn + 1) % len(self.players)
        self.notify_players(MessageHead.SRV_GAME_TURN, status='End of turn', turn=self.turn)

    def get_state(self, perspective_player=None) -> dict:
        return {}

    def notify_players(self, head, status='', *args, **kwargs):
        for player in self.players:
            self.notify_player(player, head, status=status, *args, **kwargs)

    def notify_player(self, player, head, status='', *args, **kwargs):
        try:
            kwargs.update({
                GameMessageProtocol.P_STATE: self.get_state(perspective_player=player),
                GameMessageProtocol.P_YOUR_SIDE: self.players.index(player)
            })
            msg = GameMessage(head, game_id=self.id, status=status, *args, **kwargs)
            player.send(msg)
        except Exception as err:
            self.logger.error(err)

    def end(self, interrupted=False):
        self.logger.info('Game finished, interrupted={0}'.format(interrupted))
        self.notify_players(MessageHead.SRV_GAME_END, status='finished', interrupted=interrupted)
        self.is_active = False

    def close(self):
        for player in self.players:
            player.on_message.remove(self._on_player_message)
            player.on_disconnect.remove(self._on_player_disconnect)

            player.in_game = False
