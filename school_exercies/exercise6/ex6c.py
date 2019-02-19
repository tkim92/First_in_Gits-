def seperatevowel(aword):
    vowels = "aeiouAEIOU"
    newword = ""
    i = 0
    if checkpuncs(aword) != True:
        while i < len(aword):

            if aword[0] in vowels:
                newword = aword + "way"
                return checkcapital(newword)
            else:
                if aword[i] in vowels:
                    newword = aword[i:] + aword[:i] + 'ay'
                    return checkcapital(newword)
                else:
                    i += 1
    else:
        yourpunc = aword[-1]
        aword = aword[:-1]
        while i < len(aword):
            if aword[0] in vowels:
                newword = aword + "way"
                return checkcapital(newword) + yourpunc
            else:
                if aword[i] in vowels:
                    newword = aword[i:] + aword[:i] + 'ay'
                    return checkcapital(newword) + yourpunc
                else:
                    i += 1

def checkcapital(aword):
    for i in aword:
        if i.isupper():
            return aword.capitalize()
    return aword


def checkpuncs(aword):
    puncs = ".,?-!"
    i = 0
    while i < len(aword):
        if aword[i] in puncs:
            return True
        else:
            i += 1
    return False

def igpay(english):
    eng = english.split()
    pl = ""
    for i in eng:
        pl = pl + " " + seperatevowel(i)
    return pl.lstrip()
