#! /usr/bin/env python3
import serial
from serial.tools import list_ports
EMPTY_PORT_ERROR = '!port is empty'
UNAVAILABLE_PORT_ERROR = '!port is empty'


class SerialDevice():

    def create_connection(self):
        connection = serial.Serial(self.port_name)
        connection.baudrate = self.BAUD_RATE
        connection.timeout = self.READ_TIMEOUT
        return connection

    def get_response(self):
        connection = self.create_connection()
        connection.write(self.QUERY_SEQUENCE)
        return connection.readline()


class Cas(SerialDevice):

    def __init__(self, port_name):
        self.port_name = port_name
        self.BAUD_RATE = 9600
        self.READ_TIMEOUT = 0.05
        self.QUERY_SEQUENCE = '\x00'.encode()

    def get_formatted_response(self):
        try:
            result = self.get_response()
            if result:
                return (result[0:2] + result[11:20]).decode()
            else:
                return EMPTY_PORT_ERROR
        except serial.serialutil.SerialException:
            return UNAVAILABLE_PORT_ERROR


class ControlScales(SerialDevice):

    def __init__(self, port_name):
        self.port_name = port_name
        self.BAUD_RATE = 9600
        self.READ_TIMEOUT = 0.05
        self.QUERY_SEQUENCE = '\x02B\x03'.encode('ascii')

    def get_formatted_response(self):
        try:
            result = self.get_response()
            if result:
                return result[4:15].decode()
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
            print("Curr port "+port)
            try:
                response = Cas(port).get_response()
                if response and b'g' in response:
                    devices['cas'] = port
                    continue
                else:
                    response = ControlScales(port).get_response()
                    if response and b'(kg)' in response:
                        devices['bdu'] = port
                        continue

            except serial.serialutil.SerialException:
                print ("Not all serial ports are available")

        return devices


if __name__ == '__main__':

    print(Discoverer.get_available_ports())
    print(Discoverer.get_available_devices())