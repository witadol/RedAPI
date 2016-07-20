#! /usr/bin/env python3
#coding: utf-8

import serial
import time
def readCas():

    ser = serial.Serial('/dev/ttyS0')
    ser.baudrate = 9600
    ser.stopbits = serial.STOPBITS_ONE
    ser.timeout = 0.09
    while True:
        ser.
        ser.write('\x00'.encode())
        print(ser.readline())




def readBdu():
    ser = serial.Serial('/dev/ttyS0')
    ser.baudrate = 9600
    ser.stopbits = serial.STOPBITS_ONE
    ser.timeout = 0.05
    while True:
        ser.write('\x02B\x03'.encode('ascii'))
        print(ser.readline())


#readBdu()

readCas()