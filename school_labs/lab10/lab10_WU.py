import random
# fileobj = open('somefile','w')
# for i in range(3):
#     record = " "
#     for j in range(1,4):
#         record += str(i*3+j) + ','
#     record = record[:-1]
#     fileobj.write(record)
#     if i < 2:
#         fileobj.write('\n')
# fileobj.close()

testdata = open('mydata','w')
for i in range(1000):
    each_row = " "
    myint = random.randint(-1000,1000)
    testdata.write((str(i + 1) + "," + str(myint)))
    if i < 999:
        testdata.write("\n")
testdata.close()
