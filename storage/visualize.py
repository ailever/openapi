
#%%
from pprint import pprint
from ailever.forecast import TSA
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd

plt.rcParams["font.family"] = 'NanumBarunGothic'


#%%
class Visualization:
    def __init__(self, additional_stocks=[], ratio=0.9):
        self.stock = fdr.StockListing('KRX').set_index('Name')
        self.stock_names = ['NH투자증권', '삼성증권','신한지주', 'KB금융']
        self.stock_names.extend(additional_stocks)
        self.config = dict()
        self.config['ratio'] = ratio 

    def datareader(self, name, start='2020-01-01', end='2020-10-01', verbose=True):
        if verbose : pprint(self.stock[self.stock.index == name].to_dict())
        code = str(self.stock[self.stock.index == name].Symbol.values.squeeze())

        stock_price = fdr.DataReader(code, start=start, end=end)['Close']

        x = stock_price.index.values
        y = stock_price.values
        return x, y
    
    def scenario01(self, start='2020-01-01', end='2020-10-01', verbose=True, save=None):
        if not end: end = np.datetime64('today')

        fig = plt.figure(figsize=(20,15))
        layout = (3,1)
        ax00 = plt.subplot2grid(layout, (0,0))
        ax01 = plt.subplot2grid(layout, (1,0))
        ax02 = plt.subplot2grid(layout, (2,0))

        KS200 = fdr.DataReader('KS200', start=start, end=end)['Close']
        x = KS200.index.values
        y = KS200.values

        # axes : (0, 0) > kospi200 index
        ax00.scatter(x, y, marker='*', c='black')
        ax00.plot(x, y, label='KS200', c='black')
        ax00.axvline(start, c='grey', ls='--')
        ax00.axvline(end, c='black', ls='--')
        ax00.set_title('[KS200]')
        ax00.grid(True)
        ax00.legend()

        # axes : (1, 0) > stock prices
        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end, verbose=verbose)
            ax01.scatter(x, y, marker='*')
            ax01.plot(x, y, label=f'{name}')
        ax01.axvline(start, c='grey', ls='--')
        ax01.axvline(end, c='black', ls='--')
        ax01.set_title('[Price]')
        ax01.grid(True)
        ax01.legend()

        # axes : (2, 0) > normalized stock prices
        x = KS200.index.values
        y = KS200.values
        y = (y - y.mean())/y.std()
        ax02.scatter(x, y, marker='*', c='black')
        ax02.plot(x, y, label='KS200', c='black')
        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end, verbose=verbose)
            y = (y - y.mean())/y.std()
            ax02.scatter(x, y, marker='*')
            ax02.plot(x, y, label=f'{name}')
        ax02.axhline(0, c='black', ls='--')
        ax02.axvline(start, c='grey', ls='--')
        ax02.axvline(end, c='black', ls='--')
        ax02.set_title('[Normalized Price]')
        ax02.grid(True)
        ax02.legend()

        plt.tight_layout()
        if save : plt.savefig('analysis01.png')
        plt.show()

    # past
    def scenario02(self, start='2020-01-01', end='2020-10-01', verbose=True, save=None):
        if not end: end = np.datetime64('today')
        time_range = np.arange(start, end, dtype='datetime64[D]')
        start_ = time_range[int(len(time_range)*self.config['ratio'])]
        self.config['scenario02'] = dict()
        self.config['scenario02']['start'] = start
        self.config['scenario02']['start_'] = start_
        self.config['scenario02']['end'] = end
        self.config['scenario02']['ks200'] = fdr.DataReader('KS200', start=start, end=end)['Close']
        self.config['scenario02']['ks200_'] = fdr.DataReader('KS200', start=start_, end=end)['Close']

        fig = plt.figure(figsize=(20,15))
        layout = (3,1)
        ax00 = plt.subplot2grid(layout, (0,0))
        ax01 = plt.subplot2grid(layout, (1,0))
        ax02 = plt.subplot2grid(layout, (2,0))

        # axes : (0, 0) > differencing for normalized stock prices based on kospi200 index
        ks200_x = self.config['scenario02']['ks200_'].index.values
        ks200_y = self.config['scenario02']['ks200_'].values
        ks200_y = (ks200_y - ks200_y.mean())/ks200_y.std()
        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start_, end=end, verbose=verbose)
            y = (y - y.mean())/y.std()
            y = y - ks200_y
            ax00.scatter(x, y, marker='*')
            ax00.plot(x, y, label=f'{name}')
        ax00.axhline(0, c='black', ls='--')
        ax00.axvline(start_, c='r', ls='--')
        ax00.axvline(end, c='black', ls='--')
        ax00.grid(True)
        ax00.set_title('[Present : Normalized]')
        ax00.legend()

        # axes : (1, 0) > normalized stock prices
        ks200_x = self.config['scenario02']['ks200'].index.values
        ks200_y = self.config['scenario02']['ks200'].values
        ks200_y = (ks200_y - ks200_y.mean())/ks200_y.std()
        ax01.scatter(ks200_x, ks200_y, marker='*', c='black')
        ax01.plot(ks200_x, ks200_y, label='KS200', c='black')
        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end, verbose=verbose)
            y = (y - y.mean())/y.std()
            ax01.scatter(x, y, marker='*')
            ax01.plot(x, y, label=f'{name}')
        ax01.axhline(0, c='black', ls='--')
        ax01.axvline(start, c='grey', ls='--')
        ax01.axvline(start_, c='r', ls='--')
        ax01.axvline(end, c='black', ls='--')
        ax01.set_title('[Past : Normalized]')
        ax01.grid(True)
        ax01.legend()

        # axes : (2, 0) > differencing for normalized stock prices based on kospi200 index
        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end, verbose=verbose)
            y = (y - y.mean())/y.std()
            y = y - ks200_y
            ax02.scatter(x, y, marker='*')
            ax02.plot(x, y, label=f'{name}')
        ax02.axhline(0, c='black', ls='--')
        ax02.axvline(start, c='grey', ls='--')
        ax02.axvline(start_, c='r', ls='--')
        ax02.axvline(end, c='black', ls='--')
        ax02.set_title('[Past : Diff]')
        ax02.grid(True)
        ax02.legend()


        plt.tight_layout()
        if save : plt.savefig('analysis02.png')
        plt.show()


    # future
    def scenario03(self, start='2020-01-01', end='2020-10-01', verbose=True, save=None):
        if not end: end = np.datetime64('today')
        time_range = np.arange(start, end, dtype='datetime64[D]')
        end_ = time_range[int(len(time_range)*self.config['ratio'])]
        self.config['scenario03'] = dict()
        self.config['scenario03']['start'] = start
        self.config['scenario03']['end'] = end
        self.config['scenario03']['end_'] = end_
        self.config['scenario03']['ks200'] = fdr.DataReader('KS200', start=start, end=end)['Close']
        self.config['scenario03']['ks200_'] = fdr.DataReader('KS200', start=start, end=end_)['Close']
        
        fig = plt.figure(figsize=(20,25))
        layout = (5,1)
        ax00 = plt.subplot2grid(layout, (0,0))
        ax01 = plt.subplot2grid(layout, (1,0))
        ax02 = plt.subplot2grid(layout, (2,0))
        ax03 = plt.subplot2grid(layout, (3,0))
        ax04 = plt.subplot2grid(layout, (4,0))

        # axes : (0, 0) > differencing for normalized stock prices based on kospi200 index until end_
        ks200_x = self.config['scenario03']['ks200_'].index.values
        ks200_y = self.config['scenario03']['ks200_'].values
        ks200_y = (ks200_y - ks200_y.mean())/ks200_y.std()
        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end_, verbose=verbose)
            y = (y - y.mean())/y.std()
            y = y - ks200_y
            ax00.scatter(x, y, marker='*')
            ax00.plot(x, y, label=f'{name}')
        ax00.axhline(0, c='black', ls='--')
        ax00.axvline(start, c='grey', ls='--')
        ax00.axvline(end_, c='r', ls='--')
        ax00.set_title('[Past : Diff]')
        ax00.grid(True)
        ax00.legend()

        # axes : (1, 0) > normalized stock prices until end_
        ax01.scatter(ks200_x, ks200_y, marker='*', c='black')
        ax01.plot(ks200_x, ks200_y, label='KS200', c='black')
        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end_, verbose=verbose)
            y = (y - y.mean())/y.std()
            ax01.scatter(x, y, marker='*')
            ax01.plot(x, y, label=f'{name}')
        ax01.axhline(0, c='black', ls='--')
        ax01.axvline(start, c='grey', ls='--')
        ax01.axvline(end_, c='r', ls='--')
        ax01.set_title('[Past : Normalized]')
        ax01.grid(True)
        ax01.legend()

        # axes : (2, 0) > differencing for normalized stock prices based on kospi200 index
        ks200_x = self.config['scenario03']['ks200'].index.values
        ks200_y = self.config['scenario03']['ks200'].values
        ks200_y = (ks200_y - ks200_y.mean())/ks200_y.std()
        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end, verbose=verbose)
            y = (y - y.mean())/y.std()
            y = y - ks200_y
            ax02.scatter(x, y, marker='*')
            ax02.plot(x, y, label=f'{name}')
        ax02.axhline(0, c='black', ls='--')
        ax02.axvline(start, c='grey', ls='--')
        ax02.axvline(end_, c='r', ls='--')
        ax02.axvline(end, c='black', ls='--')
        ax02.set_title('[Present : Diff]')
        ax02.grid(True)
        ax02.legend()

        # axes : (3, 0) > normalized stock prices
        ax03.scatter(ks200_x, ks200_y, marker='*', c='black')
        ax03.plot(ks200_x, ks200_y, label='KS200', c='black')
        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end, verbose=verbose)
            y = (y - y.mean())/y.std()
            ax03.scatter(x, y, marker='*')
            ax03.plot(x, y, label=f'{name}')
        ax03.axhline(0, c='black', ls='--')
        ax03.axvline(start, c='grey', ls='--')
        ax03.axvline(end_, c='r', ls='--')
        ax03.axvline(end, c='black', ls='--')
        ax03.set_title('[Present : Normalized]')
        ax03.grid(True)
        ax03.legend()

        # axes : (4, 0) > stock prices
        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end, verbose=verbose)
            ax04.scatter(x, y, marker='*')
            ax04.plot(x, y, label=f'{name}')
        ax04.axvline(start, c='grey', ls='--')
        ax04.axvline(end_, c='r', ls='--')
        ax04.axvline(end, c='black', ls='--')
        ax04.set_title('[Present : Origin]')
        ax04.grid(True)
        ax04.legend()

        plt.tight_layout()
        if save : plt.savefig('analysis03.png')
        plt.show()

    def scenario04(self, start='2020-01-01', end='2020-10-01', verbose=True, save=None):
        if not end: end = np.datetime64('today')
        self.config['scenario04'] = dict()

        fig = plt.figure()
        layout = (2,1)
        ax00 = plt.subplot2grid(layout, (0,0))

        plt.tight_layout()
        if save : plt.savefig('analysis04.png')
        plt.show()

    def scenario05(self, start='2020-01-01', end='2020-10-01', verbose=True, save=None):
        if not end: end = np.datetime64('today')
        self.config['scenario05'] = dict()

        fig = plt.figure()
        layout = (2,1)
        ax00 = plt.subplot2grid(layout, (0,0))

        plt.tight_layout()
        if save : plt.savefig('analysis05.png')
        plt.show()

plotting_board = Visualization(additional_stocks=[], ratio=0.5)
#plotting_board.scenario01(start='2019-01-01', end=None, verbose=None, save=None)
#plotting_board.scenario02(start='2019-01-01', end=None, verbose=None, save=None)
#plotting_board.scenario03(start='2020-04-01', end=None, verbose=None, save=None)
plotting_board.scenario04()
