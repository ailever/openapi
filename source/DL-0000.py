import torch
import torch.nn as nn
from torchviz import make_dot

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = nn.Linear(2,2)

    def forward(self, x):
        return self.linear(x)

model = Model()
x = torch.Tensor(100,2).uniform_(0,1)
y = model(x)

make_dot(y, params=dict(model.named_parameters()))
