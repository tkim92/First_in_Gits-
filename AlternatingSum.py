import numpy as np



# Ex4.C Alternating Sum

def altSum(values_in_list):
    altsum = 0
    for index, value in enumerate(values_in_list):
        if index%2 == 0:
            altsum += value
        else:
            altsum -= value
    return altsum

def main():
    mylist = []
    continuity = True
    while continuity == True:
        myvalue = input("Enter a floating point value: ")
        if myvalue == "":
            continuity = False
        else:
            mylist.append(float(myvalue))

    print("The alternating sum is {0}: ".format(altSum(mylist)))


if __name__ == "__main__":
    main()
