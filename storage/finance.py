#%%
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%%
def datareader(code, period):
    stock_price = fdr.DataReader(code)['Close'][-period:]
    x = stock_price.index.values
    y = stock_price.values
    return x, y

x, y = datareader(code='002900', period=300)
plt.scatter(x,y, c='r', marker='*')
plt.plot(x,y)
plt.grid()
plt.show()

price = pd.DataFrame({'index':x, 'price':y}).set_index('index')
price.describe()

#%%
