#%%
import os
import argparse
import time
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch import optim
from torchsummary import summary
import pandas_datareader.data as web
import FinanceDataReader as fdr

Obj = type('Obj', (), {})
def load():
    parser = argparse.ArgumentParser()
    parser.add_argument('--info', type=Obj, default=Obj())
    parser.add_argument('--dataset', type=Obj, default=Obj())
    parser.add_argument('--model', type=Obj, default=Obj())
    parser.add_argument('--training', type=Obj, default=Obj())
    parser.add_argument('--validation', type=Obj, default=Obj())
    parser.add_argument('--evaluation', type=Obj, default=Obj())
    parser.add_argument('--alert', type=Obj, default=Obj())

    options = parser.parse_args()
    options.info.id = 'ailever'
    options.info.path = '.Log'
    options.info.output = 'prediction.csv'
    options.training.device = 'cuda' if torch.cuda.is_available() else 'cpu'
    options.training.saving_period = 50
    options.training.batch = 100
    options.training.epochs = 1
    options.training.on = True
    options.validation.on = True
    options.evaluation.on = False
    options.alert.options_info = True
    options.alert.dataset_info = True
    options.alert.model_info = True
    options.alert.training_batch = False
    options.alert.training_epoch = True
    options.alert.validation_batch = True
    options.alert.validation_epoch = True
    options.alert.batch_period = 20
    options.alert.epoch_period = 5
    options.dataset.split_rate = 0.9
    options.dataset.sequence = 100       # length
    options.dataset.prediction = 5       # rate

    return options

options = load()
if options.alert.options_info:
    print(f'\n{"TRAINING ENVIRONMENT INFORMATION":-^100}')
    print(f"[ID] ID : {options.info.id}")
    print(f"[TRAINING] Device : {options.training.device}")
    print(f"[TRAINING] Saving Period : {options.training.saving_period}")
    print(f"[TRAINING] Saving Path : {options.info.path}")
    print(f"[TRAINING] Batch : {options.training.batch}")
    print(f"[TRAINING] Epochs : {options.training.epochs}")
    print(f"[ALERT] options_info : {options.alert.options_info}")
    print(f"[ALERT] dataset_info : {options.alert.dataset_info}")
    print(f"[ALERT] training_batch : {options.alert.training_batch}")
    print(f"[ALERT] training_epoch : {options.alert.training_epoch}")
    print(f"[ALERT] validation_batch : {options.alert.validation_batch}")
    print(f"[ALERT] validation_epoch : {options.alert.validation_epoch}")
    print(f"[ALERT] epoch_period : {options.alert.epoch_period}")
    print(f"[ALERT] batch_period : {options.alert.batch_period}")

if not os.path.isdir(options.info.path):
    os.mkdir(options.info.path)
    print(f"\n[AILEVER] The folder {options.info.path} is created!")

#%%
def scaler(x, confidence_level=1):
    #x = (x-confidence_level*x.mean())/(x.std()/np.sqrt(len(x)))
    x = (x-confidence_level*x.mean())/(x.std())
    return x

class AileverDataset(Dataset):
    def __init__(self, options, split_type=None):
        self.mode = split_type
        self.sequence = options.dataset.sequence
        self.prediction = options.dataset.prediction

        #df = web.DataReader('005380', 'naver', start='2018-06-29', end='2020-09-29')
        df = fdr.DataReader('005380', 2020)
        index = pd.to_numeric(pd.to_datetime(df.index)).values
        series = df['Low'].values
        df = pd.DataFrame({'index':index , 'series':series})
        data = df.values.astype(np.float64)

        # scaling
        data[:,0] = scaler(data[:,0], 2.58)
        data[:,1] = scaler(data[:,1], 2.58)

        spliter = int(options.dataset.split_rate*len(data))

        self.dataset = Obj()
        self.dataset.index = data[:, 0:1]
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
        if self.mode == None:
            return len(self.dataset.y)
        elif self.mode == 'train':
            return len(self.train_dataset.y) - self.sequence
        elif self.mode == 'validation':
            return len(self.validation_dataset.y) - self.sequence
        elif self.mode == 'test':
            return len(self.test_dataset.y) - self.sequence

    def __getitem__(self, idx):
        if self.mode == None:
            x_item = torch.from_numpy(self.dataset.x[idx]).type(torch.FloatTensor).to(options.training.device)
            y_item = torch.from_numpy(self.dataset.y[idx]).type(torch.FloatTensor).to(options.training.device)
        elif self.mode == 'train':
            x_item = torch.from_numpy(self.train_dataset.x[idx : idx+self.sequence-self.prediction]).type(torch.FloatTensor).to(options.training.device)
            y_item = torch.from_numpy(self.train_dataset.y[idx+self.sequence-self.prediction : idx+self.sequence]).type(torch.FloatTensor).to(options.training.device)
        elif self.mode == 'validation':
            x_item = torch.from_numpy(self.validation_dataset.x[idx : idx+self.sequence-self.prediction]).type(torch.FloatTensor).to(options.training.device)
            y_item = torch.from_numpy(self.validation_dataset.y[idx+self.sequence-self.prediction : idx+self.sequence]).type(torch.FloatTensor).to(options.training.device)
        elif self.mode == 'test':
            x_item = torch.from_numpy(self.test_dataset.x[idx : idx+self.sequence-self.prediction]).type(torch.FloatTensor).to(options.training.device)
            y_item = torch.from_numpy(self.test_dataset.y[idx+self.sequence-self.prediction : idx+self.sequence]).type(torch.FloatTensor).to(options.training.device)
        return x_item, y_item
 

class AileverModel(nn.Module):
    def __init__(self, options):
        super(AileverModel, self).__init__()
        self.lstm = nn.LSTM(2, options.dataset.sequence, 3, batch_first=True)
        self.linear = nn.Linear(options.dataset.sequence, options.dataset.prediction)

    def forward(self, x):
        x, (h, c) = self.lstm(x)
        p = self.linear(h[-1])
        return p


class AileverCriterion(nn.Module):
    def __init__(self, options):
        super(AileverCriterion, self).__init__()
        self.mse = nn.MSELoss()

    def forward(self, hypothesis, target):
        cost = self.mse(hypothesis, target)
        return cost

#%%
dataset = Obj()
dataset.train = AileverDataset(options, split_type='train')
dataset.validation = AileverDataset(options, split_type='validation')
dataset.test = AileverDataset(options, split_type='test')
dataset.loader = Obj()
dataset.loader.train = DataLoader(dataset.train, batch_size=options.training.batch, shuffle=False, drop_last=True)
dataset.loader.validation = DataLoader(dataset.validation, batch_size=options.training.batch, shuffle=False, drop_last=True)
dataset.loader.test = DataLoader(dataset.test, batch_size=options.training.batch, shuffle=False, drop_last=True)
if options.alert.dataset_info:
    print(f'\n*{"DATASET INFORMATION":-^100}*')
    print(f"[DATASET][ALL] Dataset all x : {dataset.train.dataset.x.shape}")
    print(f"[DATASET][ALL] Dataset all y : {dataset.train.dataset.y.shape}")
    print(f"[DATASET][ALL] Dataset split rate : {options.dataset.split_rate}")
    print(f"[DATASET][LEARNING] Dataset train x info : {next(iter(dataset.train))[0].size()}")
    print(f"[DATASET][LEARNING] Dataset train y info : {next(iter(dataset.train))[1].size()}")
    print(f"[DATASET][LEARNING] Dataset validation x info : {next(iter(dataset.validation))[0].size()}")
    print(f"[DATASET][LEARNING] Dataset validation y info : {next(iter(dataset.validation))[1].size()}")
    print(f"[DATASET][LEARNING] Dataset-loader train x info : {next(iter(dataset.loader.train))[0].size()}")
    print(f"[DATASET][LEARNING] Dataset-loader train y info : {next(iter(dataset.loader.train))[1].size()}")
    print(f"[DATASET][LEARNING] Dataset-loader validation x info : {next(iter(dataset.loader.validation))[0].size()}")
    print(f"[DATASET][LEARNING] Dataset-loader validation y info : {next(iter(dataset.loader.validation))[1].size()}")
    print(f'* Example, X[:10]')
    print(dataset.train.dataset.x[:10])
    print(f'* Example, Y[:10]')
    print(dataset.train.dataset.y[:10])

model = AileverModel(options).to(options.training.device)
criterion = AileverCriterion(options).to(options.training.device)
optimizer = optim.Adam(model.parameters(), lr=1e-1, weight_decay=1e-7)
if options.alert.model_info:
    print(f'\n*{"MODEL INFORMATION":-^100}*')
    summary(model, next(iter(dataset.train))[0].size())

    delay = 5
    if options.training.on:
        print(f"\n[AILEVER] Artificial neural network will start to learn about your dataset after {delay} sec.")
    else:
        print(f"\n[AILEVER] Training is not progressed. If you want to train, set options.training.on to True in load().")
    print(f"[AILEVER] Check your dataset and model information.\n")
    time.sleep(delay)

if os.path.isfile(options.info.path+'/'+options.info.id+'.pth'):
    try:
        checkpoint = torch.load(options.info.path+'/'+options.info.id+'.pth')
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        print(f"\n[AILEVER] The file {options.info.path+'/'+options.info.id+'.pth'} is successfully loaded!")
    except RuntimeError:
        os.remove(options.info.path+'/'+options.info.id+'.pth')
        print(f"\n[AILEVER] The previous file {options.info.path+'/'+options.info.id+'.pth'} is successfully removed!")
        

if options.training.on:
    print(f'\n*{"TRAINING ARTIFICIAL NUERAL NETWORK":-^100}*')
    for epoch in range(options.training.epochs):
        # Training
        model.train()
        losses = []
        for batch_idx, (x_train, y_train) in enumerate(dataset.loader.train):
            x_train = x_train
            y_train = y_train.squeeze()

            # forward
            hypothesis = model(x_train)
            if epoch == 0 and batch_idx == 0 :
                print(f"[TRAINING] [1] x_train : {x_train.size()}")
                print(f"[TRAINING] [2] hypothesis : {hypothesis.size()}")
                print(f"[TRAINING] [3] y_train : {y_train.size()}")
            cost = criterion(hypothesis, y_train)

            # backward
            optimizer.zero_grad()
            cost.backward()
            optimizer.step()
            losses.append(cost)

            if options.alert.training_batch and (batch_idx+1) % options.alert.batch_period == 0:
                print(f'[TRAINING][Epoch:{epoch + 1}/{options.training.epochs}][Batch Index:{batch_idx + 1}/{len(dataset.loader.train)}] : Loss = {cost}')


        if options.alert.training_epoch and (epoch+1) % options.alert.epoch_period == 0:
            print(f'[TRAINING][Epoch:{epoch + 1}/{options.training.epochs}] : Loss = {torch.Tensor(losses).mean()}')
            print(f'  - Prediction/True : {hypothesis[0].data}/{y_train[0].data}')

        if epoch % options.training.saving_period == 0:
            torch.save({'model_state_dict': model.state_dict(),
                        'optimizer_state_dict': optimizer.state_dict()}, options.info.path+'/'+options.info.id+'.pth')
            print(f"[AILEVER][Epoch:{epoch + 1}/{options.training.epochs}] The file {options.info.path+'/'+options.info.id+'.pth'} is successfully saved!")

        # Validation
        if options.training.on:
            with torch.no_grad():
                model.eval()
                losses = []
                for batch_idx, (x_train, y_train) in enumerate(dataset.loader.validation):
                    x_train = x_train
                    y_train = y_train.squeeze()

                    # forward
                    hypothesis = model(x_train)
                    cost = criterion(hypothesis, y_train)
                    losses.append(cost)

                    if options.alert.validation_batch and (batch_idx+1) % options.alert.batch_period == 0:
                        print(f'[VALIDATION][Epoch:{epoch + 1}/{options.training.epochs}][Batch Index:{batch_idx + 1}/{len(dataset.loader.validation)}] : Loss = {cost}')

                if options.alert.validation_epoch and (epoch+1) % options.alert.epoch_period == 0:
                    print(f'[VALIDATION][Epoch:{epoch + 1}/{options.training.epochs}] : Loss = {torch.Tensor(losses).mean()}')
                    print(f'  - Prediction/True : {hypothesis[0].data}/{y_train[0].data}')

torch.save({'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict()}, options.info.path+'/'+options.info.id+'.pth')

print(f"[AILEVER] The file {options.info.path+'/'+options.info.id+'.pth'} is successfully saved!")

if options.evaluation.on:
    print(f'\n*{"EVALUATION":-^100}*')
    with torch.no_grad():
        model.eval()
        period = []
        predictions = []
        ground_truths = []
        for idx, (x_train, y_train) in enumerate(dataset.test):
            x_train = x_train
            y_train = y_train.squeeze()

            # forward
            hypothesis = model(x_train)
            predictions.append(hypothesis.data.cpu())
            ground_truths.append(y_train.cpu())
        
        index = dataset.test.dataset.index.squeeze()
        predictions = torch.stack(predictions).numpy().squeeze()
        ground_truths = torch.stack(ground_truths).numpy().squeeze()
        predictions = pd.DataFrame({'index':index, 'prediction':predictions, 'ground_truth':ground_truths})
        predictions = predictions.set_index('index')
        predictions.to_csv(options.info.output)
        
        print(predictions.describe())
        print(f"[AILEVER] The file {options.info.output} is successfully saved!")
        
