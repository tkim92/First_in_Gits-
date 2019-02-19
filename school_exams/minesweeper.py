import turtle
import random
import math

class Cell:
    # llc_x = lower left corner x, and same for llc_y
    def __init__(self,myt,llc_x,llc_y,width,height):
        # 7 private instance variables, and the initializer method contains 5 arguments.
        self.__xmin = llc_x
        self.__ymin = llc_y
        self.__xmax = width + llc_x
        self.__ymax = height + llc_y
        self.__myt = myt
        self.__bomb = False
        self.__cleared = False
    # get/set methods for instances are made as 'helpers': next 8 methods below.
    def getxMin(self):
        return self.__xmin

    def getxMax(self):
        return self.__xmax

    def getyMin(self):
        return self.__ymin

    def getyMax(self):
        return self.__ymax

    def setxMin(self,x):
        self.__xmin = x

    def setxMax(self,x):
        self.__xmax = x

    def setyMin(self,y):
        self.__ymin = y

    def setyMax(self,y):
        self.__ymax = y

    def isIn(self,x,y):
        if self.__xmin <= x <= self.__xmax and self.__ymin <= y <= self.__ymax:
            return True
        return False

    def setBomb(self):
        self.__bomb = True

    def isBomb(self):
        if self.__bomb == True:
            return True
        return False

    def clear(self):
        self.__cleared = True
        self.draw()

    def isCleared(self):
        if self.__cleared:
            return True
        return False

        # c = count in String

    def showCount(self,c):
        self.__myt.penup()
        # adjust location of writing number corresponding to grid/cell size
        self.__myt.goto((self.__xmax + self.__xmin)/2, (self.__ymax + self.__ymin)/2)
        self.__myt.write(c,align = "center", font = ("Arial",int((self.__xmax-self.__xmin)/2),"normal"))

    def rectangle(self,color):
        self.__myt.hideturtle()
        self.__myt.fillcolor(color)
        self.__myt.begin_fill()
        for i in range(0,2):
            self.__myt.forward(abs(self.__xmax - self.__xmin))
            self.__myt.left(90)
            self.__myt.forward(abs(self.__ymax - self.__ymin))
            self.__myt.left(90)
        self.__myt.end_fill()

    def draw(self):
        self.__myt.penup()
        self.__myt.goto(self.__xmin,self.__ymin)
        self.__myt.pendown()
        if self.__cleared:
            if self.__bomb:
                # We have special case for 'reds'; presence of Mines.
                # Indicate mines by writing *
                self.rectangle("red")
                self.__myt.penup()
                self.__myt.goto((self.__xmax + self.__xmin)/2, (self.__ymax + self.__ymin)/2)
                self.__myt.pendown()
                self.__myt.write("*",font = ("Arial",int((self.__xmax-self.__xmin)/2),"normal"))
            else:
                self.rectangle("grey")
        else:
            self.rectangle("green")

class Minesweeper:
    def __init__(self,rows,cols,mines,visible = False):
        # Three instance variables
        self.__t = turtle.Turtle()
        self.__s = self.__t.getscreen()
        self.__grid = self.setGrid(rows,cols,mines)

        # initializer method sets Turtle graphic environment.
        self.__t.penup()
        self.__t.hideturtle()
        self.__t.speed(0)
        self.__s.setworldcoordinates(0,0,cols,rows)
        self.__s.tracer(0)
        self.drawMinefield(self.__grid,visible)
        self.__s.onclick(self.__mouseClick)
        self.__s.update()
    # This row,col is from your initial input value when instantiating the object
    def setGrid(self,row,col,mines):
        mygrid = []
        for i in range(0,row):
            myrow = []
            for j in range(0,col):
                # Notice that the very first object is located at [0][0] as in the grid location.
                myCell = Cell(self.__t,0,row-1,1,1)
                myrow += [myCell]
            mygrid.append(myrow)
            myrow = []

        # After making a grid which has all different objects (they may have same information but, still they are differnt objects.)
        # Now create a list that has all objects of the grid.
        list_of_objects = []
        row_location = len(mygrid) - 1
        for i in mygrid:
            col_location = 0
            # each object should have its unique information, s.t. xmin ymin and mine
            # set the unique location of each object.
            for j in range(0,len(i)):
                i[j].setyMin(row_location)
                i[j].setyMax(row_location + 1)
                i[j].setxMin(col_location * 1)
                i[j].setxMax(i[j].getxMax() + col_location * 1)
                list_of_objects.append(i[j])
                col_location += 1
            row_location -= 1

        # Then randomly select objects based on given number of mines and set mines on.
        random.shuffle(list_of_objects)
        for j in range(0,mines):
            list_of_objects[j].setBomb()
        # Lastly, return the grid that contains all updated information.
        return mygrid
    # method that helps draw Minefield.
    def drawMinefield(self,grid,visible):
        if visible == False:
            for i in range(0,len(grid)):
                for j in range(0,len(grid[0])):
                    grid[i][j].draw()
        else:
            # if visible, clear all cells that contain mines.
            if visible == True:
                for i in range(0,len(grid)):
                    for j in range(0,len(grid[0])):
                            if grid[i][j].isBomb():
                                grid[i][j].clear()
                                grid[i][j].draw()
    # This row & col: the grid location of the  object, that I clikced.
    def countBomb(self,row,col):
        # Description of 4 dictionaries below explained later under dictionaries method.
        atMargin,row_MinMax,col_MinMax = self.dictionaries()
        Bomb_count = 0
        # check if clicked grid location is on boundary of the grid
        if self.onBoundary(row,col) == False:
            for i in (-1,0,1):
                for j in (-1,0,1):
                    if self.__grid[row + i][col + j].isBomb():
                        Bomb_count += 1
                    else:
                        Bomb_count = Bomb_count
        else:
            # if only 3 neighboring cells existing.
            # possible range of changes for row/col drived from dictionary
            if (row,col) in atMargin:
                row_changes = atMargin[(row,col)][0]
                col_changes = atMargin[(row,col)][1]
            # when its on very top (row = 0) or very botton (row = max)
            elif row in (0,len(self.__grid)-1) and (row,col) not in atMargin:
                row_changes = row_MinMax[row][0]
                col_changes = row_MinMax[row][1]
            # when its on very left (col = 0) or very right (col = max)
            elif col in (0,len(self.__grid[0])-1) and (row,col) not in atMargin:
                row_changes = col_MinMax[col][0]
                col_changes = col_MinMax[col][1]
            # after checking the location and its specific range of changes in row/col, we check the number of bombs.
            for p in row_changes:
                for q in col_changes:
                    if self.__grid[row + p][col + q].isBomb():
                        Bomb_count += 1
                    else:
                        Bomb_count = Bomb_count
        return Bomb_count
        # This row & col as same as above; your clicked object's grid location
    # Check if clicked location is on boundary.
    def onBoundary(self,row,col):
        if row in (0,len(self.__grid)-1) or col in (0,len(self.__grid[0])-1):
            return True
        return False
    # every possible case of range of changes in row/col is formed as dictionaries.
    def dictionaries(self):
        # atMargin: location where has three neighboring cells
        atMargin = {(0,0):([0,1],[0,1]), (0,len(self.__grid[0])-1):([0,1],[-1,0]), (len(self.__grid)-1,0):([-1,0],[0,1]), (len(self.__grid)-1,len(self.__grid[0])-1):([-1,0],[-1,0]),}
        # row_MinMax: location where is at top/bottom of the grid
        row_MinMax = {0:([0,1],[-1,0,1]),len(self.__grid)-1:([0,-1],[-1,0,1])}
        # col_MinMax: location where is at very left/right of the grid
        col_MinMax = {0:([-1,0,1],[0,1]),len(self.__grid[0])-1:([-1,0,1],[-1,0])}
        return (atMargin,row_MinMax,col_MinMax)
    # cells with not yet cleared & no mines
    def cellsRemaining(self):
        remainingCells = 0
        for i in range(0,len(self.__grid)):
            for j in range(0,len(self.__grid[0])):
                if self.__grid[i][j].isCleared() == False and self.__grid[i][j].isBomb() == False:
                    remainingCells += 1
        return remainingCells
    # convert my clicked x,y coordinates to grid location of the cell that contains the x,y coordinates
    def getRowCol(self,x,y):
        for i in range(0,len(self.__grid)):
            for j in range(0,len(self.__grid[0])):
                if self.__grid[i][j].isIn(x,y):
                    return (i,j)
        return (-1,-1)
    # return x,y location in coordinates, then use them as follow
    # this method is private.
    def __mouseClick(self,x,y):
        # first convert x,y into the specific row/col location of the object.
        row,col = self.getRowCol(x,y)[0],self.getRowCol(x,y)[1]
        End = False
        # Cases of winning or losing
        if self.__grid[row][col].isBomb():
            self.drawMinefield(self.__grid,True)
            End = True
        else:
            self.clearCell(row,col)

        if self.cellsRemaining() == 0:
            self.drawMinefield(self.__grid,True)

        # write information of winning/losing game.
        self.__t.penup()
        if End:
            self.__t.goto(3,6)
            self.__t.write("Game Over",align = "left", font = ("Arial",int(100),"normal"))
        elif End == False and self.cellsRemaining() == 0:
            self.__t.goto(1,6)
            self.__t.write("Congratuation! You Win!",align = "left", font = ("Arial",int(70),"normal"))
    # recursive method that will clears cells with no mine.
    def clearCell(self,row,col):
        atMargin,row_MinMax,col_MinMax = self.dictionaries()
        # prevent to fall into the infinite/excessive recursion by clearing cells that have already been cleared.
        if self.__grid[row][col].isCleared() == False:
            self.__grid[row][col].clear()
            self.__grid[row][col].draw()
            # base case: selecting cell has mine on its neighbors
            if self.countBomb(row,col) != 0:
                self.__grid[row][col].showCount(str(self.countBomb(row,col)))
            # reduction case (well, in this case, rather, 'spreading cases')
            else:
                if self.onBoundary(row,col) == False:
                    for i in (-1,0,1):
                        for j in (-1,0,1):
                            # at each neighboring cells with no mines, run clearCell again.
                            self.clearCell(row + i, col + j)
                else:
                    # details of following stpes are explained on countBomb method.
                    if (row,col) in atMargin:
                        row_changes = atMargin[(row,col)][0]
                        col_changes = atMargin[(row,col)][1]

                    elif row in (0,len(self.__grid)-1) and (row,col) not in atMargin:
                        row_changes = row_MinMax[row][0]
                        col_changes = row_MinMax[row][1]

                    elif col in (0,len(self.__grid[0])-1) and (row,col) not in atMargin:
                        row_changes = col_MinMax[col][0]
                        col_changes = col_MinMax[col][1]

                    for p in row_changes:
                        for q in col_changes:
                            # at each neighboring cells with no mines, run clearCell again.
                            self.clearCell(row + p, col + q)

def main():
    mygame = Minesweeper(14,14,15)

if __name__ == "__main__":
    main()
