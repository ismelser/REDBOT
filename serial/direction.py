from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO

from collections import deque
import numpy as np
import imutils
import cv2
import time

import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)


camera=PiCamera()
camera.resolution=(1664,928)
rawCap=PiRGBArray(camera)
camera.capture(rawCap,format="bgr")
frame=rawCap.array



blueLower = (100, 50, 0)
blueUpper = (140, 255, 200)
pts = deque(maxlen=64)

frame = imutils.resize(frame, width=1000)
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
# loop over the set of tracked points
for i in range(1, len(pts)):
	# if either of the tracked points are None, ignore
	# them
	if pts[i - 1] is None or pts[i] is None:
		continue

	# otherwise, compute the thickness of the line and
	# draw the connecting lines
	print(pts[i])

if center!=None:
	print(center)
	position=(center[0]/10.0)+40
	print(int(position))
	#ser.write([pos])
	if position>50:
		print("Right frame")
	if position<50:
		print("Left frame")
else:
	print("Out of frame")
	ser.write(bytearray([90]))

# cleanup the camera and close any open windows
cv2.destroyAllWindows()
