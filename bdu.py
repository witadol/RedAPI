#! /usr/bin/env python3
import sys
from redlib import ControlScales
PORT_NAME = '/dev/ttyS1'


def getResponse(port_name):
    bdu = ControlScales(port_name)
    print(bdu.get_response().decode())



if len(sys.argv) > 1:
    port_name = sys.argv[1]
    getResponse(port_name)
else:
    print("Please, select name of interface")
