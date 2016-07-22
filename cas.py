#! /usr/bin/env python3
import sys
from redlib import Cas
PORT_NAME = '/dev/ttyS0'


def get_response(port_name):
    cas = Cas(port_name)
    print(cas.get_formatted_response())

if len(sys.argv) > 1:
    port_name = sys.argv[1]
    get_response(port_name)
else:
    print("Please, select name of interface")