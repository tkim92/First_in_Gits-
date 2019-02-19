import random
import turtle


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

def showMatrix(turtle_object,m):
    i = 0
    while i < len(m):
        j = 0
        while j < len(m):
            if m[i][j] != 0:
                turtle_object.goto(len(m)-1-i,j)
                turtle_object.dot()
            j += 1
        i += 1

def main():
    num = int(input("Ener your number(# of rows & cols): "))
    num_dot = int(input("Enter your number(for # of dots): "))
    val = int(input("Enter your value(for population): "))
    t1 = turtle.Turtle()

    screen = t1.getscreen()
    screen.setworldcoordinates(0,0,num-1,num-1)

    t1.penup()
    t1.hideturtle()

    ident = identity(num)
    amatrix = matrix(num,0)
    pop = population(amatrix,num_dot,val)

    screen.tracer(0)
    showMatrix(t1,pop)
    screen.update()

if __name__ == "__main__":
    main()
