#! /usr/bin/env python3
import time
import sys
import serial
from redlib import RelayWrapper, UNAVAILABLE_PORT_ERROR

try:
    relay = RelayWrapper()
    time.sleep(0.05)
    if len(sys.argv) > 1:
        if sys.argv[1] == 'red':
            relay.enable_k1()
        elif sys.argv[1] == 'white':
            relay.enable_k2()
        elif sys.argv[1] == 'green':
            relay.enable_k3()
        else:
            relay.enable_k1()
    else:
        relay.disable_all()
except serial.serialutil.SerialException:
    print(UNAVAILABLE_PORT_ERROR)