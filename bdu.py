#! /usr/bin/env python3
import sys
from redlib import ControlScales
PORT_NAME = '/dev/ttyS1'


def get_response(port_name):
    bdu = ControlScales(port_name)
    print(bdu.get_formatted_response())


if len(sys.argv) > 1:
    port_name = sys.argv[1]
    get_response(port_name)
else:
    print("Please, select name of interface")
