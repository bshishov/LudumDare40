from network import protocol_pb2 as proto


class Domain:
    LOBBY = proto.Message.LOBBY
    GAME = proto.Message.GAME


class HEAD:
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


def serialize(msg):
    return msg.SerializeToString()


def deserialize(raw_data):
    msg = proto.Message()
    msg.ParseFromString(raw_data)
    return msg
