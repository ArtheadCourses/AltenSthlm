
import argparse

#Add two verbose levels
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display the sqaure of this number", type=int)
    parser.add_argument("-v", "--verbose", type=int, choices=[0,1,2],
                        help="increase output verbosity")

    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbose == 2:
        print("The square of {0} equals {1}".format(args.square, answer))
    elif args.verbose == 1:
        print("{0}^2 = {1}".format(args.square, answer))
    else:
        print(answer)
    
if __name__ == '__main__':
    main()