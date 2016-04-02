from example import kNearestNeighbour
import random

random.seed(0)

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

trainSize = len(trainSet)
crossValidationSizes = [int(trainSize * f) for f in crossValidationFactors]


def isSameClass(predictedClass, x, cvTestSetWithClasses):
    return predictedClass == [xx[1] for xx in cvTestSetWithClasses if xx[0] == x][0]


for k in kRange:
    for cvFactor in crossValidationFactors:
        cvSize = int(trainSize * cvFactor)
        counter = 0
        for i in range(testTimes):
            cvTrainSet = set(random.sample(trainSet, cvSize))
            cvTestSetWithClasses = trainSet - cvTrainSet
            cvTestSet = {x[0] for x in cvTestSetWithClasses}
            for x in cvTestSet:
                predictedClass = kNearestNeighbour(list(cvTrainSet), x, k)
                if isSameClass(predictedClass, x, cvTestSetWithClasses):
                    counter += 1
        checkFactor = trainSize - cvSize
        print("for " + str(int(cvFactor * 100)) + "% with k=" + str(k) + ": " +
              str(counter) + "/" + str(testTimes * checkFactor) +
              " = " + str(int((counter * 100) / (checkFactor * testTimes)))) + "%"
