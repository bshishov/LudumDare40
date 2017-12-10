import argparse
import logging

from lobby import Lobby
from game.rules import export_db
import connection

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 8976

DB_EXPORT_PATH = '../client/Assets/Data/db.json'


def main(args):
    logging.info('Exporting game database to: {0}'.format(DB_EXPORT_PATH))
    export_db(DB_EXPORT_PATH)

    lobby = Lobby()
    server = connection.Server(args.host, args.port)
    server.on_client_connect.append(lobby.on_client_connect)
    server.on_client_disconnect.append(lobby.on_client_disconnect)
    connection.run_loop(timeout=0.5)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Started')

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Host to bind the socket to", type=str, default=DEFAULT_HOST)
    parser.add_argument("--port", help="Port to run the server on", type=int, default=DEFAULT_PORT)

    main(parser.parse_args())
