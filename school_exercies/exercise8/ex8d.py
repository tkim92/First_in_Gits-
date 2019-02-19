def telTranslate(astr):
    chTonum = {("A","B","C"):2, ("D","E","F"):3, ("G","H","I"):4, ("J","K","L"):5, ("M","N","O"):6, ("P","Q","R","S"):7, ("T","U","V"):8, ("W","X","Y","Z"):9}
    number = ""
    for i in astr:
        i = i.upper()
        for keys in chTonum:
            if i in keys:
                number = number + str(chTonum[keys])
        if i.isdigit():
            number = number + i

    if len(number) == 10:
        print("Numeric telephone number is: {0}-{1}-{2}".format(number[:3],number[3:6],number[6:]))
    elif len(number) == 7:
        print("Numeric telephone number is: {0}-{1}".format(number[:3],number[3:]))
    else:
        print("Invalid number!")

def main():

    putnum = input("Enter a telephone number(press enter to quite) : ")

    while putnum != "":
        telTranslate(putnum)
        putnum = input("Enter a telephone number(press enter to quite) : ")

if __name__ == "__main__":
    main()
