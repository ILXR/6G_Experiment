import os
import time
from client import Client
from server import SocketServer


def wait_for_exit():
    try:
        while True:
            time.sleep(0.2)
    except KeyboardInterrupt:
        os._exit(0)


def client_main():
    client = Client()
    client.start()


def server_main():
    server = SocketServer()
    server.start()


if __name__ == "__main__":
    server_main()
    time.sleep(1)
    client_main()
    wait_for_exit()
