def charNumber(char):
    if char.upper() in ("A","B","C"):
        return 2
    elif char.upper() in ("D","E","F"):
        return 3
    elif char.upper() in ("G","H","I"):
        return 4
    elif char.upper() in ("J","K","L"):
        return 5
    elif char.upper() in ("M","N","O"):
        return 6
    elif char.upper() in ("P","Q","R","S"):
        return 7
    elif char.upper() in ("T","U","V"):
        return 8
    elif char.upper() in ("W","X","Y","Z"):
        return 9

def telTranslate(phrase):
    tele = ""
    tele_list = phrase.split("-")
    for i in tele_list:
        tele += i
    mydigit = ""
    for i in tele:
        if i.isdigit():
            mydigit += i
        else:
            mydigit += str(charNumber(i))
    number = "{0}-{1}-{2}-{3}".format(mydigit[0],mydigit[1:4],mydigit[4:7],mydigit[7:])
    return number

def main():
    teln = input("Enter a telephone number: ")
    while teln != "":
        print("number is: {0}".format(telTranslate(teln)))
        teln = input("Enter a telephone number: ")

if __name__ == "__main__":
    main()
