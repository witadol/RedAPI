#! /usr/bin/env python
import pyudev

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='tty')

devices = {'Atmel Corp.':'Fiscal printer', 'Sagem': 'POS terminal', 'Prolific Technology, Inc.': 'Lamp'}
states = {'remove': 'DISCONNECTED FROM', 'add': 'CONNECTED TO'}

for action, device in monitor:
    vendor = dict(device)['ID_VENDOR_FROM_DATABASE']
    try:
        print(devices[vendor]+ " was " + states[action])
        #print('{0}:\n{1}\n{2}'.format(action,dict(device), device.subsystem, ))
    except KeyError:
        pass