import turtle

def turtlestar():

    length = turtle.numinput("Inbox","Enter desired length: ")

    turtle.left(36)
    for i in range(5):
        turtle.forward(length)
        turtle.left(144)

def main():
    turtle.showturtle()
    turtlestar()

if __name__ == '__main__':
    main()
