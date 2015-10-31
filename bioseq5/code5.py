from numpy import array, zeros
from numpy import random, sum
from numpy import tanh, ones, append


class NeuralNet(object):
    @staticmethod
    def convertSeqToVector(seq, indexDict):
        numLetters = len(indexDict)
        vector = [0.0] * len(seq) * numLetters

        for pos, letter in enumerate(seq):
            index = pos * numLetters + indexDict[letter]
            vector[index] = 1.0

        return vector

    def __init__(self):
        aminoAcids = 'ACDEFGHIKLMNPQRSTVWY'
        self.aaIndexDict = {x: i for i, x in enumerate(aminoAcids)}
        self.ssCodes = 'HCE'
        self.ssIndexDict = {x: i for i, x in enumerate(self.ssCodes)}

    def train(self, data):
        self.trainingData = [(self.convertSeqToVector(seq, self.aaIndexDict),
                              self.convertSeqToVector(ss, self.ssIndexDict))
                             for seq, ss in data]

        self.neuralNetTrain(3, 1000)

    def predict(self, seq):
        testVec = self.convertSeqToVector(seq, self.aaIndexDict)
        testArray = array([testVec, ])
        _, _, sOut = self.neuralNetPredict(testArray)
        index = sOut.argmax()
        return self.ssCodes[index]

    def neuralNetTrain(self, numHid, steps=100, rate=0.5, momentum=0.2):
        numInp = len(self.trainingData[0][0])
        numOut = len(self.trainingData[0][1])
        numInp += 1

        self.wMatrixIn = random.random((numInp, numHid)) - 0.5
        self.wMatrixOut = random.random((numHid, numOut)) - 0.5

        cInp = zeros((numInp, numHid))
        cOut = zeros((numHid, numOut))

        for step in range(steps):
            random.shuffle(self.trainingData)  # Important
            error = 0.0

            for inputs, knownOut in self.trainingData:
                sigIn, sigHid, sigOut = self.neuralNetPredict(inputs)

                diff = knownOut - sigOut
                error += sum(diff * diff)

                gradient = ones(numOut) - (sigOut * sigOut)
                outAdjust = gradient * diff

                diff = sum(outAdjust * self.wMatrixOut, axis=1)
                gradient = ones(numHid) - (sigHid * sigHid)
                hidAdjust = gradient * diff

                # update output
                change = outAdjust * sigHid.reshape(numHid, 1)
                self.wMatrixOut += (rate * change) + (momentum * cOut)
                cOut = change

                # update input
                change = hidAdjust * sigIn.reshape(numInp, 1)
                self.wMatrixIn += (rate * change) + (momentum * cInp)
                cInp = change

    def neuralNetPredict(self, inputVec):
        signalIn = append(inputVec, [1.0])  # input layer

        prod = signalIn * self.wMatrixIn.T
        sums = sum(prod, axis=1)
        signalHid = tanh(sums)  # hidden layer

        prod = signalHid * self.wMatrixOut.T
        sums = sum(prod, axis=1)
        signalOut = tanh(sums)  # output layer

        return signalIn, signalHid, signalOut