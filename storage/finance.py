#%%
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
from pprint import pprint
import pandas as pd
import numpy as np

#%%
markets = ['NASDAQ', 'NYSE', 'AMEX', 'SSE', 'SZSE', 'HKEX', 'TSE', 'HOSE',
           'KRX', 'KOSPI', 'KOSDAQ', 'KONEX',
           'KRX-DELISTING',
           'KRX-ADMINISTRATIVE',
           'S&P500', 'SP500']

stock = fdr.StockListing('KRX').set_index('Name')

#%%
def datareader(name, period):
    pprint(stock[stock.index == name].to_dict())
    code = str(stock[stock.index == name].Symbol.values.squeeze())
    stock_price = fdr.DataReader(code)['Close'][-period:]
    x = stock_price.index.values
    y = stock_price.values
    return x, y

x, y = datareader(name='동양물산', period=52*1)
plt.scatter(x,y, c='r', marker='*')
plt.plot(x,y)
plt.grid()
plt.show()

price = pd.DataFrame({'index':x, 'price':y}).set_index('index')
price.describe()

#%%
