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

def print_usage():
    """ This function prints usage
    """
    print("""Usage: python calc.py <action> <number1> <number2>
        action: add | sub | mul | div | mod
        number1 is integer
        number2 is integer
        """)


def is_int(value):
    """ This is to check if numeric arguments
    """
    try:
        int_value = int(value)
    except ValueError:
        return False
    return True

def validate_arguments(arguments):
    """ This function validates arguments and displays error messages to the user
    
    Arguments: arguments

    Returns:
      True if the arguments are valid, False otherwise
    """
    if len(arguments) != 3:
        print("Incorrect number of arguments")
        print_usage()
        return False
    valid_actions = ('add','sub','mul','div','mod')
    if arguments[0].lower() not in valid_actions:
        print("Invalid Action")
        print_usage()
        return False
    if not is_int(arguments[1]) and is_int(arguments[2]):
        print("pass integers only")
        print_usage()
        return False
    return True

def main(arguments):
    """ This function executes when the file is called directly
    Arguments:
      agruments
    """
    if not validate_arguments(arguments):
        sys.exit(1)

    # get arguments excluding file name
    # arguments = sys.argv[1::]
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

if __name__ =="__main__":
    # print(sys.argv[1::])
    main(sys.argv[1::])
