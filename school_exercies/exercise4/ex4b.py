import string
# instead of doing multiple while loops, try using isdigit() isalpha()... method

def check_length(x):
    if len(x) >= 8:
        return True
    else:
        return False

def check_upper(x):
    U_count = 0
    i = 0
    while i < len(x):
        if x[i] == x[i].upper():
            U_count += 1
        i += 1

    if U_count >= 1:
        return True
    else:
        return False

def check_digit(x):
    D_count = 0
    j = 0
    while j < len(x):
        if x[j].isdigit() == True:
            D_count += 1
        j += 1

    if D_count >= 2:
        return True
    else:
        return False

def check_pucs(x):
    puncs = string.punctuation
    P_count = 0
    i = 0
    while i < len(x):
        if x[i] in puncs:
            P_count += 1
        else:
            P_count = P_count
        i += 1

    # just return P_count

    if P_count >= 1:
        return True
    else:
        return False

def passwordCheck(x):
    if check_length(x) and check_upper(x) and check_digit(x) and check_pucs(x):
        return True
    else:
        return False

def main():
    password = input("enter a password: ")
    password_list = list(password)
    # print("lentgh OK? {0}".format(check_length(password_list)))
    # print("upper OK? {0}".format(check_upper(password_list)))
    # print("digit OK? {0}".format(check_digit(password_list)))
    # print("puncs OK? {0}".format(check_pucs(password_list)))
    # passwordCheck(password_list)

    if passwordCheck(password_list) == True:
        print("{0} is a valid".format(password))
    else:
        while passwordCheck(password_list) == False:
            print("{0} is not a valid password".format(password))
            password = input("enter a password: ")
            password_list = list(password)
            passwordCheck(password_list)

        if passwordCheck(password_list) == True:
            print("{0} is a valid password".format(password))

if __name__ == "__main__":
    main()
