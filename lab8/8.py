import cv2

vid_capture = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output1 = cv2.VideoWriter("output.avi", vid_cod, 20.0, (640,480))
output2 = cv2.VideoWriter("contours.avi", vid_cod, 20.0, (640,480))

ret,background = vid_capture.read()
# background = cv2.fastNlMeansDenoisingColored(background,None,10,10,7,21)
while(True):
	ret,frame = vid_capture.read()
	# frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
	image = cv2.subtract(background,frame)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	r,image=cv2.threshold(image,5,255,cv2.THRESH_BINARY)
	contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	contours.remove(contours[0])
	contour = max(contours, key=cv2.contourArea)
	bg=background.copy()
	cont = cv2.drawContours(bg, contour, -1, (0,0,0), 3)
	cv2.imshow("countours",cont)
	image=cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
	cv2.imshow("My cam video", image)
	output1.write(image)
	output2.write(cont)
	if cv2.waitKey(1) &0XFF == ord('x'):
		break

vid_capture.release()
output1.release()
output2.release()
cv2.destroyAllWindows()