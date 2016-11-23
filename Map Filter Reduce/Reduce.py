from functools import reduce

def get_max(a, b):
    if a > b:
        return a
    else:
        return b

def get_sum(a, b):
    return a + b

def main():
    list_of_numbers = [23, 143, 13, 4, 33, 9, 16, 97]
    max = reduce(get_max, list_of_numbers)
    print(max)

    sum = reduce(get_sum, list_of_numbers)
    print(sum)

if __name__ == '__main__':
    main()