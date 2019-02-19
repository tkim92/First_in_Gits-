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
    if m == -1:
        print("Error: cannot sum matrices of different sizes")
    else:
        for myrow in m:
            for mycol in myrow:
                print(mycol, end = "  ")
            print()

def sizeMatch(A,B):
    if len(A) == len(B):
        if len(A[0]) == len(B[0]):
            return True
        else:
            False
    else:
        False

def matrixSum(A,B):
    sum_Matrix = []
    sum_Row = []

    if sizeMatch(A,B) == True:
        i = 0
        while i < len(A):
            j = 0
            while j < len(A):
                sumRowData = A[i][j] + B[i][j]
                sum_Row.append(sumRowData)
                j += 1
            sum_Matrix.append(sum_Row)
            sum_Row = []
            i += 1
        return sum_Matrix
    else:
        return -1

def main():
    print("Matrix A:")
    Matrix_A = getMatrix()
    print("Matrix B:")
    Matrix_B = getMatrix()
    Matrix_Sum = matrixSum(Matrix_A,Matrix_B)
    printMatrix(Matrix_Sum)
if __name__ == "__main__":
    main()
