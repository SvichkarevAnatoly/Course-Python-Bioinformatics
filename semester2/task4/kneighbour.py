def getFeatureDistance(vector1, vector2):
    distance = 0.0
    for a, b in zip(vector1, vector2):
        delta = a - b
        distance += delta * delta
    return distance


def kNearestNeighbour(knowns, query, k=7):
    if k >= len(knowns):
        raise Exception('Length of training data must be larger than k')

    dists = []
    for vector, cat in knowns:
        dist = getFeatureDistance(vector, query)
        dists.append((dist, cat))  # Vector could be included

    dists.sort()
    closest = dists[:k]

    counts = {}
    for dist, cat in closest:
        counts[cat] = counts.get(cat, 0) + 1

    bestCount = max(counts.values())
    bestCats = [cat for cat in counts if counts[cat] == bestCount]

    for dist, cat in closest:
        if cat in bestCats:
            return cat
