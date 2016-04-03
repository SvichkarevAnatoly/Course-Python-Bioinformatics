from numpy import random

from support import crossValidation

crossValidationFactors = [0.95, 0.85, 0.75, 0.5]
kRange = range(1, 4)
testTimes = 10

spread = 0.12
means = [(0.0, 0.0), (1.0, 1.0), (1.0, 0.0)]
sizeDims = (100, 2)

random.seed(0)
data = [
    (random.normal(means[0], spread, sizeDims), "A"),
    (random.normal(means[1], spread, sizeDims), "B"),
    (random.normal(means[2], spread, sizeDims), "C")
]

trainSet = set()
for classData in data:
    classLabel = classData[1]
    for vector in classData[0]:
        tupleVector = ()
        for x in vector:
            tupleVector = tupleVector + (float(x),)
        trainSet.add((tupleVector, classLabel))

crossValidation(trainSet, crossValidationFactors, kRange, testTimes)
