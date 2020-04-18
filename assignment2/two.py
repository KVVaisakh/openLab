import cv2
import numpy

org = cv2.imread("logndlinear.jpg",0)
m=numpy.max(org)				# m[1] will have max pixel value
c=255/(numpy.log(1+m))
logImage = numpy.array(c*numpy.log(1+org),dtype=numpy.uint8)

cv2.imwrite("logq2.jpg",logImage)