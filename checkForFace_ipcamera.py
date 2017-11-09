# checks to see if image in front of ultrasonic sensor is a face (runs for 10s)
# NOT instantaneous (some time after object is detected)

import urllib
import serial
import cv2
import numpy as np
import time

# link to IP Camera 
# (I used IP Webcam Android App by Pavel Khlebovich)
# enter your the URL to your own IP camera
# shot.jpg accesses a single frame image from camera to be analyzed
url = 'http://000.000.0.00:8080/shot.jpg'

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceDetected = False
currentTime = time.time() # current time in secs
stopTime = currentTime + 10.0

while(time.time() < stopTime):
    # getting color image and processing with numpy then decoding
    imgResponse = urllib.urlopen(url)
    imgNp = np.array(bytearray(imgResponse.read()), dtype = np.uint8)
    img = cv2.imdecode(imgNp, -1)
    # must convert to gray to use OpenCV on it
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # get all faces in the frame
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    if(faces != ()):
        faceDetected = True
    # draw rectangles around faces
    for(x,y,w,h) in faces:
        # (image, intial point of rec, end point of rec, color in rgb, thickness of rec)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
    cv2.imshow("IP Camera", img)
    if(cv2.waitKey(1) == ord('q')): # delay until user presses 'q' to quit
       break
    #k = cv2.waitKey(30) & 0xff
    #if k == 27:
        #break
    
cv2.destroyAllWindows()

if(faceDetected):   # print "yes" if face detected, else print nothing
    print "yes"

