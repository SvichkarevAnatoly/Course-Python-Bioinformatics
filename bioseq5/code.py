import numpy
from numpy import exp, power, array, zeros, sqrt
from numpy import nonzero, random, abs, sum, dot
from numpy import tanh, ones, append


def neuralNetPredict(inputVec, weightsIn, weightsOut):
    signalIn = append(inputVec, 1.0)  # input layer
    prod = signalIn * weightsIn.T
    sums = sum(prod, axis=1)
    signalHid = tanh(sums)  # hidden layer
    prod = signalHid * weightsOut.T
    sums = sum(prod, axis=1)
    signalOut = tanh(sums)  # output layer
    return signalIn, signalHid, signalOut


def neuralNetTrain(trainData, numHid, steps=100, rate=0.5, momentum=0.2):
    numInp = len(trainData[0][0])
    numOut = len(trainData[0][1])
    numInp += 1
    minError = None
    sigInp = ones(numInp)
    sigHid = ones(numHid)
    sigOut = ones(numOut)
    wInp = random.random((numInp, numHid)) - 0.5
    wOut = random.random((numHid, numOut)) - 0.5
    bestWeightMatrices = (wInp, wOut)

    cInp = zeros((numInp, numHid))
    cOut = zeros((numHid, numOut))
    for x, (inputs, knownOut) in enumerate(trainData):
        trainData[x] = (array(inputs), array(knownOut))
    for step in range(steps):  # xrange in Python 2
        random.shuffle(trainData)  # Important
    error = 0.0
    for inputs, knownOut in trainData:
        sigIn, sigHid, sigOut = neuralNetPredict(inputs, wInp, wOut)
    diff = knownOut - sigOut
    error += sum(diff * diff)
    gradient = ones(numOut) - (sigOut * sigOut)
    outAdjust = gradient * diff
    diff = sum(outAdjust * wOut, axis=1)
    gradient = ones(numHid) - (sigHid * sigHid)
    hidAdjust = gradient * diff
    # update output
    change = outAdjust * sigHid.reshape(numHid, 1)
    wOut += (rate * change) + (momentum * cOut)
    cOut = change
    # update input
    change = hidAdjust * sigIn.reshape(numInp, 1)
    wInp += (rate * change) + (momentum * cInp)
    cInp = change
    if (minError is None) or (error < minError):
        minError = error
    bestWeightMatrices = (wInp.copy(), wOut.copy())
    print("Step: %d Error: %f" % (step, error))
    return bestWeightMatrices


def convertSeqToVector(seq, indexDict):
    numLetters = len(indexDict)
    vector = [0.0] * len(seq) * numLetters
    for pos, letter in enumerate(seq):
        index = pos * numLetters + indexDict[letter]
    vector[index] = 1.0
    return vector


if __name__ == '__main__':
    print("\nFeed-forward neural network sequence training\n")

    seqSecStrucData = [
        ('ADTLL', 'E'),
        ('DTLLI', 'E'),
        ('TLLIL', 'E'),
        ('LLILG', 'E'),
        ('LILGD', 'E'),
        ('ILGDS', 'E'),
        ('LGDSL', 'C'),
        ('GDSLS', 'H'),
        ('DSLSA', 'H'),
        ('SLSAG', 'H'),
        ('LSAGY', 'H'),
        ('SAGYR', 'C'),
        ('AGYRM', 'C'),
        ('GYRMS', 'C'),
        ('YRMSA', 'C'),
        ('RMSAS', 'C')
    ]
    aminoAcids = 'ACDEFGHIKLMNPQRSTVWY'
    aaIndexDict = {}
    for i, aa in enumerate(aminoAcids):
        aaIndexDict[aa] = i
    print("aminoAcids", aminoAcids)
    print("aaIndexDict", aaIndexDict)
    ssIndexDict = {}
    ssCodes = 'HCE'
    for i, code in enumerate(ssCodes):
        ssIndexDict[code] = i
    # Classes
    print("ssCodes", ssCodes)
    print("ssIndexDict", ssIndexDict)
    trainingData = []
    for seq, ss in seqSecStrucData:
        inputVec = convertSeqToVector(seq, aaIndexDict)
    outputVec = convertSeqToVector(ss, ssIndexDict)
    trainingData.append((inputVec, outputVec))
    print("trainingData", seq, ss)
    print("inputVec", inputVec)
    print("outputVec", outputVec)
    wMatrixIn, wMatrixOut = neuralNetTrain(trainingData, 3, 1000)
    print("wMatrixIn", wMatrixIn)
    print("wMatrixOut", wMatrixOut)
    print("\nFeed-forward neural network sequence prediction\n")
    testSeq = 'DLLSA'
    print("testSeq", testSeq)
    testVec = convertSeqToVector(testSeq, aaIndexDict)
    testArray = array([testVec, ])
    print("testVec", testVec)

    print("testArray", testArray)
    sIn, sHid, sOut = neuralNetPredict(testArray, wMatrixIn, wMatrixOut)
    print("sOut", sOut)
    index = sOut.argmax()
    print("Test prediction: %s" % ssCodes[index])
