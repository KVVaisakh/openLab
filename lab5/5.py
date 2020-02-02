import cv2
import math
import numpy

img = cv2.imread("histogram.png")
#1
imgtemp=img
img2=img
dim=img.shape
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgtemp=cv2.cvtColor(imgtemp, cv2.COLOR_BGR2GRAY)
cv2.imwrite("original.jpg",img)
# a
intensity=[]
for i in range(256):
	intensity.append(0)
for i in img:
	for j in i:
		intensity[j]=intensity[j]+1
for i in range(1,256):
	intensity[i]=intensity[i-1]+intensity[i]
for i in range(256):
	intensity[i]=round((255*intensity[i])/intensity[255])
for i in range(dim[0]):
	for j in range(dim[1]):
		img[i][j]=intensity[img[i][j]]
cv2.imwrite("equilised.jpg",img)
# b
imgAut=cv2.equalizeHist(imgtemp)
cv2.imwrite("equilisedAutomated.jpg",imgAut)

# 2
for i in img2:
	for j in i:
		j[0]=0
		j[1]=0
cv2.imwrite("warmed.jpg",img2)