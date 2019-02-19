import random
import turtle
import time


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

def neighbor(m,x,y):
    c = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if m[i][j] == 1:
                c += 1
    if m[x][y] == 1:
        c -= 1
    return c

def dieORalive(m,x,y):
    c = neighbor(m,x,y)
    if m[x][y] == 0 and c == 3:
        m[x][y] = 1
    else:
        if c < 2 or c > 3:
            m[x][y] = 0
def update(m):
    for i in range(1,len(m)-2):
        for j in range(1,len(m)-2):
            dieORalive(m,i,j)

def main():
    # num = int(input("Ener your number(# of rows & cols): "))
    # num_dot = int(input("Enter your number(for # of dots): "))
    # val = int(input("Enter your value(for population): "))
    t1 = turtle.Turtle()

    screen = t1.getscreen()
    screen.setworldcoordinates(0,0,100-1,100-1)

    t1.penup()
    t1.hideturtle()
# #
#     ident = identity(num)
    # amatrix = matrix(num,0)
    amatrix = matrix(100,0)
    # pop = population(amatrix,num_dot,val)
    pop = population(amatrix,500,1)
    for i in range(0,50):
        print("AAA")
        screen.tracer(0)
        showMatrix(t1,pop)
        update(pop)
        screen.update()
        time.sleep(1)
        t1.clear()

if __name__ == "__main__":
    main()
