import turtle
turtle.speed(0)
scr = turtle.Screen()
scr.setworldcoordinates(0,0,240,240)
turtle.showturtle()

turtle.penup()
turtle.hideturtle()
turtle.color("red")
turtle.begin_fill()
for i in range(5):
    turtle.forward(30)
    turtle.left(90)
turtle.end_fill()
