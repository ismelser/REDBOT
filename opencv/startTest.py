import picamera
import time

# How long does camera initialization take?
start = time.time()
with picamera.PiCamera() as camera:
    pass
print(time.time() - start)
