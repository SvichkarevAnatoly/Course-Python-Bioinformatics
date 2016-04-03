from crossvalidation import crossValidation

crossValidationFactors = [0.95, 0.85, 0.75, 0.5]
kRange = range(1, 4)
testTimes = 10

trainSet = {
    ((1.0, 0.0, 0.0), 'warm'),  # red
    ((0.0, 1.0, 0.0), 'cool'),  # green
    ((0.0, 0.0, 1.0), 'cool'),  # blue
    ((0.0, 1.0, 1.0), 'cool'),  # cyan
    ((1.0, 1.0, 0.0), 'warm'),  # yellow
    ((1.0, 0.0, 1.0), 'warm'),  # magenta
    ((0.0, 0.0, 0.0), 'cool'),  # black
    ((0.5, 0.5, 0.5), 'cool'),  # grey
    ((1.0, 1.0, 1.0), 'cool'),  # white
    ((1.0, 1.0, 0.5), 'warm'),  # light yellow
    ((0.5, 0.0, 0.0), 'warm'),  # maroon
    ((1.0, 0.5, 0.5), 'warm'),  # pink
}

crossValidation(trainSet, crossValidationFactors, kRange, testTimes)
