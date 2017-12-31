import asyncore
import logging
import socket
import struct
import sys
import traceback

from network.protocol import Message
from utils import EventSubscription


__all__ = ['Server', 'ClientChannel', 'run_loop']


RECV_BUFFER_SIZE = 8192
HEADER_FMT = 'h'
HEADER_SIZE = struct.calcsize(HEADER_FMT)


class Server(asyncore.dispatcher):
    def __init__(self, host, port, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)

        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.logger.debug('Listening on {0}:{1}'.format(host, port))
        self.on_client_connect = EventSubscription()
        self.on_client_disconnect = EventSubscription()

    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            return

        sock, (host, port) = pair
        client = ClientChannel(sock=sock)
        client.on_disconnect.append(self.client_disconnected)
        self.logger.debug('Incoming connection from {0}:{1}'.format(host, port))
        self.on_client_connect(client)

    def handle_close(self):
        self.logger.debug('Closing connection')
        self.close()

    def client_disconnected(self, client):
        self.logger.debug('Client disconnected')
        self.on_client_disconnect(client)


class ClientChannel(asyncore.dispatcher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.socket, 'getpeername'):
            self.logger = logging.getLogger('Client_{0}_{1}'.format(*self.socket.getpeername()))
        else:
            self.logger = logging.getLogger('Client')
        self.logger.debug('Client handler started')
        self.on_disconnect = EventSubscription()
        self.on_message = EventSubscription()
        self.is_active = True
        self.read_buffer = b''
        self.write_buffer = b''

    def handle_read(self):
        recv_buffer = self.recv(8192)
        if recv_buffer is None or len(recv_buffer) == 0:
            return

        self.read_buffer += recv_buffer
        while len(self.read_buffer) > 0:
            msg_len = struct.unpack(HEADER_FMT, self.read_buffer[:HEADER_SIZE])[0]
            if len(self.read_buffer) < HEADER_SIZE + msg_len:
                # more data required
                return

            data = self.read_buffer[HEADER_SIZE:HEADER_SIZE + msg_len]

            # remove message data from buffer
            self.read_buffer = self.read_buffer[HEADER_SIZE + msg_len:]
            if len(data) > 0:
                try:
                    msg = Message()
                    msg.parse_from_bytes(data)
                    self.logger.debug('Got a message: {0}'.format(msg))
                    self.on_message(msg)
                except Exception as err:
                    self.logger.error('Could not recognize message: {0}\ndata: {1}'.format(err, data))
                    traceback.print_exc(file=sys.stderr)

    def send_message(self, message: Message):
        try:
            data = message.encode_to_bytes()
            self.write_buffer += struct.pack(HEADER_FMT, len(data)) + data
        except Exception as err:
            self.logger.error('Could not send message: {0}\nmessage: {1}'.format(err, message))

    def handle_close(self):
        self.logger.debug('Closing connection')
        self.close()
        self.on_disconnect(self)
        self.is_active = False

    def writable(self):
        return len(self.write_buffer) > 0

    def handle_write(self):
        sent = self.send(self.write_buffer)
        self.write_buffer = self.write_buffer[sent:]

    def __del__(self):
        self.logger.debug('Handler deleted')


def run_loop(*args, **kwargs):
    asyncore.loop(*args, **kwargs)
