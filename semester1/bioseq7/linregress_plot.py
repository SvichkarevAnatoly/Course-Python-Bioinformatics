from numpy import random
from scipy.stats import linregress

random.seed(0)

xVals = random.normal(0.0, 1.0, 100)
yVals = 2.0 + -0.7 * xVals + random.normal(0.0, 0.2, 100)

grad, yInt, corrCoeff, pValue, stdErr = linregress(xVals, yVals)

print('LR 2:', grad, yInt, corrCoeff, pValue, stdErr)

xValsFit = [xVals.min(), xVals.max()]
yValsFit = [yInt + x * grad for x in xValsFit]

from matplotlib import pyplot

pyplot.plot(xVals, yVals, 'o')
pyplot.plot(xValsFit, yValsFit)
pyplot.show()
