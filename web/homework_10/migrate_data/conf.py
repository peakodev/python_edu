import configparser
import os


script_dir = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(script_dir, 'config.ini')
config = configparser.ConfigParser()
config.read(config_file)
