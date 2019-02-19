def power(a,n):
    if n < 1:
        return 1
    return a * power(a,n-1)

def main():
    base = int(input("Enter your base number: "))
    apv = int(input("Enter your power number: "))

    print(power(base,apv))

if __name__ == "__main__":
    main()
