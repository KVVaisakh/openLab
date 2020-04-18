import cv2
import numpy

imgtrn = cv2.imread("original.jpg")
dimtrn = imgtrn.shape

imgray = cv2.cvtColor(imgtrn, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(imgray, 60, 255, 0)
cv2.imshow("binary",binary)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(contours)

cv2.drawContours(imgtrn, contours, -1, (0,255,0), 1)
cv2.imshow("turned",imgtrn)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("ch.jpg",img)