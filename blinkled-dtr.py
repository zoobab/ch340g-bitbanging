#!/usr/bin/python
import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 1500000, timeout=None, xonxoff=None, rtscts=None, dsrdtr=None)

count = 0
while (count < 100000):
#    print 'The count is:', count
    count = count + 1
    print '''Setting RTS to True'''
    ser.setRTS(True)
    time.sleep(3.2)
    print '''Setting RTS to False'''
    ser.setRTS(False)
    time.sleep(3.2)
