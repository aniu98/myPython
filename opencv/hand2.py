import cv2

def video_capture():
	cap = cv2.VideoCapture(0)
	while True:
	# capture frame-by-frame
		ret, frame = cap.read()

		# our operation on the frame come here
		# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 可选择灰度化

		# display the resulting frame
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'): # 按q键退出
			
			# when everything done , release the capture
			cap.release()
			cv2.destroyAllWindows()
			break

video_capture()
