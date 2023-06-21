#importing modules
import numpy as np
import matplotlib.pyplot as plt

#taking two parameters row and col number
def randomImg(row,col):
    image = np.random.randint(0, 256, (row, col))
    plt.matshow(image)
    
#execution and testing
if __name__ == "__main__":
    randomImg(720,1080)
