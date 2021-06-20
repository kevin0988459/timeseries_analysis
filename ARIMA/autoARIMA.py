import pmdarima as pm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def autoArimaFit(sales_data , seasonal):
    smodel = pm.auto_arima(sales_data, start_p=1, start_q=1,
                             test='adf',
                             max_p=3, max_q=3, m=12,
                             start_P=0, seasonal=seasonal,
                             d=None, D=1, trace=True,
                             error_action='ignore',
                             suppress_warnings=True,
                             stepwise=True)
    return smodel

def autoArimaPlot(sales_data , smodel):
    n_periods = len(sales_data)
    fitted, confint = smodel.predict(n_periods=n_periods,
                                      return_conf_int=True)
    fitted_series = pd.Series(fitted, index=sales_data.index)
    lower_series = pd.Series(confint[:, 0], index=sales_data.index)
    upper_series = pd.Series(confint[:, 1], index=sales_data.index)
    plt.plot(sales_data)
    plt.plot(fitted_series, color='darkgreen' ,label = 'SARIMA forecast')
    plt.fill_between(lower_series.index,
                     lower_series,
                     upper_series,
                     color='k', alpha=.15, label = 'CI')
    plt.legend()
    plt.title("Auto SARIMA")
    plt.show()



