import add_module
from add_module import add
from add_module import add as add2
from add_module import * #Never use this version

def main():
    #Uses import add_module
    print(add_module.add(3,6))
    #Uses from add_module import add
    print(add(4,5))
    #Uses from add_module import add as add2
    print(add2(1,3))



if __name__ == '__main__':
    main()