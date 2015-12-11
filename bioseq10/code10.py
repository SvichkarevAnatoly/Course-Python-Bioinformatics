from rpy2.robjects import FloatVector, IntVector, Formula
from rpy2.robjects.packages import importr


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
