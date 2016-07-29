#! /usr/bin/env python
import pyudev
from redlib import DEVICES_AND_VENDORS

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='tty')


states = {'remove': 'DISCONNECTED FROM', 'add': 'CONNECTED TO'}

for action, device in monitor:
    vendor = dict(device)['ID_VENDOR_FROM_DATABASE']
    try:
        print(DEVICES_AND_VENDORS[vendor] + " was " + states[action])
        #print('{0}:\n{1}\n{2}'.format(action,dict(device), device.subsystem, ))
    except KeyError:
        pass