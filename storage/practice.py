#%%
import torch
import torch.nn as nn
from torch import optim
from torchsummary import summary
from torchviz import make_dot

#%%
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = nn.Linear(1,1)

    def forward(self, x):
        x = self.linear(x)
        return x

class Criterion(nn.Module):
    def __init__(self):
        super(Criterion, self).__init__()
        self.mse = nn.MSELoss()

    def forward(self, hypothesis, target):
        return self.mse(hypothesis, target)

x_train = torch.arange(0,10).type(torch.FloatTensor).unsqueeze(-1)
target = torch.arange(0,10).type(torch.FloatTensor).unsqueeze(-1).mul(5).add(10)

model = Model()
criterion = Criterion()
optimizer = optim.SGD(model.parameters(), lr=0.01)
summary(model, (1,))
make_dot(model(x_train), dict(model.named_parameters()))

#%%
epochs = 1000
for epoch in range(epochs):
    hypothesis = model(x_train)
    cost = criterion(hypothesis, target)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch%100 == 0:
        print(cost)

print(model.linear.weight)
print(model.linear.bias)

