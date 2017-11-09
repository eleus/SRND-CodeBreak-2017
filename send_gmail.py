# Tutorial: https://automatetheboringstuff.com/chapter16/
# https://gist.github.com/alexle/6576366


import smtplib

import urllib
import cv2
import numpy as np

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# link to IP Camera 
# (I used IP Webcam Android App by Pavel Khlebovich)
# enter your the URL to your own IP camera
# shot.jpg accesses a single frame image from camera to be analyzed
url = 'http://000.000.0.00:8080/shot.jpg'

# enter phone number to be sent notification before @tmomail.net
# this domain is for tmobile providers only 
to = '5555555555@tmomail.net'
# enter email you want notification to be sent from
gmail_user = 'email@domain.com'
# enter the password for the email account
gmail_pwd = 'password'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)

# take picture
imgResp = urllib.urlopen(url)
imgNp = np.asarray(bytearray(imgResp.read()), dtype="uint8")
img = cv2.imdecode(imgNp, cv2.IMREAD_COLOR)
cv2.imwrite('snapshot.png', img)
cv2.destroyAllWindows()

''' with webcam
cam = cv2.VideoCapture(1)
ret, img = cam.read()
cv2.imwrite('snapshot.png', img)
cv2.destroyAllWindows()
cam.release()
img_file = open('snapshot.png', 'rb')
'''

header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Face Detected! \n'
print header
msg_text = header + '\n this is test msg from python script \n\n'

msg = MIMEMultipart()
msg.attach(MIMEText(msg_text, 'plain'))

img_file = open('snapshot.png', 'rb')
msg_img = MIMEImage(img_file.read())
img_file.close()

msg.attach(msg_img)


smtpserver.sendmail(gmail_user, to, msg.as_string())
print 'done!'
smtpserver.close()



'''
import smtplib
import cv2

to = '1234567890@tmomail.net'
gmail_user = 'email@gmail.com'
gmail_pwd = 'password'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
#header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
header = 'To:' + to + '\n' + 'From: ' + '' + '\n' + 'Subject: Motion Camera \n'
print header
msg = header + '\n Person Dectected! \n\n'
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'
smtpserver.close()

'''
