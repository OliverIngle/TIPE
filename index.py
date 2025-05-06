from moteurimage import *

img = Graphique(10, 10, "World")
img.setcolor(255, 0, 0)
img.setpixel(5, 5, 0, 0, 0)

img.show()

_ = input()
img.setpixel(5, 1, 255, 255, 255)
img.update()
