""" Investment Calculator
"""
import sys

def calc_interest_amount(p, ri, t):
    """ check arguments
    """
    interest_amount = p + ri + t
    return interest_amount

def calc_total_amount(pa, ia):
    """ check arguments
    """
    total_amount =  pa + ia
    return total_amount

def print_usage():
    """ This function prints usage
    """
    print("""Usage: python investment.py <action> <total_investment> <interest-rate> <time-period>
        action: lumpsum | sip
        total_investment : Integer / Float
        interest-rate : Integer / Float
        time-period : Integer / Float
        """)

def is_numeric(value):
    """ check numeric
    """
    try:
        int(value) or float(value)
    except ValueError:
        print("Principle, rate-of-interest, Period should be numeric")
        return False
    return True

def validate_arguments(arguments):
    """ check arguments
    """
    if len(arguments) != 4:
        print("Incorect number of arguments")
        print_usage()
        return False
    valid_actions = ('lumpsum','sip')
    if arguments[0].lower() not in valid_actions:
        print("Invalid Action")
        print_usage()
        return False
    if not (is_numeric(arguments[1]) and is_numeric(arguments[2]) and is_numeric(arguments[3])):
        print("pass numeric values only")
        print_usage()
        return False 
    return True

def main(arguments):
    """ Calculate Lumpsum
    """
    if not validate_arguments(arguments):
        sys.exit(1)

    action = arguments[0]
    invest_amt = arguments[1]
    interest_rate = arguments[2]
    time_period = arguments[3]

    if action.lower() == 'lumpsum':
        interest_amt = calc_interest_amount(invest_amt, interest_rate, time_period)
        total_value = calc_total_amount(invest_amt, interest_amt)
    elif action.lower() == 'sip':
        interest_amt = calc_interest_amount(invest_amt, interest_rate, time_period)
        total_value = calc_total_amount(invest_amt, interest_amt)
    else:
        print("Incorrect Action! Actions Supported: lumpsum, sip")
        sys.exit(1)
    print(invest_amt)
    print(interest_amt)
    print(total_value)

if __name__ == "__main__":
    main(sys.argv[1::])