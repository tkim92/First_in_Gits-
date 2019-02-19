def addDB(dic,str1,str2):
    if str1 in dic:
        dic[str1] += [str2]
    else:
        dic[str1] = [str2]

    if str2 in dic:
        dic[str2] += [str1]
    else:
        dic[str2] = [str1]

def findDB(dic,key):

    if key in dic:
        return dic[key]
    else:
        return []

def removeDB(dic,str1,str2):
    if str1 in dic:
        if dic[str1] != []:
            dic[str1].remove(str2)
        else:
            del dic[str1]
    elif str2 in dic:
        if dic[str2] != []:
            dic[str2].remove(str1)
        else:
            del dic[str2]

def main():
    command = input("-->")
    alist = command.split()
    dics = {}

    while command != 'end':

        if len(alist) == 3:
            if alist[0] == 'add':
                addDB(dics,alist[1],alist[2])
            elif alist[0] == 'del':
                removeDB(dics,alist[1],alist[2])
            else:
                print("Invalid Command")
        elif len(alist) == 2:

            if alist[0] == 'find':
                print(findDB(dics,alist[1]))
            else:
                print("Invalid Command")
        elif alist[0] == 'clear':
            dics = {}
        command = input("-->")
        alist = command.split()
