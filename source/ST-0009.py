import statsmodels.api as sm
import statsmodels.tsa.api as smt
import matplotlib.pyplot as plt

# dataset
target = sm.datasets.sunspots.load_pandas().data['SUNACTIVITY'] + 10
target.plot(marker='o', color='black', legend=True, figsize=(12,5)) 

# Holt-Winter's TS(Ad,M)
model = smt.ExponentialSmoothing(target, seasonal_periods=24, trend='add', seasonal='mul', damped_trend=True).fit(use_boxcox=True)
model.fittedvalues.plot(style='--',  color='blue', label=r'$\alpha=%s$'%model.model.params['smoothing_level'])
forecast = model.forecast(24).rename(r'$\alpha=%s$'%model.model.params['smoothing_level'])
forecast.plot(marker='o', color='blue')

plt.legend()
plt.show()

# [smt.ExponentialSmoothing]
# trend :(str) “add”, “mul”, “additive”, “multiplicative”, None
# damped_trend :(bool) 
# seasonal :(str) “add”, “mul”, “additive”, “multiplicative”, None
# initialization_method :(str) None, ‘estimated’, ‘heuristic’, ‘legacy-heuristic’, ‘known’
# initial_level : (float)
# initial_trend : (float)
# initial_seasonal : (array_like)
# use_boxcox : {True, False, ‘log’, float}
# bounds : (dict)[str, tuple[float, float]]
# dates : (array_like) of datetime
# freq : (str) ‘B’, ‘D’, ‘W’, ‘M’, ‘A’, or ‘Q’
# missing : (str)  ‘none’, ‘drop’, and ‘raise’
