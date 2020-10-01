#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.api as smt
from scipy import stats
import pandas_datareader.data as web

def stationary(TS):
    """
    Augmented Dickey-Fuller test

    Null Hypothesis (H0): [if p-value > 0.5, non-stationary]
    >   Fail to reject, it suggests the time series has a unit root, meaning it is non-stationary.
    >   It has some time dependent structure.
    Alternate Hypothesis (H1): [if p-value =< 0.5, stationary]
    >   The null hypothesis is rejected; it suggests the time series does not have a unit root, meaning it is stationary.
    >   It does not have time-dependent structure.
    """
    result = smt.adfuller(TS)

    print(f'[ADF Statistic] : {result[0]}')
    print(f'[p-value] : {result[1]}')
    for key, value in result[4].items():
        print(f'[Critical Values {key} ] : {value}')


def tsplot(TS, period=7, lags=None, figsize=(18, 20), style='bmh'):
    if not isinstance(TS, pd.Series):
        TS = pd.Series(TS)

    with plt.style.context(style):
        fig = plt.figure(figsize=figsize)
        # mpl.rcParams['font.family'] = 'Ubuntu Mono'

        layout = (6, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        dc_trend_ax = plt.subplot2grid(layout, (1, 0), colspan=2)
        dc_seasonal_ax = plt.subplot2grid(layout, (2, 0), colspan=2)
        dc_resid_ax = plt.subplot2grid(layout, (3, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (4, 0))
        pacf_ax = plt.subplot2grid(layout, (4, 1))
        qq_ax = plt.subplot2grid(layout, (5, 0))
        pp_ax = plt.subplot2grid(layout, (5, 1))

        TS.plot(ax=ts_ax)
        ts_ax.set_title('Time Series')
        smt.seasonal_decompose(TS, model='additive', period=period).trend.plot(ax=dc_trend_ax)
        dc_trend_ax.set_title('[Decompose] Time Series Trend')
        smt.seasonal_decompose(TS, model='additive', period=period).seasonal.plot(ax=dc_seasonal_ax)
        dc_seasonal_ax.set_title('[Decompose] Time Series Seasonal')
        smt.seasonal_decompose(TS, model='additive', period=period).resid.plot(ax=dc_resid_ax)
        dc_resid_ax.set_title('[Decompose] Time Series Resid')
        smt.graphics.plot_acf(TS, lags=lags, ax=acf_ax, alpha=0.5)
        smt.graphics.plot_pacf(TS, lags=lags, ax=pacf_ax, alpha=0.5)
        sm.qqplot(TS, line='s', ax=qq_ax)
        qq_ax.set_title('QQ Plot')
        stats.probplot(TS, sparams=(TS.mean(), TS.std()), plot=pp_ax)

        plt.tight_layout()
        plt.savefig('time_series_analysis.png')
        plt.show()


#%% loading stock data
start = '2018-06-29'
end = '2020-09-29'
df = web.DataReader('005380', 'naver', start=start, end=end)
index = pd.to_numeric(pd.to_datetime(df.index)).values
series = df['Low'].values
ts = pd.DataFrame({'index': index, 'series': series})
ts = ts.set_index('index')
data = ts.values.astype(np.float64)
data = data.squeeze()

period=int(365/4)
trend = smt.seasonal_decompose(data, model='additive', period=period).trend
seasonal = smt.seasonal_decompose(data, model='additive', period=period).seasonal
resid = smt.seasonal_decompose(data, model='additive', period=period).resid

tsplot(data, period=period)

#%% [Stationary]
stationary(data)
#stationary(trend)
#stationary(seasonal)
#stationary(resid)

#%% [Descriptive Statistics]
pd.DataFrame(data).describe()
#pd.DataFrame(trend).describe()
#pd.DataFrame(seasonal).describe()
#pd.DataFrame(resid).describe()

#%% [Plot Time Series] : trend + seasonal + resid
_, axes = plt.subplots(3,1)
pd.DataFrame(data).plot(ax=axes[0],)
pd.DataFrame(data).hist(ax=axes[1],)
pd.DataFrame(data).plot(kind='kde', ax=axes[2])
axes[0].grid(True)
axes[1].grid(True)
axes[2].grid(True)
plt.show()

#%% [Plot Trend]
_, axes = plt.subplots(3,1)
pd.DataFrame(trend).plot(ax=axes[0],)
pd.DataFrame(trend).hist(ax=axes[1],)
pd.DataFrame(trend).plot(kind='kde', ax=axes[2])
axes[0].grid(True)
axes[1].grid(True)
axes[2].grid(True)
plt.show()

#%% [Plot Seasonal]
_, axes = plt.subplots(3,1)
pd.DataFrame(seasonal).plot(ax=axes[0],)
pd.DataFrame(seasonal).hist(ax=axes[1],)
pd.DataFrame(seasonal).plot(kind='kde', ax=axes[2])
axes[0].grid(True)
axes[1].grid(True)
axes[2].grid(True)
plt.show()


#%% [Plot Resid]
_, axes = plt.subplots(3,1)
pd.DataFrame(resid).plot(ax=axes[0],)
pd.DataFrame(resid).hist(ax=axes[1],)
pd.DataFrame(resid).plot(kind='kde', ax=axes[2])
axes[0].grid(True)
axes[1].grid(True)
axes[2].grid(True)
plt.show()

#%% [Forecast]
model = smt.arima.ARIMA(ts.values, order=(2, 0, 2), trend='n').fit()
prediction = model.predict(start=end, end='2020-10-10')
plt.plot(ts.index.values, ts.values, label="train data")
plt.plot(pd.date_range(start=end, end='2020-10-10'), prediction, label="predicted data")
plt.legend()
plt.grid(True)
plt.show()

#%%
np.random.seed(12345)
arparams = np.array([.75, -.25])
maparams = np.array([.65, .35])

ar = np.r_[1, -arparams] # add zero-lag and negate
ma = np.r_[1, maparams] # add zero-lag


#%% Generate Samples
num_samples = 250
y = smt.arma_generate_sample(ar, ma, nsample=num_samples)
dates = pd.date_range(start='2020-01-01', freq="D", periods=num_samples)
y = pd.Series(y, index=dates)

set_size = len(y)
train_size = int(len(y)*0.7)
train_y = y.iloc[:train_size]
test_y = y.iloc[train_size:]
print(train_y, len(train_y))

#%% tsplot
tsplot(train_y)

#%% fit model
model = smt.arima.ARIMA(train_y, order=(2, 0, 2), trend='n').fit()
model.params

#%% [1] predict : train
sm.graphics.tsa.plot_predict(model, start=0, end=train_size)
plt.plot(train_y)
plt.grid(True)
plt.show()

prediction = model.predict(start=0, end=train_size)
((train_y - prediction)**2).mean()

#%% [2] predict : test
sm.graphics.tsa.plot_predict(model, start=train_size, end=(set_size-1))
plt.plot(test_y)
plt.grid(True)
plt.show()

#%% [3] predict : train + test
prediction = model.predict(start=train_size, end=(set_size-1))
plt.plot(train_y.index.values, train_y.values, label="train data")
plt.plot(test_y.index.values, test_y.values, label="test data")
plt.plot(test_y.index.values, prediction, label="predicted data")
plt.legend()
plt.grid(True)
plt.show()

#model.predict(start='2020-01-01', end='2020-01-02')
