#!/usr/bin/python

# RTS to True  == 0V
# RTS to False == 3.7V

import time
import serial

ser = serial.Serial("/dev/ttyUSB0")

count = 0
while (count < 100000):
#   print 'The count is:', count
    count = count + 1
#    print "Setting RTS to True"
    ser.setRTS(True)
#    time.sleep(3.0)
#    print "Setting RTS to False"
    ser.setRTS(False)
#    time.sleep(3.0)
