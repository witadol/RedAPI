#! /usr/bin/env python3
import time
from serial.tools import list_ports
start = time.clock()
for port in list_ports.comports():
    print(port.device)
    print(port.manufacturer)

elapsed = time.clock() - start
print('ELAPSE {0}'.format(elapsed))