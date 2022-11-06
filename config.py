import os
import configparser
from common.AppException import AppException

app_path = os.path.dirname(__file__)

def get_settings():
    settins_file = os.path.join(app_path,"config/settings.cfg")
    config = configparser.ConfigParser()
    config.read(settins_file)
    return config
