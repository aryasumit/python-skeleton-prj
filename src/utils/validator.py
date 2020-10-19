"""
Utility functions to validate dataframe
"""

# Importing required Libraries
import logging

log = logging.getLogger('validator')

def is_non_empty_and_has_columns(df, columns):
    """
    Asserts if the specified columns exist in the given dataframe
    Params:
    df - The dataframe which should be inspected
    columns - The list of column names to look for in the dataframe

    Returns: True if the specified columns exist, raises Exception otherwise
    """
    if df.empty:
        log.error('Dataframe is empty!')
        raise Exception('Dataframe is empty!')

    if not set(columns).issubset(set(df.columns)):
        log.error('Missing columns! Required columns in dataframe: {}, Found columns: {}'.format(str(columns),
                                                                                                     str(df.columns)))
        raise Exception('Missing columns! Required columns in dataframe = {}, Found columns: {}'.format(str(columns),
                                                                                                        str(df.columns)))

    log.info('Dataframe validation successful!')
