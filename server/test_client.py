import argparse
import asyncore
import logging
import socket
import threading
import sys
import time

from main import DEFAULT_HOST, DEFAULT_PORT
from utils import EventSubscription
from protocol import *
from rules import *


class TestClient(asyncore.dispatcher):
    def __init__(self, host, port, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)

        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.logger.info('Connected to {0}:{1}'.format(host, port))
        self.on_message = EventSubscription()

    def handle_read(self):
        data = self.recv(8192)
        if data is not None and len(data) > 0:
            try:
                msg = deserialize(data)
                self.logger.debug('Got a message: {0}'.format(msg))
                self.on_message(msg)
            except Exception as err:
                self.logger.error('Could not recognize message: {0}\ndata: {1}'.format(err, data))

    def send_message(self, message):
        try:
            self.send(serialize(message))
        except Exception as err:
            self.logger.error('Could not send message: {0}\nmessage: {1}'.format(err, message))

    def process_cmd(self, cmd):
        self.logger.info('Command: {0}'.format(cmd))
        pass

    def handle_close(self):
        self.logger.info('Disconnected')
        self.close()


class TestPlayer(object):
    def __init__(self, client):
        self._logger = logging.getLogger('Player')
        self._client = client  # type: TestClient
        self._client.on_message.append(self.on_message)
        self._is_queue = False
        self._is_in_game = False
        self._game_id = None
        self._side = None

    def on_message(self, message):
        if message.domain == MESSAGE_DOMAIN_GAME and message.head == MESSAGE_HEAD_HELLO:
            self._is_queue = False
            self._is_in_game = True
            self._game_id = message.body[P_GAME_ID]
            self._side = message.body['side']
            self._logger.info('Game started: id={0} side={1}'.format(self._game_id, self._side))

        if self._is_queue:
            if message.status == 'queue stopped':
                self._is_queue = False
                self._logger.info('Queue stopped')

        if self._is_in_game:
            if message.domain == MESSAGE_DOMAIN_GAME and message.head == MESSAGE_HEAD_ENDED:
                self._is_in_game = False
                self._game_id = None
                self._logger.info('Game finished')

    def send(self, message):
        self._logger.debug('Sending: {0}'.format(message))
        if self._is_in_game:
            message.game_id = self._game_id
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

    def play_card(self, card):
        if self._is_in_game:
            self.send(GameMessage(MESSAGE_HEAD_ACTION, status='action',
                                  action={'type': ACTION_PLAY_CARD, 'card': card}))

    def fire(self):
        if self._is_in_game:
            self.send(GameMessage(MESSAGE_HEAD_ACTION, status='action',
                                  action={'type': ACTION_FIRE_WEAPON}))

    def end_turn(self):
        if self._is_in_game:
            self.send(GameMessage(MESSAGE_HEAD_ACTION, status='action',
                                  action={'type': ACTION_END_TURN}))

    def start_queue(self, ship, weapon):
        self._is_queue = True
        self.send(LobbyMessage(MESSAGE_HEAD_START_QUEUE, status='start', ship=ship, weapon=weapon))

    def stop_queue(self):
        self.send(LobbyMessage(MESSAGE_HEAD_STOP_QUEUE, status='stop'))
        self._is_queue = False


def main(args):
    client = TestClient(args.host, args.port)
    player = TestPlayer(client)

    loop_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop")
    loop_thread.start()

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

    main(parser.parse_args())
