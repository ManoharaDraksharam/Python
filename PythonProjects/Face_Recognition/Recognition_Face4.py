import cv2
import numpy


# loading the source image
img = cv2.imread('Image1.png')

# converting to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


faces_rects = haar_cascade_face.detectMultiScale(img_gray, scaleFactor = 1.2, minNeighbors = 5);

# getting no. of faces detected
print('Faces Detected : ', len(faces_rects))

for (x,y,w,h) in faces_rects:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('image', img)
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)
