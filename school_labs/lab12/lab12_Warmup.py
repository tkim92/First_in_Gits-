import turtle

myt = turtle.Turtle()
myt.speed(0)

myt.penup()
myt.goto(40,40)
myt.circle(100)
myt.pendown()
myt.circle(100)

myt.fillcolor("red")
myt.begin_fill()
myt.circle(100)
myt.end_fill()

myt.penup()
myt.goto(-50,-50)
myt.pendown()
myt.fillcolor("blue")
myt.begin_fill()
for i in range(2):
    myt.forward(100)
    myt.right(90)
    myt.forward(50)
    myt.right(90)
myt.end_fill()

def mouseInput(x,y):
    # print(x)
    # print(type(x))
    print(x,',',y)

scr = myt.getscreen()
x = scr.onclick()
print(x)
scr.listen()
