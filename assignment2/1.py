import cv2
import numpy

org = cv2.imread("inputq1.jpeg")
trn = cv2.imread("transformed.jpeg")
org = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
trn = cv2.cvtColor(trn, cv2.COLOR_BGR2GRAY)

img=org.copy()
for i in range(org.shape[0]):
	for j in range(org.shape[1]):
		if(img[i][j] > 105 and img[i][j] < 164):
			img[i][j] = 32
blur = cv2.GaussianBlur(img,(9,9),0)

cv2.imwrite("outputq1.jpeg",blur)
