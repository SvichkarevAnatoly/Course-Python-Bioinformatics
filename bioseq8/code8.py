import rpy2.robjects as r


def t_test(x, y, same_variance=False):
    func = r.r['t.test']
    arg_dict = {'var.equal': same_variance}
    result = func(x=r.FloatVector(x), y=r.FloatVector(y), **arg_dict)

    return result[0][0], result[2][0]

