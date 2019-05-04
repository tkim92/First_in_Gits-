def letterCombinations(digits):
    letterlist = []
    a = "abcdefghijklmnopqrstuvwxyz"
    mydigits = [each_digit for each_digit in "23456789"]
    myletters = [a[myindex:] if myindex == 21 else a[myindex:myindex+3] for myindex in [0,3,6,9,12,15,18,21]]
    mydict = dict(zip(mydigits,myletters))
    mytuple = zip(mydigits,myletters)


    #
    # if len(digits) == 1:
    #     for i in mydict[digits]:
    #         letterlist.append(i)
    # else:
    #
    #     z = 0
    #     while z < len(mydict):
    #
    #     for j in mydict[digits]:
    #





    return(letterlist)
