import argparse
import asyncore
import logging
import socket
import sys
import threading
import time
import enum

from game.rules import *
from main import DEFAULT_HOST, DEFAULT_PORT
from network.connection import ClientChannel
from network.protocol import *
from network.protocol_tools import *
from utils import set_interval


class TestPlayer(object):
    class Status(enum.Enum):
        IDLE_IN_LOBBY = 0,
        IN_QUEUE = 1,
        IN_GAME = 2

    def __init__(self, client):
        self._logger = logging.getLogger('Player')
        self._client = client  # type: ClientChannel
        self._client.on_message.append(self.on_message)
        self._status = TestPlayer.Status.IDLE_IN_LOBBY
        self._game_id = None
        self._side = None
        self._last_state = None  # type: GameState

    def on_message(self, message):
        if self._status == TestPlayer.Status.IN_GAME:
            if message.domain == Domain.GAME:
                game_id = get_message_body(message).game_id
                if game_id != self._game_id:
                    self._logger.warning('Wrong game_id: {0}'.format(message))
                else:
                    self.on_game_message(message)
            else:
                self._logger.warning('Received non-game message while in game: {0}'.format(message))
        else:
            if message.domain == Domain.LOBBY:
                self.on_lobby_message(message)
            else:
                self._logger.warning('Received non-lobby message while in lobby: {0}'.format(message))

        print('Message: {0}'.format(message.status))

    def on_lobby_message(self, message):
        if message.head == Head.SRV_QUEUE_STARTED:
            self._status = TestPlayer.Status.IN_QUEUE
            self._logger.info('Queue started')

        if message.head == Head.SRV_QUEUE_STOPPED:
            self._status = TestPlayer.Status.IDLE_IN_LOBBY
            self._logger.info('Queue stopped')

        if message.head == Head.SRV_QUEUE_GAME_CREATED:
            self._status = TestPlayer.Status.IN_GAME
            self._game_id = get_message_body(message).game_id
            self._logger.info('Game created: id={0}'.format(self._game_id))

    def on_game_message(self, message):
        if message.head == Head.SRV_GAME_STARTED:
            self._side = get_message_body(message).your_side
            self._logger.info('Game started: id={0} side={1}'.format(
                self._game_id, self._side))

        if message.head == Head.SRV_GAME_ENDED:
            self._status = TestPlayer.Status.IDLE_IN_LOBBY
            self._logger.info('Game ended')

        if message.head == Head.SRV_GAME_ACTION:
            self._logger.info('Game action')

        if message.head == Head.SRV_GAME_EFFECT:
            body = get_message_body(message)
            ef_name = body.effect.effect_name
            ef_entity = body.effect.source_entity
            ef_args = ' '.join(['{0}:{1}'.format(a.key, a.value) for a in body.effect.arguments])

            if ef_name is not None:
                self._logger.info('Applied [{0}] {2} to entity {1}'.format(
                    ef_name, ef_entity, ef_args))

        if message.head == Head.SRV_GAME_TURN:
            self._logger.info('Game turn')

        if message.head == Head.SRV_GAME_PLAYER_LEFT:
            self._logger.info('Player left')

        msg_body = get_message_body(message)
        if hasattr(msg_body, 'state'):
            self._last_state = msg_body.state

    def send(self, message):
        self._logger.debug('Sending: {0}'.format(message))
        self._client.send_message(message)

    def do(self, cmd, *args):
        if self._status == TestPlayer.Status.IDLE_IN_LOBBY:
            if cmd == 'queue' or cmd == 'q':
                if len(args) < 2:
                    logging.warning('Specify <SHIP> <WEAPON>')
                    return
                self.start_queue(*args)

        if self._status == TestPlayer.Status.IN_QUEUE:
            if cmd == 'queue' or cmd == 'q':
                logging.info('Stopping search')
                self.stop_queue()

        if self._status == TestPlayer.Status.IN_GAME:
            if cmd in ['play', 'card', 'p', 'c']:
                if len(args) < 1:
                    logging.warning('Specify <CARD>')
                    return
                self.do_action(PlayerAction.PLAY_CARD, args[0])

            if cmd in ['gain', 'cheat', 'g']:
                if len(args) < 1:
                    logging.warning('Specify <CARD>')
                    return
                self.do_action(PlayerAction.CHEAT_GAIN_CARD, args[0])

            if cmd in ['fire', 'f', 'shoot']:
                self.do_action(PlayerAction.FIRE_WEAPON)

            if cmd in ['end', '\r\n', 'turn', 'skip']:
                self.do_action(PlayerAction.END_TURN)

            if cmd in ['state', 's']:
                self.state(print_all=False)

            if cmd in ['all', 'sa', 'a']:
                self.state(print_all=True)

    def do_action(self, action_type: PlayerAction, card=None):
        msg = game_message(Head.CLI_GAME_ACTION, game_id=self._game_id, status='action')
        msg.game.action.action = action_type
        if card is not None:
            msg.game.action.card = card
        self.send(msg)

    def state(self, print_all=False):
        if self._last_state is None:
            self._logger.warning('Last state is None')
            return

        if print_all:
            print(self._last_state)
        else:
            my_state = self._last_state
            for o in self._last_state.objects:
                if o.is_player and o.side == self._side:
                    my_state = o
                    break
            if my_state is not None:
                print(my_state)
        print('You play on side: {0}'.format(self._side))

    def start_queue(self, ship, weapon):
        self.send(lobby_message(Head.CLI_QUEUE_START, status='Start Queue', ship=ship, weapon=weapon))

    def stop_queue(self):
        self.send(lobby_message(Head.CLI_QUEUE_STOP, status='Stop queue'))


def main(args):
    client = ClientChannel()
    client.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((args.host, args.port))
    player = TestPlayer(client)

    loop_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop", kwargs={'timeout': 0.5})
    loop_thread.start()

    # TODO: move to args
    if args.auto:
        set_interval(1, player.do('q', args.ship, args.weapon))

    stop_requested = False

    while not stop_requested:
        time.sleep(1)
        cmd = input()
        if cmd == 'exit':
            sys.exit(1)

        if cmd is not None and len(cmd) > 0:
            cmd = cmd.split(' ')
            player.do(*cmd)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Started')

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Host to bind the socket to", type=str, default=DEFAULT_HOST)
    parser.add_argument("--port", help="Port to run the server on", type=int, default=DEFAULT_PORT)
    parser.add_argument("--auto", help="Use auto queue", action='store_true')
    parser.add_argument("--ship", help="Default ship", type=str, default='scout')
    parser.add_argument("--weapon", help="Default weapon", type=str, default='harpoon')

    main(parser.parse_args())
