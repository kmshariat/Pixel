#importing modules
import random
import numpy as np
import matplotlib.pyplot as plt

#taking two parameters row and col number
def randomImg(row,col):
    image = np.zeros((row,col))
    for i in range(row):
        for j in range(col):
            image[i][j] = random.randint(0,255) #pixel value will range from 0 to 255
    plt.matshow(image)
    
#execution and testing
if __name__ == "__main__":
    randomImg(255,255)
