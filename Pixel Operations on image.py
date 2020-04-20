#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 as cv
import numpy as np


# In[3]:


img= cv.imread('hazard10.jpg')
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()


# In[4]:


#row columns and channels
print('The Shape of image is : ')
print(img.shape)
#total number of array elements in the image
print('The size of image is : ')
print(img.size)

print('The datatype of pixel values in the image is : ')
print(img.dtype)


# In[5]:


#accessing a pixel value BGR image
px= img[100,100]
print('value of pixel at 100x100 is ')
print(px)


# In[6]:


blue= img[100,100,0]
print('blue value of pixel at 100x100 is ')
print(blue)


# In[7]:


#changing color at 100x100

img[100,100]=[255,255,255]

cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




