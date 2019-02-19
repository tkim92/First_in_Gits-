part 1

def mul(a,b):
    i = 1
    m = 0
    if a > b:
        while i <= b:
            m += a
            i += 1
        return m
    else:
        while i <= a:
            m += b
            i += 1
        return m

def main():
    a = int(input("Enter your first integer: "))
    b = int(input("Enter your second integer: "))
    print(mul(a,b))

if __name__ == "__main__":
    main()


def emul(a,b):
    if a >= b:
        big = a
        small = b
    else:
        big = b
        small = a

    product = 0

    while small != 0:

        if small%2 == 0:
            product = product
        else:
            product += big

        big *= 2
        small //= 2
    return product

def main():
    a = int(input("Enter your first integer: "))
    b = int(input("Enter your second integer: "))
    print(emul(a,b))

if __name__ == "__main__":
    main()
