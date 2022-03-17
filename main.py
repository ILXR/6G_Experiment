import os
import time
from util import *
from client import *


def wait_for_exit():
    try:
        while True:
            time.sleep(0.2)
    except KeyboardInterrupt:
        os._exit(0)


def main():
    client = Client()
    client.start()
    wait_for_exit()


if __name__ == "__main__":
    main()
