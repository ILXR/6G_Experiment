import time
import random
import socket

from util import *
from client_module import *
from threading import Thread

net = Net(INPUT_SIZE, 256, 128, OUTPUT_SIZE)


def gen_data(size=DATA_SIZE):
    (m, n) = size
    return {
        "data": [[[round(random.random() * 25 + 15, 2) for i in range(m)]
                  for j in range(n)] for k in range(BATCH_SIZE)],
        'send1_time':
        time.time()
    }


class Client_Send(Thread):

    def __init__(self, socket):
        self.socket = socket
        Thread.__init__(self)

    def run(self):
        while (True):
            # 定时发送采集数据
            time.sleep(INTERVAL)
            data = gen_data()
            start = time.time()
            if (INPUT_SIZE != OUTPUT_SIZE):
                data['data'] = get_result(net, data['data'])
            end = time.time()
            data['process_time'] = end - start
            data = json2bytes(data)
            size = get_bytes(len(data))
            self.socket.send(size)
            self.socket.send(data)


class Client_Recv(Thread):

    def __init__(self, socket):
        self.socket = socket
        Thread.__init__(self)

    def run(self):
        LOG("CLIENT_RECV")
        while (True):
            # 解析服务器返回的结果
            byte_data = b''
            while(len(byte_data) < 2):
                byte_data += self.socket.recv(2)
            size = get_int(byte_data)
            recv2_time = time.time()
            data = b''
            while (len(data) < size):
                data += self.socket.recv(size - len(data))
            data = bytes2json(data, "CLIENT_RECV")
            recv3_time = time.time()
            delay = ((recv2_time - data['send1_time']) -
                     (data['recv1_time'] - data['send2_time'])) / 2
            LOG("CLIENT_RECV", "收到识别结果 ：", data['result'])
            print(
                "本地处理时间 ：{:6} ms\n数据发送时延 ：{:6} ms\n计算时延     ：{:6} ms\n结果接收时延 ：{:6} ms\n"
                .format(
                    round(data['process_time'] * 1000, 2),
                    round((delay + data['send3_time'] - data['send2_time']) *
                          1000, 2),
                    round((data['recv1_time'] - data['send3_time']) * 1000, 2),
                    round((delay + recv3_time - recv2_time) * 1000, 2)))


class Client(Thread):

    def __init__(self):
        self.host = HOST_NAME
        self.port = HOST_PORT
        LOG("CLIENT", "host name: {}\nhost port: {}".format(HOST_NAME, HOST_PORT))
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Thread.__init__(self)

    def run(self):
        while (True):
            try:
                self.socket.connect((self.host, self.port))
                self.send_thread = Client_Send(self.socket)
                self.recv_thread = Client_Recv(self.socket)
                self.send_thread.start()
                self.recv_thread.start()
                while (True):
                    time.sleep(1)
            except Exception as e:
                LOG("CLIENT", e)
                self.socket.close()
                time.sleep(1)
