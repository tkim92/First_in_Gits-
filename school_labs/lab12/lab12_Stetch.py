import turtle
import random

class Shape:
    def __init__(self,x = 0,y = 0,col = "",fill = False):
        self.x = x
        self.y = y
        self.color = col
        self.fillcolor = fill

    def setFillcolor(self,string):
        self.color = string

    def setFilled(self,bool):
        self.color = True

    def isFilled(self):
        return self.fillcolor


class Circle(Shape):
    def __init__(self,x,y,col,fill,rad = 1):
        super().__init__(x,y,col,fill)
        self.radius = rad

    def draw(self,myt):
        myt.penup()
        myt.goto(self.x,self.y)
        myt.pendown()
        if self.fillcolor == True:
            myt.fillcolor(self.color)
            myt.begin_fill()
            myt.circle(self.radius)
            myt.end_fill()
        else:
            myt.circle(self.radius)

class Display:
    def __init__(self):
        self.t1 = turtle.Turtle()
        self.scr = self.t1.getscreen()
        self.elements = []
        self.t1.hideturtle()
        self.t1.speed(0)
        self.scr.onclick(self.mouseevent)
        self.scr.listen()

    def mouseevent(self,x,y):
        clist = ["red","blue","green","black","yellow"]
        cirlcecolor = random.shuffle(clist)
        ranradius = random.randint(10,100)
        mycircle = circle(x,y,circlecolor[0],True,randradius)
        mycircle.draw(self.t1)

class Display:
    def __init__(self):
        self.myt = turtle.Turtle()
        self.scr = self.myt.getscreen()
        self.elements = []
        self.myt.speed(0)
        self.myt.hideturtle()

        self.scr.onclick(self.mouseEvent)
        self.scr.listen()


    def mouseEvent(self,x,y):
        rad = random.randint(10,100)
        color = ["blue","red"]
        random.shuffle(color)
        col = color[0]
        mycircle = Circle(x,y,col,True,rad)
        mycircle.draw(self.myt)
