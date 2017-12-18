from enum import Enum
import json

__all__ = ['PROTOCOL_VERSION', 'ENCODING', 'MessageDomain', 'MessageHead', 'Message', 'GameMessage', 'LobbyMessage',
           'serialize', 'deserialize']

PROTOCOL_VERSION = '0.0.1'
ENCODING = 'utf-8'


class MessageDomain(Enum):
    GAME = 'game'
    LOBBY = 'lobby'


class MessageHead(Enum):
    DEFAULT = ''

    # [SERVER] Base server messages
    SRV_ERROR = 's.error'
    SRV_HELLO = 's.hello'

    # [SERVER] Queue message
    MSG_SRV_QUEUE_STARTED = 's.q.started'
    MSG_SRV_QUEUE_STOPPED = 's.q.stopped'
    SRV_QUEUE_GAME_CREATED = 's.g.created'

    # [SERVER] Game messages
    MSG_SRV_GAME_BEGIN = 's.g.begin'
    SRV_GAME_END = 's.g.end'
    MSG_SRV_GAME_PLAYER_LEFT = 's.g.player_left'
    SRV_GAME_TURN = 's.g.turn'
    MSG_SRV_GAME_ACTION = 's.g.action'  # redirect player action
    MSG_SRV_GAME_EFFECT = 's.g.effect'

    # [CLIENT] Messages
    CLI_QUEUE_START = 'c.q.start'
    CLI_QUEUE_STOP = 'c.q.stop'
    CLI_GAME_ACTION = 'c.g.action'


class GameMessageProtocol(Enum):
    P_STATE = 'state'
    P_GAME_ID = 'game_id'
    P_YOUR_SIDE = 'side'


class Message(object):
    type = ''
    status = ''
    body = {}

    def __init__(self, domain, head, status='', **kwargs):
        self.head = head
        self.domain = domain
        self.status = status
        self.body = kwargs

    def __str__(self):
        return str(self.__dict__)


class GameMessage(Message):
    def __init__(self, head, game_id, *args, **kwargs):
        kwargs.update({GameMessageProtocol.P_GAME_ID.value: game_id})
        super().__init__(domain=MessageDomain.GAME, head=head, *args, **kwargs)


class LobbyMessage(Message):
    def __init__(self, head, *args, **kwargs):
        super().__init__(domain=MessageDomain.LOBBY, head=head, *args, **kwargs)


def serialize(obj):
    if isinstance(obj, Message):
        data = json.dumps(obj.__dict__)
    else:
        data = json.dumps(obj)
    return bytes(data, ENCODING)


def deserialize(data):
    if isinstance(data, bytes):
        data = data.decode(ENCODING)
    msg = Message(MessageDomain.GAME, MessageHead.DEFAULT)
    msg.__dict__ = json.loads(data)
    return msg
