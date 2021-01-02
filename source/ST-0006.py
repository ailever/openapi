import statsmodels.api as sm
import statsmodels.tsa.api as smt
import matplotlib.pyplot as plt

# dataset
target = sm.datasets.sunspots.load_pandas().data['SUNACTIVITY'] + 10
target.plot(marker='o', color='black', legend=True, figsize=(12,5)) 

# Holt TS(Ad,N)
model = smt.Holt(target, exponential=True, damped_trend=True).fit()
model.fittedvalues.plot(style='--',  color='blue', label=r'$\alpha=%s$'%model.model.params['smoothing_level'])
forecast = model.forecast(24).rename(r'$\alpha=%s$'%model.model.params['smoothing_level'])
forecast.plot(marker='o', color='blue')

plt.legend()
plt.show()

# [smt.Holt]
# exponential :(bool)
# damped_trend :(bool)
# initialization_method :(str) None, ‘estimated’, ‘heuristic’, ‘legacy-heuristic’, ‘known’
# initial_level :(float)
# initial_trend :(float)
