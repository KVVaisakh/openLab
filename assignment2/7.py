import cv2
from skimage.exposure import rescale_intensity
import numpy

def convolve(image, kernal):
	output = numpy.zeros(image.shape, dtype="float32")
	pad=(kernal.shape[0]-1)//2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,cv2.BORDER_REPLICATE)
	for i in range(pad,image.shape[0]-pad):
		for j in range(pad,image.shape[1]-pad):
			section = image[i-pad:i+pad+1  , j-pad:j+pad+1]
			s = (kernal*section).sum()
			output[i-pad][j-pad]=s
	return output

def sobel(image):
	kernal = numpy.array([[1,2,1],[0,0,0],[-1,-2,-1]])
	kernalt = kernal.T
	img1 = convolve(image,kernal)
	img2= convolve(image,kernalt)
	return img1,img2

array = numpy.array([[0,0,0,0,0],[0,0,0,0,0],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10]])
sob = sobel(array)
print(sob)

# array([[  0.,   0.,   0.,   0.,   0.],
#        [-40., -40., -40., -40., -40.],
#        [-40., -40., -40., -40., -40.],
#        [  0.,   0.,   0.,   0.,   0.],
#        [  0.,   0.,   0.,   0.,   0.]], dtype=float32), 
# array([[0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]], dtype=float32)

array = numpy.array([[0,0,0,10,10],[0,0,0,10,10],[0,0,0,10,10],[0,0,0,10,10],[0,0,0,10,10]])
sob = sobel(array)
print(sob)

# array([[0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]], dtype=float32), 
# array([[  0.,   0., -40., -40.,   0.],
#        [  0.,   0., -40., -40.,   0.],
#        [  0.,   0., -40., -40.,   0.],
#        [  0.,   0., -40., -40.,   0.],
#        [  0.,   0., -40., -40.,   0.]], dtype=float32)

array = numpy.array([[0,0,0,0,10],[0,0,0,10,10],[0,0,10,10,10],[0,10,10,10,10],[10,10,10,10,10]])
sob = sobel(array)
print(sob)

# array([[  0.,   0., -10., -20., -10.],
#        [  0., -10., -30., -30., -10.],
#        [-10., -30., -30., -10.,   0.],
#        [-40., -30., -10.,   0.,   0.],
#        [-30., -10.,   0.,   0.,   0.]], dtype=float32), 
# array([[  0.,   0., -10., -40., -30.],
#        [  0., -10., -30., -30., -10.],
#        [-10., -30., -30., -10.,   0.],
#        [-20., -30., -10.,   0.,   0.],
#        [-10., -10.,   0.,   0.,   0.]], dtype=float32)
