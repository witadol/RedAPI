#! /usr/bin/env python3
import sys
import serial
from redlib import SerialDevice, BDU_REQUEST, EMPTY_PORT_ERROR, UNAVAILABLE_PORT_ERROR
PORT_NAME = '/dev/ttyS0'


def get_response(port_name):
    try:
        cas = SerialDevice(port_name, BDU_REQUEST)
        result = cas.get_response_on_request()
        if result:
            print(result[4:15].decode())
        else:
            print(EMPTY_PORT_ERROR)
    except serial.serialutil.SerialException:
        print(UNAVAILABLE_PORT_ERROR)

#get_response(PORT_NAME)

if len(sys.argv) > 1:
    port_name = sys.argv[1]
    get_response(port_name)
else:
    print("Please, select name of interface")
