"""
This file sets up the logging. Adds both file logger and console logger.
"""

import os
import logging
from logging. handlers import TimedRotatingFileHandler

def setup(log_level = logging.INFO):
    """
    Setting the console and file loggers with required format and setting log level
    :return:
    """
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    root_logger = logging.getLogger()

    # Setting root Logging Level. to INFO by default
    root_logger.setLevel(log_level)

    # Creating the rotating file Logging handler and enabling it
    current_path = os.path.abspath(os.path.dirname(__file__))
    rotating_handler = TimedRotatingFileHandler(os.path.join(current_path, '..', '..', 'logs', 'app.log'),
                                                when='midnight', interval=1)
    rotating_handler.suffix = '%Y%m%d'
    rotating_handler.setFormatter(log_formatter)
    root_logger. addHandler(rotating_handler)

    # Creating the console Logging handler and enabling it
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    logging.info('Successfully setup logger')
