
def div(a, b):
    if b == 0:
        raise ValueError("Error: Value for b can not be 0")
    result = a / b
    return result

def main():
    try:
        x = div(10, 0)
    except ValueError as e:
        print(e)
        raise
        #x = div(10, 2)
    else:
        pass
        #Will only execute if we did not get an exception
    finally:
        print("Will always print")
        #Will always execute


if __name__ == '__main__':
    main()