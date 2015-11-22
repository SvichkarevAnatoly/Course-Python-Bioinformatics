import rpy2.robjects as r
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage

stap = SignatureTranslatedAnonymousPackage


def simple_call(r_func_name, x):
    func = r.r[r_func_name]
    result = func(x=r.FloatVector(x))
    return result[0]


def t_test(x, y, same_variance=False):
    func = r.r['t.test']
    arg_dict = {'var.equal': same_variance}
    result = func(x=r.FloatVector(x), y=r.FloatVector(y), **arg_dict)
    # return t, p_value
    return result[0][0], result[2][0]


def mean(x):
    return simple_call("mean", x)


def mode(x):
    # define mode function in R
    func_str = '''mode <- function(x) {
        ux <- unique(x)
        ux[which.max(tabulate(match(x, ux)))]
    }'''
    # get moda function
    rf = stap(func_str, "mode")
    result = rf.mode(x=r.FloatVector(x))
    return result[0]


def median(x):
    return simple_call("median", x)


def dispersion(x):
    return simple_call("var", x)


def standard_deviation(x):
    return simple_call("sd", x)


def confidence_interval(x):
    func = r.r['t.test']
    result = func(x=r.FloatVector(x))
    return result[4][0], result[3][1] - result[4][0]