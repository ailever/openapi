import statsmodels.api as sm
import statsmodels.tsa.api as smt
import matplotlib.pyplot as plt

# dataset
target = sm.datasets.sunspots.load_pandas().data['SUNACTIVITY'] + 10
target.plot(marker='o', color='black', legend=True, figsize=(12,5)) 

# ETS(A,A,N)
model = smt.ETSModel(target, seasonal_periods=24, error='add', trend='add', seasonal=None, damped_trend=False).fit(use_boxcox=True)
model.fittedvalues.plot(style='--',  color='blue', label=r'$ETS$')
forecast = model.forecast(24).rename(r'$ETS$')
forecast.plot(marker='o', color='blue')

plt.legend()
plt.show()

# [smt.ETSModel]
# error :(str) “add”-default or “mul”.
# trend :(str) “add”, “mul”, or None-default
# damped_trend :(bool) True, False-Default 
# seasonal :(str) “add”, “mul”, or None-default
# seasonal_periods :(int)
# initialization_method :(str) None, ‘estimated’-default, ‘heuristic’, ‘known’
# initial_level : (float)
# initial_trend : (float)
# initial_seasonal : (array_like)
# use_boxcox : {True, False, ‘log’, float}
# bounds : (dict)[str, tuple[float, float]]
# - “smoothing_level”
# - “smoothing_trend”
# - “smoothing_seasonal”
# - “damping_trend”
# - “initial_level”
# - “initial_trend”
# - “initial_seasonal.0”, …, “initial_seasonal.<m-1>”
# dates : (array_like) of datetime
# freq : (str) ‘B’, ‘D’, ‘W’, ‘M’, ‘A’, or ‘Q’
# missing : (str)  ‘none’, ‘drop’, and ‘raise’
