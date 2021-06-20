import matplotlib.pyplot as plt


def dataPlot(sales_data):
    plt.title("time series plot", fontsize=20)
    plt.ylabel("Sales", fontsize=16)
    plt.xlabel("Month", fontsize=16)
    plt.plot(sales_data)
    plt.show()
def firstDiffPlot(sales_data):
    diff_x_axis = sales_data.diff(1)
    plt.title("first diff time series plot", fontsize=20)
    plt.ylabel("Sales", fontsize=16)
    plt.xlabel("Month", fontsize=16)
    plt.plot(diff_x_axis)
    plt.show()

def monthlyDiffPlot(sales_data):
    diff_x_axis = sales_data.diff(12)
    plt.title("monthly diff time series plot", fontsize=20)
    plt.ylabel("Sales", fontsize=16)
    plt.xlabel("Month", fontsize=16)
    plt.plot(diff_x_axis)
    plt.show()
