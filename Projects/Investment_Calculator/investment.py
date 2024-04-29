import argparse
from calculators.lumpsum import returns as lumpsum_returns
from calculators.sip import returns as sip_returns
from persistence.csv_file import write_result
from decorators.storage import store_in_csv

# def store_results(principal, time, rate, 
#                  investment_type, future_value):
#     """ this
#     """
#     write_result(principal, rate, time, 
#                  investment_type, future_value)

@store_in_csv   
def print_result(principal, time, rate, 
                 investment_type, future_value):
    """ This method prints results
    """
    # store_results(principal,time,rate,investment_type, future_value)
    print(f"for your {investment_type} investment of {principal} will be {round(future_value,2)} in next {time} years")

def argument_parser():
    """ This method creates an argument parser
    """
    parser = argparse.ArgumentParser(
      description="Investment Calculator")
    # parser.add_argument('lumpsum', type=str)
    parser.add_argument(
        'investment_type', 
        type=str,
        choices = ['lumpsum','sip'],
        help = "Investment type"
        )
    parser.add_argument(
        '-p',
        '--principal',
        type=int,
        required=True,
        help = "present value of investment"
        )
    parser.add_argument(
        '-r',
        '--rate',
        type=int,
        required=True,
        help = 'expected yearly returns'
        )
    parser.add_argument(
        '-t',
        '--time',
        type=int,
        required=True,
        help='time in years')
    return parser

if __name__ == "__main__":
    args = argument_parser().parse_args()
    # print(args)
    # result = lumpsum(
    #     principal = args.principal,
    #     interest_rate = args.interest_rate,
    #     time_in_years = args.time_period
    # )
    # print(f"Your Investment of {args.principal} will be {result} in next {args.time_period} years")
    if args.investment_type == 'lumpsum':
        result = lumpsum_returns(
            principal = args.principal,
            interest_rate = args.rate,
            time_in_years = args.time
        )
        print_result(args.principal,args.time, args.rate,args.investment_type,result)           
        # print(f"Your Investment of {args.principal} will be {round(result,2)} in next {args.time} years")
    elif args.investment_type == 'sip':
         result = sip_returns(
            invested_amount = args.principal,
            return_rate = args.rate,
            total_period_years = args.time
         )
         print_result(args.principal,args.time, args.rate,args.investment_type,result)           
        #  print(f"Your Investment of {args.principal} will be {round(result,2)} in next {args.time} years")
