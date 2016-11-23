from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO

from collections import deque
import numpy as np
import imutils
import cv2
import time

f=open("position.txt",'r+')
pos=float(f.read())
print(pos)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
pwm=GPIO.PWM(18,50)
pwm.start(5)
pwm.ChangeDutyCycle((-pos/18)+12)
pwm.ChangeDutyCycle((-pos/18)+12)
time.sleep(1)
print("Servo Done")
camera=PiCamera()
camera.resolution=(720,640)
rawCap=PiRGBArray(camera)
blueLower = (100, 50, 0)
blueUpper = (140, 255, 200)
pts = deque(maxlen=64)
camera.capture(rawCap,format="bgr")
frame=rawCap.array
frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
frame = imutils.resize(frame, width=600)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, blueLower, blueUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
center = None
if len(cnts) > 0:
	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
pts.appendleft(center)
for i in range(1, len(pts)):
	print(pts[i])
if center!=None:
	print(center)
	position=(center[0]/600.0)+0.5
	print(position)
	pos=pos+(position*2)
	print(pos)
	f.seek(0)
	f.write(str(pos))
	f.truncate()
	f.close()
	pwm.ChangeDutyCycle((-pos/18)+12)
	time.sleep(1)
else:
	print("Out of frame")

GPIO.cleanup()
