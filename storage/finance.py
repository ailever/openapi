#%%
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

#%%
def datareader(code, period):
    stock_price = fdr.DataReader(code)['Close'][-period:]
    x = stock_price.index.values
    y = stock_price.values
    return x, y

x, y = datareader(code='002900', period=100)
plt.scatter(x,y, c='r', marker='*')
plt.plot(x,y)
plt.grid()
plt.show()


#%%
