import sys
import code5 as c


def read_training_set(file_name):
    with open(file_name, 'r') as ts_file:
        return map(lambda l: tuple(l.strip().split()), ts_file.readlines())

nn = c.NeuralNet()

sys.stdout.write('Read training set: ')
big_training_set = read_training_set("SecondStructureTrainData.txt")
sys.stdout.write('done\n')

sys.stdout.write('Train: ')
nn.train(big_training_set, 10)
sys.stdout.write('done\n')

sys.stdout.write('Predict: ')
testSeq = 'DLLSA'
predictedClass = nn.predict(testSeq)
sys.stdout.write('done\n')

print("Test prediction: %s" % predictedClass)
