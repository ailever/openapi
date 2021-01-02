import numpy as np
import matplotlib.pyplot as plt
import statsmodels
import statsmodels.api as sm

# https://en.wikipedia.org/wiki/General_matrix_notation_of_a_VAR(p)
# Vector Form : Y_t = c + A1*Y_t-1 + A2*Y_t-2 + e
c = np.array([5,
              3]) # intercept
A1 = np.array([[ 0.2,  0],
               [-1.1,1.1]])
A = np.array([A1])
var_e = np.array([[  1, 0.8],
                  [0.8,   2]]) # sigma_u

# VARProcess
fit = statsmodels.tsa.vector_ar.var_model.VARProcess(A, c, var_e)
samples = statsmodels.tsa.vector_ar.util.varsim(fit.coefs, fit.intercept, fit.sigma_u, steps=100)
samples1 = np.c_[samples[:,0], samples[:,1]]
samples2 = np.c_[samples[:,1], samples[:,0]]

# Granger Causality Test
print('\n[Y2 -> Y1]')
sm.tsa.stattools.grangercausalitytests(samples1, maxlag=3, verbose=True)
print('\n[Y1 -> Y2]')
sm.tsa.stattools.grangercausalitytests(samples2, maxlag=3, verbose=True)
