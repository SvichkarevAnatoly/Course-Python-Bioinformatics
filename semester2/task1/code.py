from numpy import dot, random, sqrt, vstack
from matplotlib import pyplot


def euclidean_dist(vector_a, vector_b):
    diff = vector_a - vector_b
    return sqrt(dot(diff, diff))


def find_neighbours(data_fn, dist_func, threshold):
    neighbour_dict = {}
    n = len(data_fn)
    for i_l1 in range(n):
        neighbour_dict[i_l1] = []

    for i_l2 in range(0, n - 1):
        for j in range(i_l2 + 1, n):
            dist = dist_func(data_fn[i_l2], data_fn[j])
            if dist < threshold:
                neighbour_dict[i_l2].append(j)
                neighbour_dict[j].append(i_l2)
    return neighbour_dict


def simple_cluster(data_sc, threshold, dist_func=euclidean_dist):
    neighbour_dict = find_neighbours(data_sc, dist_func, threshold)
    clusters_sc = []
    pool = set(range(len(data_sc)))
    cluster_data = []
    while pool:
        i_sc = pool.pop()
        neighbours = neighbour_dict[i_sc]
        cluster_sc = set()
        cluster_sc.add(i_sc)

        pool2 = set(neighbours)
        while pool2:
            j = pool2.pop()

            if j in pool:
                pool.remove(j)
                cluster_sc.add(j)
                neighbours2 = neighbour_dict[j]
                pool2.update(neighbours2)

        clusters_sc.append(cluster_sc)

        for cluster_sc in clusters_sc:
            cluster_data.append([data_sc[i_sc] for i_sc in cluster_sc])
    return cluster_data


def db_scan_cluster(data_dbsc, threshold, min_neighbour, dist_func=euclidean_dist):
    neighbour_dict = find_neighbours(data_dbsc, dist_func, threshold)
    clusters_dbsc = []
    noise = set()
    pool = set(range(len(data_dbsc)))

    while pool:
        i_dbsc = pool.pop()
        neighbours = neighbour_dict[i_dbsc]

        if len(neighbours) < min_neighbour:
            noise.add(i_dbsc)
        else:
            cluster_dbsc = set()
            cluster_dbsc.add(i_dbsc)
            pool2 = set(neighbours)
            while pool2:
                j = pool2.pop()
                if j in pool:
                    pool.remove(j)
                    neighbours2 = neighbour_dict.get(j, [])

                if len(neighbours2) < min_neighbour:
                    noise.add(j)
                else:
                    pool2.update(neighbours2)
                    cluster_dbsc.add(j)
            clusters_dbsc.append(cluster_dbsc)
    noise_data = [data_dbsc[i_l1] for i_l1 in noise]

    cluster_data = []
    for cluster_dbsc in clusters_dbsc:
        cluster_data.append([data_dbsc[i_l2] for i_l2 in cluster_dbsc])

    return cluster_data, noise_data


if __name__ == '__main__':
    print("\nSimple associative clustering\n")
    spread = 0.12
    sizeDims = (100, 2)
    data = [random.normal((0.0, 0.0), spread, sizeDims),
            random.normal((1.0, 1.0), spread, sizeDims),
            random.normal((1.0, 0.0), spread, sizeDims)]
    data = vstack(data)
    random.shuffle(data)  # Randomise order

    clusters = simple_cluster(data, 0.10)
    colors = ['#F0F0F0', '#A0A0A0', '#505050',
              '#D0D0D0', '#808080', '#202020']

    markers = ['d', 'o', 's', '>', '^']

    i = 0
    for cluster in clusters:
        allX, allY = zip(*cluster)

        if len(cluster) > 3:
            color = colors[i % len(colors)]
            marker = markers[i % len(markers)]
            pyplot.scatter(allX, allY, s=30, c=color, marker=marker)
            i += 1
        else:
            pyplot.scatter(allX, allY, s=5, c='black', marker='o')

    pyplot.xlabel("X")
    pyplot.ylabel("Y")
    pyplot.title("Figure 1. Simple associative clustering")
    pyplot.savefig("Figure_1")
    pyplot.show()
