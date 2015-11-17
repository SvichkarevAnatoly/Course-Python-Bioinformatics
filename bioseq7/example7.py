from matplotlib import pyplot
from numpy import random

mean = 0.0
stdDev = 1.0
values = [1, 2, 2, 3, 2, 1, 4, 2, 3, 1, 0]
counts = [(values.count(val), val) for val in set(values)]
count, mode = max(counts)
print(mode)

from scipy import stats
from numpy import array

valArray = array(values, float)
mode, count = stats.mode(valArray)
print('Mode:', mode[0])  # Result is 2


def getMedian(values):
    vSorted = sorted(values)
    nValues = len(values)
    if nValues % 2 == 0:  # even number
        index = nValues // 2
        median = sum(vSorted[index - 1:index + 1]) / 2.0
    else:
        index = (nValues - 1) // 2
        median = vSorted[index]
    return median


med = getMedian(values)

from numpy import median

med = median(valArray)
print('Median:', med)  # Result is 2

values = [1, 2, 2, 3, 2, 1, 4, 2, 3, 1, 0]
mean = sum(values) / float(len(values))

from numpy import array, mean

valArray = array(values, float)

m = valArray.mean()
# or
m = mean(valArray)

print('Mean', m)  # Result is 1.909

valArray2 = array([[7, 9, 5], [1, 4, 3]])

print(valArray2.mean())  # All elements - result is 4.8333

print(valArray2.mean(axis=0))  # Column means - result is [4.0, 6.5, 4.0]

print(valArray2.mean(axis=1))  # Row means - result is [7.0, 2.6667]

values = [1, 2, 2, 3, 2, 1, 4, 2, 3, 1, 0]

n = float(len(values))
mean = sum(values) / n
diffs = [v - mean for v in values]
variance = sum([d * d for d in diffs]) / (n - 1)  # Unbiased estimate

from numpy import array

valArray = array(values)

variance = valArray.var()  # Biased estimate
print('Var 1', variance)  # Result is 1.1736

variance = valArray.var(ddof=1)  # Unbiased estimate
print('Var 2', variance)  # Result is 1.2909

from numpy import std, sqrt

stdDev = sqrt(variance)
stdDev = std(valArray)  # Biased estimate - 1.0833
stdDev = valArray.std(ddof=1)  # "Unbiased" estimate - 1.1362

print('Std:', stdDev)

stdErrMean = valArray.std(ddof=1) / sqrt(len(valArray))

from scipy.stats import sem

stdErrMean = sem(valArray, ddof=1)  # Result is 0.3426

from numpy import mean, std, sqrt
from scipy.stats import t


def tConfInterval(samples, confidence, isOneSided=True):
    n = len(samples)
    sampleMean = mean(samples)
    sampleStdDev = std(samples, ddof=1)  # Unbiased estimate
    if not isOneSided:
        confidence = 0.5 * (1 + confidence)
    interval = t(n - 1).ppf(confidence) * sampleStdDev / sqrt(n)
    return sampleMean, interval


from numpy import array

samples = array([1.752, 1.818, 1.597, 1.697, 1.644, 1.593, 1.878, 1.648,
                 1.819, 1.794, 1.745, 1.827])

sMean, intvl = tConfInterval(samples, 0.95, isOneSided=False)

print('Sample mean: %.3f, 95%% interval:%.4f' % (sMean, intvl))

from numpy import random, cov

xVals = random.normal(0.0, 1.0, 100)
yVals1 = random.normal(0.0, 1.0, 100)  # Random, independent of xVals

deltas = random.normal(0.0, 0.75, 100)
yVals2 = 0.5 + 2.0 * (xVals - deltas)  # Derived from xVals

cov1 = cov(xVals, yVals1)
# The exact value depends on the random numbers
# Cov 1: [[0.848, 0.022]
# [0.022, 1.048]]

cov2 = cov(xVals, yVals2)
# The exact value depends on the random numbers
# Cov 2: [[0.848, 1.809]
# [1.809, 5.819]]

from numpy import corrcoef

r1 = corrcoef(xVals, yVals1)[0, 1]  # Result is: 0.0231
r2 = corrcoef(xVals, yVals2)[0, 1]  # Result is: 0.8145

from numpy import std

cov2 = cov2[0, 1]  # X-Y element
stdDevX = std(xVals, ddof=1)
stdDevY = std(yVals2, ddof=1)

r2 = cov2 / (stdDevX * stdDevY)

from numpy import cov, var, mean, random

xVals = random.normal(0.0, 1.0, 100)
yVals = 2.0 + -0.7 * xVals + random.normal(0.0, 0.2, 100)

grad = cov(xVals, yVals) / var(xVals, ddof=1)
yInt = mean(yVals) - grad * mean(xVals)
print('LR 1:', grad, yInt)  # Result for one run was: -0.711 2.04

from scipy.stats import linregress
from matplotlib import pyplot

grad, yInt, corrCoeff, pValue, stdErr = linregress(xVals, yVals)

print('LR 2:', grad, yInt, corrCoeff, pValue, stdErr)
# Result for one run was: -0.712, 2.04, -0.949, 9.639e-51, 0.0240

xValsFit = [xVals.min(), xVals.max()]
yValsFit = [yInt + x * grad for x in xValsFit]

pyplot.plot(xVals, yVals, 'o')
pyplot.plot(xValsFit, yValsFit)
pyplot.show()
