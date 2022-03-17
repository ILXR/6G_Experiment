import json

# data format
to_send = {
    "data": [
        [21.02, 19.28, 20.81, 20.15],
        [21.02, 19.24, 20.88, 20.17],
        # .....  80 x 4
    ],
    'send1_time': 1641987209.497838,  # 客户端开始发送数据 - 客户端时间
    'send2_time': 1641987219.497838,  # 服务器开始接收数据 - 服务器时间
    "send3_time": 1641987229.497838,  # 服务器收到全部数据 - 服务器时间

    "recv1_time": 1641987239.497838,  # 服务器开始发送数据 - 服务器时间
    "recv2_time": 1641987249.497838,  # 客户端开始接收数据 - 客户端时间
    "recv3_time": 1641987259.497838,  # 客户端收到全部数据 - 客户端时间
}


def get_bytes(number):
    return number.to_bytes(length=2, byteorder='big', signed=False)


def get_int(bytes_data):
    return int.from_bytes(bytes_data, byteorder='big', signed=False)


def json2bytes(obj):
    res = None
    try:
        res = str.encode(
            json.dumps(obj), encoding='GBK')
    except Exception as e:
        print(e, "\njson to bytes failed:", obj)
    finally:
        return res


def bytes2json(obj):
    res = None
    try:
        res = json.loads(bytes.decode(
            obj, encoding='GBK'))
    except Exception as e:
        print(e, "\nbytes to json failed:", obj)
    finally:
        return res
