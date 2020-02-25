"""
    - created at feb 03/2020 by mjghasempour
    - this package get configuration of servers and other things that thay are static from json file
        and then send value objects to top level
"""

import json

from easydict import EasyDict as edict

from .singleton import singleton
from commons.constants.app_paths import (CONFIG_PATH)


@singleton
class ConfigManager:
    def __init__(self):
        self.config_path = CONFIG_PATH
    
    def __read_config__(self):
        with open(self.config_path, 'r') as file:
            configs = json.loads(file.read().strip("\n"))
        return configs

    @property
    def get(self):
        return edict(self.__read_config__())
