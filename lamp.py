#! /usr/bin/env python3
import time
import sys
import serial
from redlib import RelayWrapper, UNAVAILABLE_PORT_ERROR

try:

    if len(sys.argv) > 1:
        relay = RelayWrapper(sys.argv[1])
        time.sleep(0.05)
        if len(sys.argv) > 2:
            if sys.argv[2] == 'red':
                relay.enable_k1()
            elif sys.argv[2] == 'white':
                relay.enable_k2()
            elif sys.argv[2] == 'green':
                relay.enable_k3()
            else:
                relay.enable_k1()
        else:
            relay.disable_all()
    else:
        print("Please, select name of interface")
except serial.serialutil.SerialException:
    print(UNAVAILABLE_PORT_ERROR)