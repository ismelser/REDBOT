import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)


time.sleep(0.1)
num=int(input("->"))
#num=90
sent=bytearray([num])
ser.write(sent)
time.sleep(1)
input("Press Any Key to Continue")
