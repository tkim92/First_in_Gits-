
class Smatrix:
    def __init__(self):
        self.__matrix = {}

    def get(self,row,col):
        if self.__matrix != {}:
            return self.__matrix[(row,col)]
        else:
            return str(0)

    def set(self,row,col,value):
        if value != 0:
            self.__matrix[(row,col)] = value
        else:
            del self.__matrix[(row,col)]

    def __repr__(self):
        keys = list(self.__matrix.keys())
        keys.sort()
        print(keys)
        myrow = keys[0][0]
        mycol = keys[0][1]

        mymatrix = []
        myrows = []

        for rows in range(0,myrow + 1):
            for cols in range(0, mycol + 1):
                myrows += [cols]
            mymatrix.append(myrows)
        mymatrix[myrow][mycol] = self.get(myrow,mycol)

        return str(mymatrix)

""" My problem is,,, I somehow display the input value in matrix form, but
when I set to different rows/cols with new value, the matrix forom does not get
changed accordingly.
"""
    # def __add__(self,rhand):
    #     return Sm
