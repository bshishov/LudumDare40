from protobuf3.message import Message
from enum import Enum
from protobuf3.fields import MessageField, Int32Field, EnumField, StringField, BoolField


class BuffState(Message):
    pass


class CardState(Message):
    pass


class EntityState(Message):
    pass


class GameState(Message):
    pass


class GameAction(Message):
    pass


class GameEffectArgument(Message):
    pass


class GameEffect(Message):
    pass


class SrvHello(Message):
    pass


class CliQueuePreferences(Message):
    pass


class SrvQueueGameCreated(Message):
    pass


class SrvGameStarted(Message):
    pass


class SrvGameMessage(Message):
    pass


class SrvGameEnded(Message):
    pass


class SrvPlayerLeft(Message):
    pass


class Message(Message):
    pass


class Domain(Enum):
    LOBBY = 0
    GAME = 1


class Head(Enum):
    SRV_HELLO = 0
    SRV_ERROR = 1
    SRV_QUEUE_STARTED = 2
    SRV_QUEUE_STOPPED = 3
    SRV_QUEUE_GAME_CREATED = 4
    SRV_GAME_STARTED = 5
    SRV_GAME_ENDED = 6
    SRV_GAME_PLAYER_LEFT = 7
    SRV_GAME_TURN = 8
    SRV_GAME_ACTION = 9
    SRV_GAME_EFFECT = 10
    CLI_QUEUE_START = 11
    CLI_QUEUE_STOP = 12
    CLI_GAME_ACTION = 13


class Side(Enum):
    NEUTRAL = 0
    A = 1
    B = 2


class PlayerAction(Enum):
    PLAY_CARD = 0
    FIRE_WEAPON = 1
    END_TURN = 2
    CHEAT_GAIN_CARD = 3

BuffState.add_field('name', StringField(field_number=1, optional=True))
BuffState.add_field('duration', Int32Field(field_number=2, optional=True))
CardState.add_field('name', StringField(field_number=1, optional=True))
CardState.add_field('cost_offense', Int32Field(field_number=2, optional=True))
CardState.add_field('cost_defense', Int32Field(field_number=3, optional=True))
EntityState.add_field('id', Int32Field(field_number=1, optional=True))
EntityState.add_field('name', StringField(field_number=2, optional=True))
EntityState.add_field('side', EnumField(field_number=3, optional=True, enum_cls=Side))
EntityState.add_field('hp', Int32Field(field_number=4, optional=True))
EntityState.add_field('energy', Int32Field(field_number=5, optional=True))
EntityState.add_field('max_energy', Int32Field(field_number=6, optional=True))
EntityState.add_field('energy_gain', Int32Field(field_number=7, optional=True))
EntityState.add_field('muted', BoolField(field_number=8, optional=True))
EntityState.add_field('armed', BoolField(field_number=9, optional=True))
EntityState.add_field('locked', BoolField(field_number=10, optional=True))
EntityState.add_field('damage_mod', Int32Field(field_number=11, optional=True))
EntityState.add_field('buffable', BoolField(field_number=12, optional=True))
EntityState.add_field('is_player', BoolField(field_number=13, optional=True))
EntityState.add_field('position', Int32Field(field_number=14, optional=True))
EntityState.add_field('buffs', MessageField(field_number=15, repeated=True, message_cls=BuffState))
EntityState.add_field('weapon_name', StringField(field_number=16, optional=True))
EntityState.add_field('ship_name', StringField(field_number=17, optional=True))
EntityState.add_field('hand_cards', Int32Field(field_number=18, optional=True))
EntityState.add_field('deck_cards', Int32Field(field_number=19, optional=True))
EntityState.add_field('hand', MessageField(field_number=20, repeated=True, message_cls=CardState))
GameState.add_field('id', StringField(field_number=1, optional=True))
GameState.add_field('turn', EnumField(field_number=2, optional=True, enum_cls=Side))
GameState.add_field('objects', MessageField(field_number=3, repeated=True, message_cls=EntityState))
GameAction.add_field('action', EnumField(field_number=1, optional=True, enum_cls=PlayerAction))
GameAction.add_field('card', StringField(field_number=2, optional=True))
GameEffectArgument.add_field('value', Int32Field(field_number=1, optional=True))
GameEffectArgument.add_field('key', StringField(field_number=2, optional=True))
GameEffect.add_field('source_entity', Int32Field(field_number=1, optional=True))
GameEffect.add_field('target_entity', Int32Field(field_number=2, optional=True))
GameEffect.add_field('action', MessageField(field_number=3, optional=True, message_cls=GameAction))
GameEffect.add_field('effect_name', StringField(field_number=4, optional=True))
GameEffect.add_field('arguments', MessageField(field_number=5, repeated=True, message_cls=GameEffectArgument))
SrvHello.add_field('version', StringField(field_number=1, optional=True))
SrvHello.add_field('players', Int32Field(field_number=2, optional=True))
CliQueuePreferences.add_field('ship', StringField(field_number=1, optional=True))
CliQueuePreferences.add_field('weapon', StringField(field_number=2, optional=True))
SrvQueueGameCreated.add_field('game_id', StringField(field_number=1, optional=True))
SrvQueueGameCreated.add_field('side', EnumField(field_number=2, optional=True, enum_cls=Side))
SrvGameStarted.add_field('game_id', StringField(field_number=1, optional=True))
SrvGameStarted.add_field('your_side', EnumField(field_number=2, optional=True, enum_cls=Side))
SrvGameMessage.add_field('game_id', StringField(field_number=1, optional=True))
SrvGameMessage.add_field('state', MessageField(field_number=2, optional=True, message_cls=GameState))
SrvGameMessage.add_field('action', MessageField(field_number=4, optional=True, message_cls=GameAction))
SrvGameMessage.add_field('effect', MessageField(field_number=5, optional=True, message_cls=GameEffect))
SrvGameMessage.add_field('your_side', EnumField(field_number=6, optional=True, enum_cls=Side))
SrvGameEnded.add_field('game_id', StringField(field_number=1, optional=True))
SrvGameEnded.add_field('interrupted', BoolField(field_number=2, optional=True))
SrvPlayerLeft.add_field('game_id', StringField(field_number=1, optional=True))
SrvPlayerLeft.add_field('player_id', Int32Field(field_number=2, optional=True))
Message.add_field('domain', EnumField(field_number=1, optional=True, enum_cls=Domain))
Message.add_field('head', EnumField(field_number=2, optional=True, enum_cls=Head))
Message.add_field('status', StringField(field_number=3, optional=True))
Message.add_field('error', StringField(field_number=4, optional=True))
Message.add_field('hello', MessageField(field_number=5, optional=True, message_cls=SrvHello))
Message.add_field('game_created', MessageField(field_number=6, optional=True, message_cls=SrvQueueGameCreated))
Message.add_field('game_started', MessageField(field_number=7, optional=True, message_cls=SrvGameStarted))
Message.add_field('game_ended', MessageField(field_number=8, optional=True, message_cls=SrvGameEnded))
Message.add_field('game', MessageField(field_number=9, optional=True, message_cls=SrvGameMessage))
Message.add_field('queue_prefs', MessageField(field_number=10, optional=True, message_cls=CliQueuePreferences))
Message.add_field('player_left', MessageField(field_number=11, optional=True, message_cls=SrvPlayerLeft))
