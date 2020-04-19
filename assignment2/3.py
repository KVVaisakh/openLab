import cv2
import numpy


src = cv2.imread("ChessBoardGrad.png",0)
box = cv2.boxFilter(src, -1, (224,224))
img = src- box
cv2.imwrite("corrected.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()