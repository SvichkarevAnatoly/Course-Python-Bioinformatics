from multiprocessing import Pool


def calcFunc(n, m):
    print("Running %d %d" % (n, m))
    result = sum([x * x for x in range(n) if x % m == 0])
    print("Result %d %d : %d " % (n, m, result))
    return result


if __name__ == '__main__':
    inputList = [37645, 8374634, 3487584, 191981, 754967, 12345]
    pool = Pool()
    jobs = []
    for value in inputList:
        inputArgs = (value, 2)
        job = pool.apply_async(calcFunc, inputArgs)
        jobs.append(job)

    results = []

    for job in jobs:
        result = job.get()
        results.append(result)

    pool.close()
    pool.join()
    print(results)
