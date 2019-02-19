import turtle
turtle.showturtle()

def Drawcircle(radius):
    turtle.speed(0)
    scaled_radius = radius/100

    #bluecircle
    turtle.penup()
    turtle.left(180)
    turtle.forward(300*scaled_radius)
    turtle.left(90)
    turtle.pensize(7)
    turtle.pendown()
    turtle.color("blue")
    turtle.circle(radius)
    #blackcircle
    turtle.left(90)
    turtle.penup()
    turtle.forward(225*scaled_radius)
    turtle.right(90)
    turtle.color("black")
    turtle.pendown()
    turtle.circle(radius)
    #redcircle
    turtle.left(90)
    turtle.penup()
    turtle.forward(225*scaled_radius)
    turtle.right(90)
    turtle.color("red")
    turtle.pendown()
    turtle.circle(radius)
    #yellocircle
    turtle.right(90)
    turtle.penup()
    turtle.forward(240*scaled_radius)
    turtle.left(90)
    turtle.forward(100*scaled_radius)
    turtle.right(90)
    turtle.forward(100*scaled_radius)
    turtle.left(90)
    turtle.pendown()
    turtle.color("yellow")
    turtle.circle(radius)
    #greencircle
    turtle.left(90)
    turtle.penup()
    turtle.color("green")
    turtle.forward(230*scaled_radius)
    turtle.right(90)
    turtle.pendown()
    turtle.circle(radius)

Drawcircle(120)
