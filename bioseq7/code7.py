import math
import numpy


def mean(data):
    return sum(data) / float(len(data))


def mode(data):
    return max(set(data), key=data.count)


def median(data):
    return numpy.median(data)


def dispersion(data):
    return math.sqrt(standard_deviation(data))


def standard_deviation(data):
    n = float(len(data))
    mean = sum(data) / n
    diffs = [v - mean for v in data]
    return sum([d ** 2 for d in diffs]) / n


def confidence_interval(data, confidence, is_one_sided=True):
    import numpy
    import scipy.stats
    n = len(data)
    # Unbiased estimate
    date_std_dev = numpy.std(data, ddof=1)
    if not is_one_sided:
        confidence = 0.5 * (1 + confidence)
    interval = scipy.stats.t(n - 1).ppf(confidence) * date_std_dev / \
               math.sqrt(n)
    return mean(data), interval
