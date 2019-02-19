def int2alp(n):
    if n == 10:
        return "A"
    elif n == 11:
        return "B"
    elif n == 12:
        return "C"
    elif n == 13:
        return "D"
    elif n == 14:
        return "E"
    elif n == 15:
        return "F"
    else:
        return str(n)

def convertBase(n,base):
    if n//base == 0:
        newstr = int2alp(n%base)
    else:
        newstr = convertBase(n//base,base) + int2alp(n%base)
    return newstr

def main():
    yourn = int(input("Enter your n number: "))
    yourbase = int(input("Enter your base number: "))
    print(convertBase(yourn,yourbase))

if __name__ == "__main__":
    main()


# TA Answer
#
# def convertBase(n, base):
#     conversionString = "0123456789ABCDEFG"
#     if n//base == 0: #base case--n<base, so can find digit simply from
#                      #   indexing conversionString
#         return conversionString[n]
#     else: #recursive step--result of converting the rest (to get the higher
#           #   "digits") plus the conversion of the current digit
#         return convertBase(n//base, base) + conversionString[n%base]
