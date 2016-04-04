import numpy

from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
import matplotlib.pyplot as plot

a = 1
b = 2

# set seed
numpy.random.seed(1)

nPointsList = range(100, 1001, 100)
for nPoints in nPointsList:
    # x values for plotting
    xPlot = [(float(i) / float(nPoints) - 0.5) for i in range(nPoints + 1)]

    # x needs to be list of lists.
    x = [[s] for s in xPlot]

    # y (labels) has random noise added to x-value
    # Build a simple data set with y = x + random
    y = [a + b * s * s + numpy.random.normal(scale=0.1) for s in xPlot]

    nrow = len(x)

    # fit trees with several different values for depth and use x-validation to see which works best.
    depthList = [1, 2, 3, 4, 5, 6, 7]

    xvalMSE = []
    for iDepth in depthList:
        oosErrors = 0.0
        # Define test and training index sets
        idxTest = [a for a in range(nrow) if a % 2 == 0]
        idxTrain = [a for a in range(nrow) if a % 2 != 0]

        # Define test and training attribute and label sets
        xTrain = [x[r] for r in idxTrain]
        xTest = [x[r] for r in idxTest]

        yTrain = [y[r] for r in idxTrain]
        yTest = [y[r] for r in idxTest]

        # train tree of appropriate depth and accumulate out of sample (oos) errors
        treeModel = DecisionTreeRegressor(max_depth=iDepth)
        treeModel.fit(xTrain, yTrain)

        # save last tree
        if iDepth == depthList[2] and nPoints == nPointsList[-1]:
            yHat = treeModel.predict(xTrain)
            plot.figure()
            plot.plot(xTrain, yTrain, label='True y')
            plot.plot(xTrain, yHat, label='Tree Prediction ', linestyle='--')
            plot.legend(bbox_to_anchor=(1, 0.2))
            plot.axis('tight')
            plot.xlabel('x')
            plot.ylabel('y')
            plot.savefig('trainsetEx2.png')

            # draw the tree
            with open("treeEx2.dot", 'w') as f:
                f = tree.export_graphviz(treeModel, out_file=f)

        treePrediction = treeModel.predict(xTest)
        error = [yTest[r] - treePrediction[r] for r in range(len(yTest))]

        # accumulate squared errors
        oosErrors += sum([e * e for e in error])

        # average the squared errors and accumulate by tree depth
        mse = oosErrors / (nrow * 0.5)
        xvalMSE.append(mse)

    print "for n=" + str(nPoints) + \
          " MSEs=" + "[%s]" % ", ".join("%.3f" % x for x in xvalMSE)
