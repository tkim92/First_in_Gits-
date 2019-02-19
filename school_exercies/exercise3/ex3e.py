

def gcd(a,b):

    a = abs(int(a))
    b = abs(int(b))

    if b > a:
        a, b = b, a
        # @@@@@@ very good to know! a,b = b,a !!

    while b != 0:
        new_a = b
        new_b = a % b
        a = new_a
        b = new_b
    return new_a


def main():

    a = (input("Enter your first value: "))

    while a != "":

        b = (input("Enter your second value: "))
        print("The GCD of " + str(a) + " and " + str(b) + " is " + str(gcd(a,b)))
        a = (input("Enter your first value: "))


if __name__ == "__main__":
    main()
