def div_by_3(n):
    return n % 3 == 0

def main():
    list_of_numbers = [23, 143, 13, 4, 33, 9, 16, 97]
    #result = list(filter(div_by_3 , list_of_numbers))
    #result = list(filter(lambda n: n % 3 == 0, list_of_numbers))
    result = [n for n in list_of_numbers if n % 3 == 0]
    print(result)

    result = [n**2 for n in list_of_numbers if n % 3 == 0]
    result2 = list(map(lambda n: n**2, filter(lambda n: n % 3 ==0, list_of_numbers)))
    print(result)
    print(result2)

if __name__ == '__main__':
    main()