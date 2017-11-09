# takes 20 photos of faces seen on the camera 
import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(1)

uniqueID = raw_input("Enter your unique ID: ")
sampleNum = 0
offset = 50
font = cv2.FONT_HERSHEY_SIMPLEX
xTemp = 0
yTemp = 0
wTemp = 0
hTemp = 0

while(True):
    # return color image and status value
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # get all faces in the frame
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    # draw rectangles around faces
    for(x,y,w,h) in faces:
        sampleNum = sampleNum + 1
        # (image, intial point of rec, end point of rec, color in rgb, thickness of rec)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
        cv2.imwrite("faceData/User."+str(uniqueID)+"."+str(sampleNum)+".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)
        cv2.waitKey(100)
        # hold the value of face retangle box size (assuming only one face captured)
        xTemp = x
        yTemp = y
        wTemp = w
        hTemp = h
    # write the sample number on the image before displaying
    cv2.putText(img,str(sampleNum),(xTemp+wTemp+10, yTemp+hTemp+10), font, 4,(255,255,255),2,) #cv2.LINE_AA)
    cv2.imshow("Face", img);
    cv2.waitKey(1)
    if(sampleNum >= 20):
        break;
cam.release()
cv2.destroyAllWindows() 
