""" This module hsa code for decarators
"""
from persistence.csv_file import write_result
from persistence.json_file import write_results as json_write

def store_in_csv(func):
    """ This decorator write results to csv file
    """
    def store_results(*args,**kwargs):
        write_result(*args,**kwargs)
        func(*args,**kwargs)
    return store_results

def store_in_json(func):
    """ This decorator write results to csv file
    """
    def store_results(*args,**kwargs):
        json_write(*args,**kwargs)
        func(*args,**kwargs)
    return store_results