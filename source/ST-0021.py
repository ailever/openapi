import numpy as np
from symfit import parameters, variables, sin, cos, Fit
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.api as smt

white_noise = np.random.normal(0,1, size=300)
time_series = np.zeros_like(white_noise)
for t, noise in enumerate(white_noise):
    deterministic_trend = 0*(0.03*t)**2 + 0*(0.03*t)**1 + 0*(0.03*t)**0
    deterministic_season = -10*np.cos(2*(2*np.pi)*t/(30)) + 10*np.cos(1*(2*np.pi)*t/(30)) + 1*np.cos(0*(2*np.pi)*t/(30))

    schtochastic_trend = 0*time_series[t-1] + 0*white_noise[t-1]
    schtochastic_season = 0*time_series[t-30] + 0*white_noise[t-30]

    deterministic_term = 1*deterministic_trend + 1*deterministic_season
    schtochastic_term = 1*schtochastic_trend + 1*schtochastic_season
    time_series[t] = 1*deterministic_term + 1*schtochastic_term + noise 

# [d=0] random process
y = time_series
_, axes = plt.subplots(9,1, figsize=(12, 25))
axes[0].plot(y, 'o-')
axes[0].set_title("[d+=0] Random Process")
axes[0].grid(True)

smt.graphics.plot_acf(y, lags=40, ax=axes[1])
axes[1].set_xlim(-1, 41)
axes[1].set_ylim(-1.1, 1.1)
axes[1].set_title("[d+=0] : Experimental partial autocorrelation function of an random process")
axes[1].grid(True)

smt.graphics.plot_pacf(y, lags=40, ax=axes[2])
axes[2].set_xlim(-1, 41)
axes[2].set_ylim(-1.1, 1.1)
axes[2].set_title("[d+=0] : Experimental partial autocorrelation function of an random process")
axes[2].grid(True)

# [d=1] random process
def fourier_series(x, f, n=0):
    # Make the parameter objects for all the terms
    a0, *A = parameters(','.join([f'a{i}' for i in range(0, n + 1)]))
    B = parameters(','.join([f'b{i}' for i in range(1, n + 1)]))
    # Construct the series
    series = a0 + sum(ai*cos(i*f*x) + bi*sin(i*f*x)
                     for i, (ai, bi) in enumerate(zip(A, B), start=1))
    return series

x_, y_ = variables('x, y')
w_, = parameters('w')
model_dict = {y_: fourier_series(x_, f=w_, n=5)}; print(model_dict)

X = np.arange(len(y)); Y = time_series
fit = Fit(model_dict, x=X, y=Y); # Define a Fit object for this model and data
fit_result = fit.execute(); print(fit_result)
y = Y - fit.model(x=X, **fit_result.params).y

axes[3].plot(X, fit.model(x=X, **fit_result.params).y, 'o-', c='r', alpha=0.5, label='fit value')
axes[3].plot(X, Y, 'o-', c='gray', label='previous')
axes[3].plot(X, y, 'o-', label='current')                    # time series (y) removed season
axes[3].set_title("[d+=1] Random Process : Differencing")
axes[3].legend()
axes[3].grid(True)

smt.graphics.plot_acf(y, lags=40, ax=axes[4])
axes[4].set_xlim(-1, 41)
axes[4].set_ylim(-1.1, 1.1)
axes[4].set_title("[d+=1] : Experimental partial autocorrelation function of an random process")
axes[4].grid(True)

smt.graphics.plot_pacf(y, lags=40, ax=axes[5])
axes[5].set_xlim(-1, 41)
axes[5].set_ylim(-1.1, 1.1)
axes[5].set_title("[d+=1] Experimental partial autocorrelation function of an random process")
axes[5].grid(True)

# [d=2] random process
def polynomial(x, coef):
    degree = len(coef) - 1
    value = 0
    for i in range(degree+1):
        value += coef[i]*x**(degree-i)
    return value
season = 15; degree = 2
X = np.arange(len(y))
X_ = X%season
Y = y
coef = np.polyfit(X_, Y, degree); print(f'Coefficients: {coef}')
y = Y - polynomial(X_, coef)
axes[6].plot(X, polynomial(X_, coef), 'o-', c='red', label='fit value')
axes[6].plot(X, Y, 'o-', c='gray', label='previous')
axes[6].plot(X, y, 'o-', label='current')
axes[6].set_title("[d+=2] Random Process : Differencing")
axes[6].legend()
axes[6].grid(True)

smt.graphics.plot_acf(y, lags=40, ax=axes[7])
axes[7].set_xlim(-1, 41)
axes[7].set_ylim(-1.1, 1.1)
axes[7].set_title("[d+=2] : Experimental partial autocorrelation function of an random process")
axes[7].grid(True)

smt.graphics.plot_pacf(y, lags=40, ax=axes[8])
axes[8].set_xlim(-1, 41)
axes[8].set_ylim(-1.1, 1.1)
axes[8].set_title("[d+=2] Experimental partial autocorrelation function of an random process")
axes[8].grid(True)

plt.tight_layout()
plt.show()
