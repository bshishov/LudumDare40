from enum import Enum, unique
import json

from utils import unroll_enum_dict

__all__ = ['PROTOCOL_VERSION', 'ENCODING', 'MessageDomain', 'MessageHead', 'Message', 'GameMessage', 'LobbyMessage',
           'serialize', 'deserialize', 'GameMessageProtocol']

PROTOCOL_VERSION = '0.0.1'
ENCODING = 'utf-8'


@unique
class MessageDomain(Enum):
    GAME = 'game'
    LOBBY = 'lobby'


@unique
class MessageHead(Enum):
    # [SERVER] Base server messages
    SRV_ERROR = 's.error'
    SRV_HELLO = 's.hello'

    # [SERVER] Queue message
    SRV_QUEUE_STARTED = 's.q.started'
    SRV_QUEUE_STOPPED = 's.q.stopped'
    SRV_QUEUE_GAME_CREATED = 's.g.created'

    # [SERVER] Game messages
    SRV_GAME_BEGIN = 's.g.begin'
    SRV_GAME_END = 's.g.end'
    SRV_GAME_PLAYER_LEFT = 's.g.player_left'
    SRV_GAME_TURN = 's.g.turn'
    SRV_GAME_ACTION = 's.g.action'  # redirect player action
    SRV_GAME_EFFECT = 's.g.effect'

    # [CLIENT] Messages
    CLI_QUEUE_START = 'c.q.start'
    CLI_QUEUE_STOP = 'c.q.stop'
    CLI_GAME_ACTION = 'c.g.action'


@unique
class GameMessageProtocol(Enum):
    STATE = 'state'
    GAME_ID = 'game_id'
    YOUR_SIDE = 'side'


@unique
class MessageProtocol(Enum):
    DOMAIN = 'domain'
    HEAD = 'head'
    STATUS = 'status'
    BODY = 'body'


class Message(object):
    type = ''
    status = ''
    body = {}

    def __init__(self, domain: MessageDomain, head: MessageHead, status='', **kwargs):
        self.head = head  # type: MessageHead
        self.domain = domain  # type: MessageDomain
        self.status = status
        self.body = kwargs  # type: dict

    def __str__(self):
        return str(self.__dict__)


class GameMessage(Message):
    def __init__(self, head, game_id, *args, **kwargs):
        kwargs.update({GameMessageProtocol.GAME_ID.value: game_id})
        super().__init__(domain=MessageDomain.GAME, head=head, *args, **kwargs)


class LobbyMessage(Message):
    def __init__(self, head, *args, **kwargs):
        super().__init__(domain=MessageDomain.LOBBY, head=head, *args, **kwargs)


def serialize(msg: Message):
    if isinstance(msg, Message):
        d = unroll_enum_dict(msg.__dict__)
        data = json.dumps(d)
    else:
        raise RuntimeError('Expected message, got: {0}'.format(type(msg)))
    return bytes(data, ENCODING)


def deserialize(raw_data):
    if isinstance(raw_data, bytes):
        raw_data = raw_data.decode(ENCODING)
    data = json.loads(raw_data)
    domain = MessageDomain(data.get(MessageProtocol.DOMAIN.value))
    head = MessageHead(data.get(MessageProtocol.HEAD.value))
    status = data.get(MessageProtocol.STATUS.value, '')
    body = data.get(MessageProtocol.BODY.value)

    if domain == MessageDomain.GAME:
        game_id = body.get(GameMessageProtocol.GAME_ID.value)
        return GameMessage(head, game_id, status=status, **body)
    if domain == MessageDomain.LOBBY:
        return LobbyMessage(head, status=status, **body)
    raise RuntimeError('Unknown message domain: {0}'.format(domain))
