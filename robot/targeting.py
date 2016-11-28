import picamera
import picamera.array
import imutils
import cv2
import time
import numpy as np
from collections import deque

cv2.namedWindow("Frame")
cv2.namedWindow("Ball")
cv2.resizeWindow("Ball",200,200)

blueLower = (100, 100, 20)
blueUpper = (120, 255, 255)
whiteLower = (0,100,100)
whiteUpper = (180,255,255)
pts = deque(maxlen=32)


with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.resolution=(1664,928)
    time.sleep(1)
    with picamera.array.PiRGBArray(camera) as stream:
        for i in range(1,50):
          camera.capture(stream, format='bgr', use_video_port=True)
          image = stream.array
          frame=imutils.resize(image,width=1000)
          output=imutils.resize(image,width=1000)
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
          radius=int(radius)
          x1=center[0]-radius
          x2=center[0]+radius
          y1=center[1]-radius
          y2=center[1]+radius
          print(frame.shape)
          ball=frame[y1:y2,x1:x2].copy()
          print(np.average(ball[:,:,0]))
          print(np.average(ball[:,:,1]))
          print(np.average(ball[:,:,2]))
          print("---")
          if center!=None:
             cv2.circle(output,(center),radius,(0,255,0),1)
             cv2.rectangle(output, (center[0]-radius,center[1]+radius),(center[0]+radius,center[1]-radius),(255,255,255),1)
          cv2.line(frame,(500,0),(500,557),(0,0,200),3)
          cv2.imshow("Ball",ball)
          cv2.imwrite("ball.jpg",ball)
          cv2.imshow("Frame",output)
          key=cv2.waitKey(0) & 0xFF
          if key == ord("q"):
            break
          stream.truncate(0)
          print(i)
