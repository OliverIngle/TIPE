import cv2
import numpy as np
import matplotlib.pyplot as plt

class Graphique:
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot()
    line = ax.imshow()

    def __init__(self, x , y, name):
        self.name = name
        self.xsize = x
        self.ysize = y
        self.image = np.zeros((x, y, 3), np.uint8)

    def update(self):
        plt.imshow(self.image)
        plt.draw()
        plt.clf()

        return

    def setcolor(self, r, g, b):
        self.image[:] = (r, g, b)

    def setpixel(self, x, y, r, g, b):
        self.image[x, y] = (r, g, b)
    
    def live(self):
        return

    def show(self):
        plt.imshow(self.image)
        plt.draw()
        plt.clf()
