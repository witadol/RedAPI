#! /usr/bin/env python3
from redlib import Cas
PORT_NAME = '/dev/ttyS0'


cas = Cas(PORT_NAME)
while True:
    print(cas.get_response())
