from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt



def plotACF(sales_data):
    lags = len(sales_data) - 1
    plot_acf(sales_data, lags= lags, alpha=0.05, title="Sales ACF" )
    plt.show()

def firstDiffACF(sales_data):
    diff_x_axis = sales_data.diff(1)
    lags = len(diff_x_axis) - 1
    plot_acf(diff_x_axis, lags= lags - 1, alpha=0.05, title="First difference ACF" )
    plt.show()

def monthlyDiffACF(sales_data):
    diff_x_axis = sales_data.diff(12).fillna(0)
    lags = len(diff_x_axis) - 1
    plot_acf(diff_x_axis, lags= lags - 1, alpha=0.05, title="monthly difference ACF" )
    plt.show()

def seasonalDiffACF(sales_data):
    diff_x_axis = sales_data.diff(4)
    lags = len(diff_x_axis) - 1
    plot_acf(diff_x_axis, lags= lags - 1, alpha=0.05, title="seasonal difference ACF" )
    plt.show()


