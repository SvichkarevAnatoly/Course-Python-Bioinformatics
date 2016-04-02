from example import kNearestNeighbour

trainSet = [((1.0, 0.0, 0.0), 'warm'),  # red
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
            ]

testSet = [(0.7, 0.7, 0.2),
           (0.1, 0.0, 0.0),
           (0.5, 0.5, 0.5)]
kRange = range(1, 4)

for k in kRange:
    for testCase in testSet:
        predictedClass = kNearestNeighbour(trainSet, testCase, k)
        print("for " + str(testCase) +
              " and k=" + str(k) +
              " predicted class: " + predictedClass)
