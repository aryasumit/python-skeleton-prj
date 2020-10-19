# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:14:00 2020

@author: Arya Sumit
"""

import logging

# Get the logger object to be used this file
log = logging.getLogger('process data')

def filter_age_gt_forty():
    global customer_df
    global cust_age_gt_forty
    cust_age_gt_forty = customer_df[customer_df['age']>40]