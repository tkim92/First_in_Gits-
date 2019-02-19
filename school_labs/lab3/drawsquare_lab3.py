import turtle
# turtle.showturtle() <- should be in your main function

def Drawsquare(sidelength):
    i = 1
    while i <= 10:
        turtle.forward(sidelength)
        turtle.left(90)
        turtle.forward(sidelength)
        turtle.left(90)
        turtle.forward(sidelength)
        turtle.left(90)
        turtle.forward(sidelength)
        turtle.left(90)
        turtle.left(36)
        i += 1

def main():
    turtle.showturtle()
    Drawsquare(100)

if __name__ == '__main__':
    main()
