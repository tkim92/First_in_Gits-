import time
import random


""" Seem to work fine when I run it on terminal, but when I push it to github
for feedback, it says there is an attribute error.

I don't understand why it says it doesn't have attribute called 'start'
"""
class Stopwatch:
    """
    AAAAAAAAAAAAA
    When it's private, we don't __init__(self,time,time)????
    """
    def __init__(self):
        self.__start = time.time()
        self.__end = time.time()

    def start(self):
        self.__start = time.time()

    def stop(self):
        self.__end = time.time()

    def elapsedTime(self):
        return self.__end - self.__start

    def getStartTime(self):
        return self.__start

    def getEndTime(self):
        return self.__end

def main():
    t = Stopwatch()
    element = random.randint(0,10000)
    mylist = []
    for i in range(0,10000):
        mylist.append(i)
    t.getStartTime()
    mylist.sort()
    t.getEndTime()
    print(t.elapsedTime())

if __name__ == '__main__':
    main()
