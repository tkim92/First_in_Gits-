# Ex6.B Word Seperation
# Seperate words by spaces with first word of the pharse starting with an uppercase letterself.

def seperate(phrase):
    mystr = phrase[0]
    for i in phrase[1:]:
        if i.isupper():
            mystr += " "
            mystr += i.lower()
        else:
            mystr += i
    return (mystr)

def combine(phrase2):
    newstr = ""
    words = phrase2.split(" ")
    print(words)
    for i in words:
        i = i.capitalize()
        newstr += i
    return (newstr)
