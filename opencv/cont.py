from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import io
from collections import deque
import numpy as np
import imutils
import cv2
import time

pos=90
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
pwm=GPIO.PWM(18,50)
pwm.start(5)
pwm.ChangeDutyCycle((-pos/18)+12)
pwm.ChangeDutyCycle((-pos/18)+12)
time.sleep(1)
print("Servo Done")

blueLower = (100, 50, 0)
blueUpper = (140, 255, 200)

with PiCamera() as camera:
	camera.resolution=(320, 240)
	while True:
		stream = io.BytesIO()
		camera.capture(stream, format='jpeg', use_video_port=True)
		data = np.fromstring(stream.getvalue(), dtype=np.uint8)
		frame = cv2.imdecode(data, 1)
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
		if center!=None:
			print(center)
			position=(center[0]/600.0)-0.5
			print(position)
			pos=pos+(position*10)
			print(pos)
			pwm.ChangeDutyCycle((-pos/18)+12)
		else:
			print("Out of frame")
