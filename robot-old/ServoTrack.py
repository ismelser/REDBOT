import picamera
import picamera.array
import imutils
import cv2
import time
from collections import deque

import serial
ser = serial.Serial('/dev/ttyUSB0', 9600) #Serial

blueLower = (100, 100, 75)
blueUpper = (120, 255, 255)

point=90

cv2.namedWindow("Frame")

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.resolution=(1664,928)
    ser.write(bytearray([90])) #Serial
    time.sleep(1)
    ser.write(bytearray([90])) #Serial
    time.sleep(1)
    with picamera.array.PiRGBArray(camera) as stream:
        for i in range(1,50):
          camera.capture(stream, format='bgr', use_video_port=True)
          image = stream.array
          frame=imutils.resize(image,width=1000)
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
          print(center)
          try:
            point=(-center[0]/25.0)+20+point
            print(((-center[0])/25.0)+20)
            print("Point="+str(point))
            if point<0: point=90
            if point>180: point=90
            if point==None: point=90
            ser.write(bytearray([int(point)])) #Serial
            print("Set")
            cv2.circle(frame,(center),int(radius),(0,255,0),2)
          except:
            pass
          cv2.imshow("Frame",frame)
          key=cv2.waitKey(2000) & 0xFF
          if key == ord("q"):
            ser.write(bytearray([90]))
            break
          stream.truncate(0)
          print(i)
