# using OpenCV with an IP camera (using phone + IP Camera app)
# https://www.youtube.com/watch?v=2xcUzXataIk&index=9&list=PLnjEM1fs09cGGjdCLSue8Kw7GmWDhGlMh

import urllib
import cv2
import numpy as np

# link to IP Camera 
# (I used IP Webcam Android App by Pavel Khlebovich)
# enter your the URL to your own IP camera
# shot.jpg accesses a single frame image from camera to be analyzed
url = 'http://000.000.0.00:8080/shot.jpg'

while True:
    imgResp = urllib.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype = np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('test', img)
    if(ord('q') == cv2.waitKey(10)):
        exit(0)

