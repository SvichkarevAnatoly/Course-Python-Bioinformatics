import random

import exercise1 as ex1
import crossvalidation as cv

random.seed(0)
crossValidationFactors = [0.95, 0.85, 0.75, 0.5]

print cv.crossvalidate(cv.algf_tree, cv.tree_comparator, ex1.train_colors, cvfactors=crossValidationFactors)
