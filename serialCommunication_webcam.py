# Made with PySerial, on Python 2.7.12
# made to connect with webcam
# https://pythonhosted.org/pyserial/pyserial.html
# PySerial Tutorial: https://www.youtube.com/watch?v=KB67cuaEJOU
# OpenCV Tutorial: https://www.youtube.com/watch?v=1Jz24sVsLE4&list=PLnjEM1fs09cGGjdCLSue8Kw7GmWDhGlMh

import serial
import time
# help get return value from running facial detection script
import sys
import subprocess

# allows Arduino to finsih loading code before runing this file
time.sleep(5)

def strToInt(data):
        strInt = ''.join(x for x in data if x.isdigit())
        # some data points may be empty so we must check empty string
        if(strInt == ''):
                return -1
        else:
                return int(strInt)
        
ser = serial.Serial('COM3', baudrate = 9600, timeout=1)
objDetected = False

while 1:
        # read data and decode to remove arduino formating
        arduinoData = ser.readline().encode('utf-8')  #decode('ascii')

        # a carriage return (13) and NL line feed (new line) (10) at the end of data read
        # this is based on the serial settings
        # so only check the first letter when checking for a program reset (aka button pressed)
        if('PROGRAM RESET' in arduinoData): 
                objDetected = False
        
        distance = strToInt(arduinoData)

        # if object is with 50 cm, then send this string which will prompt
        # red LED to turn off and a yellow one to turn on
        if((distance <= 50) and (distance >= 0)):
                print arduinoData
                objDetected = True
                ser.write('d')
                #the very next Arduino serial output after less than 50 cm reading
                print ser.readline(), ser.readline()
                # check if a face was detected
                print 'Capturing...'
                # run face detecting python script
                scriptOutput = subprocess.check_output([sys.executable, "checkForFace_webcam.py", "34"])
                print 'Done capturing...'
                if(scriptOutput != ''):
                        print 'Face detected!'
                        ser.write('y')
                else:
                        print 'Face NOT detected!'
                        ser.write('n')
                                                
        if(not objDetected):
                print(arduinoData)
        #print (distance)
        #print 'objDetected: ', objDetected


