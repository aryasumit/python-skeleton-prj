"""
This file performs the Extract, transform and load logic to create and save the features required for the model
"""

import logging
import pandas as pd

from utils.file_path_helper import get_path_raw_file
from utils.validator import is_non_empty_and_has_columns

# Get the logger object to be used this file
log = logging.getLogger('etl')


def transform():
    customer_df = pd.read_csv(get_path_raw_file("customer/cust_data.csv"))
    is_non_empty_and_has_columns(customer_df, ['id', 'name', 'age'])
    log.info(f'The customer row count is: {customer_df.shape[0]}')
