""" This module is used for calculating
systematic investments

Assumptins:
  This calculator as of now expects the investment is done monthly
"""

def returns(
    invested_amount,
    return_rate,
    total_period_years):
    """
    This method calcualtes returns of monthly siop
    """
    n = total_period_years * 12
    i = (return_rate/12)/100
    future_value = invested_amount * (((1+i) ** (n) - 1)/i) * (1 + i)
    return future_value
