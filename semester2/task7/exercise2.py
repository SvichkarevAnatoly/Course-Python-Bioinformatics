import numpy
import random

import matplotlib.pyplot as plot
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree

a = 1
b = 2

# Build a simple data set with y = x + random
nPoints = 1000

# x values for plotting
xPlot = [(float(i) / float(nPoints) - 0.5) for i in range(nPoints + 1)]

# x needs to be list of lists.
x = [[s] for s in xPlot]

# y (labels) has random noise added to x-value
# set seed
numpy.random.seed(1)
random.seed(1)

y = [a + b * s * s + numpy.random.normal(scale=0.1) for s in xPlot]

# take fixed test set 30% of sample
nSample = int(nPoints * 0.30)
idxTest = random.sample(range(nPoints), nSample)
idxTest.sort()
idxTrain = [idx for idx in range(nPoints) if not (idx in idxTest)]

# Define test and training attribute and label sets
xTrain = [x[r] for r in idxTrain]
xTest = [x[r] for r in idxTest]
yTrain = [y[r] for r in idxTrain]
yTest = [y[r] for r in idxTest]

# train a series of models on random subsets of the training data
# collect the models in a list and check error of composite as list grows
# maximum number of models to generate
numTreesMax = 20

# tree depth - typically at the high end
treeDepth = 5

# initialize a list to hold models
modelList = []
predList = []

# number of samples to draw for stochastic bagging
nBagSamples = int(len(xTrain) * 0.5)

for iTrees in range(numTreesMax):
    idxBag = random.sample(range(len(xTrain)), nBagSamples)
    xTrainBag = [xTrain[i] for i in idxBag]
    yTrainBag = [yTrain[i] for i in idxBag]

    modelList.append(DecisionTreeRegressor(max_depth=treeDepth))
    modelList[-1].fit(xTrainBag, yTrainBag)

    # make prediction with latest model and add to list of predictions
    latestPrediction = modelList[-1].predict(xTest)
    predList.append(list(latestPrediction))

# build cumulative prediction from first "n" models
mse = []
allPredictions = []
for iModels in range(len(modelList)):
    # average first "iModels" of the predictions
    prediction = []
    for iPred in range(len(xTest)):
        prediction.append(sum([predList[i][iPred] \
                               for i in range(iModels + 1)]) / (iModels + 1))

    allPredictions.append(prediction)
    errors = [(yTest[i] - prediction[i]) for i in range(len(yTest))]
    mse.append(sum([e * e for e in errors]) / len(yTest))

nModels = [i + 1 for i in range(len(modelList))]

# MSE versus number of trees in Bagging ensemble
plot.plot(nModels, mse)
plot.axis('tight')
plot.xlabel('Number of Models in Ensemble')
plot.ylabel('Mean Squared Error')
plot.ylim((0.0, max(mse)))
# plot.show()
plot.savefig("mseEx2.png")
plot.close()

# Comparison of prediction and actual label as functions of attribute
plot.plot(xTest, allPredictions[0])
plot.plot(xTest, allPredictions[9])
plot.plot(xTest, allPredictions[19])
plot.plot(xTest, yTest, linestyle="--")
plot.axis('tight')
plot.xlabel('x value')
plot.ylabel('Predictions')
# plot.show()
plot.savefig("predictionsEx2.png")
plot.close()

# save first 2 tree
with open("tree1Ex2.dot", 'w') as f1:
    f1 = tree.export_graphviz(modelList[0], out_file=f1)

with open("tree2Ex2.dot", 'w') as f2:
    f2 = tree.export_graphviz(modelList[1], out_file=f2)
