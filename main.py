import numpy as np
import matplotlib.pyplot as plt
import imageio

path = ''

exampleImage = imageio.imread('imageName.png')

#length and width of quilt in squares
xSize = 5
ySize = 6

#Squares are each image you uploaded
squaresList = []
sqrSize = squaresList[0].shape[0]
if squaresList[-1].shape[0] < sqrSize:
    sqrSize = squaresList[-1].shape[0]

for i, val in enumerate(squaresList):
    if val.shape != (sqrSize, sqrSize, 3):
        val = np.resize(val, (sqrSize, sqrSize, 3))
        squaresList[i] = val
quilt = []

n = 1
for i in range(int((xSize*ySize))):
    quilt.append(squaresList[0])
    squaresList = (squaresList[-n:] + squaresList[:-n])

quiltArray = np.zeros((xSize*sqrSize, ySize*sqrSize, 3))
for i in range(xSize):
    for m in range(ySize):
        itrI = i*sqrSize
        itrM = m*sqrSize
        quiltArray[itrI:itrI+120, itrM:itrM+120, :] = quilt[i+m][:][:]

print(quiltArray.shape)
quiltArray = quiltArray / quiltArray.max()
#imageio.imsave(path + '/quilt3.png', quiltArray)
plt.imshow(quiltArray)
plt.show()
