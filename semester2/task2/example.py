from numpy import array, cov, dot, linalg
from numpy import random, sqrt, vstack, zeros
from random import sample

from matplotlib import pyplot


def euclidean_dist(vector_a, vector_b):
    diff = vector_a - vector_b
    return sqrt(dot(diff, diff))


def k_means(data_km, k_km, centers_km=None):
    if centers_km is None:
        centers_km = array(sample(data_km, k_km))

    change = 1
    while change > 1e-8:
        clusters_km = [[] for _ in range(k_km)]
        for vector in data_km:
            diffs = centers_km - vector
            dists = (diffs * diffs).sum(axis=1)
            closest = dists.argmin()
            clusters_km[closest].append(vector)

        change = 0
        for i_km, cluster_km in enumerate(clusters_km):
            cluster_km = array(cluster_km)
            center = cluster_km.sum(axis=0) / len(cluster_km)
            diff = center - centers_km[i_km]
            change += (diff * diff).sum()
            centers_km[i_km] = center
    return centers_km, clusters_km


def jump_method_cluster(data_jmc, k_range=None, cycles=10):
    n, dims = data_jmc.shape

    if k_range is None:
        start, limit = (2, n + 1)
    else:
        start, limit = k_range

    power = dims / 2.0
    distortions = {}
    inv_cov_mat = linalg.pinv(cov(data_jmc.T))

    for k_jmc in range(start, limit):
        mean_dists = zeros(cycles)

        for c in range(cycles):
            sum_dist = 0.0
            centers_jmc, clusters_jmc = k_means(data_jmc, k_jmc)

            for i_jmc, cluster_jmc in enumerate(clusters_jmc):
                size = len(cluster_jmc)
                diffs = array(cluster_jmc) - centers_jmc[i_jmc]

                for j, diff in enumerate(diffs):
                    dist = dot(diff.T, dot(diff, inv_cov_mat))
                    sum_dist += dist / size

            mean_dists[c] = sum_dist / (dims * k_jmc)
        distortions[k_jmc] = min(mean_dists) ** (-power)

    max_jump = None
    best_k = None
    for k_jmc in range(start + 1, limit):
        jump = distortions[k_jmc] - distortions[k_jmc - 1]
        if (max_jump is None) or (jump > max_jump):
            max_jump = jump
            best_k = k_jmc
    return best_k


def plot_clusters(clusters_pc, centers_pc, figure_name):
    colors = ['#FF0000', '#00FF00', '#0000FF',
              '#FFFF00', '#00FFFF', '#FF00FF']
    for i, cluster in enumerate(clusters_pc):
        x, y = zip(*cluster)
        color = colors[i % len(colors)]
        pyplot.scatter(x, y, c=color, marker='o')

    x, y = zip(*centers_pc)
    pyplot.scatter(x, y, s=100, c='black', marker='o')
    pyplot.xlabel("X")
    pyplot.ylabel("Y")
    pyplot.savefig(figure_name)
    pyplot.show()


if __name__ == '__main__':
    random.seed(0)
    spread = 0.12
    sizeDims = (100, 2)
    print("K-means clustering\n")
    testDataA = random.random((1000, 2))
    centers, clusters = k_means(testDataA, 3)
    plot_clusters(clusters, centers, "Figure_1")

    testDataB1 = random.normal(0.0, 2.0, (100, 2))
    testDataB2 = random.normal(7.0, 2.0, (100, 2))
    testDataB = vstack([testDataB1, testDataB2])

    centers, clusters = k_means(testDataB, 2)
    plot_clusters(clusters, centers, "Figure_2")

    print("Jump method to determine number of k-means clusters\n")
    data = [random.normal((0.0, 0.0), spread, sizeDims),
            random.normal((1.0, 1.0), spread, sizeDims),
            random.normal((1.0, 0.0), spread, sizeDims)]
    data = vstack(data)
    random.shuffle(data)

    k = jump_method_cluster(data, (2, 10), 20)
    print("Number of clusters: " + str(k))

    centers, clusters = k_means(data, k)
    plot_clusters(clusters, centers, "Figure_3")
