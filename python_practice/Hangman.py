import turtle
import random

def body(x):
    x.penup()
    x.goto(0,50)
    x.pendown()

    x.left(90)
    x.forward(100)

    x.right(90)
    x.forward(100)

    x.right(90)
    x.forward(300)

def underscore(y,word):
    print(word)
    y.penup()
    starting_x_coords = 0 - (len(word)//2)
    starting_y_coords = -250
    y.goto(starting_x_coords,starting_y_coords)

    for i in word:
        y.pendown()
        y.forward(20)
        y.penup()
        y.forward(10)
        # y.pendown()

def theman(z,num):

    if num == 1:
        z.circle(25)

    elif num == 2:
        z.right(90)
        z.forward(50)
        z.left(90)

    elif num == 3:
        z.penup()
        z.goto(0,-25)
        z.left(45)
        z.pendown()
        z.forward(30)
        z.right(45)

    elif num == 4:
        z.penup()
        z.goto(0,-25)
        z.right(225)
        z.pendown()
        z.forward(30)
        z.left(225)

    elif num == 5:
        z.penup()
        z.goto(0,-50)
        z.right(45)
        z.pendown()
        z.forward(30)
        z.left(45)

    elif num == 6:
        z.penup()
        z.goto(0,-50)
        z.right(135)
        z.pendown()
        z.forward(30)
        z.left(135)

def main():

    mywords = ["happy","unhappy","snow","minnesota","macbook"]

    myt = turtle.Turtle()
    myt2 = turtle.Turtle()
    myt3 = turtle.Turtle()

    myt.hideturtle()
    myt2.hideturtle()
    myt3.hideturtle()

    myt.speed(0)
    myt2.speed(0)
    myt3.speed(0)

    body(myt)
    selected_word = random.choice(mywords)
    underscore(myt2,selected_word)

    wrong_choices = 0
    remaining = len(selected_word)
    flag = "go"

    while flag == "go":
        mychoice = turtle.textinput("Hangman!","Guess a letter: ")

        if mychoice not in selected_word:
            wrong_choices += 1
            theman(myt3,wrong_choices)

        else:
            pos = 0
            for i in selected_word:
                if selected_word[pos] == mychoice:
                    myt2.goto(30*pos-len(selected_word)//2,-250)
                    myt2.write(i,font = ("Arial",30,"normal"))
                    remaining -= 1
                pos += 1

        if wrong_choices == 6 or remaining == 0:
            flag = "stop"
            myt2.goto(0,-280)
            myt2.write("Game Over", font = ("Arial",30,"normal"))


if __name__ == "__main__":
    main()
