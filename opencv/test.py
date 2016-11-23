#!/usr/bin/python3.4

import cv2

vidCap=cv2.VideoCapture(0)
ret, frame = vidCap.read()
cv2.imshow('frame',ret)


