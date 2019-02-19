import random
import turtle

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def tree(t,trunkLength):

    angle = random.randint(15,45)
    length = random.randint(12,18)

    if trunkLength < 5:
        return
    else:
        t.forward(trunkLength)
        t.right(angle)
        tree(t,trunkLength-length)
        t.left(2*angle)
        tree(t,trunkLength-length)
        t.right(angle)
        t.backward(trunkLength)

def main():
    t1 = turtle.Turtle()
    t1.speed(0)
    t1.left(90)
    tree(t1,100)

if __name__ == "__main__":
    main()
