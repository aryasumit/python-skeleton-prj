"""
This is the main file that can be executed to run the whole pipeline end-to-end
"""

import logging

from utils import logger
logger.setup()

from data_prep.etl import transform

# Getting the logger to be used for this file
log = logging.getLogger('pipeline')


def main():
    # Invoke ETL and feature engineering functions
    log.info("Invoking the transform function")
    transform()

    # Invoke modeling functions
    log.info("Invoking the modeling function")

    # Invoke final functions to save model outputs
    log.info("Invoking the save output function")


if __name__ == "__main__":
    main()
