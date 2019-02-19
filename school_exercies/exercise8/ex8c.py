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

def reverse(dic):
    rdic = {}
    for i in dic:
        if dic[i] in rdic:
            rdic[dic[i]] += [i]
        else:
            rdic[dic[i]] = [i]
    return rdic

def main():
    mystr = input("Enter a text string: ")
    adict = letterFrequency(mystr)
    rev = reverse(adict)

    freqs = list(rev.keys())
    freqs.sort(reverse = True)

    for i in freqs:
        alplist = list(rev[i])
        alplist.sort()
        for j in alplist:
            print("{0}  {1}".format(j,i))

if __name__ == '__main__':
    main()
