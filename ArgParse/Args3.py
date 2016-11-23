
import argparse

#This program will take a number as an argument and square it
#and present the result back to the user.
#Note. This version does not work
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display the sqaure of this number")

    args = parser.parse_args()

    print(args.square**2)
    
if __name__ == '__main__':
    main()