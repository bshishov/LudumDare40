import network.protocol as proto

m = proto.Message()
m.domain = proto.Domain.LOBBY
m.head = proto.Head.SRV_HELLO
m.status = 'Hello'
print(dir(m))

print(dir(m.game))
m.game.game_id = '123123'
m.hello.version = '0.0.1'  # this discards game

m.game.effect.source_entity = 10
m.game.effect.source_entity = 12
m.game.effect.action.action = proto.PlayerAction.PLAY_CARD
m.game.effect.action.card = 'some card'
m.game.state.id = '123123'
m.game.state.turn = proto.Side.A
for i in range(3):
    e = proto.EntityState()
    e.id = i
    e.name = 'SomeEntity {0}'.format(i)
    e.hp = 10
    e.energy = 5
    e.position = 10
    e.is_player = False
    e.armed = True
    e.muted = False

    for j in range(5):
        c = proto.CardState()
        c.name = 'some card {0}'.format(j)
        c.cost_offense = 2
        c.cost_defense = 2
        e.hand.append(c)

    m.game.state.objects.append(e)

s = m.encode_to_bytes()

print(s)

m2 = proto.Message()
m2.parse_from_bytes(s)

#print(MessageToJson(m2))
print(m2)

