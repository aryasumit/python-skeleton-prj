# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:19:43 2020

@author: Arya Sumit
"""

import logging
from utils.file_path_helper import get_path_processed_file

# Get the logger object to be used this file
log = logging.getLogger('write output file')

def save_output():
    global cust_age_gt_forty
    cust_age_gt_forty.to_csv(get_path_processed_file("cust_age_gt_forty.csv"))