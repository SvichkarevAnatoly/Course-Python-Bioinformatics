from multiprocessing import Process


def calcFunc(n, m):
    print("Running %d %d" % (n, m))
    result = sum([x * x for x in range(n) if x % m == 0])
    print("Result %d %d : %d " % (n, m, result))
    return result


if __name__ == '__main__':
    job1 = Process(target=calcFunc, args=(8745678, 2))
    job2 = Process(target=calcFunc, args=(2359141, 3))
    job1.start()
    job2.start()
    job1.join()
    job2.join()
