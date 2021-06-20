import pandas as pd
from timeseries_data_plot import dataplot
from ACF_PACF import ACF, PACF
from exponentail_smoothing import exponential_plot
from ARIMA import autoARIMA
data = pd.read_csv('datafile.csv')
sales_data = data['Sales']
## plot original data
dataplot.dataPlot(sales_data)
## plot original data ACF
ACF.plotACF(sales_data)
## plot original data PACF
PACF.plotPACF(sales_data)
## plot differencing data
dataplot.monthlyDiffPlot(sales_data)
## plot differencing ACF
ACF.monthlyDiffACF(sales_data)
## plot differencing PACF
PACF.monthlyDiffPACF(sales_data)
## fit the exponentail method
exponential_plot.plotExponentialSmoothing(sales_data)
## fit the autoARIMA
smodel = autoARIMA.autoArimaFit(sales_data,seasonal=True)
## plot autoARIMA
autoARIMA.autoArimaPlot(sales_data, smodel)
