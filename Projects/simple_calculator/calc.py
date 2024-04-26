"""This project aims at buliding a command line calculator
* As of now this project supports
  * Addition
  * Subtraction
  * Multiplication
  * Division
  * Modulus
Author: Santosh A 
CreatedOn: 21/Apr/2024
"""

import sys

def add(number1, number2):
  """ Fcuntion to add 2 numbers
  Args: 
    number1
    number2
  Retruns:
    sum of number1 & number2
  """
  return number1 + number2

def sub(number1, number2):
  """ Fcuntion to sub 2 numbers
  Args: 
    number1
    number2
  Retruns:
    diff of number1 & number2
  """
  return number1 - number2

def mul(number1, number2):
  """ Fcuntion to mul 2 numbers
  Args: 
    number1
    number2
  Retruns:
    product of number1 & number2
  """
  return number1 * number2

def div(number1, number2):
  """ Fcuntion to divided 2 numbers
  Args: 
    number1
    number2
  Retruns:
    division of number1 & number2
  """
  return number1 / number2

def mod(number1, number2):
  """ Fcuntion to find modulus 2 numbers
  Args: 
    number1
    number2
  Retruns:
    modulus of number1 & number2
  """
  return number1 % number2

# get arguments excluding file name
arguments = sys.argv[1::]
# print(arguments)
# get action
action = arguments[0]
# get input numbers
number1 = int(arguments[1])
number2 = int(arguments[2]) 

if action.lower() == 'add':
  result = add(number1, number2)
elif action.lower() == 'sub':
  result = sub(number1, number2)
elif action.lower() == 'mul':
  result = mul(number1, number2)
elif action.lower() == 'div':
  result = div(number1, number2)
elif action.lower() == 'mod':
  result = mod(number1, number2)
else:
  print("Incorrect Action! Actions Supported: add, sub, mul, div and mod")
  sys.exit(1)

print(result)