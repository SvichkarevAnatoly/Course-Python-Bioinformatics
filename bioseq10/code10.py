from rpy2.robjects import r
from rpy2.robjects import FloatVector, IntVector, Formula
from rpy2.robjects.packages import importr
from math import sqrt
from numpy import log as ln

import bioseq8.code8 as c


def mlr(y, x1, x2):
    stats = importr('stats')
    y = FloatVector(y)
    x1 = IntVector(x1)
    x2 = IntVector(x2)

    fmla = Formula('y ~ x1 + x2')
    env = fmla.environment
    env['y'] = y
    env['x1'] = x1
    env['x2'] = x2

    fit = stats.lm(fmla)
    return fit[0][0], fit[0][1], fit[0][2]


def norm(n, mean=0, sd=1):
    rnorm = r.rnorm
    return rnorm(n, mean=mean, sd=sd)


def gamma(n, shape=1, scale=1):
    rgamma = r.rgamma
    return rgamma(n, shape=shape, scale=scale)


def lnorm(n, meanlog=0, sdlog=1):
    rlnorm = r.rlnorm
    return rlnorm(n, meanlog=meanlog, sdlog=sdlog)


def param_norm(x):
    return c.mean(x), c.standard_deviation(x)


def param_gamma(x):
    m = c.mean(x)
    sd = c.standard_deviation(x)
    shape = (m ** 2) / sd
    scale = (sd ** 2) / m
    return shape, scale


def param_lnorm(x):
    m = c.mean(x)
    sd = c.standard_deviation(x)
    meanlog = ln(m) - ln(1 + sd / (m ** 2))
    sdlog = sqrt(ln(1 + sd / (m ** 2)))
    return meanlog, sdlog
