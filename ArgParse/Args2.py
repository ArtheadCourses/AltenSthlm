
import argparse
def main():
    #Create an argument parser
    parser = argparse.ArgumentParser()

    #Add one argument to the parser
    parser.add_argument("echo")

    #Parse the arguments passed to the program
    args = parser.parse_args()

    #Print the argument
    print(args.echo)
    
if __name__ == '__main__':
    main()