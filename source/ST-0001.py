import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.api as smt

phi, Phi = 0, 0
theta, Theta = 0.5, 0.8
ar_params = np.array([])
ma_params = np.array([theta, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Theta, theta*Theta])
ar, ma = np.r_[1, -ar_params], np.r_[1, ma_params]
y = sm.tsa.ArmaProcess(ar, ma).generate_sample(500, burnin=50)

time_series = pd.Series(y)
train = time_series[:400]
test = time_series[400:]

p, d, q = 0, 0, 1
P, D, Q = 0, 0, 1
model = smt.SARIMAX(train, order=(p,d,q), seasonal_order=(P,D,Q,12)).fit(trend='c')
prediction_train = model.predict()
prediction_test = model.get_forecast(len(test)).predicted_mean
prediction_test_bound = model.get_forecast(len(test)).conf_int()

_, axes = plt.subplots(1,1, figsize=(12,5))
axes.plot(test.index, prediction_test, c='r', label='predict')
axes.fill_between(pd.DataFrame(prediction_test_bound, index=test.index).index,
                  pd.DataFrame(prediction_test_bound, index=test.index).iloc[:,0],
                  pd.DataFrame(prediction_test_bound, index=test.index).iloc[:,1], color='k', alpha=0.15)

train.plot(label='train', ax=axes)
test.plot(label='test', ax=axes)
axes.grid(True)
axes.legend()
plt.show()
