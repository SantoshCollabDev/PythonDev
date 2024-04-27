import argparse

from calculators.lumpsum import lumpsum

def argument_parser():
    """ This method creates an argument parser
    """
    parser = argparse.ArgumentParser(
      description="Investment Calculator")
    # parser.add_argument('lumpsum', type=str)
    parser.add_argument(
        'investment_type', 
        type=str,
        choices = ['lumpsum'],
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
        help = 'rate of interest'
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
        result = lumpsum(
            principal = args.principal,
            interest_rate = args.rate,
            time_in_years = args.time
        )
        print(f"Your Investment of {args.principal} will be {result} in next {args.time} years")