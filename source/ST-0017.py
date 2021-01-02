import numpy as np
import statsmodels.api as sm

Y1 = np.random.normal(size=500).cumsum()    # deterministic/schtochastic
Y2 = 0.3 * Y1 + np.random.normal(size=500)  # schtochastic/deterministic
Y = 0.3 * Y1 - Y2

statistic, pvalue, _ = sm.tsa.coint(Y1, Y2)
if pvalue < 0.05:
    print(f'p-value : {pvalue}')
    print(' > Two time series have cointegration relation.')
else:
    print(f'p-value : {pvalue}')
    print(" > Two time series don't have cointegration relation.")
