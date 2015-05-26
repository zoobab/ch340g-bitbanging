#!/usr/bin/python

# RTS to True  == 0V
# RTS to False == 3.7V

import time
import serial

ser = serial.Serial("/dev/ttyUSB0")
pin="DTR"

count = 0
while (count < 100000):
    print 'The count is:', count
    count = count + 1
    print '''Setting ''' + pin + ''' to True'''
    ser.setDTR(True)
    time.sleep(3.0)
    print "Setting DTR to False"
    ser.setDTR(False)
    time.sleep(3.0)
