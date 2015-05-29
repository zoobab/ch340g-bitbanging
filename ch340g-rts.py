#!/usr/bin/python

# RTS to True  == 0V
# RTS to False == 3.7V

# DTR to True on CH340G  == 0V
# DTR to False on CH340G == 3.7V

import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 1500000, timeout=None, xonxoff=None, rtscts=None, dsrdtr=None)

count = 0
while (count < 100000):
#    print 'The count is:', count
    count = count + 1
    print '''Setting RTS to True'''
    ser.setRTS(True)
    time.sleep(3.0)
    print '''Setting RTS to False'''
    ser.setRTS(False)
    time.sleep(3.0)
