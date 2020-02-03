import cv2
import math
import numpy

img = cv2.imread("histogram.png")
imgtemp=img
img2=img
#1
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
x=20
for i in img2:
	for j in i:
		if j[2]<(255-x):
			j[2]=j[2]+x
		else:
			j[2]=255
		if j[0]>x:
			j[0]=j[0]-x
		else:
			j[0]=0
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
for i in img2:
	for j in i:
		if j[2]<225:
			j[2]=j[2]+30
		else:
			j[2]=255
cv2.imwrite("warmed.jpg",img2)