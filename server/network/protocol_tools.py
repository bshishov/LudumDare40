from network.protocol import *
from enum import Enum


class MessageBody(Enum):
    NONE = None
    HELLO = 'hello'
    GAME_CREATED = 'game_created'
    GAME_STARTED = 'game_started'
    GAME_ENDED = 'game_ended'
    GAME = 'game'
    QUEUE_PREFS = 'queue_prefs'
    PLAYER_LEFT = 'player_left'


head_to_body_map = {
    Head.SRV_HELLO: MessageBody.HELLO,
    Head.SRV_ERROR: MessageBody.NONE,
    Head.SRV_QUEUE_GAME_CREATED: MessageBody.GAME_CREATED,
    Head.SRV_QUEUE_STARTED: MessageBody.NONE,
    Head.SRV_QUEUE_STOPPED: MessageBody.NONE,
    Head.SRV_GAME_STARTED: MessageBody.GAME_STARTED,
    Head.SRV_GAME_PLAYER_LEFT: MessageBody.PLAYER_LEFT,
    Head.CLI_QUEUE_START: MessageBody.QUEUE_PREFS,
    Head.CLI_QUEUE_STOP: MessageBody.NONE,
    Head.SRV_GAME_EFFECT: MessageBody.GAME
}


def generic_message(domain: Domain, head: Head, status: str='', **kwargs):
    message = Message()
    message.domain = domain
    message.head = head
    message.status = status
    body = head_to_body_map[head]  # type: MessageBody
    if body == MessageBody.NONE:
        msg_body = message
    else:
        msg_body = getattr(message, body.value)
    for key in kwargs:
        setattr(msg_body, key, kwargs[key])
    return message


def lobby_message(head: Head, status: str='', **kwargs):
    return generic_message(Domain.LOBBY, head, status, **kwargs)


def game_message(head: Head, status: str='', **kwargs):
    return generic_message(Domain.GAME, head, status, **kwargs)


def get_message_body(message: Message, body: MessageBody = MessageBody.NONE):
    if body is MessageBody.NONE:
        body = head_to_body_map[message.head]
    return getattr(message, body.value)


def get_side(player_index: int) -> Side:
    if player_index is 0:
        return Side.A
    if player_index is 1:
        return Side.B
    return Side.NEUTRAL
