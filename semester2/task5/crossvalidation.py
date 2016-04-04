import random
import example as e


def crossvalidate(algf, comparator, data, cvfactors, trials=100):
    errors = []
    for factor in cvfactors:
        error = 0.0
        for i in range(trials):
            trainset, testset = dividedata(data, factor)
            error += testalgorithm(algf, comparator, trainset, testset)
        errors.append(error / trials)
    return errors


def testalgorithm(algf, comparator, trainset, testset):
    error = 0.0
    for row in testset:
        guess = algf(trainset, row[:-1])  # row without last item
        error += comparator(row[-1], guess) ** 2  # row's last item
    return error / len(testset)


def dividedata(data, factor=0.95):
    testsize = len(data) * (1 - factor)
    testsize = 1 if testsize < 1 else testsize

    testset = [data[i] for i in random.sample(xrange(len(data)), testsize)]
    trainset = [item for item in data if item not in testset]
    return trainset, testset


def algf_tree(trainset, observation):
    tree = e.buildtree(trainset)
    return e.classify(observation, tree)


def entropy_on_uniquecounts(uniquecounts_dict):
    from math import log
    log2 = lambda x: log(x) / log(2)
    # Now calculate the entropy
    ent = 0.0
    for r in uniquecounts_dict.keys():
        p = float(uniquecounts_dict[r]) / sum(uniquecounts_dict.values())
        ent -= p * log2(p)
    return ent


def tree_comparator(test_class, tree_branch, scoref=entropy_on_uniquecounts):
    if test_class in tree_branch:
        tree_branch[test_class] -= 1
    return scoref(tree_branch)
