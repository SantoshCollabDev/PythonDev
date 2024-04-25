"""
This module will have resulable numeric functions
encountered during my python learning
"""

def is_even(number: int):
  """ This function determines if the number is even or odd

  Args:
    number: number to be checked

  Retruns:
    True if even, False otherwise
  """
  if number <=0:
    return False
  
  return number % 2 == 0

def factors(number: int):
  """ This function returns a lsit of factors of the given number

  Args:
    number: number for which factors to be found out

  Returns:
    a list of factors  
  """
  factors_list = []
  half_of_number = number // 2 + 1
  for index in range(1,half_of_number):
    if number % index == 0:
      factors_list.append(index)
  return factors_list