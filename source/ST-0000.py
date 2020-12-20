import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.api as smt

white_noise = np.random.normal(size=500)
time_series = np.zeros_like(white_noise)
for t, noise in enumerate(white_noise):
    time_series[t] = 0.5*time_series[t-1] + 0.25*time_series[t-2] + noise - 1*white_noise[t-1] + 0.6*white_noise[t-2]

time_series = pd.Series(time_series.cumsum())
train = time_series[:70]
test = time_series[70:]

p, d, q = 2, 1, 2
model = smt.ARIMA(train, order=(p,d,q)).fit(trend='c')

_, axes = plt.subplots(1,1, figsize=(12,5))
model.plot_predict(start=d, end=100-1, ax=axes)
values = model.forecast(30)[0]
low_bound = model.forecast(30)[2][:,0]
high_bound = model.forecast(30)[2][:,1]
train.plot(label='train', ax=axes)
test.plot(label='test', ax=axes)
axes.plot(time_series, c='black', lw=0.5, ls='--', label='train+test')
axes.plot(range(70,100), values, label='model.forecast')
axes.plot(range(70,100), low_bound, c='red', ls='--', lw=1)
axes.plot(range(70,100), high_bound, c='red', ls='--', lw=1)
axes.grid(True)
axes.legend()
plt.show()
