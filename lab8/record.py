import cv2

vid_capture = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
inpt = cv2.VideoWriter("input.avi", vid_cod, 20.0, (640,480))

while(True):
	ret,frame = vid_capture.read()
	inpt.write(frame)
	cv2.imshow("My cam video", frame)
	if cv2.waitKey(1) &0XFF == ord('x'):
		break
cv2.destroyAllWindows()

vid_capture.release()
inpt.release()
cv2.destroyAllWindows()