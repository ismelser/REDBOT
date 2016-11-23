import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

num="20"
print type(num)
var=ser.write(u"20")
print var
line=ser.readline()
print line
