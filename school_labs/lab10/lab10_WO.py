f = open('all_day.csv','r')
line = f.readline()
title = line.split(',')
print(title)

j = 0
for i in title:
    print(str(j) + " " + i)
    j += 1


allline = f.readlines()
print(allline[1])

listline = allline[1].split(',')

sortlist = []
for i in range(0,len(allline)):
    listline = allline[i].split(',')
    sortlist.append(listline[4] + " : " + listline[13] + ',' + listline[14])
# print(sortlist)
for i in sortlist:
    eachline = i.split(':')
    eachline[0] = float(eachline[0])
sortlist.sort()

for j in sortlist:
    print(j)
