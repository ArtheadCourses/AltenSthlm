class MyException(Exception):
    def __init__(self, value, location, msg):
        super().__init__()
        self.value = value
        self.location = location
        self.msg = msg

    def __str__(self):
        return "There was an error in {0} with code: {1}. Message: {2}".\
            format(self.location, self.value, self.msg)


def div(a, b):
    if b == 0:
        raise MyException(32, "div()", "The second argument (b) can not be 0")
    result = a / b
    return result

def main():
    try:
        x = div(10, 0)
    except MyException as e:
        print(e)
        x = div(10, 2)
    else:
        pass
        #Will only execute if we did not get an exception
    finally:
        print("Will always print")
        #Will always execute
    print(x)

if __name__ == '__main__':
    main()