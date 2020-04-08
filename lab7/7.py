import cv2
import numpy
from PIL import Image

def mul(img,src,kernal):
	for i in range(0,src.shape[0]):
		for j in range(0,src.shape[1]):
			temp=0
			for k in range(-1,2):
				for l in range(-1,2):
					if(i+k in range(0,src.shape[0]) and j+l in range(0,src.shape[1])):
						temp+=src[i+k][j+l]*kernal[k][l]
					else:
						temp=0
			img[i][j]=temp

	return img

def laplacian(src):
	img = numpy.asarray(src,dtype="int32")
	src = numpy.asarray(src,dtype="int32")
	kernal = numpy.array([[0,1,0],[1,-4,1],[0,1,0]])

	img=mul(img,src,kernal)

	return img

def sobel(src):
	img = numpy.asarray(src,dtype="int32")
	img2 = numpy.asarray(src,dtype="int32")
	src = numpy.asarray(src,dtype="int32")
	kernal = numpy.array([[1,2,1],[0,0,0],[-1,-2,-1]])
	kernalt = kernal.T
	img = mul(img,src,kernal)
	img2= mul(img2,src,kernalt)
	
	return img,img2

img = cv2.imread("img.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#1
lap = laplacian(imgray)

#2
sob = sobel(imgray)

Image.fromarray(lap).show()
Image.fromarray(sob[0]).show()
Image.fromarray(sob[1]).show()

cv2.imwrite("laplacian.jpg",lap)
cv2.imwrite("sobel1.jpg",sob[0])
cv2.imwrite("sobel2.jpg",sob[1])
