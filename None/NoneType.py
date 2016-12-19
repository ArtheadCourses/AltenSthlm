def test_func(name, name_list=None):
    if not name_list:
        name_list = []
    name_list.append(name)
    print(name_list)


def main():
    test_list = ['Eric']
    test_func('Anna')
    test_func('Peter', test_list)
    test_func('John')


if __name__ == '__main__':
    main()
