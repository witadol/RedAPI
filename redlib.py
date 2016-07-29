#! /usr/bin/env python3
import serial
import pyudev
import time
import re
from serial.tools import list_ports

# Error messages
EMPTY_PORT_ERROR = '!port is empty'
UNAVAILABLE_PORT_ERROR = '!port is empty'

# Initial requests
CAS_REQUEST = b'\x00'
BDU_REQUEST = b'\x02B\x03'
LAMP_REQUEST = b'\x50'
LAMP_INIT = b'\x51'

# Device's vendors
DEVICES_AND_VENDORS = {'Atmel Corp.': 'Fiscal',
                       'Sagem': 'POS',
                       'Prolific Technology, Inc.': 'Lamp'}


class SerialDevice():

    def __init__(self, port_name, query_seq=b'', baud_rate=9600, timeout=0.06):
        self.connection = serial.Serial(port_name)
        self.connection.baudrate = baud_rate
        self.connection.timeout = timeout
        self.query_sequence = query_seq

    def redefine_query_sequence(self,sequence):
        self.query_sequence = sequence

    def create_connection(self):
        self.connection = serial.Serial(self.port_name)
        self.connection.baudrate = self.baud_rate
        self.connection.timeout = self.read_timeout

    def send_sequence(self, sequence):
        self.connection.write(sequence)

    def get_response(self):
        self.connection.readline()

    def get_response_on_request(self):
        self.connection.write(self.query_sequence)
        return self.connection.readline()


class RelayWrapper:
    ATTRIBUTE = u'ID_VENDOR'
    ATTRIBUTE_NAME = "Prolific_Technology_Inc."

    def __init__(self, device_port):
        #device_port = self.find_device(RelayWrapper.ATTRIBUTE, RelayWrapper.ATTRIBUTE_NAME)
        self.relay = SerialDevice(device_port, LAMP_REQUEST)
        if self.relay.get_response_on_request() == b'\xab':
            print('first communication')
            time.sleep(0.05)
            self.relay.send_sequence(LAMP_INIT)

    @staticmethod
    def find_device(attribute, attribute_name):
        context = pyudev.Context()
        for device in context.list_devices(subsystem='tty'):
            device_node = device.device_node

            if device_node.find("USB") != -1:
                if dict(device)[attribute] == attribute_name:
                    print('Device is located on {0}'.format(device.device_node))
                    return device.device_node

        return "not found"

    def disable_all(self):
        time.sleep(0.05)
        self.relay.send_sequence(b'\x00')

    def enable_k1(self):
        time.sleep(0.05)
        self.relay.send_sequence(b'\x01')

    def enable_k2(self):
        time.sleep(0.05)
        self.relay.send_sequence(b'\x02')

    def enable_k3(self):
        time.sleep(0.05)
        self.relay.send_sequence(b'\x04')


class Discoverer:
    @staticmethod
    def get_available_ports():
        return [port.device for port in list_ports.comports()]

    @staticmethod
    def find_lamp_relay(attribute, attribute_name):
        context = pyudev.Context()
        for device in context.list_devices(subsystem='tty'):
            device_node = device.device_node

            if device_node.find("USB") != -1:
                if dict(device)[attribute] == attribute_name:
                    print('Device is located on {0}'.format(device.device_node))
                    return device.device_node

        return "not found"

    @staticmethod
    def get_usb_devices():
        devices = {}
        pattern = re.compile('(ACM|USB)')

        context = pyudev.Context()
        for device in context.list_devices(subsystem='tty'):

            dev_properties = dict(device)
            port_name = dev_properties['DEVNAME']
            if pattern.search(port_name):
                vendor = dict(device)['ID_VENDOR_FROM_DATABASE']
                try:
                    devices[DEVICES_AND_VENDORS[vendor]] = port_name
                except KeyError:
                    pass

        return devices

    @staticmethod
    def get_all_devices():
        devices = {}
        devices.update(Discoverer.get_serial_devices())
        devices.update(Discoverer.get_usb_devices())
        return  devices

    @staticmethod
    def get_serial_devices():
        devices = {}

        for port in Discoverer.get_available_ports():
            print("Curr port "+port)
            try:
                device = SerialDevice(port, CAS_REQUEST) #cas sequnce
                response = device.get_response_on_request()
                if response and b'g' in response:
                    devices['cas'] = port
                    continue
                else:
                    device.redefine_query_sequence(BDU_REQUEST) #bdu sequnce
                    response = device.get_response_on_request()
                    if response and b'(kg)' in response:
                        devices['bdu'] = port
                        continue

            except serial.serialutil.SerialException:
                print ("Not all serial ports are available")

        return devices


if __name__ == '__main__':

    #print(Discoverer.get_available_ports())
    #print(Discoverer.get_serial_devices())
    #print(Discoverer.get_usb_devices())
    print(Discoverer.get_all_devices())