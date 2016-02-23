import sys
import code5 as c
from random import Random


def read_training_set(file_name):
    with open(file_name, 'r') as ts_file:
        parse_line = lambda l: tuple(l.strip().split())
        return map(parse_line, ts_file.readlines())


def train_and_predict(activation_func="th"):
    rand = Random(0)
    nn = c.NeuralNet(rand, activation_func)

    sys.stdout.write('Train: ')
    nn.train(big_training_set, 10)
    sys.stdout.write('done\n')
    sys.stdout.write('Predict: ')
    predictedClass = nn.predict(testSeq)
    sys.stdout.write('done\n')
    print("Test prediction: %s" % predictedClass)


sys.stdout.write('Read training set: ')
big_training_set = read_training_set("SecondStructureTrainData.txt")
sys.stdout.write('done\n')

testSeq = 'DLLSA'

train_and_predict()
train_and_predict("logistic")
