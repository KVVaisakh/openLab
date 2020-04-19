import cv2
from skimage.exposure import rescale_intensity
import numpy

def convolve(image, kernel):
	output = numpy.zeros(image.shape, dtype="float32")
	pad=(kernal.shape[0]-1)//2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,cv2.BORDER_REPLICATE)
	for i in range(pad,image.shape[0]-pad):
		for j in range(pad,image.shape[1]-pad):
			section = image[i-pad:i+pad+1  , j-pad:j+pad+1]
			s = (kernal*section).sum()
			output[i-pad][j-pad]=s
	output = rescale_intensity(output, in_range=(0, 255))
	output = (output * 255).astype("uint8")
	return output


src = cv2.imread("1200px-Monarch_In_May.jpg",0)

kernal = numpy.array(([0, 1, 0],[1, -4, 1],[0, 1, 0]), dtype="int")
img=convolve(src,kernal)

gus = cv2.GaussianBlur(src,(3,3),0)
gImg=convolve(gus,kernal)

cv2.imshow("laplacian.jpg",img)
cv2.imshow("laplacianOfGaussian.jpg",gImg)

cv2.imwrite("laplacian.jpg",img)				# more detailed outline
cv2.imwrite("laplacianOfGaussian.jpg",gImg)		# many minute details are missing
cv2.waitKey(0)
cv2.destroyAllWindows()