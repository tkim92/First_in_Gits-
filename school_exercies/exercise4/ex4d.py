def romanToDecimal(stringarg):
    if stringarg == "I":
        return 1
    elif stringarg == "V":
        return 5
    elif stringarg == "X":
        return 10
    elif stringarg == "L":
        return 50
    elif stringarg == "C":
        return 100
    elif stringarg == "D":
        return 500
    elif stringarg == "M":
        return 1000
    else:
        return 0

def subtract(stringarg_1,stringarg_2):
    if stringarg_1 == "I" and stringarg_2 == "V":
        return True
    elif stringarg_1 == "I" and stringarg_2 == "X":
        return True
    elif stringarg_1 == "X" and stringarg_2 == "L":
        return True
    elif stringarg_1 == "X" and stringarg_2 == "C":
        return True
    elif stringarg_1 == "C" and stringarg_2 == "D":
        return True
    elif stringarg_1 == "C" and stringarg_2 == "M":
        return True
    else:
        False


def main():
    total = 0
    validility = 0
    roman = input("Enter a roman numeral: ")

    i = 0
    while i < len(roman):
        if romanToDecimal(roman[i]) == 0:
            validility = -1
            i = len(roman)
        else:
            j = 1 + i
            if j != len(roman):
                if romanToDecimal(roman[i]) > romanToDecimal(roman[j]):
                    total += romanToDecimal(roman[i])
                    i += 1
                else:
                    if subtract(roman[i],roman[j]):
                        sub_amt = romanToDecimal(roman[j]) - romanToDecimal(roman[i])
                        total += sub_amt
                        i += 2
                    else:
                        validility = -1
                        i = len(roman)
            else:
                total += romanToDecimal(roman[i])
                i += 1


    if validility == 0:
        print("Decimal value is {0}".format(total))
    else:
        print("Decimal value is 0 (Invalid Roman Entered)")
#
# def main():
#     roman = input("Enter a roman numeral: ")
#     # 0 for valie -1 for invalid
#     validility = 0
#     total = 0
#     i = 0
#     while i < len(roman):
#         if romanToDecimal(roman[i]) == 0:
#             validility = -1
#             # allow it to leave the while loop and go directly to print
#         else:
#             j = i + 1
#             if j != len(roman):
#                 if subtract(roman[i],roman[j]) == True:
#                     sub_amt = romanToDecimal(roman[j]) - romanToDecimal(roman[i])
#                     # print("line 45 if I subtract...{0} and i = {1}".format(sub_amt,i))
#                     total += sub_amt
#                     # print(total)
#                 else:
#                     if romanToDecimal(roman[i]) > romanToDecimal(roman[i-1]) and i != 0:
#                         total += 0
#                         # print(total)
#                     else:
#                         # print("line 53 if I don't subract...{0} and i = {1}".format(romanToDecimal(roman[i]),i))
#                         total += romanToDecimal(roman[i])
#                         # print(total)
#             else:
#                 if subtract(roman[i-1],roman[i]) == True:
#                     sub_amt = 0
#                     # print("line 59 if I subtract...{0} and i = {1}".format(sub_amt,i))
#                     total += sub_amt
#                     # print(total)
#                 else:
#                     # print("line 63 if I don't subract...{0} and i = {1}".format(romanToDecimal(roman[i]),i))
#                     total += romanToDecimal(roman[i])
#                     # print(total)
#
#                 # print(total)
#
#         i += 1
#     if validility == 0:
#         print("Decimal value is {0}".format(total))
#     else:
#         print("Decimal value is 0 (Invalid Roman Entered)")

if __name__ == "__main__":
    main()
