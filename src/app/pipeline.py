"""
This is the main file that can be executed to run the whole pipeline end-to-end
"""

import logging

from utils import logger
logger.setup()

from data_prep.etl import transform
from data_prep.process_data import filter_age_gt_forty
from data_prep.write_output import save_output

# Getting the logger to be used for this file
log = logging.getLogger('pipeline')

def main():
    # Invoke ETL and feature engineering functions
    log.info("Invoking the transform function")
    transform()

    # Invoke modeling functions
    log.info("Invoking the modeling function")
    filter_age_gt_forty()
    
    # Invoke final functions to save model outputs
    log.info("Invoking the save output function")
    save_output()


if __name__ == "__main__":
    main()
