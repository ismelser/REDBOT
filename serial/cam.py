from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import imutils
import cv2

camera=PiCamera()
camera.resolution=(1664,928)
rawCap=PiRGBArray(camera)


camera.capture(rawCap,format="bgr")
frame=rawCap.array
frame = imutils.resize(frame, width=1000)
cv2.namedWindow("Frame")
cv2.imshow("Frame",frame)
cv2.waitKey(0)
