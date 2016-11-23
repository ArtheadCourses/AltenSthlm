
import argparse

#Add a new optional argument -v
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display the sqaure of this number", type=int)
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")

    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbose:
        print("The square of {0} equals {1}".format(args.square, answer))
    else:
        print(answer)
    
if __name__ == '__main__':
    main()