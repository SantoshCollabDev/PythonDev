""" This module will have functions
calculate lumpsum returns

Author:

Date:
"""
def returns(principal, 
            interest_rate, 
            time_in_years, 
            n=1):
    """ This function calculates lumpsum returns
    """
    result = principal * ( 1 + ((interest_rate/100)/n)) ** (n * time_in_years)
    return result



