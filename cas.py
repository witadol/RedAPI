#! /usr/bin/env python3
import sys
from redlib import Cas
PORT_NAME = '/dev/ttyS0'

def getResponse(port_name):
    cas = Cas(port_name)
    print(cas.get_response().decode())

# getResponse(PORT_NAME)


if len(sys.argv) > 1:
    port_name = sys.argv[1]

else:
    print("Please, select name of interface")