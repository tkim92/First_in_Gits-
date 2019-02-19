
# Ex4.A: Binary to Integer

def binaryToInt(binarystring):
    total = 0
    for index, number in enumerate(binarystring):
        total += int(number) * 2 ** (len(binarystring) - 1 - index)
    return total

def main():

    continuity = True

    while continuity == True:
        entered_value = input("enter a binary value: ")
        print("value is {0}".format(binaryToInt(entered_value)))
        continuity_ask = input("continue? (y/n): ")
        if continuity_ask == "n":
            continuity = False


if __name__ == '__main__':
    main()
