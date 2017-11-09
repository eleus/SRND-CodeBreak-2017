# not working on Python 2.7.12

import os
import cv2
import numpy as np
from PIL import Image 

cascadePath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath);       # error here

recognizer = cv2.createLBPHFaceRecognizer()

path = 'faceData'

def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    print imagePaths

getImagesWithID(path) 
