import random
import turtle

def direction():
    d = random.randint(1,4)
    if d == 1:
        turtle.left(0)
        turtle.forward(20)
    elif d == 2:
        turtle.left(90)
        turtle.forward(20)
    elif d == 3:
        turtle.left(180)
        turtle.forward(20)
    elif d == 4:
        turtle.left(270)
        turtle.forward(20)

def CountSteps():

    x_cord = 0
    y_cord = 0
    count = 0

    while x_cord > -220 and x_cord < 220 and y_cord > -220 and y_cord < 220:
        direction()
        turtle.pos()
        x_cord = round(turtle.xcor(), 0)
        y_cord = round(turtle.ycor(), 0)
        count += 1

    turtle.stamp()
    turtle.penup()
    turtle.goto(0,0)
    turtle.write("The number of counts of turns = " + str(count), True, align = 'center', font = ("Arial", 18, "normal"))


def main():
    turtle.showturtle
    turtle.speed(0)
    turtle.setup (width = 440, height = 440, startx = 0, starty = 0)
    CountSteps()

if __name__ == '__main__':
    main()
