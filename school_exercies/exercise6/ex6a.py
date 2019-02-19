import string
def wordlist(prose):
    puncs = string.punctuation

    for i in prose:
        if i in puncs:
            onlyalpha = prose.replace(i,"")

    onlyalpha = onlyalpha.split()

    print(puncs)

    print(onlyalpha)

    finallist = []
    for i in onlyalpha:
        if i.lower() not in finallist:
            finallist.append(i.lower())

    return finallist

print(wordlist("It was the best of times, it was the worst of times; It was the age of wisdom,     it was the age of foolishness"))

# why times; is not modified?
