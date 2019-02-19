def getMatrix():
    matrix = []
    rowstring = input("Enter values seperated by commas: ")

    i = 0
    while rowstring != "":
        rowdata = eval(rowstring)
        row = list(rowdata)
        matrix.append(row)
        rowstring = input("Enter values seperated by commas: ")
        i += 1
    return matrix

def printMatrix(m):
    for myrow in m:
        for mycol in myrow:
            print(mycol, end = "  ")
        print()

def main():
    printMatrix(getMatrix())

if __name__ == "__main__":
    main()
