#%%
import os
import argparse
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch import optim
import pandas_datareader.data as web

Obj = type('Obj', (), {})
def load():
    parser = argparse.ArgumentParser()
    parser.add_argument('--info', type=Obj, default=Obj())
    parser.add_argument('--dataset', type=Obj, default=Obj())
    parser.add_argument('--model', type=Obj, default=Obj())
    parser.add_argument('--training', type=Obj, default=Obj())

    options = parser.parse_args()
    options.info.id = 'ailever'
    options.info.path = '.Log'
    options.training.device = 'cuda' if torch.cuda.is_available() else 'cpu'
    options.training.epochs = 1000
    options.training.saving_period = 1
    options.training.batch = 10
    options.dataset.split_rate = 0.9

    return options

options = load()
print(f"[AILEVER] The device {options.training.device} is selected!")
if not os.path.isdir(options.info.path):
    os.mkdir(options.info.path)
    print(f"[AILEVER] The folder {options.info.path} is created!")

#%%
def scaler(x, confidence_level=1):
    #x = (x-confidence_level*x.mean())/(x.std()/np.sqrt(len(x)))
    x = (x-confidence_level*x.mean())/(x.std())
    return x

class AileverDataset(Dataset):
    def __init__(self, options, split_type):
        self.mode = split_type

        df = web.DataReader('005380', 'naver', start='2018-06-29', end='2020-09-29')
        index = pd.to_numeric(pd.to_datetime(df.index)).values
        series = df['Low'].values
        df = pd.DataFrame({'index':index , 'series':series})
        data = df.values.astype(np.float64)

        # scaling
        data[:,0] = scaler(data[:,0], 2.58)
        data[:,1] = scaler(data[:,1], 2.58)

        spliter = int(options.dataset.split_rate*len(data))

        self.dataset = Obj()
        self.dataset.x = data[:, 0:2]
        self.dataset.y = data[:, 1:2]

        self.train_dataset = Obj()
        self.train_dataset.x = self.dataset.x[0:spliter]
        self.train_dataset.y = self.dataset.y[0:spliter]

        self.validation_dataset = Obj()
        self.validation_dataset.x = self.dataset.x[spliter:]
        self.validation_dataset.y = self.dataset.y[spliter:]

        self.test_dataset = Obj()
        self.test_dataset.x = self.dataset.x
        self.test_dataset.y = self.dataset.y

    def __len__(self):
        if self.mode == 'train':
            return len(self.train_dataset.y)
        elif self.mode == 'validation':
            return len(self.validation_dataset.y)
        elif self.mode == 'test':
            return len(self.test_dataset.y)

    def __getitem__(self, idx):
        if self.mode == 'train':
            x_item = torch.from_numpy(self.train_dataset.x).type(torch.FloatTensor).to(options.training.device)
            y_item = torch.from_numpy(self.train_dataset.y).type(torch.FloatTensor).to(options.training.device)
        elif self.mode == 'validation':
            x_item = torch.from_numpy(self.validation_dataset.x).type(torch.FloatTensor).to(options.training.device)
            y_item = torch.from_numpy(self.validation_dataset.y).type(torch.FloatTensor).to(options.training.device)
        elif self.mode == 'test':
            x_item = torch.from_numpy(self.test_dataset.x).type(torch.FloatTensor).to(options.training.device)
            y_item = torch.from_numpy(self.test_dataset.y).type(torch.FloatTensor).to(options.training.device)
        return x_item, y_item


class AileverModel(nn.Module):
    def __init__(self, options):
        super(AileverModel, self).__init__()
        self.linear = nn.Linear(2, 1)

    def forward(self, x):
        x = F.relu(self.linear(x))
        return x

#%%
dataset = Obj()
dataset.loader = Obj()
dataset.train = AileverDataset(options, split_type='train')
dataset.validation = AileverDataset(options, split_type='validation')
dataset.loader.train = DataLoader(dataset.train, batch_size=options.training.batch, shuffle=False, drop_last=True)
dataset.loader.validation = DataLoader(dataset.validation, batch_size=options.training.batch, shuffle=False, drop_last=True)
print(f"[AILEVER] dataset train x info : {next(iter(dataset.train))[0].size()}")
print(f"[AILEVER] dataset train y info : {next(iter(dataset.train))[1].size()}")
print(f"[AILEVER] dataset validation x info : {next(iter(dataset.validation))[0].size()}")
print(f"[AILEVER] dataset validation y info : {next(iter(dataset.validation))[1].size()}")
print(f"[AILEVER] dataloader train x info : {next(iter(dataset.loader.train))[0].size()}")
print(f"[AILEVER] dataloader train y info : {next(iter(dataset.loader.train))[1].size()}")
print(f"[AILEVER] dataloader validation x info : {next(iter(dataset.loader.validation))[0].size()}")
print(f"[AILEVER] dataloader validation y info : {next(iter(dataset.loader.validation))[1].size()}")

model = AileverModel(options)
if os.path.isfile(options.info.path+'/'+options.info.id+'.pth'):
    model.load_state_dict(torch.load(options.info.path+'/'+options.info.id+'.pth'))
    print(f"[AILEVER] The file {options.info.path+'/'+options.info.id+'.pth'} is successfully loaded!")

model = model.to(options.training.device)
criterion = nn.MSELoss().to(options.training.device)
optimizer = optim.Adam(model.parameters(), lr=1e-1, weight_decay=1e-7)

for epoch in range(options.training.epochs):
    # Training
    losses = []
    model.train()
    for batch_idx, (x_train, y_train) in enumerate(dataset.loader.train):
        x_train = x_train
        y_train = y_train
        if epoch ==0 and batch_idx == 0 :
            print(f"[TRAINING] x_train : {x_train.size()}")
            print(f"[TRAINING] y_train : {y_train.size()}")

        # forward
        hypothesis = model(x_train)
        if epoch == 0 and batch_idx == 0 : print(f"[TRAINING] hypothesis : {hypothesis.size()}")
        cost = criterion(hypothesis, y_train)

        # backward
        optimizer.zero_grad()
        cost.backward()
        optimizer.step()

        if batch_idx % 100 == 0:
            print(f'[TRAINING][Epoch:{epoch + 1}/{options.training.epochs}][Batch Index:{batch_idx + 1}/{len(dataset.loader.train)}] : Loss = {cost}')

        losses.append(cost)

    print(f'[TRAINING][Epoch:{epoch + 1}/{options.training.epochs}] : Loss = {torch.Tensor(losses).mean()}')
    #print(f'- Prediction/True : {hypothesis[0].data}/{y_train[0].data}')

    if epoch % options.training.saving_period == 0:
        torch.save(model.state_dict(), options.info.path+'/'+options.info.id+'.pth')
        print(f"[AILEVER][Epoch:{epoch + 1}/{options.training.epochs}] The file {options.info.path+'/'+options.info.id+'.pth'} is successfully saved!")

    # Validation
    with torch.no_grad():
        model.eval()
        losses = []
        for batch_idx, (x_train, y_train) in enumerate(dataset.loader.validation):
            x_train = x_train
            y_train = y_train

            # forward
            hypothesis = model(x_train)
            cost = criterion(hypothesis, y_train)

            if batch_idx % 100 == 0:
                print(f'[VALIDATION][Epoch:{epoch + 1}/{options.training.epochs}][Batch Index:{batch_idx + 1}/{len(dataset.loader.validation)}] : Loss = {cost}')

            losses.append(cost)

        print(f'[VALIDATION][Epoch:{epoch + 1}/{options.training.epochs}] : Loss = {torch.Tensor(losses).mean()}')
        #print(f'- Prediction/True : {hypothesis[0].data}/{y_train[0].data}')

torch.save(model.state_dict(), options.info.path+'/'+options.info.id+'.pth')
print(f"[AILEVER] The file {options.info.path+'/'+options.info.id+'.pth'} is successfully saved!")

