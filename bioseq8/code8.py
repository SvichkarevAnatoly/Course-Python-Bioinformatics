import rpy2.robjects as r
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage

STAP = SignatureTranslatedAnonymousPackage


def t_test(x, y, same_variance=False):
    func = r.r['t.test']
    arg_dict = {'var.equal': same_variance}
    result = func(x=r.FloatVector(x), y=r.FloatVector(y), **arg_dict)
    # return t, p_value
    return result[0][0], result[2][0]


def mean(x):
    func = r.r['mean']
    result = func(x=r.FloatVector(x))
    return result[0]


def mode(x):
    # define mode function in R
    func_str = '''mode <- function(x) {
        ux <- unique(x)
        ux[which.max(tabulate(match(x, ux)))]
    }'''
    # get moda function
    rf = STAP(func_str, "mode")
    result = rf.mode(x=r.FloatVector(x))
    return result[0]


def median(x):
    func = r.r['median']
    result = func(x=r.FloatVector(x))
    return result[0]


def dispersion(x):
    func = r.r['var']
    result = func(x=r.FloatVector(x))
    return result[0]


def standard_deviation(x):
    func = r.r['sd']
    result = func(x=r.FloatVector(x))
    return result[0]
