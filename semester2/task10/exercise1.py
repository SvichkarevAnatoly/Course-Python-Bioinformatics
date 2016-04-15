import numpy

import matplotlib.pyplot as plot
from sklearn import ensemble, tree
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

data = open('glass.data.csv')

# arrange data into list for labels and list of lists for attributes
xList = []
for line in data:
    # split on comma
    row = line.strip().split(",")
    xList.append(row)

glassNames = numpy.array(['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type'])

# Separate attributes and labels
xNum = []
labels = []

for row in xList:
    labels.append(row.pop())
    l = len(row)
    # eliminate ID
    attrRow = [float(row[i]) for i in range(1, l)]
    xNum.append(attrRow)

# number of rows and columns in x matrix
nrows = len(xNum)
ncols = len(xNum[1])

# Labels are integers from 1 to 7 with no examples of 4.
# gb requires consecutive integers starting at 0
newLabels = []
labelSet = set(labels)
labelList = list(labelSet)
labelList.sort()
nlabels = len(labelList)
for l in labels:
    index = labelList.index(l)
    newLabels.append(index)

# Drawing 30% test sample may not preserve population proportions
# stratified sampling by labels.
xTemp = [xNum[i] for i in range(nrows) if newLabels[i] == 0]
yTemp = [newLabels[i] for i in range(nrows) if newLabels[i] == 0]
xTrain, xTest, yTrain, yTest = train_test_split(xTemp, yTemp, test_size=0.30, random_state=531)
for iLabel in range(1, len(labelList)):
    # segregate x and y according to labels
    xTemp = [xNum[i] for i in range(nrows) if newLabels[i] == iLabel]
    yTemp = [newLabels[i] for i in range(nrows) if \
             newLabels[i] == iLabel]

    # form train and test sets on segregated subset of examples
    xTrainTemp, xTestTemp, yTrainTemp, yTestTemp = train_test_split(
        xTemp, yTemp, test_size=0.30, random_state=531)

    # accumulate
    xTrain = numpy.append(xTrain, xTrainTemp, axis=0)
    xTest = numpy.append(xTest, xTestTemp, axis=0)
    yTrain = numpy.append(yTrain, yTrainTemp, axis=0)
    yTest = numpy.append(yTest, yTestTemp, axis=0)

missCLassError = []
nTreeList = range(50, 2000, 50)
depth = 1
for iTrees in nTreeList:
    maxFeat = 4  # try tweaking
    glassRFModel = ensemble.RandomForestClassifier(n_estimators=iTrees,
                                                   max_depth=depth, max_features=maxFeat,
                                                   oob_score=False, random_state=531)

    glassRFModel.fit(xTrain, yTrain)
    # Accumulate auc on test set
    prediction = glassRFModel.predict(xTest)
    correct = accuracy_score(yTest, prediction)

    missCLassError.append(1.0 - correct)

print "Missclassification Error for max_depth = " + str(depth)
print(missCLassError[-1])

# generate confusion matrix
pList = prediction.tolist()
confusionMat = confusion_matrix(yTest, pList)
print('')
print("Confusion Matrix")
print(confusionMat)

# plot training and test errors vs number of trees in ensemble
plot.plot(nTreeList, missCLassError)
plot.xlabel('Number of Trees in Ensemble')
plot.ylabel('Missclassification Error Rate')
# plot.show()
plot.savefig("mer" + str(depth) + "depth.png")
plot.close()

# Plot feature importance
featureImportance = glassRFModel.feature_importances_

# normalize by max importance
featureImportance = featureImportance / featureImportance.max()

# plot variable importance
idxSorted = numpy.argsort(featureImportance)
barPos = numpy.arange(idxSorted.shape[0]) + .5
plot.barh(barPos, featureImportance[idxSorted], align='center')
plot.yticks(barPos, glassNames[idxSorted])
plot.xlabel('Variable Importance')
# plot.show()
plot.savefig("varImp" + str(depth) + "depth.png")

# save first 2 tree
with open("tree1Ex1.dot", 'w') as f1:
    f1 = tree.export_graphviz(glassRFModel.estimators_[0], out_file=f1)

with open("tree2Ex1.dot", 'w') as f2:
    f2 = tree.export_graphviz(glassRFModel.estimators_[1], out_file=f2)
