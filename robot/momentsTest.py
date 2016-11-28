
import picamera
import picamera.array
import imutils
import cv2
import time
import numpy as np
from collections import deque
import vLibrary as v

cv2.namedWindow("Frame")

frame=v.takeFrame()
ball=cv2.imread("ball.jpg",0)


#grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
grey=frame[:,:,0]
ret,thresh = cv2.threshold(grey,40,55,0)
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


surf = cv2.xfeatures2d.SURF_create(400)
#orb = cv2.ORB_create()
kp1, des1 = surf.detectAndCompute(grey,None)
kp2, des2 = surf.detectAndCompute(ball,None)
print(kp1)
print(des1)

#cv2.imshow("Frame",img3)
#cv2.waitKey(0)
