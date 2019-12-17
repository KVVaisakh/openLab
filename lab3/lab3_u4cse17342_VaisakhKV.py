import cv2

#1
img=cv2.imread("ff_disney5_f.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#2
s="panda_images/panda"
avimg=cv2.imread("panda_images/panda01.jpg")
for i in range(2,26):
	if i<=9:
		temp=s+"0"+str(i)+".jpg"
	else:
		temp=s+str(i)+".jpg"
	img=cv2.imread(temp)
	avimg=cv2.addWeighted(avimg,1-1/i,img,1/i,0)

cv2.imshow("img",avimg)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#3b
import numpy
import math 

img =cv2.imread("vaishak.jpg")
dim = img.shape

a=math.pi/4
imgt= numpy.zeros((int((dim[0]+dim[1])*math.cos(a)),int((dim[0]+dim[1])*math.sin(a)),3), numpy.uint8)

mat=numpy.array([[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]])
pos=numpy.zeros((dim[0]*dim[1],2), numpy.uint16)

k=0
for i in range(dim[0]):
	for j in range(dim[1]):
		pos[k]=[i,j]
		k+=1

newPos=numpy.dot(pos,mat)
newPos=newPos.astype(int)

minx=newPos.min(axis=0)
for i in range(k):
	# newPos[i][0]+=(-minx[0])
	newPos[i][1]+=(-minx[1])
	k-=1

k=0
for i in range(dim[0]):
	for j in range(dim[1]):
		imgt[newPos[k][0]][newPos[k][1]]=img[i][j]
		k+=1

cv2.imshow("img",imgt)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#3a
import numpy

img =cv2.imread("vaishak.jpg")
dim = img.shape
print(dim)

imgt= numpy.zeros((max(dim[0],dim[1]),max(dim[0],dim[1]),3), numpy.uint8)
print(imgt.shape)

for i in range(dim[0]):
	for j in range(dim[1]):
		imgt[(dim[1]-j+i)//2][(i+j)//2]=img[i][j]

cv2.imshow("img",imgt)
cv2.waitKey(5000)
cv2.destroyAllWindows()
