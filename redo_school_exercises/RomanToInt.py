import numpy as np

# Ex4.C Roman Numerals
def romanToDecimal(stringarg):
    mydict = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    mydict2 = {"IV":-2, "IX":-2, "XL":-20, "XC":-20, "CD":-200, "CM":-200}

    sum_amt = 0
    for i in stringarg:
        if i in mydict:
            sum_amt += mydict[i]

    for romans in mydict2:
        if romans in stringarg:
            sum_amt += mydict2[romans]
    return sum_amt

def main():
    myroman = input("Enter a roman numberal: ")
    print("Decimal value is: {0}".format(romanToDecimal(myroman)))

if __name__ == "__main__":
    main()
