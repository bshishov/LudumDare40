import json

VERSION = '0.0.0.0.0.0.0.0.1'

MESSAGE_DOMAIN_GAME = 'game'
MESSAGE_DOMAIN_LOBBY = 'lobby'

# Base messages
MESSAGE_HEAD_DEFAULT = ''
MESSAGE_HEAD_ERROR = 'error'
MESSAGE_HEAD_ACK = 'ack'
MESSAGE_HEAD_HELLO = 'hello'

# Queue
MESSAGE_HEAD_STATS = 'stats'
MESSAGE_HEAD_START_QUEUE = 'start_queue'
MESSAGE_HEAD_STOP_QUEUE = 'stop_queue'

# GAME
MESSAGE_HEAD_ACTION = 'action'
MESSAGE_HEAD_TURN = 'turn'
MESSAGE_HEAD_PLAYER_LEFT = 'player_left'
MESSAGE_HEAD_ENDED = 'ended'


P_GAME_ID = 'game_id'


ENCODING = 'utf-8'


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
    def __init__(self, head, *args, **kwargs):
        super().__init__(domain=MESSAGE_DOMAIN_GAME, head=head, *args, **kwargs)


class LobbyMessage(Message):
    def __init__(self, head, *args, **kwargs):
        super().__init__(domain=MESSAGE_DOMAIN_LOBBY, head=head, *args, **kwargs)


def serialize(obj):
    if isinstance(obj, Message):
        data = json.dumps(obj.__dict__)
    else:
        data = json.dumps(obj)
    return bytes(data, ENCODING)


def deserialize(data):
    if isinstance(data, bytes):
        data = data.decode(ENCODING)
    msg = Message(MESSAGE_DOMAIN_GAME, MESSAGE_HEAD_DEFAULT)
    msg.__dict__ = json.loads(data)
    return msg
