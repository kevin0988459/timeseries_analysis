from skgstat import Variogram


def variogramPlot(t, sales):
    V = Variogram(t, sales)
    V.plot()
