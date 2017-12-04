import asyncore
import socket
import logging

from utils import EventSubscription
from protocol import serialize, deserialize, MESSAGE_SEPARATOR


RECV_BUFFER_SIZE = 8192


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
        self.logger = logging.getLogger('Client_{0}_{1}'.format(*self.socket.getpeername()))
        self.logger.debug('Client handler started')
        self.on_disconnect = EventSubscription()
        self.on_message = EventSubscription()
        self.is_active = True
        self.buffer = b''

    def handle_read(self):
        recv_buffer = self.recv(8192)
        if recv_buffer is None or len(recv_buffer) <= 0:
            return

        self.buffer += recv_buffer
        while len(self.buffer) > 0:
            sep_index = self.buffer.find(MESSAGE_SEPARATOR, 0)
            data = self.buffer[:sep_index]

            # if separator not found
            if sep_index < 0:
                return

            # remove message data from buffer
            self.buffer = self.buffer[sep_index + len(MESSAGE_SEPARATOR):]
            if len(data) > 0:
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

    def handle_close(self):
        self.logger.debug('Closing connection')
        self.close()
        self.on_disconnect(self)
        self.is_active = False

    def __del__(self):
        self.logger.debug('Handler deleted')


def run_loop(*args, **kwargs):
    asyncore.loop(*args, **kwargs)
