from network import protocol_pb2 as proto

VERSION = '0.0.1'


class Side:
    NEUTRAL = proto.Message.NEUTRAL
    A = proto.Message.A
    B = proto.Message.B


class PlayerAction:
    PLAY_CARD = proto.Message.PLAY_CARD
    FIRE_WEAPON = proto.Message.FIRE_WEAPON
    END_TURN = proto.Message.END_TURN


class Domain:
    LOBBY = proto.Message.LOBBY
    GAME = proto.Message.GAME


class Head:
    # [SERVER] Base server messages
    SRV_ERROR = proto.Message.SRV_ERROR
    SRV_HELLO = proto.Message.SRV_HELLO

    # [SERVER] Queue message
    SRV_QUEUE_STARTED = proto.Message.SRV_QUEUE_STARTED
    SRV_QUEUE_STOPPED = proto.Message.SRV_QUEUE_STOPPED
    SRV_QUEUE_GAME_CREATED = proto.Message.SRV_QUEUE_GAME_CREATED

    # [SERVER] Game messages
    SRV_GAME_BEGIN = proto.Message.SRV_GAME_BEGIN
    SRV_GAME_END = proto.Message.SRV_GAME_END
    SRV_GAME_PLAYER_LEFT = proto.Message.SRV_GAME_PLAYER_LEFT
    SRV_GAME_TURN = proto.Message.SRV_GAME_TURN
    SRV_GAME_ACTION = proto.Message.SRV_GAME_ACTION  # redirect player action
    SRV_GAME_EFFECT = proto.Message.SRV_GAME_EFFECT

    # [CLIENT] Messages
    CLI_QUEUE_START = proto.Message.CLI_QUEUE_START
    CLI_QUEUE_STOP = proto.Message.CLI_QUEUE_STOP
    CLI_GAME_ACTION = proto.Message.CLI_GAME_ACTION


def lobby_message_head(head, status=''):
    message = proto.Message()
    message.domain = Domain.LOBBY
    message.head = head
    message.status = status
    return message


def game_message_head(head, game_id, status=''):
    message = proto.Message()
    message.domain = Domain.GAME
    message.head = head
    message.status = status
    message.game.game_id = game_id
    return message


def hello(num_players):
    message = lobby_message_head(Head.SRV_HELLO, status='hello')
    message.hello.version = VERSION
    message.hello.players = num_players


def error(domain, error_message, status='error'):
    message = proto.Message()
    message.domain = domain
    message.status = status
    message.head = Head.SRV_ERROR
    message.error = error_message


def error_lobby(error_message):
    return error(Domain.LOBBY, error_message)


def error_game(error_message):
    return error(Domain.GAME, error_message)


def queue_started():
    return lobby_message_head(Head.SRV_QUEUE_STARTED, status='queue started')


def queue_stopped():
    return lobby_message_head(Head.SRV_QUEUE_STOPPED, status='queue stopped')


def game_created(game_id):
    message = lobby_message_head(Head.SRV_QUEUE_GAME_CREATED, 'game created')
    message.game.game_id = game_id
    return message


def game_begin(game_id, side):
    message = game_message_head(Head.SRV_GAME_BEGIN, game_id, status='begin')
    message.your_side = side
    return message


def serialize(message):
    return message.SerializeToString()


def deserialize(data):
    message = proto.Message()
    message.ParseFromString(data)
    return message
