import cv2
import numpy as np

vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output1 = cv2.VideoWriter("output.avi", vid_cod, 20.0, (640,480))
output2 = cv2.VideoWriter("contours.avi", vid_cod, 20.0, (640,480))

vid = cv2.VideoCapture('input.avi')
ret,background = vid.read()

kernel = np.ones((50,50),np.uint8)
while(True):
	ret, frame = vid.read()
	if ret == False:
		break
	cv2.imshow('Frame',frame)
	if cv2.waitKey(25) & 0xFF == ord('x'):
		break

	image = cv2.subtract(background , frame)
	cv2.imshow("subtract",image)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	r,image=cv2.threshold(image,5,255,cv2.THRESH_BINARY)
	image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

	# gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
	# cv2.imshow("outline",gradient)

	contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	# contours.remove(contours[0])
	if(contours):
		contour = max(contours, key=cv2.contourArea)
	else:
		contour = 0
	bg=background.copy()
	cont = cv2.drawContours(bg, contour, -1, (0,0,0), 3)
	cv2.imshow("countours",cont)
	image=cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
	cv2.imshow("binary", image)
	output1.write(image)
	output2.write(cont)

vid.release()
output1.release()
output2.release()
cv2.destroyAllWindows()