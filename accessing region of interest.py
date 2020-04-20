import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('hazard10.jpg')
img1 = cv.imread('hazard10.jpg')
cv.imshow('Image',img)

#use matplotlib to find pixel range of ball
##
##img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
##plt.imshow(img_RGB)
##plt.axis('off')
##
##plt.show()

ball =img[235:295,465:530]
ball1 = img[235:295,465:530]
#convert the ball region to white

ball1=([255,255,255])
img1[235:295,465:530]=ball1

cv.imshow('Image1',img1)

img[235:295,555:620]=ball

cv.imshow('Image2',img)

cv.waitKey(0)
cv.destroyAllWindows()




