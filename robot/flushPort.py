import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(0.1)
ser.flush()
ser.flushInput()
ser.close()
