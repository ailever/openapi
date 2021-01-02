import torch
import torch.nn as nn
from torch import optim

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = nn.Linear(3,1)
        self.head_attention = nn.MultiheadAttention(embed_dim=1, num_heads=1)

    def forward(self, x):
        q = x.transpose(0,1)
        Q, w = self.head_attention(q,q,q)
        Q_t = Q.transpose(0,1).squeeze(-1)
        harmonic_x = self.linear(Q_t).squeeze()

        """
        x = (batch, sequence, x_dim)
        q = (sequence, batch, x_dim)
        Q = (sequence, batch, x_dim)
        Q_t = (batch, sequence)

        x = (5,3,1)
        q = (3,5,1)
        Q = (3,5,1)
        Q_t = (5,3)
        """

        return harmonic_x

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
optimizer = optim.SGD(model.parameters(), lr=0.001)
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
