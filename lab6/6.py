import cv2
import math
import numpy

img = cv2.imread("img.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#1
output = cv2.boxFilter(imgray,0,(5,5))
cv2.imshow('output',output)
cv2.imwrite("boxFilter.jpg",output)

#2
output1=cv2.GaussianBlur(imgray,(5,5),0)
cv2.imshow('output1',output1)
cv2.imwrite("GaussianBlur.jpg",output1)
cv2.waitKey(0)
cv2.destroyAllWindows()