def mean(data):
    return sum(data) / float(len(data))


def mode(data):
    return max(set(data), key=data.count)


def median(data):
    import numpy
    return numpy.median(data)


def dispersion(data):
    import math
    return math.sqrt(standard_deviation(data))


def standard_deviation(data):
    n = float(len(data))
    mean = sum(data) / n
    diffs = [v - mean for v in data]
    return sum([d ** 2 for d in diffs]) / n
