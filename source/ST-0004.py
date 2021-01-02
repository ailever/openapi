import statsmodels.api as sm
import statsmodels.tsa.api as smt
import matplotlib.pyplot as plt

# dataset
target = sm.datasets.sunspots.load_pandas().data['SUNACTIVITY']
target.plot(marker='o', color='black', legend=True, figsize=(12,5))

# TS(N,N) : Simple Exponential Smoothing
model = smt.SimpleExpSmoothing(target).fit(smoothing_level=0.9, optimized=False)
model.fittedvalues.plot(style='--',  color='blue', label=r'$\alpha=%s$'%model.model.params['smoothing_level'])
forecast = model.forecast(24).rename(r'$\alpha=%s$'%model.model.params['smoothing_level'])
forecast.plot(marker='o', color='blue')

plt.legend()
plt.show()

# [smt.SimpleExpSmoothing]
# initialization_method :(str) None, ‘estimated’, ‘heuristic’, ‘legacy-heuristic’, ‘known’
# initial_level:(float)
