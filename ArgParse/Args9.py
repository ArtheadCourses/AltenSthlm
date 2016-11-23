
import argparse

#Add two arguments, base and exponent
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("base", help="the base", type=int)
    parser.add_argument("exponent", help="the base", type=int)
    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="increase output verbosity")

    args = parser.parse_args()
    answer = args.base ** args.exponent
    if args.verbose >= 2:
        print("{0} to the power of {1} equals {2}".format(args.base, args.exponent, answer))
    elif args.verbose == 1:
        print("{0}^{1} = {2}".format(args.base, args.exponent, answer))
    else:
        print(answer)
    
if __name__ == '__main__':
    main()