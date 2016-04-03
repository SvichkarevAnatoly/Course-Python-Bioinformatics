import random

from example import kNearestNeighbour


def isSameClass(predictedClass, x, cvTestSetWithClasses):
    return predictedClass == [xx[1] for xx in cvTestSetWithClasses if xx[0] == x][0]


def crossValidation(trainSet, crossValidationFactors, kRange, testTimes):
    trainSize = len(trainSet)

    random.seed(0)
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