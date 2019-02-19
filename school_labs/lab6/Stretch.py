import random

def matrix(n,init):
    mymatrix = []
    myrow = []
    for i in range(0,n):
        for j in range(0,n):
            myrow.append(init)
        mymatrix.append(myrow)
        myrow = []
    return mymatrix

def identity(n):
    yourmat = matrix(n,0)
    for i in range(0,n):
        yourmat[i][i] = 1
    return yourmat

def population(m,n,value):
    i = 0
    while i < n:
        a = random.randint(0,len(m)-1)
        b = random.randint(0,len(m)-1)
        if m[a][b] == value:
            i = i
        else:
            m[a][b] = value
            i += 1
    return m

def main():
    num = int(input("Enter your number: "))
    val = int(input("Enter your value: "))
    #
    # print(identity(num))
    print(population(matrix(num,0),num,val))


if __name__ == "__main__":
    main()
