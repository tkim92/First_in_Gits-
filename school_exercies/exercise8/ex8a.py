def letterFrequency(astr):
    d = {}
    for i in astr:
        if i != " ":
            i = i.lower()
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    return d


def main():
    mystr = input("Enter a text string: ")
    adict = letterFrequency(mystr)
    alps = 'abcdefghijklmnopqrstuvwxyz'
    for i in alps:
        if i in adict:
            print("{0}   {1}".format(i,adict[i]))

if __name__ == '__main__':
    main()
