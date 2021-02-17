from ailever.forecast import TSA, sarima

time_series = sarima.Process(trendparams=(2,1,1), trendAR=[0.3,0.4], trendMA=[0.3,],
                             seasonalparams=(1,1,1,20), seasonAR=[0.1,], seasonMA=[0.4,])
tsa = TSA(time_series.samples)
tsa.ETS(error='mul', trend='add', seasonal='mul', damped_trend=True)
tsa.SARIMAX(order=(2,1,1), seasonal_order=(1,1,1,20))
