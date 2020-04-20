import cv2 as cv
import numpy as np

img = cv.imread('hazard10.jpg')
img1 = cv.imread('hazard10.jpg',0)

cv.imshow('image',img) #First window name second image
cv.imshow('image1',img1)
key =cv.waitKey(0) #returns unicode value of the keypress

if key==27:
    cv.destroyAllWindows()
if key==ord('s'):
    cv.imwrite('greyhazard10.jpg',img1)
