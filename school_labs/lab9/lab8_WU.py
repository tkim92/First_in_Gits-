names = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10,23,13,18,12]

#1

def makeDictionary(list1,list2):
    d = {}
    for i in range(len(list1)):
        d[list1[i]] = list2[i]
    return d

scoreDict = makeDictionary(names,scores)

#2
scoreDict['barb']

#3
scoreDict['john'] = 19
print(scoreDict)

#4
vlist = list(scoreDict.values())
print(vlist)

#5
tot = 0
for i in vlist:
    tot += i
ave = tot / len(vlist)
print(ave)

#6
del scoreDict['tom']
print(scoreDict)

#7
scoreDict['sally'] = 13
print(scoreDict)

#8
def getScore(name,dic):
    if name in dic:
        return dic[name]
    else:
        print("Not in Dictionary")
        return -1
