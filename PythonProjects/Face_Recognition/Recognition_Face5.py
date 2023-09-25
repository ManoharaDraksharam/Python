import face_recognition
import cv2
import numpy as np
import os

known_faces_dir = "Known_faces"


print("loading known faces")

known_face_encodings = []
known_names = []


for name in os.listdir(known_faces_dir):
	for filename in os.listdir(f"{known_faces_dir}/{name}"):
	
		image = face_recognition.load_image_file(f"{known_faces_dir}/{name}/{filename}")
		face_encoding = face_recognition.face_encodings(image)[0]
		known_face_encodings.append(face_encoding)
		known_names.append(name)


video_capture = cv2.VideoCapture(0)

print("processing unknown faces")

unknown_face_location1 = []
unknown_face_encoding1 = []


while True:
   
	ret, frame = video_capture.read()

	small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)     
	RGB = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
          
	unknown_face_location1 = face_recognition.face_locations(RGB)
	unknown_face_encoding1 = face_recognition.face_encodings(RGB,unknown_face_location1)
	
	face_names = []        
	for face_encoding in unknown_face_encoding1:
		
		
		matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
		name1 = "Unknown"
            
		face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
		best_match_index = np.argmin(face_distances)
                                                
		if matches[best_match_index]:
            		name1 = known_names[best_match_index]
		face_names.append(name1)
		
       
	for (top, right, bottom, left), name2 in zip(unknown_face_location1, face_names):
        
        	top *= 4
        	right *= 4
        	bottom *= 4
        	left *= 4
        
        	cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        
        	cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        	font = cv2.FONT_HERSHEY_DUPLEX
        	cv2.putText(frame, name2, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


	cv2.imshow('Video', frame)

    
	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break

video_capture.release()
cv2.destroyAllWindows()



