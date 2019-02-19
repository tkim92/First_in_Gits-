def ltrcount(mystring):
    i = 0
    count = 0
    while i < len(mystring):
        if mystring[i].isalpha() == True:
            count += 1
            i += 1
        else:
            i += 1
    return count

def reverse(mystring):
    rev_string = ""
    i = len(mystring) - 1
    while i >= 0:
        rev_string += mystring[i]
        i -= 1
    return rev_string

def ispalindrom(mystring):
    newstring = ""
    i = 0
    while i < len(mystring):
        if mystring[i].isalpha() == True:
            newstring += mystring[i]
            i += 1
        else:
            i += 1

    if newstring.lower() == reverse(newstring.lower()):
        return True
    else:
        return False

def main():
    mystr = input("Enter a string: ")
    if ispalindrom(mystr) == True:
        print("{0} is a palindrome".format(mystr))
    else:
        print("{0} is not a palindrome".format(mystr))

    ask = input("Continue? (y/n): ")

    while ask != "n":
        mystr = input("Enter a string: ")
        if ispalindrom(mystr) == True:
            print("{0} is a palindrome".format(mystr))
        else:
            print("{0} is not a palindrome".format(mystr))

        ask = input("Continue? (y/n): ")

if __name__ == "__main__":
    main()
