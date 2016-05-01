from numpy import exp, array, zeros, sqrt
from numpy import random, sum, dot
from time import time

from matplotlib import pyplot


def getFeatureDistance(vector1, vector2):
    distance = 0.0
    for a, b in zip(vector1, vector2):
        delta = a - b
        distance += delta * delta
    return distance


def convertSeqToVector(seq, indexDict):
    numLetters = len(indexDict)
    vector = [0.0] * len(seq) * numLetters
    for pos, letter in enumerate(seq):
        index = pos * numLetters + indexDict[letter]
        vector[index] = 1.0
    return vector


def kernelGauss(vectorI, vectorJ, sigma=1.0):
    sigma2 = sigma * sigma
    diff = vectorI - vectorJ
    dotProd = dot(diff, diff)
    return exp(-0.5 * dotProd / sigma2)


def kernelLinear(vectorI, vectorJ, mean):
    diffI = vectorI - mean
    diffJ = vectorJ - mean
    return dot(diffI, diffJ)


def svmTrain(knowns, data, kernelFunc, kernelParams, limit=1.0, maxSteps=500, relax=1.3):
    m, n = data.shape
    supports = zeros(m, float)
    change = 1.0  # arbitrary but big start

    kernelArray = zeros((m, m), float)
    for i in xrange(m):  # xrange in Python 2
        for j in xrange(i + 1):  # xrange in Python 2
            coincidence = kernelFunc(data[i], data[j], *kernelParams)
            kernelArray[i, j] = kernelArray[j, i] = coincidence
    kernelArray += 1

    steps = 0
    while (change > 1e-4) and (steps < maxSteps):
        prevSupports = supports.copy()

        sortSup = [(val, i) for i, val in enumerate(supports)]
        sortSup.sort(reverse=True)

        # random.shuffle(sortSup) - also possible
        for support, i in sortSup:
            pull = sum(supports * kernelArray[i, :] * knowns)

            adjust = knowns[i] * pull - 1.0
            supports[i] -= adjust * relax / kernelArray[i, i]
            supports[i] = max(0.0, min(limit, supports[i]))

        nonZeroSup = [(val, i) for i, val in enumerate(supports) if val > 0]

        if not nonZeroSup:
            continue

        nonZeroSup.sort()

        inds = [x[1] for x in nonZeroSup]
        niter = 1 + int(sqrt(len(inds)))

        for i in xrange(niter):  # xrange in Python 2
            for j in inds:
                pull = sum(kernelArray[j, inds] * knowns[inds] * supports[inds])
                adjust = knowns[j] * pull - 1.0
                supports[j] -= adjust * relax / kernelArray[j, j]
                supports[j] = max(0.0, min(limit, supports[j]))

        diff = supports - prevSupports
        change = sqrt(sum(diff * diff))
        steps += 1
    return supports, steps, kernelArray


def svmPredict(query, data, knowns, supports, kernelFunc, kernelParams):
    prediction = 0.0
    for j, vector in enumerate(data):
        support = supports[j]

        if support > 0:
            coincidence = kernelFunc(vector, query, *kernelParams) + 1.0
            prediction += coincidence * support * knowns[j]
    return prediction


def svmSeparation(knowns, supports, kernelArray):
    score = 0.0
    nz = [i for i, val in enumerate(supports) if val > 0]

    for i, known in enumerate(knowns):
        prediction = sum(supports[nz] * knowns[nz] * kernelArray[nz, i])

        if known * prediction > 0.0:  # same sign
            score += 1.0
    return 100.0 * score / len(knowns)


if __name__ == '__main__':
    # print("\nSupport vector machine training\n")
    random.seed(int(time()))
    numPoints = 16
    kernelFunc = kernelGauss
    catData = []

    for x in range(1, 6):
        for y in range(1, 6):
            xNorm = x / 6.0  # Normalise range [0,1]
            yNorm = y / 6.0

            if (x == 3) and (y == 3):
                category = -1.0
            elif (x % 2) == (y % 2):
                category = 1.0
            else:
                category = -1.0

            xvals = random.normal(xNorm, 0.05, numPoints)
            yvals = random.normal(yNorm, 0.05, numPoints)

            for i in xrange(numPoints):  # xrange in Python 2
                catData.append((xvals[i], yvals[i], category))

    catData = array(catData)
    random.shuffle(catData)

    knowns = catData[:, -1]
    data = catData[:, :-1]

    # plot training data
    colors = ["black" if label == -1.0 else "grey" for label in knowns]
    pyplot.scatter(data[:, 0], data[:, 1], color=colors)
    pyplot.savefig("ex1-train-" + str(numPoints) + "-" + kernelFunc.__name__)
    # pyplot.show()
    pyplot.close()

    t0 = time()
    params = (0.1,)
    supports, steps, kernelArray = svmTrain(knowns, data, kernelFunc, params)
    score = svmSeparation(knowns, supports, kernelArray)
    t1 = time()
    print(str(numPoints) + "-" + kernelFunc.__name__)
    print('time taken = %.3f' % (t1 - t0))
    print('Known data: %5.2f%% correct' % (score))

    # print("\nSupport vector machine prediction boundaries\n")
    ds1x = []
    ds1y = []
    ds2x = []
    ds2y = []
    x = 0.0
    while x < 1.0:
        y = 0.0
        while y < 1.0:
            query = array((x, y))
            prediction = svmPredict(query, data, knowns, supports, kernelFunc, params)

            if prediction > 0:
                ds1x.append(x)
                ds1y.append(y)
            else:
                ds2x.append(x)
                ds2y.append(y)

            y += 0.02
        x += 0.02

    pyplot.scatter(ds1x, ds1y, color='grey')
    pyplot.scatter(ds2x, ds2y, color='black')
    pyplot.savefig("ex1-class-" + str(numPoints) + "-" + kernelFunc.__name__)
    # pyplot.show()
