import cv2
import numpy as np

img = cv2.imread('Fig09_5.tif')
img2 = cv2.imread('Fig09_7.tif')
img3 = cv2.imread('Fig09_11.tif')
img4 = cv2.imread('Fig09_16.tif')

kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imwrite("erosion.jpg",erosion)

dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imwrite("dilation.jpg",dilation)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite("opening.jpg",opening)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("closing.jpg",closing)

closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("charecter.jpg",closing)

opening = cv2.morphologyEx(img3, cv2.MORPH_OPEN, kernel)
cv2.imwrite("fingerprint.jpg",opening)

gradient = cv2.morphologyEx(img4, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite("outline.jpg",gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()

