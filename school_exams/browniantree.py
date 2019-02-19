import turtle
import random
import time

def get_coordinate(t,pin_num):
    # for first row on the top, 4 pins
    if pin_num in range(0,4):
        t.goto(-150,200)
        for i in range(pin_num):
            t.forward(100)
        return t.pos()

    # for second row from the top, 3 pins
    elif pin_num in range(4,7):
        t.goto(-100,100)
        for i in range(4,pin_num):
            t.forward(100)
        return t.pos()

    # for the second row from the bottom, 2 pins
    elif pin_num in range(7,9):
        t.goto(-50,0)
        for i in range(7,pin_num):
            t.forward(100)
        return t.pos()

    # for the last row, 1 pin
    elif pin_num == 9:
        t.goto(0,-100)
        return t.pos()

def get_n(first_roll):

    # if NULL, choose random between 1 - 9
    if first_roll == "":
        first_roll = random.randint(1,9)
        return int(first_roll)
    else:
        first_roll = int(first_roll)
        if first_roll >= 10:
            return 10
        else:
            return first_roll
    # integer-ized the value, which was inputed as a string.

def get_m(first_roll,second_roll):

    # if NULL, chose randomly from the remaining elements in your list.
    # The list should be modified before get_m funciton has been excuted.
    if second_roll == "":
        second_roll = random.randint(0,10-first_roll)
    elif int(second_roll) > 10 - first_roll:
        second_roll = 10 - first_roll
    return int(second_roll)
    # same intuition as is for get_n function

def draw_pins(t,n,l):
    # t = turtle object
    # n = number of pins that are toppled on first roll
    # l = list of possible pins, i.e. list of present standing pins.

    for i in l:
        t.goto(get_coordinate(t,i))

        # first 'n' elements in the list should be randomized because the list would have been shufflled priorly.
        if i in l[:n]:
            # Red refers to the toppled pins.
            t.color("white")
            t.shape("square")
            t.stamp()
            t.color("black")
            # adjust location of X to make it balanced.
            newcoord = t.pos() - (0,10)
            t.goto(newcoord)
            t.write("X","right",font = ("Arial", 20, "normal"))

        else:
            # Blue refers to the still - standing pins.
            t.color("blue")
            t.shape("circle")
            t.stamp()

def is_strike(t,n):
    # n = number of pins that are toppled on first roll
    t.goto(-30,-200)
    if n == 10:
        return True

def is_spare(t,n,m):
    # m = number of pins that are toppled on second roll
    t.color("black")
    if n + m == 10:
        t.goto(-30,-200)
        return True
    elif n + m < 10:
        t.goto(-100,-200)
        standing_pin_number = 10 - n - m
        return False

def last_frame(t,scores):
    count = 1
    # Count the number of rolls at 10th frame
    while count <= 4:
        # count 1,2,3 are general counts of rolls at 10th frame
        # count = 4 allows to print the final score after either 2 or 3 rolls have been completed.
        if count < 3:
            p_pins = [0,1,2,3,4,5,6,7,8,9]
            draw_pins(t,0,p_pins)
            n = turtle.textinput("Frame: 10","Enter # of pins (null for random)")
            n = get_n(n)

            random.shuffle(p_pins)
            scores.append(n)
            draw_pins(t,n,p_pins)

            if is_strike(t,n) == True:
                t.write("Strike!",font = ("Arial", 30, "normal"))
                time.sleep(1)
                t.clear()
                count += 1
                # if strike, your count increases by 1.

            else:
                m = turtle.textinput("Frame: 10","Enter # of pins (null for random)")
                m = get_m(n,m)

                p_pins = p_pins[n:]
                scores.append(m)
                draw_pins(t,m,p_pins)

                if is_spare(t,n,m) == True:
                    t.write("Spare",font = ("Arial", 30, "normal"))
                    time.sleep(1)
                    t.clear()
                    count += 2
                    # count increases by 2 since it includes your first roll, which is value of n.
                else:
                    count += 3
                    # Neither stike nor spare in the first 2 rolls at 10th frame.
                    # So count += 3 to allow it to print final score

        elif count == 3:
            # This refers to your 3rd roll if qualifed.
            # This should be your very last roll, so the game should end after this roll.
            p_pins = [0,1,2,3,4,5,6,7,8,9]
            draw_pins(t,0,p_pins)
            n = turtle.textinput("Frame: 10","Enter # of pins (null for random)")
            n = get_n(n)

            random.shuffle(p_pins)
            scores.append(n)
            draw_pins(t,n,p_pins)
            count += 1
            # count is added again to allow it to print the final score

        else:
            # When count == 4
            # All 3 or 2 rolls at 10th frame have been completed.
            # now wants to provide the final score.
            t.goto(-100,-200)
            t.color("black")
            t.write("Final Score: {0}".format(finalScore(scores)),font = ("Arial", 30, "normal"))
            time.sleep(2)
            count = 5
            # this count = 5 allows to exit from while loop as count > 4

def finalScore(pinlist):

    total = 0
    # total refers to the consecutive points as the index of elements in the list increases.
    i = 0
    # i refers to the very first index in the list.

    while i < len(pinlist):
        j = i + 1
        k = i + 2
        # j and k refers to next value and one after next value respectively.

        if len(pinlist[j:]) > 2:
            # testing whether 3rd roll exists at 10th frame.
            # cases that satisfy pinlist[j:] <= 2 " will be either "No 3rd roll" or "three strikes at 10th frame"

            if j < len(pinlist) and k < len(pinlist):

                if pinlist[i] == 10:
                    # When we have strike
                    total += pinlist[i] + pinlist[j] + pinlist[k]
                    i += 1
                    # If strike, next addition starts at right next to previous i

                elif pinlist[i] + pinlist[j] == 10:
                    # When we have spare
                    total += pinlist[i] + pinlist[j] + pinlist[k]
                    i += 2
                    # If spare, next addition starts at one after next to previous i

                elif pinlist[i] + pinlist[j] < 10:
                    # When neither strike nor spare
                    total += pinlist[i] + pinlist[j]
                    # If neither happens, next addition starts at one after next to previous i
                    i += 2
            else:
                i += 1
        else:
            # For cases of 'no 3rd roll' and 'three strikes', we just add remaining values from latest total value.
            for r in pinlist[i:]:
                total += r
                i += 1

    return total

def main():
    t = turtle.Turtle()
    scr = t.getscreen()
    t.penup()
    t.hideturtle()
    t.speed(0)

    score_list = []
    # going to store number of toppled pins at each roll here.

    frame_num = 1
    # first 9 frames will be excuted. Function for the last frame is seperated due to the 3rd roll.
    while frame_num <= 9:
        p_pins = [0,1,2,3,4,5,6,7,8,9]
        draw_pins(t,0,p_pins)

        n = turtle.textinput("Frame: {0}".format(frame_num),"Enter # of pins (null for random)")
        n = get_n(n)

        random.shuffle(p_pins)
        score_list.append(n)
        draw_pins(t,n,p_pins)

        # Check if your first roll is strike
        # If so, immediately increase frame_num by 1 and follow the loop.
        if is_strike(t,n) == True:
            t.write("Strike!",font = ("Arial", 30, "normal"))
            time.sleep(1)
            t.clear()

        else:
            # If first is not strike.
            m = turtle.textinput("Frame: {0}".format(frame_num),"Enter # of pins (null for random)")
            m = get_m(n,m)

            p_pins = p_pins[n:]
            score_list.append(m)
            draw_pins(t,m,p_pins)

            # Check if second roll is spare
            if is_spare(t,n,m) == True:
                t.write("Spare",font = ("Arial", 30, "normal"))
                time.sleep(1)
                t.clear()

            else:
                # when neither strike nor spare.
                standing_pin_number = 10 - n - m
                t.write("Open Frame : {0}".format(standing_pin_number),font = ("Arial", 30, "normal"))
                time.sleep(1)
                t.clear()
            # t.clear()
        frame_num += 1
        # Increase frame number after all loop clauses have been read.

    # After first 9 frames have been completed, the last frame runs.
    # Detailed description about last_frame is on last_frame function.
    last_frame(t,score_list)

if __name__ == '__main__':
    main()
