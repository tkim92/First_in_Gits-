#Ex6.C

#If word contains any of consonants (A,E,I,O,U), move the first word to the end with "ay"
#If not consonants, move to the end with 'way'
#argument is string

import numpy as np

def check_consonants(word):
    cons = ["A","E","O","I","U"]
    for i in word:
        if i.upper() in cons:
            return True
    return False


def igpay(phrase):

    mywords = phrase.split(" ")
    for index, words in enumerate(mywords):
        if check_consonants(words):
            mywords[index] = words[1:].capitalize() + words[0].lower() + "ay"
        else:
            mywords[index] = words[1:].capitalize() + words[0].lower() + "way"
        print(words)
        print(check_consonants(words))

    return mywords

def main():

    print(igpay("Can you speak Pig Latin?"))

if __name__ == "__main__":
    main()
