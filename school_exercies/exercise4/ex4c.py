# try to use the idea of ..... 1 * -1 * 1 * -1 .....


def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def altSum(values):

    total = values[0]

    i = 1
    while i < len(values):
        if even(i) == True:
            total += values[i]
        else:
            total -= values[i]
        i += 1

    return total

def main():

    value_list = []
    sum_value = 0

    num = input("Enter a floating point value: ")

    if num == "":
        print("The alternation sum is: 0.0")

    else:
        while num != "":
            num = float(num)
            value_list.append(num)
            sum_value = altSum(value_list)
            num = input("Enter a floating point value: ")
    print("The alternatig sum is: {0}".format(sum_value))

if __name__ == '__main__':
    main()
