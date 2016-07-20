#! /usr/bin/env python3
import serial
import time
from serial.tools import list_ports
EMPTY_PORT_ERROR = '!port is empty'
UNAVAILABLE_PORT_ERROR = '!port is empty'


class Cas:
    BAUD_RATE = 9600
    READ_TIMEOUT = 0.085
    QUERY_SEQUENCE = '\x00'.encode()

    def __init__(self, port_name):
        connection = serial.Serial(port_name)
        connection.baudrate = Cas.BAUD_RATE
        connection.timeout = Cas.READ_TIMEOUT
        self.connection = connection

    def get_response(self):
        connection = self.connection
        try:

            result = connection.readline()
            while result:
                if len(result) == 22:
                    return result[0:2] + result[11:21]
                result = connection.readline()
            else:
                return EMPTY_PORT_ERROR
        except serial.serialutil.SerialException:
            return UNAVAILABLE_PORT_ERROR


class ControlScales:
    BAUD_RATE = 9600
    READ_TIMEOUT = 0.05
    QEURY_SEQUENCE = '\x02B\x03'.encode('ascii')

    def __init__(self, port_name):
        connection = serial.Serial(port_name)
        connection.baudrate = Cas.BAUD_RATE
        connection.timeout = Cas.READ_TIMEOUT
        self.connection = connection

    def get_response(self):
        connection = self.connection
        try:
            if connection.readline():
                return connection.readline()[1:12]
            else:
                return EMPTY_PORT_ERROR
        except serial.serialutil.SerialException:
            return UNAVAILABLE_PORT_ERROR


class Discoverer:
    @staticmethod
    def get_available_ports():
        return [port.device for port in list_ports.comports()]

    @staticmethod
    def get_available_devices():
        devices = {}

        for port in Discoverer.get_available_ports():
            try:
                connection = serial.Serial(port)
                connection.baudrate = 9600
                connection.timeout = 0.1

                connection.write(Cas.QUERY_SEQUENCE)
                response = connection.readline()
                if response and b'g' in response:
                    devices['cas'] = port
                    continue
                else:
                    connection.write(ControlScales.QEURY_SEQUENCE)
                    response = connection.readline()
                    if response and b'(kg)' in response:
                        devices['bdu'] = port
                        continue

            except serial.serialutil.SerialException:
                print ("Not all serial ports are available")

        return devices


if __name__ == '__main__':

#    print(Discoverer.get_available_ports())
    print(Discoverer.get_available_devices())