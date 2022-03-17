import torch.nn as nn
import numpy as np
import torch


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


def get_result(net, input_data):
    res = []
    for i in range(4):
        x = input_data[:, i].reshape(1, 80)
        x = torch.from_numpy(x).float()
        y = net(x)
        tem = [round(item, 3) for item in y[0].detach().numpy().tolist()]
        res.append(tem.index(max(tem)))
    return res
