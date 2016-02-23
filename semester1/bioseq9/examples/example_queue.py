from multiprocessing import Process, Queue


def calcFuncWithQ(queue, n, m):
    result = sum([x * x for x in range(n) if x % m == 0])
    queue.put((n, m, result))


if __name__ == '__main__':
    queue = Queue()
    job1 = Process(target=calcFuncWithQ, args=(queue, 8745676, 2))
    job2 = Process(target=calcFuncWithQ, args=(queue, 2359461, 3))
    job1.start()
    job2.start()
    job1.join()
    job2.join()
    print("Result", queue.get())
    print("Result", queue.get())
    queue.close()
