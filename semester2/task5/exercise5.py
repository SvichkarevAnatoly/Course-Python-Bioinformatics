import random

import example as e
import exercise1 as ex1
import exercise2 as ex2
import crossvalidation as cv

print "===Entropy==="
print "===ex1==="
tree = e.buildtree(ex1.train_colors)
e.printtree(tree)
print "===prune==="
e.prune(tree, 0.1)
e.printtree(tree)

print "===ex2==="
tree = e.buildtree(ex1.train_colors)
print "for " + str(ex2.test_colors[0]) + " predicted branch with " + str(e.classify(ex2.test_colors[0], tree))
print "for " + str(ex2.test_colors[1]) + " predicted branch with " + str(e.classify(ex2.test_colors[1], tree))
print "for " + str(ex2.test_colors[2]) + " predicted branch with " + str(e.mdclassify(ex2.test_colors[2], tree))

print "===ex3 - ex4==="
random.seed(0)
crossValidationFactors = [0.95, 0.85, 0.75, 0.5]
print cv.crossvalidate(cv.algf_tree, cv.tree_comparator, ex1.train_colors, cvfactors=crossValidationFactors)

print
print "======================================================================="
print "===Gini Impurity==="
print "===ex1==="
tree = e.buildtree(ex1.train_colors, scoref=e.giniimpurity)
e.printtree(tree)
print "===prune==="
e.prune(tree, 0.1)
e.printtree(tree)

print "===ex2==="
tree = e.buildtree(ex1.train_colors, scoref=e.giniimpurity)
print "for " + str(ex2.test_colors[0]) + " predicted branch with " + str(e.classify(ex2.test_colors[0], tree))
print "for " + str(ex2.test_colors[1]) + " predicted branch with " + str(e.classify(ex2.test_colors[1], tree))
print "for " + str(ex2.test_colors[2]) + " predicted branch with " + str(e.mdclassify(ex2.test_colors[2], tree))

print "===ex3 - ex4==="
random.seed(0)
crossValidationFactors = [0.95, 0.85, 0.75, 0.5]
print cv.crossvalidate(cv.algf_tree, cv.tree_comparator,
                       ex1.train_colors,
                       cvfactors=crossValidationFactors, scoref=e.giniimpurity)
