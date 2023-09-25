import cv2 as cv
import numpy as np
import face_recognition 


frame = cv.VideoCapture(0)

if not frame.isOpened():
	print("The camera is closed")
	

while True: 
	
	ret, img = frame.read()
	gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
	
	if ret == True:
		cv.imshow('captured Video', gray)
		
	x = cv.waitKey(1)	
	
	if x == ord('s'):
		cv.imwrite('Mano.jpg', gray)
		break
	elif  x == ord('q'):
		break		
		
obama_image = face_recognition.load_image_file('obama.jpg')
justintimberlake_image = face_recognition.load_image_file('JustinTimberlake.jpg')
ryanrenolds_image = face_recognition.load_image_file('RyanRelonds.jpg')

unknown_image = face_recognition.load_image_file('Mano.jpg')

try:
	obama_encoding = face_recognition.face_encodings(obama_image)[0]
	justintimberlake_encoding = face_recognition.face_encodings(justintimberlake_image)[0]
	ryanrenolds_encoding = face_recognition.face_encodings(ryanrenolds_image)[0]
	
	unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
	print("Unable to loacate any faces, check image files")
	exit()

known_faces =[obama_encoding, justintimberlake_encoding, ryanrenolds_encoding]

results = face_recognition.compare_faces(known_faces, unknown_encoding)

print("Is the unknown face a picture of Obama? {}".format(results[0]))
print("Is the unknown face a picture of Justin? {}".format(results[1]))
print("Is the unknown face a picture of Ryan? {}".format(results[2]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))

frame.release()
cv.destroyAllWindows()	
