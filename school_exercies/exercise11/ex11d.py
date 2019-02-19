import random

class Player:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def getGuess(self):
        return 0

class HumanPlayer(Player):
    def __init__(self,name):
        super().__init__(name)

    def getGuess(self):
        guess = int(input("Enter your guess: "))
        return guess

class ComputerPlayer(Player):
    def __init__(self,name):
        super().__init__(name)

    def getGuess(self):
        Cguess = random.randint(0,100)
        return Cguess

def guessingGame(player1, player2):
    answer = random.randint(0,100)
    while(True):
        print(player1.getName()+"'s turn to guess: ", end="")
        guess = player1.getGuess()
        if checkForWin(player1,guess,answer):
            return
        print(player2.getName()+"'s turn to guess: ", end="")
        guess = player2.getGuess()
        if checkForWin(player2,guess,answer):
            return
def checkForWin(player,guess,answer):
    print(player.getName(),"guesses", guess)
    if answer == guess:
        print("You're right! You win!")
        return True
    elif answer < guess:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    return

def main():
    guessingGame(HumanPlayer("Kim"),HumanPlayer("Sun"))
    guessingGame(HumanPlayer("Kim"),ComputerPlayer("Apple"))
    guessingGame(ComputerPlayer("Apple"),ComputerPlayer("Dell"))

if __name__ == "__main__":
    main()
