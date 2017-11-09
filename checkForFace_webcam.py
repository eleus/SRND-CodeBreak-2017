# checks to see if image in front of ultrasonic sensor is a face (runs for 10s)
# NOT instantaneous (some time after object is detected)

import cv2
import numpy as np
import time

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# the number '1' could be someother number for different computers, check other nums
cam = cv2.VideoCapture(1)

faceDetected = False
currentTime = time.time() # current time in secs
stopTime = currentTime + 10.0

while(time.time() < stopTime):
    # return color image and status value
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # get all faces in the frame
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    if(faces != ()):
        faceDetected = True
    # draw rectangles around faces
    for(x,y,w,h) in faces:
        # (image, intial point of rec, end point of rec, color in rgb, thickness of rec)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
    cv2.imshow("Webcam", img)
    if(cv2.waitKey(1) == ord('q')): # delay until user presses 'q' to quit
       break
    #k = cv2.waitKey(30) & 0xff
    #if k == 27:
        #break
    
cam.release()
cv2.destroyAllWindows()

if(faceDetected):   # print "yes" if face detected, else print nothing
    print "yes"

