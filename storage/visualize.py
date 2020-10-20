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
    def __init__(self, additional_stocks=[], ratio=0.9, freq=5):
        self.stock = fdr.StockListing('KRX').set_index('Name')
        self.stock_names = ['NH투자증권', '삼성증권','신한지주', 'KB금융']
        self.stock_names.extend(additional_stocks)
        self.config = dict()
        self.config['ratio'] = ratio 
        self.config['freq'] = freq 

    def datareader(self, name, start='2020-01-01', end='2020-10-01', verbose=True):
        if verbose : pprint(self.stock[self.stock.index == name].to_dict())
        code = str(self.stock[self.stock.index == name].Symbol.values.squeeze())

        stock_price = fdr.DataReader(code, start=start, end=end)['Close']

        x = stock_price.index.values
        y = stock_price.values
        return x, y

    # [present]   
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

    # [past]
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


    # [future]
    def scenario03(self, start='2020-01-01', end='2020-10-01', verbose=True, save=None):
        if not end: end = np.datetime64('today')
        time_range = np.arange(start, end, dtype='datetime64[D]')
        end_ = time_range[int(len(time_range)*self.config['ratio'])]
        self.config['scenario03'] = dict()
        self.config['scenario03']['freq'] = self.config['freq']
        self.config['scenario03']['start'] = start
        self.config['scenario03']['end'] = end
        self.config['scenario03']['end_'] = end_
        self.config['scenario03']['ks200'] = fdr.DataReader('KS200', start=start, end=end)['Close']
        self.config['scenario03']['ks200_'] = fdr.DataReader('KS200', start=start, end=end_)['Close']
        for name in self.stock_names:
            self.config['scenario03'][f'{name}_'] = self.datareader(name=name, start=start, end=end_, verbose=verbose)
            self.config['scenario03'][f'{name}'] = self.datareader(name=name, start=start, end=end, verbose=verbose)
        
        fig = plt.figure(figsize=(20,35))
        layout = (8,1)
        ax00 = plt.subplot2grid(layout, (0,0))
        ax01 = plt.subplot2grid(layout, (1,0))
        ax02 = plt.subplot2grid(layout, (2,0))
        ax03 = plt.subplot2grid(layout, (3,0))
        ax04 = plt.subplot2grid(layout, (4,0))
        ax05 = plt.subplot2grid(layout, (5,0))
        ax06 = plt.subplot2grid(layout, (6,0), rowspan=2)

        # axes : (0, 0) > differencing for normalized stock prices based on kospi200 index until end_
        ks200_x = self.config['scenario03']['ks200_'].index.values
        ks200_y = self.config['scenario03']['ks200_'].values
        ks200_y = (ks200_y - ks200_y.mean())/ks200_y.std()
        for name in self.stock_names:
            x, y = self.config['scenario03'][f'{name}_']
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
        ks200_x = self.config['scenario03']['ks200_'].index.values
        ks200_y = self.config['scenario03']['ks200_'].values
        ks200_y = (ks200_y - ks200_y.mean())/ks200_y.std()
        ax01.scatter(ks200_x, ks200_y, marker='*', c='black')
        ax01.plot(ks200_x, ks200_y, label='KS200', c='black')
        for name in self.stock_names:
            x, y = self.config['scenario03'][f'{name}_']
            y = (y - y.mean())/y.std()
            ax01.scatter(x, y, marker='*')
            ax01.plot(x, y, label=f'{name}')
        ax01.axhline(0, c='black', ls='--')
        ax01.axvline(start, c='grey', ls='--')
        ax01.axvline(end_, c='r', ls='--')
        ax01.set_title('[Past : Normalized]')
        ax01.grid(True)
        ax01.legend()

        # axes : (2, 0) > normalized trend of stock prices until end_
        ks200_x = self.config['scenario03']['ks200_'].index.values
        ks200_y = self.config['scenario03']['ks200_'].values
        trend = smt.seasonal_decompose(ks200_y, model='additive', freq=self.config['scenario03']['freq'], two_sided=True).trend
        ndiff = int(np.isnan(trend).sum()/2)
        ks200_x = ks200_x[ndiff:-ndiff]
        ks200_y = trend[~np.isnan(trend)]
        ks200_y = (ks200_y - ks200_y.mean())/ks200_y.std()
        ax02.scatter(ks200_x, ks200_y, marker='*', c='black')
        ax02.plot(ks200_x, ks200_y, label='KS200', c='black')
        for name in self.stock_names:
            x, y = self.config['scenario03'][f'{name}_']
            trend = smt.seasonal_decompose(y, model='additive', freq=self.config['scenario03']['freq'], two_sided=True).trend
            ndiff = int(np.isnan(trend).sum()/2)
            x = x[ndiff:-ndiff]
            y = trend[~np.isnan(trend)]
            y = (y - y.mean())/y.std()

            ax02.scatter(x, y, marker='*')
            ax02.plot(x, y, label=f'{name}')
        ax02.axhline(0, c='black', ls='--')
        ax02.axvline(start, c='grey', ls='--')
        ax02.axvline(end_, c='r', ls='--')
        ax02.set_title('[Past : Normalized trend]')
        ax02.grid(True)
        ax02.legend()

        # axes : (3, 0) > differencing for normalized stock prices based on kospi200 index
        ks200_x = self.config['scenario03']['ks200'].index.values
        ks200_y = self.config['scenario03']['ks200'].values
        ks200_y = (ks200_y - ks200_y.mean())/ks200_y.std()
        for name in self.stock_names:
            x, y = self.config['scenario03'][f'{name}']
            y = (y - y.mean())/y.std()
            y = y - ks200_y

            ax03.scatter(x, y, marker='*')
            ax03.plot(x, y, label=f'{name}')
        ax03.axhline(0, c='black', ls='--')
        ax03.axvline(start, c='grey', ls='--')
        ax03.axvline(end_, c='r', ls='--')
        ax03.axvline(end, c='black', ls='--')
        ax03.set_title('[Present : Diff]')
        ax03.grid(True)
        ax03.legend()

        # axes : (4, 0) > normalized stock prices
        ks200_x = self.config['scenario03']['ks200'].index.values
        ks200_y = self.config['scenario03']['ks200'].values
        ks200_y = (ks200_y - ks200_y.mean())/ks200_y.std()
        ax04.scatter(ks200_x, ks200_y, marker='*', c='black')
        ax04.plot(ks200_x, ks200_y, label='KS200', c='black')
        for name in self.stock_names:
            x, y = self.config['scenario03'][f'{name}']
            y = (y - y.mean())/y.std()

            ax04.scatter(x, y, marker='*')
            ax04.plot(x, y, label=f'{name}')
        ax04.axhline(0, c='black', ls='--')
        ax04.axvline(start, c='grey', ls='--')
        ax04.axvline(end_, c='r', ls='--')
        ax04.axvline(end, c='black', ls='--')
        ax04.set_title('[Present : Normalized]')
        ax04.grid(True)
        ax04.legend()

        # axes : (5, 0) > normalized trend of stock prices
        ks200_x = self.config['scenario03']['ks200'].index.values
        ks200_y = self.config['scenario03']['ks200'].values
        trend = smt.seasonal_decompose(ks200_y, model='additive', freq=self.config['scenario03']['freq'], two_sided=True).trend
        ndiff = int(np.isnan(trend).sum()/2)
        ks200_x = ks200_x[ndiff:-ndiff]
        ks200_y = trend[~np.isnan(trend)]
        ks200_y = (ks200_y - ks200_y.mean())/ks200_y.std()
        ax05.scatter(ks200_x, ks200_y, marker='*', c='black')
        ax05.plot(ks200_x, ks200_y, label='KS200', c='black')
        for name in self.stock_names:
            x, y = self.config['scenario03'][f'{name}']
            trend = smt.seasonal_decompose(y, model='additive', freq=self.config['scenario03']['freq'], two_sided=True).trend
            ndiff = int(np.isnan(trend).sum()/2)
            x = x[ndiff:-ndiff]
            y = trend[~np.isnan(trend)]
            y = (y - y.mean())/y.std()

            ax05.scatter(x, y, marker='*')
            ax05.plot(x, y, label=f'{name}')
        ax05.axhline(0, c='black', ls='--')
        ax05.axvline(start, c='grey', ls='--')
        ax05.axvline(end_, c='r', ls='--')
        ax05.axvline(end, c='black', ls='--')
        ax05.set_title('[Present : Normalized]')
        ax05.grid(True)
        ax05.legend()

        # axes : (6, 0) > stock prices
        for name in self.stock_names:
            x, y = self.config['scenario03'][f'{name}']

            ax06.scatter(x, y, marker='*')
            ax06.plot(x, y, label=f'{name}')
        ax06.axvline(start, c='grey', ls='--')
        ax06.axvline(end_, c='r', ls='--')
        ax06.axvline(end, c='black', ls='--')
        ax06.set_title('[Present : Origin]')
        ax06.grid(True)
        ax06.legend()

        plt.tight_layout()
        if save : plt.savefig('analysis03.png')
        plt.show()

    # [decompose]
    def scenario04(self, start='2020-01-01', end='2020-10-01', verbose=True, save=None):
        if not end: end = np.datetime64('today')
        self.config['scenario04'] = dict()
        self.config['scenario04']['freq'] = self.config['freq']

        fig = plt.figure(figsize=(20,18))
        layout = (4,1)
        ax00 = plt.subplot2grid(layout, (0,0))
        ax01 = plt.subplot2grid(layout, (1,0))
        ax02 = plt.subplot2grid(layout, (2,0))
        ax03 = plt.subplot2grid(layout, (3,0))

        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end, verbose=verbose)
            result = smt.seasonal_decompose(y, model='additive', freq=self.config['scenario04']['freq'], two_sided=False)
            ax00.scatter(x, result.observed, marker='*')
            ax00.plot(x, result.observed, label=f'{name}')
            ax01.scatter(x, result.trend, marker='*')
            ax01.plot(x, result.trend, label=f'{name}')
            ax02.scatter(x, result.seasonal, marker='*')
            ax02.plot(x, result.seasonal, label=f'{name}')
            ax03.scatter(x, result.resid, marker='*')
            ax03.plot(x, result.resid, label=f'{name}')

        ax00.grid(True)
        ax01.grid(True)
        ax02.grid(True)
        ax03.grid(True)
        ax00.legend()
        ax01.legend()
        ax02.legend()
        ax03.legend()
        plt.tight_layout()
        if save : plt.savefig('analysis04.png')
        plt.show()

    # [trend]
    def scenario05(self, start='2020-01-01', end='2020-10-01', verbose=True, save=None):
        if not end: end = np.datetime64('today')
        self.config['scenario05'] = dict()
        self.config['scenario05']['freq'] = self.config['freq']
        for name in self.stock_names:
            self.config['scenario05'][f'{name}'] = self.datareader(name=name, start=start, end=end, verbose=verbose)

        fig = plt.figure(figsize=(20,18))
        layout = (4,1)
        ax00 = plt.subplot2grid(layout, (0,0))
        ax01 = plt.subplot2grid(layout, (1,0))
        ax02 = plt.subplot2grid(layout, (2,0))
        ax03 = plt.subplot2grid(layout, (3,0))

        for name in self.stock_names:
            x, y = self.config['scenario05'][f'{name}']
            ax00.scatter(x, y, marker='*')
            ax00.plot(x, y, label=f'{name}')

            y = (y - y.mean())/y.std()
            ax02.scatter(x, y, marker='*')
            ax02.plot(x, y, label=f'{name}')


            x, y = self.config['scenario05'][f'{name}']
            trend = smt.seasonal_decompose(y, model='additive', freq=self.config['scenario05']['freq'], two_sided=True).trend
            ndiff = int(np.isnan(trend).sum()/2)
            x = x[ndiff:-ndiff]
            y = trend[~np.isnan(trend)]

            ax01.scatter(x, y, marker='*')
            ax01.plot(x, y, label=f'{name}')

            y = (y - y.mean())/y.std()
            ax03.scatter(x, y, marker='*')
            ax03.plot(x, y, label=f'{name}')

        ax00.grid(True)
        ax01.grid(True)
        ax02.grid(True)
        ax03.grid(True)
        ax00.legend()
        ax01.legend()
        ax02.legend()
        ax03.legend()
        ax00.set_title('[Observed]')
        ax01.set_title('[Trend]')
        ax02.set_title('[Normalized observed]')
        ax03.set_title('[Normalized trend]')
        ax02.axhline(0, c='black', ls='--')
        ax03.axhline(0, c='black', ls='--')
        plt.tight_layout()
        if save : plt.savefig('analysis05.png')
        plt.show()

    def scenario06(self, start='2020-01-01', end='2020-10-01', verbose=True, save=None):
        if not end: end = np.datetime64('today')
        self.config['scenario06'] = dict()

        fig = plt.figure()
        layout = (2,1)
        ax00 = plt.subplot2grid(layout, (0,0))

        for name in self.stock_names:
            x, y = self.datareader(name=name, start=start, end=end, verbose=verbose)
            ax00.scatter(x, y, marker='*')
            ax00.plot(x, y, label=f'{name}')

        plt.tight_layout()
        if save : plt.savefig('analysis06.png')
        plt.show()


plotting_board = Visualization(additional_stocks=['삼성전자', 'SK하이닉스', '삼성바이오로직스'], ratio=0.8, freq=20)
#plotting_board.scenario01(start='2019-01-01', end=None, verbose=None, save=None)
#plotting_board.scenario02(start='2019-01-01', end=None, verbose=None, save=None)
plotting_board.scenario03(start='2020-05-01', end=None, verbose=None, save=None)
#plotting_board.scenario04(start='2020-04-01', end=None, verbose=None, save=None)
#plotting_board.scenario05(start='2020-04-01', end=None, verbose=None, save=None)
#plotting_board.scenario06(start='2020-04-01', end=None, verbose=None, save=None)
