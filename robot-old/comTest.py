import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)
#ser.flush()

time.sleep(0.1)

while True:
  num=input("->")
  if num=="q": break
  #num=90
  sent=bytearray([int(num)])
  ser.write(sent)
#  ser.flushInput()
#  while True:
#    incoming=ser.read()
#    if incoming==b'\n' or incoming==b'\r':
#      break
#    print(incoming)

ser.close()
print("END")
