class Tool:
    def __init__(self,strength,type):
        self.__strength = strength
        self.__type = type

    def setStrength(self,strength):
        self.__strength = strength

    def setType(self,type):
        self.__type = type

    def getStrength(self):
        return self.__strength

    def getType(self):
        return self.__type


class Rock(Tool):
    def __init__(self,strength,type = "r"):
        super().__init__(strength,type)


        # a is the object of rock,paper or scissors
    def fight(self,a):
        if a.getType() == "s":
            # self.setStrength = self.getStrength * 2
            return True
        elif a.getType() == "p":
            # self.setStrength = self.getStrength / 2
            return False

class Paper(Tool):
    def __init__(self,strength,type = "p"):
        super().__init__(strength,type)

    def fight(self,a):
        if a.getType() == "r":
            # self.setStrength = self.getStrength * 2
            return True
        elif a.getType() == "s":
            # self.setStrength = self.getStrength / 2
            return False

class Scissors(Tool):
    def __init__(self,strength,type = "s"):
        super().__init__(strength,type)

    def fight(self,a):
        if a.getType() == "p":
            # self.setStrength = self.getStrength * 2
            return True
        elif a.getType() == "r":
            # self.setStrength = self.getStrength / 2
            return False

def main():
    TK = Rock(5,"r")
    HN = Scissors(5,"s")

    print(HN.getType())

    print(TK.getStrength())

    print(TK.fight(HN))

if __name__ == "__main__":
    main()
