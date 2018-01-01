import argparse
import asyncore
import logging
import pprint
import socket
import sys
import threading
import time

from game.rules import *
from main import DEFAULT_HOST, DEFAULT_PORT
from network.connection import ClientChannel
from network.protocol import *
from network.protocol_tools import *
from utils import set_interval


class TestPlayer(object):
    def __init__(self, client):
        self._logger = logging.getLogger('Player')
        self._client = client  # type: ClientChannel
        self._client.on_message.append(self.on_message)
        self._is_queue = False
        self._is_in_game = False
        self._game_id = None
        self._side = None
        self._last_state = None

    def on_message(self, message):
        if not self._is_in_game:
            if message.domain == Domain.LOBBY:
                self.on_lobby_message(message)
            else:
                self._logger.warning('Received non-lobby message while in lobby: {0}'.format(message))

        if self._is_in_game:
            if message.domain == Domain.GAME:
                game_id = get_message_body(message).game_id
                if game_id != self._game_id:
                    self._logger.warning('Wrong game_id: {0}'.format(message))
                else:
                    self.on_game_message(message)
            else:
                self._logger.warning('Received non-game message while in game: {0}'.format(message))
        print(message.status)

    def on_lobby_message(self, message):
        if message.head == Head.SRV_QUEUE_STARTED:
            self._is_queue = True
            self._logger.info('Queue started')

        if message.head == Head.SRV_QUEUE_STOPPED:
            self._is_queue = False
            self._logger.info('Queue stopped')

        if message.head == Head.SRV_QUEUE_GAME_CREATED:
            self._is_queue = False
            self._is_in_game = True
            self._game_id = get_message_body(message).game_id

    def on_game_message(self, message):
        if message.head == Head.SRV_GAME_STARTED:
            self._side = get_message_body(message).your_side
            self._logger.info('Game started: id={0} side={1}'.format(
                self._game_id, self._side))

        if message.head == Head.SRV_GAME_ENDED:
            self._is_in_game = False
            self._game_id = None
            self._logger.info('Game ended')

        if message.head == Head.SRV_GAME_ACTION:
            self._logger.info('Game action')

        if message.head == Head.SRV_GAME_EFFECT:
            body = get_message_body(message)
            ef_name = body.effect.effect_name
            ef_entity = body.effect.source_entity
            ef_args = body.effect.arguments
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
        if cmd == 'queue' or cmd == 'q':
            if not self._is_queue:
                if len(args) < 2:
                    logging.warning('Specify <SHIP> <WEAPON>')
                    return
                self.start_queue(*args)
            else:
                logging.info('Stopping search')
                self.stop_queue()

        if cmd in ['play', 'card', 'p', 'c']:
            if len(args) < 1:
                logging.warning('Specify <CARD>')
                return
            self.play_card(*args)

        if cmd in ['fire', 'f', 'shoot']:
            self.fire()

        if cmd in ['end', '\r\n', 'turn', 'skip']:
            self.end_turn()

        if cmd in ['state', 's']:
            self.state(print_all=False)

        if cmd in ['all', 'sa', 'a']:
            self.state(print_all=True)

    def play_card(self, card):
        if self._is_in_game:
            self.send(game_message(Head.CLI_GAME_ACTION,
                                  game_id=self._game_id,
                                  status='action',
                                  action={'type': PlayerActionType.PLAY_CARD, 'card': card}))

    def fire(self):
        if self._is_in_game:
            self.send(game_message(Head.CLI_GAME_ACTION,
                                  game_id=self._game_id,
                                  status='action',
                                  action={'type': PlayerActionType.FIRE_WEAPON}))

    def end_turn(self):
        if self._is_in_game:
            self.send(game_message(Head.CLI_GAME_ACTION,
                                   game_id=self._game_id,
                                   status='action',
                                   action={'type': PlayerActionType.END_TURN}))

    def state(self, print_all=False):
        if self._last_state is None:
            self._logger.warning('Last state is None')
            return
        pp = pprint.PrettyPrinter(indent=4)

        if print_all:
            pp.pprint(self._last_state)
        else:
            my_state = self._last_state.get(self._side, None)
            if my_state is not None:
                pp.pprint(my_state)
        print('You play on side: {0}'.format(self._side))

    def start_queue(self, ship, weapon):
        self._is_queue = True
        self.send(lobby_message(Head.CLI_QUEUE_START, status='Start Queue',
                               ship=ship, weapon=weapon))

    def stop_queue(self):
        self.send(lobby_message(Head.CLI_QUEUE_STOP, status='Stop queue'))
        self._is_queue = False


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
