import random
import treeclassification as e


def crossvalidate(algf, comparator, data, cvfactors, trials=100, scoref=e.entropy):
    errors = []
    for factor in cvfactors:
        error = 0.0
        for i in range(trials):
            trainset, testset = dividedata(data, factor)
            error += testalgorithm(algf, scoref, comparator, trainset, testset)
        errors.append(error / trials)
    return errors


def testalgorithm(algf, scoref, comparator, trainset, testset):
    error = 0.0
    for row in testset:
        guess = algf(trainset, row[:-1], scoref)  # row without last item
        error += comparator(row[-1], guess) ** 2  # row's last item
    return error / (len(testset) * len(trainset))


def dividedata(data, factor=0.95):
    testsize = len(data) * (1 - factor)
    testsize = 1 if testsize < 1 else int(round(testsize))

    testset = [data[i] for i in random.sample(xrange(len(data)), testsize)]
    trainset = [item for item in data if item not in testset]
    return trainset, testset


def algf_tree(trainset, observation, scoref):
    tree = e.buildtree(trainset, scoref)
    return e.classify(observation, tree)


# metric for prediction
def tree_comparator(test_class, tree_leaf):
    if test_class not in tree_leaf:
        return sum(tree_leaf.values())
    else:
        if len(tree_leaf) == 1:  # only test_class in branch
            return 0
        else:
            others = sum([value for key, value in tree_leaf.iteritems() if key != test_class])
            return float(others) / tree_leaf[test_class]
