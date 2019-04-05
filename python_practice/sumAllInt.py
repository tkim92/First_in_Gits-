
def sumAll(myint):
    if myint == 0:
        return 0
    else:
        return myint%10 + sumAll(myint//10)


def main():
    yournum = int(input("정수입력해라: "))
    print(sumAll(yournum))


if __name__ == "__main__":
    main()
