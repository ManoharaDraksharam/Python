import numpy as np
import cv2 as cv
import os, fnmatch

cap = cv.VideoCapture(0)

if not cap.isOpened():
	print("Cannot open camera")
	exit()
	
i=0

while True:

	ret, frame = cap.read()
	

	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break
	
# Our operations on the frame come here
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
# Display the resulting frame
	cv.imshow('frame', gray)
	
	'''image_files = find('*.png', '/home/manohara/PythonProjects')
	
	print(image_files)'''
	
	a=cv.waitKey(1) 
	
	'print(a)
	
	if a == ord('c'):
		i = i+1
		cv.imwrite("captured"+str(i)+".png", frame)
	elif a == ord('q'):
		break
	
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
  




