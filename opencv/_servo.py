import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)
pwm.start(5)

pos=input()

pwm.ChangeDutyCycle(int(pos))
time.sleep(1)

GPIO.cleanup()
