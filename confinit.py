import configparser
CONFIG_FILE = 'config.ini'

config = configparser.ConfigParser()
config['PORTS'] = {'cas': '/dev/ttyS0',
                     'bdu': 'dev/ttyS1'}
with open(CONFIG_FILE, 'w') as configfile:
    config.write(configfile)