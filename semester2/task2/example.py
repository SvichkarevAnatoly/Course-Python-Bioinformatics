from matplotlib import pyplot
from random import randint, sample
from numpy import array, cov, diag, dot, linalg, ones
from numpy import outer, random, sqrt, vstack, zeros


def euclideanDist(vectorA, vectorB):
    diff = vectorA - vectorB
    return sqrt(dot(diff, diff))


def kMeans(data, k, centers=None):
    if centers is None:
        centers = array(sample(list(data), k))  # list() not needed in Python 2

    change = 1.0
    prev = []

    while change > 1e-8:
        clusters = [[] for x in range(k)]
        for vector in data:
            diffs = centers - vector
            dists = (diffs * diffs).sum(axis=1)
            closest = dists.argmin()
            clusters[closest].append(vector)

    change = 0
    for i, cluster in enumerate(clusters):
        cluster = array(cluster)
        center = cluster.sum(axis=0) / len(cluster)
        diff = center - centers[i]
        change += (diff * diff).sum()
        centers[i] = center
    return centers, clusters


def kMeansSpread(data, k):
    n = len(data)
    index = randint(0, n - 1)
    indices = set([index])

    influence = zeros(n)
    while len(indices) < k:
        diff = data - data[index]
        sumSq = (diff * diff).sum(axis=1) + 1.0
        influence += 1.0 / sumSq
        index = influence.argmin()

        while index in indices:
            index = randint(0, n - 1)
        indices.add(index)

    centers = vstack([data[i] for i in indices])
    return kMeans(data, k, centers)


def jumpMethodCluster(data, kRange=None, cycles=10):
    n, dims = data.shape

    if kRange is None:
        start, limit = (2, n + 1)
    else:
        start, limit = kRange
    power = dims / 2.0
    distortions = {}
    invCovMat = linalg.pinv(cov(data.T))

    for k in range(start, limit):
        meanDists = zeros(cycles)

        for c in range(cycles):
            sumDist = 0.0
            centers, clusters = kMeans(data, k)

            for i, cluster in enumerate(clusters):
                size = len(cluster)
                diffs = array(cluster) - centers[i]

                for j, diff in enumerate(diffs):
                    dist = dot(diff.T, dot(diff, invCovMat))
                    sumDist += dist / size

            meanDists[c] = sumDist / (dims * k)
        distortions[k] = min(meanDists) ** (-power)

    maxJump = None
    bestK = None

    for k in range(start + 1, limit):
        jump = distortions[k] - distortions[k - 1]
        if (maxJump is None) or (jump > maxJump):
            maxJump = jump
            bestK = k
    return bestK


if __name__ == '__main__':
    spread = 0.12
    sizeDims = (100, 2)
    print("K-means clustering\n")
    testDataA = random.random((1000, 2))  # No clumps
    centers, clusters = kMeans(testDataA, 3)

    testDataB1 = random.normal(0.0, 2.0, (100, 2))
    testDataB2 = random.normal(7.0, 2.0, (100, 2))
    testDataB = vstack([testDataB1, testDataB2])  # Two clumps

    centers, clusters = kMeans(testDataB, 2)
    colors = ['#FF0000', '#00FF00', '#0000FF',
              '#FFFF00', '#00FFFF', '#FF00FF']

    for i, cluster in enumerate(clusters):
        x, y = zip(*cluster)
        color = colors[i % len(colors)]
        pyplot.scatter(x, y, c=color, marker='o')

    x, y = zip(*centers)
    pyplot.scatter(x, y, s=40, c='black', marker='o')
    pyplot.xlabel("X")
    pyplot.ylabel("Y")
    pyplot.title("Figure 3. K-means clustering")
    pyplot.savefig("Figure_3")
    pyplot.show()

    print("Jump method to determine number of k-means clusters\n")
    data = [random.normal((0.0, 0.0), spread, sizeDims),
            random.normal((1.0, 1.0), spread, sizeDims),
            random.normal((1.0, 0.0), spread, sizeDims)]

    data = vstack(data)
    random.shuffle(data)

    k = jumpMethodCluster(data, (2, 10), 20)
    print('Number of clusters:', k)
