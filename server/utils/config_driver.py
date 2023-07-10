import yaml
import logging

class ConfigDriver:
    __instance = None

    def __new__(cls, path):
        if cls.__instance is None:
            cls.__instance = super(ConfigDriver, cls).__new__(cls)
        return cls.__instance

    def __init__(self, path):
        if hasattr(self, '__initialized'):
            return
        self.__initialized = True
        self.__path = path
    
    def read_all_settings(self):
        with open(self.__path, 'r') as file:
            try:
                config = yaml.load(file, Loader=yaml.FullLoader)
                logging.info('[ConfigDriver] Config file loaded!')
                return config
            except Exception:
                logging.error('[ConfigDriver] Config file could not be loaded!')
    
    def write(self, config_dict):
        current_config = self.read_all_settings()
        with open(self.__path, 'w') as file:
            try:
                merged_data = {**current_config, **config_dict}
                yaml.dump(merged_data, file)
                logging.info('[ConfigDriver] Config file written!')
            except Exception:
                logging.error('[ConfigDriver] Config file could not be written!')