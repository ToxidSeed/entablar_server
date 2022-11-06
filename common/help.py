import configparser

def get_settings():
    config = configparser.ConfigParser()
    config.read(settings_ini_file)      