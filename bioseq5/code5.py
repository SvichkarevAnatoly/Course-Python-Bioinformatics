from numpy import sum, array, zeros, tanh, ones, append
from scipy.special import expit
from sys import stdout
from random import Random


class NeuralNet(object):
    @staticmethod
    def convertSeqToVector(seq, indexDict):
        numLetters = len(indexDict)
        vector = [0.0] * len(seq) * numLetters

        for pos, letter in enumerate(seq):
            index = pos * numLetters + indexDict[letter]
            vector[index] = 1.0

        return vector

    @staticmethod
    def activation_function(func_name):
        if func_name == "th":
            return tanh
        if func_name == "logistic":
            return expit

    def __init__(self, rand=Random(), act_func="th"):
        self.rand = rand
        self.activation_func = self.activation_function(act_func)

        aminoAcids = 'ACDEFGHIKLMNPQRSTVWY'
        self.aaIndexDict = {x: i for i, x in enumerate(aminoAcids)}
        self.ssCodes = 'HCE'
        self.ssIndexDict = {x: i for i, x in enumerate(self.ssCodes)}

    def train(self, data, steps=1000):
        self.trainingData = [(self.convertSeqToVector(seq, self.aaIndexDict),
                              self.convertSeqToVector(ss, self.ssIndexDict))
                             for seq, ss in data]

        self.neuralNetTrain(3, steps)

    def predict(self, seq):
        testVec = self.convertSeqToVector(seq, self.aaIndexDict)
        testArray = array([testVec, ])
        _, _, sOut = self.neuralNetPredict(testArray)
        index = sOut.argmax()
        print sOut
        return self.ssCodes[index]

    def neuralNetTrain(self, numHid, steps, rate=0.5, momentum=0.2):
        numInp = len(self.trainingData[0][0])
        numOut = len(self.trainingData[0][1])
        numInp += 1

        self.wMatrixIn = self.random_matrix(numInp, numHid) - 0.5
        self.wMatrixOut = self.random_matrix(numHid, numOut) - 0.5

        cInp = zeros((numInp, numHid))
        cOut = zeros((numHid, numOut))

        for step in range(steps):
            stdout.write(str(step) + ' ')
            stdout.flush()
            self.rand.shuffle(self.trainingData)  # Important
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
        stdout.write('\n')

    def neuralNetPredict(self, inputVec):
        signalIn = append(inputVec, [1.0])  # input layer

        prod = signalIn * self.wMatrixIn.T
        sums = sum(prod, axis=1)
        signalHid = self.activation_func(sums)  # hidden layer

        prod = signalHid * self.wMatrixOut.T
        sums = sum(prod, axis=1)
        signalOut = self.activation_func(sums)  # output layer

        return signalIn, signalHid, signalOut

    def random_matrix(self, len1, len2):
        return array([[self.rand.random() for _ in range(len2)]
                      for _ in range(len1)])
