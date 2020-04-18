import cv2
import numpy

org = cv2.imread("logndlinear.jpg",0)
m=numpy.max(org)				# m[1] will have max pixelel value
c=255/(numpy.log(1+m))
logImage = numpy.array(c*numpy.log(1+org),dtype=numpy.uint8)

cv2.imwrite("logq2.jpg",logImage)

def piecewise(img,r1,s1,r2,s2):
	if (0 <= img and img <= r1):
		return (s1 / r1)*img
	elif (r1 < img and img <= r2):
		return ((s2 - s1)/(r2 - r1)) *  (img - r1) + s1
	else:
		return ((255 - s2)/(255 - r2)) *  (img - r2) + s2
r1 = 70
s1 = 0
r2 = 140
s2 = 255

vf=numpy.vectorize(piecewise)
org = vf(org,r1,s1,r2,s2)

cv2.imwrite("logq2b.jpg",org)
cv2.waitKey(0)
cv2.destroyAllWindows()