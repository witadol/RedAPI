import configparser
from redlib import Discoverer
CONFIG_FILE = 'config.ini'

config = configparser.ConfigParser()
config['PORTS'] = Discoverer.get_available_devices()
with open(CONFIG_FILE, 'w') as configfile:
    config.write(configfile)