from multiprocessing import Pool
from bioseq8.code8 import t_test
from numpy import random

random.seed(0)

N = 10
samples1 = [1.752, 1.818, 1.597, 1.697, 1.644, 1.593]
samples2 = [1.878, 1.648, 1.819, 1.794, 1.745, 1.827]

samples_set = [(samples1, samples2)]
for i in range(N-1):
    tmp_sample1 = random.normal(0.0, 1.0, 6)
    tmp_sample2 = random.normal(0.0, 1.0, 6)
    samples_set.append((tmp_sample1, tmp_sample2))

pool = Pool()
jobs = []
for i in range(N):
    inputArgs = samples_set[i]
    job = pool.apply_async(t_test, inputArgs)
    jobs.append(job)

results = []
for job in jobs:
    result = job.get()
    results.append(result)

pool.close()
pool.join()

for i, res in enumerate(results):
    print "t_test " + str(i) + ":" \
        " t=" + str(res[0]) +\
        " p-value=" + str(res[1])
