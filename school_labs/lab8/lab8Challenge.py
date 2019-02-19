def gcd(a,b):
    if a < b:
        a,b = abs(b),abs(a)
    if b == 0:
        return a
    return gcd(b,a%b)

def main():
    int1 = int(input("Enter first integer value: "))
    int2 = int(input("Enter second integer value: "))

    print("Your integers are {0} and {1}, and their GCD is {2}.".format(int1,int2,gcd(int1,int2)))

if __name__ == "__main__":
    main()
