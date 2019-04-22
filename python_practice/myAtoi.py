def myAtoi(mystr):
    mylist = mystr.split()
    mymax = 2**31-1
    mymin = -2**31
    myanswer = ""
    flag = "green"

    if len(mylist) == 0:
        return 0
    else:
        myguess = mylist[0]

        i = 0
        while i < len(myguess) and flag == "green":
            if i == 0:
                if myguess[0] in ["+","-"] or myguess[0].isdigit():
                    myanswer += myguess[0]
                else:
                    return 0
            else:
                if myguess[i].isdigit():
                    myanswer += myguess[i]
                else:
                    flag = "red"
            i += 1
    try:
        finalanswer = int(float(myanswer))
    except:
        finalanswer = 0

    if finalanswer <= mymin:
        return mymin
    elif finalanswer >= mymax:
        return mymax
    else:
        return finalanswer
