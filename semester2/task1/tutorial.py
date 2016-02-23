from numpy import random, vstack
from scipy.cluster.hierarchy import dendrogram, linkage

from matplotlib import pyplot as plt

random.seed(0)

spread = 0.12
means = [(0.0, 0.0), (1.0, 1.0), (1.0, 0.0)]
sizeDims = (100, 2)
data = [random.normal(means[0], spread, sizeDims),
        random.normal(means[1], spread, sizeDims),
        random.normal(means[2], spread, sizeDims)]
data = vstack(data)
plt.scatter(data[:, 0], data[:, 1])
plt.show()

# generate the linkage matrix
Z = linkage(data)

print Z[:20]

# calculate full dendrogram
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(Z)
plt.show()
