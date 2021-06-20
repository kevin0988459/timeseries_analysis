import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
def exponential_smoothing(series,alpha):
    result = [series[0]]
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n-1])
    return result

def plotExponentialSmoothing(series):
    alphas = simpleExponentail(series)
    with plt.style.context('seaborn-white'):
        plt.figure(figsize=(8, 4))
        alphas = [0.1,0.4,alphas]
        for alpha in alphas:
            plt.plot(exponential_smoothing(series, alpha), label="Alpha {}".format(alpha))
        plt.plot(series.values, "c", label = "Actual")
        plt.legend(loc="best")
        plt.axis('tight')
        plt.title("Exponential Smoothing")
        plt.grid(True)
        plt.show()

def simpleExponentail(series):
    fit = SimpleExpSmoothing(series, initialization_method="estimated").fit()
    alphas = fit.model.params['smoothing_level']
    return alphas
