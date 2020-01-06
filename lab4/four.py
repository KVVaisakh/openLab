import cv2
import numpy
import math 

#1
img =cv2.imread("pexels.jpeg")
a=-math.pi/4

dim = img.shape
imgt= numpy.zeros((int(abs(dim[0]*math.cos(a))+abs(dim[1]*math.sin(a))),int(abs(dim[0]*math.sin(a))+abs(dim[1]*math.cos(a))),3), numpy.uint8)

dim = imgt.shape
imgf= numpy.zeros((int(abs(dim[0]*math.cos(a))+abs(dim[1]*math.sin(a))),int(abs(dim[0]*math.sin(a))+abs(dim[1]*math.cos(a))),3), numpy.uint8)

org=(imgf.shape-dim)//2

mat=numpy.array([[math.cos(-a),-math.sin(-a)],[math.sin(-a),math.cos(-a)]])
pos=numpy.zeros((dim[0]*dim[1],2), numpy.uint16)

k=0
for i in range(dim[0]):
	for j in range(dim[1]):
		pos[k]=[i,j]
		k+=1

newPos=numpy.dot(pos,mat)




minx=newPos.min(axis=0)
for i in range(k):
	newPos[i][0]+=(-minx[0])
	newPos[i][1]+=(-minx[1])
	k-=1

k=0
for i in range(dim[0]):
	for j in range(dim[1]):
		imgt[newPos[k][0]][newPos[k][1]]=img[i][j]
		k+=1

cv2.imshow("img",imgt)
cv2.waitKey(0)
cv2.destroyAllWindows()
