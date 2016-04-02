from PIL import Image
from numpy import array, dot, dstack, log, log2, sqrt, transpose, uint8, zeros

def imageToPixmapRGB(img):
  
  img2 = img.convert('RGB')
  w, h = img2.size  
  data = img2.getdata()

  pixmap = array(data, float)
  pixmap = pixmap.reshape((h,w,3))
  
  return pixmap


def getJoinPair(distMatrix):

  n = len(distMatrix)

  minQ = None
  joinPair = None

  for i in range(n-1):
    sumRow = sum(distMatrix[i])
  
    for j in range(i+1, n):
      sumCol = sum(distMatrix[j])
    
      dist = distMatrix[i][j]
      q = (n-2)*dist - sumRow - sumCol
      
      if (minQ is None) or (q < minQ):
        minQ = q
        joinPair = [i,j]

  return joinPair

def getDistToJunction(distMatrix, i, j):
  
  n = len(distMatrix)
  row = distMatrix[i]
  column = distMatrix[j]
 
  dist = distMatrix[i][j] + (sum(row)-sum(column))/(n-2)
  dist *= 0.5

  return dist


def neighbourJoinTree(distMatrix):
 
  joinOrder = []
  n = len(distMatrix)
  tree = list(range(n))  # do not need list() in Python 2
  
  while n > 2:

    x, y = getJoinPair(distMatrix)

    node = (tree[x], tree[y])
    joinOrder.append(node)
    tree.append(node)

    del tree[y]
    del tree[x]

    distX = getDistToJunction(distMatrix, x, y)
    distY = getDistToJunction(distMatrix, y, x)
  
    distMatrix.append([0] * (n+1))

    for i in range(n):
      if i not in (x,y):

        dist = (distMatrix[x][i]-distX) + (distMatrix[y][i]-distY)
        dist *= 0.5
  
        distMatrix[i].append(dist)
        distMatrix[n][i] = dist

    del distMatrix[y]
    del distMatrix[x]
  
    for row in distMatrix:
      del row[y]
      del row[x]

    n -= 1

  tree = tuple(tree)
  joinOrder.append(tree)
  
  return tree, joinOrder


def neighbourJoinTree(distMatrix):
 
  joinOrder = []
  n = len(distMatrix)
  tree = list(range(n))  # do not need list() in Python 2
  
  while n > 2:

    x, y = getJoinPair(distMatrix)

    node = (tree[x], tree[y])
    joinOrder.append(node)
    tree.append(node)

    del tree[y]
    del tree[x]

    distX = getDistToJunction(distMatrix, x, y)
    distY = getDistToJunction(distMatrix, y, x)
  
    distMatrix.append([0] * (n+1))

    for i in range(n):
      if i not in (x,y):

        dist = (distMatrix[x][i]-distX) + (distMatrix[y][i]-distY)
        dist *= 0.5
  
        distMatrix[i].append(dist)
        distMatrix[n][i] = dist

    del distMatrix[y]
    del distMatrix[x]
  
    for row in distMatrix:
      del row[y]
      del row[x]

    n -= 1

  tree = tuple(tree)
  joinOrder.append(tree)
  
  return tree, joinOrder





################################################

def loadDataMatrix(fileName, sampleName, default=0.0):

  fileObj = open(fileName, 'r')
  
  rows = set()
  cols = set()
  dataDict = {}

  for line in fileObj:
    row, col, value = line.split()

    if row not in dataDict:
      dataDict[row] = {}

    if col in dataDict[row]:
      print('Repeat entry found for element %d, %d' % (row, col))
      continue

    dataDict[row][col] = float(value)
    
    rows.add(row)
    cols.add(col)
  
  rows = sorted(rows)
  cols = sorted(cols)
  
  nRows = len(rows)
  nCols = len(cols)

  dataMatrix = zeros((nRows, nCols), float)

  for i, row in enumerate(rows):
    for j, col in enumerate(cols):
      value = dataDict[row].get(col, default)
      dataMatrix[i,j] = value
  
  fileObj.close()

  return Microarray(sampleName, dataMatrix, rows, cols)



def loadArrayImage(fileName, sampleName, nRows, nCols=None):

  if not nCols:
    nCols = nRows
  
  dataMatrix = zeros((3, nRows, nCols), float)
  
  img = Image.open(fileName) # Auto file type
  pixmap = imageToPixmapRGB(img)
  
  height, width, depth = pixmap.shape
  
  dx = width/float(nCols)
  dy = height/float(nRows)
  xSize = 1 + (width-1)//nCols
  ySize = 1 + (height-1)//nRows

  for row in range(nRows):
    yStart = int(row*dy)
    yEnd   = yStart + ySize

    for col in range(nCols):
      xStart = int(col*dx)
      xEnd   = xStart + xSize

      elementData = pixmap[yStart:yEnd,xStart:xEnd]
      dataMatrix[:,row, col] = elementData.sum(axis=(0,1))

  
  return Microarray(sampleName, dataMatrix)


class Microarray(object):

  def __init__(self, name, data, rowData=None, colData=None):

   
    self.name = name 
    data = array(data)

    shape = data.shape
    
    if len(shape) == 3:
      self.nChannels, self.nRows, self.nCols = shape
    
    elif len(shape) == 2:
      self.nRows, self.nCols = shape
      self.nChannels = 1
      data = array([data])

    else:
      raise Exception('Array data must have either 2 or 3 axes.')  

    self.data = data
    self.origData = array(data)
  
    self.rowData = rowData or range(self.nRows)
    self.colData = colData or range(self.nCols)

  def resetData(self):
  
    self.data = array(self.origData)
    self.nChannels = len(self.data)

  def writeData(self, fileName, separator=' '):
  
    fileObj = open(fileName, 'w')
    
    for i in range(self.nRows):
      rowName = str(self.rowData[i])
      
      for j in range(self.nCols):
        colName = str(self.colData[j])

        values = self.data[:,i,j]

        lineData = [rowName, colName]
        lineData += ['%.3f' % (v,) for v in values]
        
        line = separator.join(lineData)
        fileObj.write(line + '\n')

  def makeImage(self, squareSize=20, channels=None):
    
    minVal = self.data.min()
    maxVal = self.data.max() 
    dataRange = maxVal - minVal  

    adjData = (self.data - minVal) * 255 / dataRange
    adjData = array(adjData, uint8)
   
    if not channels:
      if self.nChannels == 1:
        channels = (0,0,0) # Greyscale
      else:
        channels = list(range(self.nChannels))[:3]

    pixmap = []
    for i in channels:
      if i is None:
        pixmap.append(zeros((self.nRows, self.nCols), uint8))
      else:
        pixmap.append(adjData[i])
        
    while len(pixmap) < 3:
      pixmap.append(zeros((self.nRows, self.nCols), uint8))
     
    pixmap = dstack(pixmap)
    img = Image.fromarray(pixmap, 'RGB')

    width = self.nCols * squareSize
    height = self.nRows * squareSize
    img = img.resize((width, height))
    
    return img

  def clipBaseline(self, threshold=None, channels=None, defaultProp=0.2):
    
    if not channels:
      channels = range(self.nChannels)
    
    channels = [tuple(channels)]
    
    maxVal = self.data[channels].max()
    if threshold is None:
      limit = maxVal * defaultProp
    else:
      limit = threshold
    
    boolArray = self.data[channels] < limit
    indices = boolArray.nonzero()
        
    self.data[indices] = limit

    self.data[channels] -= limit
    self.data[channels] *= maxVal / (maxVal-limit)

 
  def normaliseSd(self, scale=1.0): 
    
    for i in range(self.nChannels):
      self.data[i] = self.data[i] * scale / self.data[i].std()


  def normaliseMean(self, scale=1.0):
    
    for i in range(self.nChannels):
      self.data[i] = self.data[i] * scale / self.data[i].mean()


  def centerMean(self):
  
    for i in range(self.nChannels):
      self.data[i] -= self.data[i].mean()


  def normaliseZscore(self):
    
    self.centerMean()
    self.normaliseSd()


  def normaliseMax(self, scale=1.0, perChannel=True):
    
    if perChannel:
      for i in range(self.nChannels):
        self.data[i] = self.data[i] * scale / self.data[i].max()
    
    else:
      self.data = self.data * scale / self.data.max()


  def normaliseRowMax(self, scale=1.0):
  
    for i in range(self.nChannels):
      self.data[i] = self.data[i] * scale / self.data[i].max(axis=1)[:,None]


  def normaliseRowMean(self, scale=1.0):
  
    for i in range(self.nChannels):
      self.data[i] = self.data[i] * scale / self.data[i].mean(axis=1)[:,None]


  def normaliseColMax(self, scale=1.0):
  
    for i in range(self.nChannels):
      self.data[i] = self.data[i] * scale / self.data[i].max(axis=0)

  def normaliseColMean(self, scale=1.0):
  
    for i in range(self.nChannels):
      self.data[i] = self.data[i] * scale / self.data[i].mean(axis=0)
    

  def normaliseRefs(self, rows, cols, scale=1.0, channels=None):
  
    if not channels:
      channels = range(self.nChannels)

    channels = tuple(channels)
    refValues = self.data[channels, rows, cols]
    
    for i in channels:
      self.data[i] = self.data[i] * scale / refValues[i].mean()
    

  def normaliseLogMean(self):

    self.clipBaseline(threshold=0.0)
    for i in range(self.nChannels):
      self.data[i] = log( 1.0 + self.data[i] / self.data[i].mean() )


  def normaliseQuantile(self, refData, channel=0):
    # could be to a different channel
    
    values = self.data[channel].flatten()
    order = values.argsort()
    
    refValues = refData.flatten()
    refValues.sort()

    refSelection = order.argsort()
    values = refValues[refSelection]
 
    self.data[channel] = values.reshape((self.nRows, self.nCols))

    
  def normaliseRowQuantile(self, channel=0):
    
    channelData = self.data[channel]
    
    orders = channelData.argsort(axis=1)
    sortedRows = array(channelData)
    sortedRows.sort(axis=1)
    refValues = sortedRows.mean(axis=0) # average over columns
 
    rows = range(self.nRows)
    self.data[channel,rows,:] = refValues[orders[rows,:].argsort()]


  def checkDataSize(self, channelData):
    
    channelData = array(channelData)
    if channelData.shape != (self.nRows, self.nCols):
      msg = 'Attempt use data of wrong size'
      raise Exception(msg)
  
    return channelData

  def setChannel(self, channelData, index=0):

    channelData = self.checkDataSize(channelData)
    self.data[index] = channelData

  def addChannel(self, channelData):

    from numpy import append
    channelData = self.checkDataSize(channelData)

    self.data = append(self.data, channelData, axis=0)
    self.nChannels += 1

  def swapChannels(self, indexA, indexB):

    self.data[(indexB, indexA)] = self.data[(indexA, indexB)]

  def removeChannel(self, index):

    from numpy import delete     
    if index < self.nChannels:
      self.data = delete(self.data, index, axis=0)

  def combineChannels(self, indexA, indexB, combFunc=None, replace=None):
    
    if not combFunc:
      import operator
      combFunc= operator.add 

    channelData = combFunc(self.data[indexA], self.data[indexB])

    if replace is None:
      self.addChannel(channelData)
      
    else:
      self.setChannel(channelData, replace)

  def __hierarchicalRowCluster(self, dataMatrix):
    

    n = len(dataMatrix[0])
    distanceMatrix = zeros((n, n), float)
    
    for channelData in dataMatrix:
      for i, row in enumerate(channelData):
        diffs = channelData - row
        sqDiffs = diffs * diffs
        sqDists = sqDiffs.sum(axis=1)
        distanceMatrix[i,:] += sqDists

    tree, joinOrder = neighbourJoinTree(distanceMatrix.tolist())

    rowOrder = list(tree)
  
    i  = 0
    while i < len(rowOrder):
    
      while not isinstance(rowOrder[i], int):
        rowOrder[i:i+1] = rowOrder[i]
    
      i += 1
  
    return rowOrder

  def hierarchicalCluster(self):
     
    rows = self.__hierarchicalRowCluster(self.data)

    
    swapped = transpose(self.data, axes=(0,2,1))
    cols = self.__hierarchicalRowCluster(swapped)

    data = self.data[:,rows] # Rearrange
    data = data[:,:,cols]
    
    data = array(data.tolist()) # to fix PIL.Image bug
    
    name = self.name + '-Sorted'
    rowData = [self.rowData[i] for i in rows]
    colData = [self.colData[j] for j in cols]

    sortedArray = Microarray(name, data, rowData, colData)
    
    return sortedArray 

if __name__ == '__main__':
  
  # Load data from an image and write out as text
  
  imgFile = 'RedGreenArray.png'
  rgArray = loadArrayImage(imgFile, 'TwoChannel', 18, 17)
  rgArray.writeData('RedGreenArrayData.txt')
  
  # G-score
  
  def gScore(data1, data2):
    data1 = array(data1) + 1e-3
    data2 = array(data2) + 1e-3

    return data1 * log2(data1/data2)

  rgArray = loadArrayImage(imgFile, 'TwoChannel', 18, 17)
  rgArray.combineChannels(0, 1, combFunc=gScore, replace=2)
  rgArray.makeImage(20, channels=(2,2,2)).save("im-11.png")

  sortedArray = rgArray.hierarchicalCluster()
  sortedArray.makeImage(20).save("im-12.png")

  print('sortedArray.rowData',sortedArray.rowData)
