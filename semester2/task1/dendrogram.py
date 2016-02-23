from numpy import random, vstack
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from matplotlib import pyplot as plt
import numpy as np

np.set_printoptions(precision=5, suppress=True)  # suppress scientific float notation

random.seed(0)

spread = 0.12
means = [(0.0, 0.0), (1.0, 1.0), (1.0, 0.0)]
sizeDims = (100, 2)
data = [random.normal(means[0], spread, sizeDims),
        random.normal(means[1], spread, sizeDims),
        random.normal(means[2], spread, sizeDims)]
data = vstack(data)

# generate the linkage matrix
Z = linkage(data)
print Z[:20]

# plot clusters
k = 3
clusters = fcluster(Z, k, criterion='maxclust')
plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='prism')
plt.savefig("Figure_2")
plt.show()

# calculate full dendrogram
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(Z)
plt.savefig("Figure_3")
plt.show()
