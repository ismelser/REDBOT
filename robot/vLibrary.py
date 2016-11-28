import imutils
import picamera
import picamera.array
import cv2
import numpy as np

def takeFrame():
   with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.resolution=(1664,928)
    with picamera.array.PiRGBArray(camera) as stream:
        for i in range(1,50):
          camera.capture(stream, format='bgr', use_video_port=True)
          image = stream.array
          frame=imutils.resize(image,width=1000)
          return frame

def colorLock(frame, lower, upper):
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   mask = cv2.inRange(hsv, lower, upper)
   mask = cv2.erode(mask, None, iterations=2)
   mask = cv2.dilate(mask, None, iterations=2)
   cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
   if len(cnts) > 0:
      c = max(cnts, key=cv2.contourArea)
      ((x, y), radius) = cv2.minEnclosingCircle(c)
      M = cv2.moments(c)
      center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
   return (center,radius)

