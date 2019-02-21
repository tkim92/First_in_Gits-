# Ex6.A
# No repeated words allowed.
def wordlist(mystr):
    wordlist = mystr.split()
    onlywords = []
    for i in wordlist:
        if i not in onlywords:
            onlywords.append(i)
    return onlywords


def main():
    mystring = input("Enter your words: ")
    print(wordlist(mystring))

if __name__ == "__main__":
    main()
