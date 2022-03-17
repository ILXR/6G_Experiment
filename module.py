import util
import torch
import numpy as np
import torch.nn as nn
from util import *


class Net(nn.Module):

    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(in_dim, n_hidden_1),
            nn.ReLU(True),
            nn.Linear(n_hidden_1, n_hidden_2),
            nn.ReLU(True),
            # 最后一层不需要添加激活函数
            nn.Linear(n_hidden_2, out_dim))

    def forward(self, x):
        x = self.layer(x)
        return x


def get_result(net, input_data):
    data = np.array(input_data)
    data = torch.from_numpy(data).float()
    res = net(data).detach().numpy().tolist()
    return res