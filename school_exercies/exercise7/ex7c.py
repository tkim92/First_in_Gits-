def numDigits(n):
    if n//10 == 0 or n//10 == -1:
        return 1
    return 1 + numDigits(n//10)

def main():
    num = int(input("Enter your number: "))

    print(numDigits(num))

if __name__ == "__main__":
    main()
