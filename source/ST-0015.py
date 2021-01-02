import numpy as np
import matplotlib.pyplot as plt
import statsmodels
import statsmodels.api as sm

# https://en.wikipedia.org/wiki/General_matrix_notation_of_a_VAR(p)
# Y_t = c + A1*Y_t-1 + A2*Y_t-2 + e
c = np.array([5,
              3]) # intercept
A1 = np.array([[ 0.2,0.3],
               [-0.6,1.1]])
A2 = np.array([[0.1,0.1],                
               [0.1,0.1]])
A = np.array([A1,A2])
var_e = np.array([[1, 0.8],
                  [0.8, 2]]) # sigma_u

# VARProcess
fit = statsmodels.tsa.vector_ar.var_model.VARProcess(A, c, var_e)
samples = statsmodels.tsa.vector_ar.util.varsim(fit.coefs, fit.intercept, fit.sigma_u, steps=100)
fit = sm.tsa.VAR(samples).fit()
fit.irf(10).plot()

# Residual Analysis
fit.plot_acorr()
plt.tight_layout()
plt.show()
