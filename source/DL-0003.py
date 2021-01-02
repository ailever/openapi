import torch
import torch.nn as nn
from torch import optim

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.lstm = nn.LSTM(1,16,1, batch_first=True)
        self.linear = nn.Linear(16,1)

    def forward(self, x):
        o, (h, c) = self.lstm(x)
        x = self.linear(h[-1]).squeeze()

        """
        x = (batch, sequence, x_dim)
        o = (batch, sequence, h_dim)
        h = (layer, batch, h_dim)

        x = torch.Size([5, 3, 1])
        o = torch.Size([5, 3, 16])
        h = torch.Size([1, 5, 16])
        """

        return x

class Criterion(nn.Module):
    def __init__(self):
        super(Criterion, self).__init__()
        self.mse = nn.MSELoss()

    def forward(self, hypothesis, target):
        return self.mse(hypothesis, target)

x_train = torch.arange(5*3).type(torch.FloatTensor).view(5,3,1)
target = x_train.mean(dim=1).squeeze()
print(x_train)
print(target, '\n')

model = Model()
optimizer = optim.SGD(model.parameters(), lr=0.1)
criterion = Criterion()

epochs = 3000
for epoch in range(epochs):
    hypothesis = model(x_train)
    cost = criterion(hypothesis, target)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch%100 == 0:
        print(cost)
