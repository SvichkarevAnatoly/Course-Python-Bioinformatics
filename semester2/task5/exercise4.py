import random

import treeclassification as tc
import exercise1 as ex1
import exercise2 as ex2
import exercise3 as ex3
import crossvalidation as cv

random.seed(0)
cvMainFactor = 0.75
trainset, testset = cv.dividedata(ex1.train_colors, cvMainFactor)

tree = tc.buildtree(trainset)
tc.printtree(tree)
tc.drawtree(tree, "ex4_original_tree_0_75.jpg")

tc.prune(tree, 0.1)
tc.printtree(tree)
tc.drawtree(tree, "ex4_prune_tree_0_75.jpg")

tree = tc.buildtree(trainset)
print "for " + str(ex2.test_colors[0]) + " predicted branch with " + str(tc.classify(ex2.test_colors[0], tree))
print "for " + str(ex2.test_colors[1]) + " predicted branch with " + str(tc.classify(ex2.test_colors[1], tree))
print "for " + str(ex2.test_colors[2]) + " predicted branch with " + str(tc.mdclassify(ex2.test_colors[2], tree))

print cv.crossvalidate(cv.algf_tree, cv.tree_comparator, trainset, cvfactors=ex3.crossValidationFactors)
