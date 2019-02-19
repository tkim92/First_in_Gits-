def emul(a,b):

    product = 0

    if a < 0 and b < 0:
        a = -1 * a
        b = -1 * b

        if a >= b:
            big = a
            small = b
        else:
            big = b
            small = a

        while small != 0:

            if small%2 == 0:
                product = product
            else:
                product += big

            big *= 2
            small //= 2
        return product

    elif a > 0 and b < 0:
        a = 1 * a
        b = -1 * b

        if a >= b:
            big = a
            small = b
        else:
            big = b
            small = a

        while small != 0:

            if small%2 == 0:
                product = product
            else:
                product += big

            big *= 2
            small //= 2
        return -1*product

    elif a < 0 and b > 0:
        a = -1 * a
        b = 1 * b

        if a >= b:
            big = a
            small = b
        else:
            big = b
            small = a

        while small != 0:

            if small%2 == 0:
                product = product
            else:
                product += big

            big *= 2
            small //= 2
        return -1*product

    elif a > 0 and b > 0:
        if a >= b:
            big = a
            small = b
        else:
            big = b
            small = a

        while small != 0:

            if small%2 == 0:
                product = product
            else:
                product += big

            big *= 2
            small //= 2
        return product


    elif a == b == 0:
        product = 0
        return 0

def main():
    a = int(input("Enter your first integer: "))
    b = int(input("Enter your second integer: "))
    print(emul(a,b))

if __name__ == "__main__":
    main()






import turtle
import random



def race(a,b,c):
    xcord_a = a.xcor()
    xcord_b = b.xcor()
    xcord_c = c.xcor()

    while xcord_a <=500 and  xcord_b <=500  and  xcord_c <=500:
        step_a = random.randint(1,15)
        a.forward(step_a)
        xcord_a = a.xcor()


        step_b = random.randint(1,15)
        b.forward(step_b)
        xcord_b = b.xcor()

        step_c = random.randint(1,15)
        c.forward(step_c)
        xcord_c = c.xcor()


def main():
    turtle.speed(0)
    scr = turtle.Screen()
    scr.setworldcoordinates(0,0,500,500)

    t1 = turtle.Turtle()
    t1.hideturtle()
    t1.shape("turtle")
    t1.fillcolor(1,0,0)
    t1.penup()
    t1.goto(0,250)
    t1.showturtle()

    t2 = turtle.Turtle()
    t2.hideturtle()
    t2.shape("turtle")
    t2.fillcolor(0,1,0)
    t2.penup()
    t2.goto(0,300)
    t2.showturtle()

    t3 = turtle.Turtle()
    t3.hideturtle()
    t3.shape("turtle")
    t3.fillcolor(0,0,1)
    t3.penup()
    t3.goto(0,200)
    t3.showturtle()

    race(t1,t2,t3)
    #race(t2)
    #race(t3)

if __name__ == "__main__":
    main()
