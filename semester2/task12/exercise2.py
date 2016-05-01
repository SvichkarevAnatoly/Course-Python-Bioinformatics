from numpy import array
from numpy import random
from time import time

from matplotlib import pyplot
from sklearn import svm

if __name__ == '__main__':
    # print("\nSupport vector machine training\n")
    random.seed(int(time()))
    numPoints = 40
    kernelFunc = "kernelGauss"
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
    pyplot.savefig("ex2-train-" + str(numPoints) + "-" + kernelFunc)
    # pyplot.show()
    pyplot.close()

    t0 = time()
    # fit the model
    # clf = svm.SVC(kernel='linear')
    clf = svm.NuSVC()
    clf.fit(data, knowns)
    score = clf.score(data, knowns)
    t1 = time()
    print(str(numPoints) + "-" + kernelFunc)
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
            prediction = clf.predict(query)

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
    pyplot.savefig("ex2-class-" + str(numPoints) + "-" + kernelFunc)
    # pyplot.show()
