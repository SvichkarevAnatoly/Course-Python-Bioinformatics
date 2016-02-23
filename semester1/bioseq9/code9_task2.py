from bioseq7.code7 import mean, mode, median, dispersion, standard_deviation
from multiprocessing import Process, Queue
import random

random.seed(0)

N = 10
functions = [mean, mode, median, dispersion, standard_deviation]
sample1 = [1, 2, 2, 3, 2, 1, 4, 2, 3, 1, 0]


def generate_samples():
    result = [sample1]
    for i in range(N - 1):
        tmp_sample = [random.randint(min(sample1), max(sample1))
                      for _ in range(len(sample1))]
        result.append(tmp_sample)
    return result


def queue_func(queue, func, data):
    result = func(data)
    queue.put((str(func.__name__), data, result))


def init_jobs(queue, data, funcs):
    jobs_list = [Process(target=queue_func, args=(queue, f, data))
                 for f in funcs]
    return jobs_list


if __name__ == '__main__':
    sample_set = generate_samples()

    q = Queue()

    for samp in sample_set:
        jobs = init_jobs(q, samp, functions)
        map(lambda x: x.start(), jobs)
        map(lambda x: x.join(), jobs)

        while not q.empty():
            func_name, data, res = q.get()
            print "On " + str(data) + " " +\
                  func_name + " = " + str(res)
    q.close()
