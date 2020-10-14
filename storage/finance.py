#%%
from pprint import pprint
from ailever.forecast import TSA
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

plt.rcParams["font.family"] = 'NanumBarunGothic'
#%%
markets = ['NASDAQ', 'NYSE', 'AMEX', 'SSE', 'SZSE', 'HKEX', 'TSE', 'HOSE',
           'KRX', 'KOSPI', 'KOSDAQ', 'KONEX',
           'KRX-DELISTING',
           'KRX-ADMINISTRATIVE',
           'S&P500', 'SP500']

stock = fdr.StockListing('KRX').set_index('Name')

stock_items = ''
for item in stock.index:
    stock_items += str(item) + '\n'
with open('stock-items.txt', 'w') as f:
    f.write(stock_items)

#%%
def datareader(name, period=0, verbose=True):
    if verbose:
        pprint(stock[stock.index == name].to_dict())
    code = str(stock[stock.index == name].Symbol.values.squeeze())
    stock_price = fdr.DataReader(code)['Close'][-period:]
    x = stock_price.index.values
    y = stock_price.values
    return x, y

def visualization(names, period=0, verbose=True):
    for name in names:
        x, y = datareader(name=name, period=period, verbose=verbose)
        plt.scatter(x, y, marker='*')
        plt.plot(x, y, label=f'{name}')
    plt.grid(True)
    plt.legend()
    plt.show()

stock_names = ['SK하이닉스', '삼성전자', 'NH투자증권', 'CJ', 'GV']
visualization(names=stock_names, period=100, verbose=None)

#%%
x, y = datareader(name='삼성전자')
price = pd.Series(data=y, index=x)
price.describe()

#%%
tsa = TSA()
Trend, Seasonal, Resid = tsa.analyze(TS=price, freq=10, lags=10)

trend = Trend.dropna()
seasonal = Seasonal.dropna()
resid = Resid.dropna()

tsa.stationary(TS=price, title='Time Series')
tsa.stationary(TS=trend, title='Trend')
tsa.stationary(TS=seasonal, title='Seasonality')
tsa.stationary(TS=resid, title='Residual')

#%%
# [Prediction] : non-interpolation
# [0] : visualization & options
fig = plt.figure(figsize=(20, 18))
layout = (4,2)
axes_00 = plt.subplot2grid(layout, (0,0), colspan=2)
axes_10 = plt.subplot2grid(layout, (1,0), colspan=1)
axes_11 = plt.subplot2grid(layout, (1,1), colspan=1)
axes_20 = plt.subplot2grid(layout, (2,0), colspan=2)
axes_30 = plt.subplot2grid(layout, (3,0), colspan=2)
conf = .05
split_rate = .7

# [1] : split dataset
y = pd.Series(y)
set_size = len(y)
train_size = int(len(y)*split_rate)
train_y = y.iloc[:train_size]
test_y = y.iloc[train_size:]
axes_00.plot(y)
axes_00.axvline(x=train_size-1, ls='--', c='skyblue')
axes_00.axvline(x=set_size-1, ls='-', c='black')
axes_00.set_title(f'[{stock_name} : Train + Test]')
axes_00.grid(True)

# [2] : training arima model
model = smt.arima.ARIMA(train_y, order=(2, 0, 2), trend='n').fit()
print(f'* ARIMA params : \n', model.params)


# [3] : prediction for train dataset
sm.graphics.tsa.plot_predict(model, start=0, end=train_size-1, alpha=conf, ax=axes_10)
axes_10.plot(train_y)
axes_10.axvline(x=train_size-1, ls='-', c='black')
axes_10.set_title('[Predict Train_Dataset]')
axes_10.grid(True)
train_prediction = model.predict(start=0, end=train_size)
mse = ((train_y - train_prediction)**2).mean()
print(f'\n* MSE : {mse}')


# [4] : prediction for test dataset
sm.graphics.tsa.plot_predict(model, start=train_size, end=(set_size-1), alpha=conf, ax=axes_11)
axes_11.plot(test_y)
axes_11.axvline(x=set_size-1, ls='-', c='black')
axes_11.set_title('[Predict Test_Dataset]')
axes_11.grid(True)


# [5] : prediction for full dataset(train+test)
sm.graphics.tsa.plot_predict(model, start=0, end=(set_size-1), alpha=conf, ax=axes_20)
axes_20.plot(train_y.index.values, train_y.values, label="train data")
axes_20.plot(test_y.index.values, test_y.values, label="test data")
axes_20.axvline(x=train_size-1, ls='--', c='skyblue')
axes_20.axvline(x=set_size-1, ls='-', c='black')
axes_20.set_title('[Full Prediction]')
axes_20.legend()
axes_20.grid(True)


# [6] : forecast for stock price in future
forecasting_steps = 10
prediction = model.predict(start=train_size, end=(set_size-1))
sm.graphics.tsa.plot_predict(model, start=0, end=(set_size-1 + forecasting_steps), alpha=conf, ax=axes_30)
axes_30.plot(train_y.index.values, train_y.values, label="train data")
axes_30.plot(test_y.index.values, test_y.values, label="test data")
axes_30.plot(test_y.index.values, prediction, label="predicted data")
axes_30.axvline(x=train_size-1, ls='--', c='skyblue')
axes_30.axvline(x=set_size-1, ls='--', c='r')
axes_30.axvline(x=set_size-1 + forecasting_steps, ls='-', c='black')
axes_30.set_title('[Forecast]')
axes_30.legend()
axes_30.grid(True)
plt.show()

