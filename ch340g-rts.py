#!/usr/bin/python

# RTS to True  == 0V
# RTS to False == 3.7V

# DTR to True  == 0V
# DTR to False == 3.7V

import time
import serial

ser = serial.Serial("/dev/ttyUSB0")
pin="CTS"

count = 0
while (count < 100000):
    print 'The count is:', count
    count = count + 1
    print '''Getting ''' + pin + ''' value'''
    ser.getCTS()
    time.sleep(3.0)
    print "Setting DTR to False"
    ser.setCTS(False)
    time.sleep(3.0)
