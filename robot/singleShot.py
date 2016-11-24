import picamera
import picamera.array
import imutils
import cv2
import time
from collections import deque

cv2.namedWindow("Frame")

blueLower = (100, 100, 75)
blueUpper = (120, 255, 255)
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
          print(frame.shape)
          cv2.line(frame,(500,0),(500,557),(0,0,200),3)
          cv2.imshow("Frame",frame)
          key=cv2.waitKey(0) & 0xFF
          if key == ord("q"):
            break
          stream.truncate(0)
          print(i)
