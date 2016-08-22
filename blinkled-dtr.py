#!/usr/bin/python
import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 1500000, timeout=None, xonxoff=None, rtscts=None, dsrdtr=None)

count = 0
while (count < 100000):
#    print 'The count is:', count
    count = count + 1
    print '''Setting DTR to ON'''
    ser.setDTR(True)
    time.sleep(1)
    print '''Setting DTR to OFF'''
    ser.setDTR(False)
    time.sleep(1)
