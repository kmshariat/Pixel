import numpy as np
import matplotlib.pyplot as plt

#give input any random image as a numpy array
image = np.array([
    [0,0,5,0],
    [2,3,0,0],
    [2,0,0,0],
    [4,5,0,0],
    [2,3,4,5]
])

shape = image.shape

#creating a shifted image
newimage = np.zeros(shape)

#vertishift takes the number of pixel shifted vertically 
#to the right as its parameter

def vertishift(m):
    for i in range(shape[0]):
        for j in range(shape[1]):
            newimage[i][j] = image[i][j-m]
    plt.matshow(newimage)
    plt.show()

#horizonshift takes the number of pixel shifted horizontally 
#to the down as its parameter

def horizonshift(n):
    for i in range(shape[0]):
        for j in range(shape[1]):
            newimage[i][j] = image[i-n][j]
    plt.matshow(newimage)
    plt.show()
