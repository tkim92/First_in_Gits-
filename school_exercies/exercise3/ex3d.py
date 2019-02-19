import turtle
import math

def DrawDot(t):
    t.color("yellow")
    t.dot(20)

def TwoOrbits(t,s):
    i = 0
    t.color("blue")
    s.color("green")
    t.shape("circle")
    s.shape("circle")

    while i <= 1080:
        # loop i for the planet orbiting sun
        t.goto(150*math.cos(math.radians(i)),150*math.sin(math.radians(i)))
        j = 0
        while j <= 1080:
            # loop j for Moon orbiting the planet
            xcord_t = 150 * math.cos(math.radians(i))
            ycord_t = 150 * math.sin(math.radians(i))
            s.goto(xcord_t + 80 * math.cos(math.radians(j)),ycord_t + 80*math.sin(math.radians(j)))
            j += 5
        i += 2

def main():
    scr = turtle.Screen()
    scr.delay(0)

    t1 = turtle.Turtle()
    t1.showturtle()

    t1.penup()
    t1.speed(0)

    t2 = turtle.Turtle()
    t2.showturtle()

    t2.penup()
    t2.speed(0)

    DrawDot(t1)
    TwoOrbits(t1,t2)

if __name__ == "__main__":
    main()
