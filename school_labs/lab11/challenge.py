class Poly:
    def __init__(self,mylist = 0):
        self.alist = [mylist[0]]
        for i in mylist[1:]:
            self.alist += [i]

    def __str__(self):
        return str(self.alist)

    def degree(self):
        return len(self.alist) - 1

    def addTerm(self,exp,coeff):
        self.alist += 
