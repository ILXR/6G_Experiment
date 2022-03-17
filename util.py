import json

HOST_NAME = "192.168.137.1"
HOST_PORT = 9999

INTERVAL = 3                    # 发送间隔
INPUT_SIZE = 80                 # 边缘处理网络输入维度
OUTPUT_SIZE = 20                # 边缘处理网络输出维度
DATA_SIZE = (INPUT_SIZE, 4)
BATCH_SIZE = 8

# data format
to_send = {
    "data": [
        # .....  batch x 4(通道) x 80(序列长度)
    ],
    'process_time': 1000,             # 客户端模型处理时间
    'send1_time': 1641987209.497838,  # 客户端开始发送数据 - 客户端时间
    'send2_time': 1641987209.497838,  # 服务器开始接收数据 - 服务器时间
    "send3_time": 1641987209.497838,  # 服务器收到全部数据 - 服务器时间
    "recv1_time": 1641987209.497838,  # 服务器开始发送数据 - 服务器时间
    "recv2_time": 1641987209.497838,  # 客户端开始接收数据 - 客户端时间
    "recv3_time": 1641987209.497838,  # 客户端收到全部数据 - 客户端时间
}


def get_bytes(number):
    return number.to_bytes(length=2, byteorder='big', signed=False)


def get_int(bytes_data):
    return int.from_bytes(bytes_data, byteorder='big', signed=False)


def json2bytes(obj):
    res = None
    try:
        res = str.encode(json.dumps(obj), encoding='GBK')
    except Exception as e:
        print(e, "\njson to bytes failed:", obj)
    finally:
        return res


def bytes2json(obj):
    res = None
    try:
        res = json.loads(bytes.decode(obj, encoding='GBK'))
    except Exception as e:
        print(e, "\nbytes to json failed:", obj)
    finally:
        return res
