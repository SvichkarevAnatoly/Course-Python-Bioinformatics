import numpy
import random

from sklearn.tree import DecisionTreeRegressor

# Build a simple data set with y = x + random
nPoints = 1000

# x values for plotting
xPlot = [(float(i) / float(nPoints) - 0.5) for i in range(nPoints + 1)]

# x needs to be list of lists.
x = [[s] for s in xPlot]

# y (labels) has random noise added to x-value
# set seed
random.seed(1)
y = [s + numpy.random.normal(scale=0.1) for s in xPlot]

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
    idxBag = []
    for i in range(nBagSamples):
        idxBag.append(random.choice(range(len(xTrain))))
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
        prediction.append(sum([predList[i][iPred] for i in range(iModels + 1)]) / (iModels + 1))
    allPredictions.append(prediction)
    errors = [(yTest[i] - prediction[i]) for i in range(len(yTest))]
    mse.append(sum([e * e for e in errors]) / len(yTest))

nModels = [i + 1 for i in range(len(modelList))]

print('Minimum MSE')
print(min(mse))
