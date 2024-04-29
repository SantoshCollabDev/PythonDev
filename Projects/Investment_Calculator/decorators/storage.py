""" This module hsa code for decarators
"""
from persistence.csv_file import write_result

def store_in_csv(func):
    """ This decorator write results to csv file
    """
    def store_results(*args,**kwargs):
        write_result(*args,**kwargs)
        func(*args,**kwargs)
    return store_results
