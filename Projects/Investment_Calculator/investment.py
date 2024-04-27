import argparse

from calculators.lumpsum import lumpsum

def argument_parser():
    """ This method creates an argument parser
    """
    parser = argparse.ArgumentParser(
      description="Investment Calculator")
    parser.add_argument('lumpsum', type=str)
    parser.add_argument('principal',
                        type=int, 
                        help = "present value of investment")
    parser.add_argument('interest_rate',
                        type=int,
                        help = 'rate of interest')
    parser.add_argument('time_period',
                        type=int,
                        help='time in years')
    return parser

if __name__ == "__main__":
    args = argument_parser().parse_args()
    print(args)
    result = lumpsum(
        principal = args.principal,
        interest_rate = args.interest_rate,
        time_in_years = args.time_period
    )
    print(f"Your Investment of {args.principal} will be {result} in next {args.time_period} years")
