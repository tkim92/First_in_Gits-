import random

def Crap(x,y):
    sum_dice = x + y
    #Win
    if sum_dice == 7 or sum_dice == 11:
        return True
    #Lose
    elif sum_dice == 2 or sum_dice == 3 or sum_dice == 12:
        return False

def main():
    dice_x = random.randint(1,6)
    dice_y = random.randint(1,6)
    sum_dice = dice_x + dice_y

    if Crap(dice_x,dice_y) == True:
        # print("Initial roll is: " + "[" + str(dice_x) + "," + str(dice_y) + "]" + " = " + str(sum_dice)+ "\nYou win!")
        print(f"Initial roll is: [{dice_x},{dice_y}] = {sum_dice} \nYou Win!")
        # print("Initial roll is: [{0},{1}] = {2} \nYou Win!".format(dice_x,dice_y,sum_dice))


    elif Crap(dice_x,dice_y) == False:
        # print("Initial roll is: " + "[" + str(dice_x) + "," + str(dice_y) + "]" + " = " + str(sum_dice) + "\nCraps! Sorry, you lose")
        print(f"Initial roll is: [{dice_x},{dice_y}] = {sum_dice} \nCraps! Sorry, you lose")
    else:
        # print ("Initial roll is: " + "[" + str(dice_x) + "," + str(dice_y) + "]" + " = " + str(sum_dice) + "\nPoint is " + str(sum_dice) + "." + " Roll again")
        print(f"Initial roll is: [{dice_x},{dice_y}] = {sum_dice}. Roll again")
        new_sum = 0
        while new_sum != sum_dice and new_sum != 7:
            new_x = random.randint(1,6)
            new_y = random.randint(1,6)
            new_sum = new_x + new_y

            if new_sum == sum_dice:
                # print ("Roll is " + "[" + str(new_x) + "," + str(new_y) + "]" + " = "+ str(new_sum) + "   You Win!")
                print(f"Roll is [{new_x},{new_y}] = {new_sum}  You Win!")
            elif new_sum == 7:
                # print ("Roll is " + "[" + str(new_x) + "," + str(new_y) + "]" + " = "+ str(new_sum) + "   You Lose")
                print(f"Roll is [{new_x},{new_y}] = {new_sum}  You Lose")
            else:
                # print("Roll is " + "[" + str(new_x) + "," + str(new_y) + "]" + " = "+ str(new_sum))
                print(f"Roll is [{new_x},{new_y}] = {new_sum}")


if __name__ == "__main__":
    main()
