import turtle
import math

def DrawDot(t):
    t.color("yellow")
    t.dot(20)

def OrbitMove(t):
    i = 0
    t.color("blue")
    t.shape("circle")

    while i <= 1080:
        t.goto(150 * math.cos(math.radians(i)),150*math.sin(math.radians(i)))
        i += 1



def main():
    scr = turtle.Screen()
    scr.delay(0)

    t1 = turtle.Turtle()
    t1.showturtle()

    t1.penup()
    t1.speed(0)

    DrawDot(t1)
    OrbitMove(t1)

if __name__ == "__main__":
    main()
