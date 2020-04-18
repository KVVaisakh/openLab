import cv2
import numpy

vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("capBinary.avi", vid_cod, 20.0, (640,480))
output1 = cv2.VideoWriter("trakked.avi", vid_cod, 20.0, (640,480))

vid = cv2.VideoCapture('input.avi')

kernel = numpy.ones((5,5),numpy.uint8)
lower_blue = numpy.array([100,60,2])
upper_blue = numpy.array([150,255,255])
while(True):
	ret, frame = vid.read()
	if ret == False:
		break
	if cv2.waitKey(25) & 0xFF == ord('x'):
		break

	blurred = cv2.GaussianBlur(frame, (41, 41), 0)
	blurred = cv2.medianBlur(blurred,31)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	mask = cv2.erode(mask, kernel, iterations=2)
	mask = cv2.dilate(mask, kernel, iterations=2)
	cv2.imshow('mask',mask)
	image=cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
	output.write(image)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	if contours:
		c = max(contours, key=cv2.contourArea)
		cont = cv2.drawContours(frame.copy(), c, -1, (0,0,0), 3)
	else:
		cont=cv2.drawContours(frame.copy(), [numpy.array([[0,0], [0,0], [0,0]])], -1, (0,0,0), 3)
	cv2.imshow('Frame',cont)
	output1.write(cont)

vid.release()
output.release()
cv2.destroyAllWindows()