# You can just use ** instead of making two_power function.

def two_power(n):
    value = 1
    if n != 0:
        for i in range(0,n):
            value *= 2
    else:
        value = 1
    return value

def binaryToInt(binarystring):
    total = 0
    binary_list = list(binarystring)
    i = 0
    while i < len(binary_list):
        # Note: binary_list[i] 는 type이 list라서 list * int 해버리면 list가 늘어날뿐임
        # 그래서 저거 int화 시켜주는것이 필수.
        convert_value = int(binary_list[i]) * two_power(len(binary_list)-i-1)
        i += 1
        total += convert_value
    return total

def continuation(yn):
    if yn == "y":
        return True
    else:
        return False

def main():
    your_string = input("Enter a binary value: ")
    print("value is: {0}".format(binaryToInt(your_string)))

    yes_no = input("continue? (y/n): ")

    while continuation(yes_no):
        # if you have boolean function, while loop basically impose True.
        your_string = input("Enter a binary value: ")
        print("value is: {0}".format(binaryToInt(your_string)))
        yes_no = input("continue? (y/n): ")


if __name__ == "__main__":
    main()
