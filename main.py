from server import SocketServer
import time
import os


def wait_for_exit():
    try:
        while True:
            time.sleep(0.2)
    except KeyboardInterrupt:
        os._exit(0)


def main():
    server = SocketServer()
    server.start()
    wait_for_exit()


if __name__ == "__main__":
    main()
