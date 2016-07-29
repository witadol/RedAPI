#! /usr/bin/env python3
import configparser
import os
from redlib import Discoverer

CONFIG_FILE = 'config.ini'
script_directory = os.path.dirname(__file__)
path_to_file = os.path.join(script_directory, CONFIG_FILE)

config = configparser.ConfigParser()
config['PORTS'] = Discoverer.get_all_devices()
with open(path_to_file, 'w') as configfile:
    config.write(configfile)