
def div(a, b):
    result = a / b
    return result

def main():
    try:
        x = div(10, 0)
    except ZeroDivisionError:
        x = div(10, 2)
   # else:
    print(x)
    
if __name__ == '__main__':
    main()