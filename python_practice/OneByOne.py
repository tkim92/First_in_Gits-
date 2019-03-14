# def sorting(mylist):
#     adfadf

def main():
    howmany = int(input())
    number_list = []

    for i in range(howmany):
        mynumber = int(input("Choose randome number: "))
        number_list.append(mynumber)

    number_list.sort()
    # number_list.sort(reverse == False)
    for i in number_list:
        print(i)


if __name__ == "__main__":
    main()
