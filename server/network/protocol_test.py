from network.protocol_pb2 import Message
from google.protobuf.json_format import MessageToJson

m = Message()
m.domain = Message.GAME
m.head = Message.SRV_HELLO
m.status = 'Hello'
print(dir(m))

print(dir(m.game))
m.game.game_id = '123123'
#m.hello.version = '0.0.1'  # this discards game
m.game.effect.source_entity = 10
m.game.effect.source_entity = 12
m.game.effect.action.action = Message.PLAY_CARD
m.game.effect.action.card = 'some card'
m.game.state.id = '123123'
m.game.state.turn = Message.A
for i in range(3):
    e = m.game.state.objects.add()
    e.id = i
    e.name = 'SomeEntity {0}'.format(i)
    e.hp = 10
    e.energy = 5
    e.position = 10
    e.is_player = False
    e.armed = True
    e.muted = False
    for j in range(5):
        c = e.hand.add()
        c.name = 'some card {0}'.format(j)
        c.cost_offense = 2
        c.cost_defense = 2



s = m.SerializeToString()

print(s)

m2 = Message()
m2.ParseFromString(s)

#print(MessageToJson(m2))
print(m2)

