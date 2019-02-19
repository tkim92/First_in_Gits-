import random

class Bug:
    def __init__(self,pos = 0):
        self.position = pos
        self.direction = 1

    def move(self):
        if self.position >= 0:
            if self.direction == 1:
                self.position += 1
            else:
                self.position -= 1
        else:
            self.position = self.position

    def turn(self):
        direction = random.randint(0,1)
        if direction == 0:
            self.direction = self.direction * -1
        else:
            self.direction = self.direction * 1

    def display(self):
        if self.direction == -1:
            return "." * self.position + "<"
        else:
            return "." * self.position + ">"

def main():
    """ Why it doesn't show the moves of bugs automatically when main is ran?
    Also, is it supposed to be kept changing direction every move?
    That saying, -1 +1 -1 +1 and so on?"""

    """
    The answer on gitbut used it as private. Why? is that neccessary?
    """

    abug = Bug(10)
    print(abug)
    for move in range(0,13):
        abug.move()
        abug.turn()
        print(abug.display())

if __name__ == "__main__":
    main()
