def int2str(n):
    if n//10 == 0:
        return str(n)
    return int2str(n//10) + str(n%10)

def main():
    aint = int(input("Enter your integer: "))

    print(int2str(aint))


if __name__ == "__main__":
    main()
