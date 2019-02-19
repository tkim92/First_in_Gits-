import turtle
import random
import math

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

    def isIN(self,x,y):
        origin = (self.x,self.y + self.radius)
        # Area = math.pi*(self.radius**2)
        newR = ((x - origin[0])**2 + (y - origin[1])**2)**(0.5)
        # newArea = math.pi*(newR**2)
        if self.radius >= newR:
            print("AAAAAA")
            return True
        return False

class Rectangle(Shape):
    def __init__(self,x,y,col,fill,width,height):
        super().__init__(x,y,col,fill)
        self.width = width
        self.height = height

    def draw(self,myt):
        myt.penup()
        myt.goto(self.x,self.y)
        myt.pendown()
        myt.fillcolor(col)
        myt.begin_fill()
        for i in range(2):
            myt.forward(width)
            myt.right(90)
            myt.forward(height)
            myt.right(90)
        myt.end_fill()

    def isIN(self,x,y):
        Area = self.height * self.width
        newArea = abs(x - self.x) * abs(y - self.y)
        if newArea <= Area:
            return True
        return False

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
        flag = True

        """
        if element list is empty, nothing to remove but just add.
        """
        if self.elements != []:
            """
            Check every objects and its isIN method if my mouse click is in.
            """
            flag2 = True
            for shapes in self.elements:
                print("Hello")
                if shapes.isIN(x,y) and flag2:
                    """
                    if it's in, remove the shape.
                    """
                    self.remove(shapes)
                    """
                    flag prevents from removing and drawing at the same time.
                    """
                    flag = False
                    flag2 = False


            """
            After all checking, if my click not in all objects, just draw new one.
            """
            if flag:
                self.add(mycircle)
        else:
            """
            First click must draw shape.
            """
            self.add(mycircle)


        if len(self.elements) == 10:
            self.scr.bye()

        # if self.elements != []:
        #     for shapes in self.elements:
        #         if shapes.isIN(x,y):
        #             flag = False
        #             self.remove(shapes)
        #         print("Not this one")
        #
        #     if flag != False:
        #         print("NO at all!!!")
        #         self.add(mycircle)
        #
        # else:
        #     self.add(mycircle)

        print(self.elements)

    def add(self,shape):
        self.elements.append(shape)
        shape.draw(self.myt)

    def remove(self,shape):
        self.elements.remove(shape)
        self.myt.clear()
        if self.elements != []:
            for shp in self.elements:
                # the shp already have the information about the 'shape'
                # just like what we did under mouseEvent: mycircle.draw(self.myt)
                shp.draw(self.myt)
        # print(self.elements)

def main():
    D = Display()

if __name__ == "__main__":
    main()
