from multiprocessing import Pool
from bioseq8.code8 import t_test
from numpy import random

random.seed(0)

N = 10
samples1 = [1.752, 1.818, 1.597, 1.697, 1.644, 1.593]
samples2 = [1.878, 1.648, 1.819, 1.794, 1.745, 1.827]


def generate_samples():
    result = [(samples1, samples2)]
    for _ in range(N - 1):
        tmp_sample1 = random.normal(0.0, 1.0, 6)
        tmp_sample2 = random.normal(0.0, 1.0, 6)
        result.append((tmp_sample1, tmp_sample2))
    return result


if __name__ == '__main__':
    sample_set = generate_samples()

    pool = Pool()
    jobs = []
    for i in range(N):
        inputArgs = sample_set[i]
        job = pool.apply_async(t_test, inputArgs)
        jobs.append(job)

    pool.close()
    pool.join()

    results = [job.get() for job in jobs]

    for i, res in enumerate(results):
        print "t_test " + str(i) + ":\t" \
              "t=" + str(res[0]) + "\t" \
              "p-value=" + str(res[1])
