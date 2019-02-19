import math

class Circle:

    """ What is the point of making it private?
    What will change when these are not private?
    """

    def __init__(self,radius = 1):
        self.__radius = radius
        self.__circumference = 2 * radius * math.pi
        self.__getArea = math.pi * radius ** 2

    def setRadius(self,r):
        self.__radius = r

    def getCircumference(self):
        return self.__circumference
        # return 2*math.pi*self.__radius

    def getArea(self):
        return self.__getArea
        # return math.pi * self.__radius**2
