def newlist(alist,newword):
    mylist = []
    for i in alist:
        mylist.append(i)
    mylist.append(newword)
    return mylist

def BisSmaller(A,B):
    i = 0
    while i < len(A):
        if A[i] != B[i]:
            if A[i] > B[i]:
                return True
            else:
                return False
        else:
            if A[i+1] == B[i+1]:
                i += 1
            else:
                if A[i+1] > B[i+1]:
                    return True
                else:
                    False

def insertString(alist,newword):
    sortlist = newlist(alist,newword)
    # print(sortlist)
    i = 0
    while i < len(sortlist):
        smallest = i
        j = i + 1
        while j < len(sortlist):
            if BisSmaller(sortlist[smallest],sortlist[j]) == True:
                # print(sortlist[i]+ "   " + sortlist[j])
                smallest = j
            j += 1
        sortlist[i],sortlist[smallest] = sortlist[smallest],sortlist[i]
        i += 1
    return sortlist

def onebyone(l):
    for i in l:
        print(i,end = "\n")

def main():
    mylist = []
    firstword = input("Enter a word: ")
    mylist.append(firstword)
    myword = input("Enter a word: ")

    while myword != "":
        mylist = insertString(mylist,myword)
        myword = input("Enter a word: ")

    onebyone(mylist)

if __name__ == "__main__":
    main()
