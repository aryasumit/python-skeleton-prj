"""
This file contains utility functions to load configuration settings present in the YAML configuration files
"""
import os
import logging
import yaml
from functools import reduce

# Inferring current path
# current_path = os.path.abspath(os.path.dirname(__file__))
current_path = "C:/Data/Portfolio/python-skeleton-prj/src"
os.chdir(current_path)
config_file_path = os.path.join(current_path, "..", "configs", "file_paths.yml")

log = logging.getLogger('config_reader')

def get_config(key_list):
    """
    Loads the file_paths yaml configuration file and returns the required
    configuration property from it
    Params: key_list - A list containing the key of the configuration to be read
    from the file. In case of a hierarchical key, it should be a list like
    ['parent', 'child']

    Returns: The value read from from the configurations file for the given key
    """
    if not os.path.exists(config_file_path):
        log.error('File paths Config file not found at: ' + config_file_path)
        raise Exception('Config file not found at: ' + config_file_path)

    with open(config_file_path) as file:
        configs = yaml.load(file, Loader = yaml.FullLoader)
        try:
            value = reduce(dict.get, key_list, configs)
        except:
            log.error('{} not found in config file: {}'.format(str(key_list), config_file_path))

    if not value:
        log.error('{} key not found in config file: ()'.format(str(key_list), config_file_path))
        raise Exception('{} key not found in config file: ()'.format(str(key_list), config_file_path))

    return value
