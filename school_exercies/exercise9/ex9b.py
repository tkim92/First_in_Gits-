# with open("ex9_excel.csv",'r+') as f:
#     line = f.readline()
#     print(line)

def main():
    f = open('Book2.csv', 'r')
    line = f.readline()
    sline = line.split(',')
    print(sline[0] + " " + sline[1]+ " " + sline[2]+ " " + sline[3])
    line = f.readline()
    for i in range(0,3):
        mystr = line.split(',')
        print(mystr[0] + "  " + mystr[1] + "  " + mystr[2] + "  " + mystr[3])
        # print("{0} {1} {2} {3}".format(mystr[0],mystr[1],mystr[2],mystr[3]))
        line = f.readline()

if __name__ == '__main__':
    main()
