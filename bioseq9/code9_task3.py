from multiprocessing import Process
import numpy
from bioseq7.code7 import line_regression_numpy as lr

numpy.random.seed(0)

grads = [-0.7, -2.7, -1.7]


def generate_xy(grad_coeff):
    x = numpy.random.normal(0.0, 1.0, 100)
    y = 2.0 + grad_coeff * x + numpy.random.normal(0.0, 0.2, 100)
    return x, y


def calc_lr(data, gr):
    g, y_int = lr(data[0], data[1])
    result_str = "on " + str(gr) + \
                 " sample: grad = " + str(g) + \
                 " yInt = " + str(y_int)
    print result_str


if __name__ == '__main__':
    sample_set = [generate_xy(grad) for grad in grads]
    jobs = [Process(target=calc_lr, args=(sample, grad))
            for sample, grad in zip(sample_set, grads)]
    map(lambda x: x.start(), jobs)
    map(lambda x: x.join(), jobs)
