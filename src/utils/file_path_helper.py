"""
Contains utility functions to construct paths to files inside the various data sub-folders
"""

import os

from utils.config_reader import get_config


def get_path_raw_file(relative_path):
    return os.path.join(get_config(['data', 'raw']), relative_path)


def get_path_intermediate_file(relative_path):
    return os.path.join(get_config(['data', 'intermediate']), relative_path)


def get_path_processed_file(relative_path):
    return os.path.join(get_config(['data', 'processed']), relative_path)
