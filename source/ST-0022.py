import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import (RBF, Matern, RationalQuadratic,
                                              ExpSineSquared, DotProduct,
                                              ConstantKernel)

kernels = [1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0)),
           1.0 * RationalQuadratic(length_scale=1.0, alpha=0.1),
           1.0 * ExpSineSquared(length_scale=1.0, periodicity=3.0,
                                length_scale_bounds=(0.1, 10.0),
                                periodicity_bounds=(1.0, 10.0)),
           ConstantKernel(0.1, (0.01, 10.0))
               * (DotProduct(sigma_0=1.0, sigma_0_bounds=(0.1, 10.0)) ** 2),
           1.0 * Matern(length_scale=1.0, length_scale_bounds=(1e-1, 10.0),
                        nu=1.5)]

x = np.random.uniform(0, 5, 10)
y = np.sin((x - 2.5) ** 2)
plt.scatter(x, y)

gp = GaussianProcessRegressor(kernel=kernels[0])
gp.fit(x[:, np.newaxis], y)

I = {} # interpolation
I['x'] = np.linspace(0, 5, 100)
I['y_mean'], I['y_std'] = gp.predict(I['x'][:, np.newaxis], return_std=True)
plt.plot(I['x'], I['y_mean'], 'k', lw=3, zorder=9)
plt.fill_between(I['x'], I['y_mean']-I['y_std'], I['y_mean']+I['y_std'], alpha=0.2, color='k')

#I['y_sample'] = gp.sample_y(I['x'][:, np.newaxis], 10)
#plt.plot(I['x'], I['y_sample'], lw=1)
