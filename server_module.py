from tkinter import Y
import torch.nn as nn
import numpy as np
import torch
from log import LOG
import util


class Net(nn.Module):
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(in_dim, n_hidden_1),
            nn.ReLU(True),
            nn.Linear(n_hidden_1, n_hidden_2),
            nn.ReLU(True),
            # 最后一层不需要添加激活函数
            nn.Linear(n_hidden_2, out_dim)
        )

    def forward(self, x):
        x = self.layer(x)
        return x

import numpy
def get_result(net, input_data):
    res = []
    x = torch.from_numpy(input_data).float()
    res = net(x).tolist()
    res = [
        [unit.index(max(unit)) for unit in bat] for bat in res
    ]
    return res
