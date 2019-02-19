# making it more readable.

def perfect(n):
    i = 1
    # m refers to the sum amount of divisors
    m = 0

    while i < n:
        if n % i == 0:
            m += i
            i += 1
        else:
            # m = m
            i += 1
    if m == n:
        return True
    else:
        return False

def main():
    a = int(input("Enter lower bound: "))
    b = int(input("Enter upper bound: "))

    for i in range(a,b+1):
        if perfect(i) == True:
            print(i)

            # Can main function be a non pure function?
            #i.e. Can I print i directly inside the main function?

if __name__ == "__main__":
    main()
