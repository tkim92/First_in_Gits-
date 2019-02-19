def series(n):
    if n <= 1:
        return 0
    return n**(n-1)/(n-1) + series(n-1)

def main():
    num = int(input("Enter your number: "))

    print(series(num))

if __name__ == "__main__":
    main()
