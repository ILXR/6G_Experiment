import time
import threading
import socketserver
from util import *
from module import *
from threading import Thread

net = Net(80, 256, 128, 8)


class Process_Thread(Thread):
    def __init__(self, socket, raw_data):
        self.socket = socket
        self.raw_data = raw_data
        Thread.__init__(self)

    def run(self):
        global net
        # 整套计算流程
        data = self.raw_data['data']
        to_send = self.raw_data
        to_send.pop('data')
        # 调用模型 ...
        input_data = np.array(data)
        res = get_result(net, input_data)
        to_send['result'] = res
        to_send['recv1_time'] = time.time()
        to_send = json2bytes(to_send)
        size = get_bytes(len(to_send))
        self.socket.send(size)
        self.socket.send(to_send)


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                size = get_int(self.request.recv(2))
                send2_time = time.time()
                if(size == 0):
                    break
                data = b''
                while(len(data) < size):
                    data += self.request.recv(size-len(data))
                data = bytes2json(data)
                data['send2_time'] = send2_time
                data['send3_time'] = time.time()
                processer = Process_Thread(self.request, data)
                processer.start()
                print(data)
        except Exception as e:
            print(e)
        finally:
            print("连接断开：", self.client_address, "\n")
            self.request.close()

    def setup(self):
        print("连接建立：", self.client_address)


class SocketServer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        HOST, PORT = "0.0.0.0", 9999
        self.server = socketserver.ThreadingTCPServer(
            (HOST, PORT), MyHandler)
        print("Start Socket Server...")
        self.server.serve_forever()
