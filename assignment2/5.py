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
	output = rescale_intensity(output, in_range=(0, 255))
	output = (output * 255).astype("uint8")
	return output

def laplace(image):
	kernal = numpy.array(([0, 1, 0],[1, -4, 1],[0, 1, 0]), dtype="int")
	image = convolve(image,kernal)
	return image

def sobel(image):
	kernal = numpy.array([[1,2,1],[0,0,0],[-1,-2,-1]])
	kernalt = kernal.T
	img1 = convolve(image,kernal)
	img2= convolve(image,kernalt)
	return img1,img2

chess = cv2.imread('ChessBoardGrad.png',0)
lenna = cv2.imread('Lenna.png',0)

lapChess = laplace(chess)
lapLenna = laplace(lenna)

cv2.imwrite("laplaceChess.jpg",lapChess)
cv2.imwrite("laplaceLenna.jpg",lapLenna)

sobChess = sobel(chess)
sobLenna = sobel(lenna)

cv2.imwrite("sobelChessX.jpg",sobChess[0])
cv2.imwrite("sobelChessY.jpg",sobChess[1])
cv2.imwrite("sobelLennaX.jpg",sobLenna[0])
cv2.imwrite("sobelLennaY.jpg",sobLenna[1])

canChess = cv2.Canny(chess,100,200)
canLenna = cv2.Canny(lenna,100,200)

cv2.imwrite("cannyChess.jpg",canChess)
cv2.imwrite("cannyLenna.jpg",canLenna)

# laplace will detect all the edges, sobel will detect only those edges in
# its defined diretion(either horizontal or vertical). Canny will remove many 
# minute details(texture etc.) from the figure, and highlight only the important edges.