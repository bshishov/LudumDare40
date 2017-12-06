import json

VERSION = '0.0.1'

MESSAGE_SEPARATOR = b'\x00\x01\x00\x01\x00\x01'

MSG_DOMAIN_GAME = 'game'
MSG_DOMAIN_LOBBY = 'lobby'

MSG_DEFAULT = ''

# [SERVER] Base server messages
MSG_SRV_ERROR = 's.error'
MSG_SRV_HELLO = 's.hello'

# [SERVER] Queue message
MSG_SRV_QUEUE_STARTED = 's.q.started'
MSG_SRV_QUEUE_STOPPED = 's.q.stopped'
MSG_SRV_QUEUE_GAME_CREATED = 's.g.created'

# [SERVER] Game messages
MSG_SRV_GAME_BEGIN = 's.g.begin'
MSG_SRV_GAME_END = 's.g.end'
MSG_SRV_GAME_PLAYER_LEFT = 's.g.player_left'
MSG_SRV_GAME_TURN = 's.g.turn'
MSG_SRV_GAME_ACTION = 's.g.action'  # redirect player action
MSG_SRV_GAME_EFFECT = 's.g.effect'

# [CLIENT] Messages
MSG_CLI_QUEUE_START = 'c.q.start'
MSG_CLI_QUEUE_STOP = 'c.q.stop'
MSG_CLI_GAME_ACTION = 'c.g.action'

P_MSG_GAME_ID = 'game_id'

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
    def __init__(self, head, game_id, *args, **kwargs):
        super().__init__(domain=MSG_DOMAIN_GAME, head=head, game_id=game_id, *args, **kwargs)


class LobbyMessage(Message):
    def __init__(self, head, *args, **kwargs):
        super().__init__(domain=MSG_DOMAIN_LOBBY, head=head, *args, **kwargs)


def serialize(obj):
    if isinstance(obj, Message):
        data = json.dumps(obj.__dict__)
    else:
        data = json.dumps(obj)
    return bytes(data, ENCODING)


def deserialize(data):
    if isinstance(data, bytes):
        data = data.decode(ENCODING)
    msg = Message(MSG_DOMAIN_GAME, MSG_DEFAULT)
    msg.__dict__ = json.loads(data)
    return msg
