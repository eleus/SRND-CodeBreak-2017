import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(1)

while(True):
    # return color image and status value
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # get all faces in the frame
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    # draw rectangles around faces
    for(x,y,w,h) in faces:
        # (image, intial point of rec, end point of rec, color in rgb, thickness of rec)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
    cv2.imshow("Face", img);
    if(cv2.waitKey(1) == ord('q')): # 1ms delay
        break;
cam.release()
cv2.destroyAllWindows() 
