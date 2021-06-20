import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf


def plotPACF(sales_data):
    nlags = len(sales_data) / 2 - 1
    plot_pacf(x=sales_data, lags=nlags, alpha=0.05, title="PACF")
    plt.show()
def monthlyDiffPACF(sales_data):
    diff_x_axis = sales_data.diff(12).fillna(0)
    nlags = len(diff_x_axis) / 2 - 1
    plot_pacf(x=diff_x_axis, lags=nlags, alpha=0.05, title="monthly difference PACF ")
    plt.show()

