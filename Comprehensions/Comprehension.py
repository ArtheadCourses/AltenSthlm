
def main():
    num_list = [1, 2, 3, 4, 5, 6, 7]
    non_comp_list = []
    for value in num_list:
        if value != 3:
            non_comp_list.append(value**2)
        else:
            non_comp_list.append(value)

    print(non_comp_list)

    comp_list = [value**2 if value != 3 else value**3 for value in num_list]
    print(comp_list)

if __name__ == '__main__':
    main()