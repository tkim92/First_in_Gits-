""" .read() = everything as a string
    .readlines() = a list of every single line as a string
    .readline() = string of current line of file,
     starting at first line, ending with null string."""

def main():
    x = """False class finally is return None continue for lambda try
    True def from nonlocal while and del global not with as elif if or yeild
    assert else import pass break except in raise"""

    keywords = x.split()
    fname = input("Enter the filename: ")

    adict = {}
    afile = open(fname,'r')
    astr = afile.read()
    listf = astr.split()

    keys = []
    for i in listf:
        if i in keywords:
            keys.append(i)

    for j in keys:
        if j in adict:
            adict[j] += 1
        else:
            adict[j] = 1

    mylist = []
    for i in adict:
        mylist.append((i,adict[i]))
    mylist.sort()
    print(mylist)

    print("Keyword frequency in alphabetic order:")
    for keyss in mylist:
        print(keyss[0] + "   " + str(keyss[1]))


if __name__ == '__main__':
    main()
