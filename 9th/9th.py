def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList


class Coords:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Coords(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        if isinstance(other, Coords):
            return Coords(self.x * other.x, self.y * other.y)
        else:
            return Coords(self.x * other, self.y * other)
    def __abs__(self):
        return Coords(abs(self.x), abs(self.y))
    def coordProduct(self):
        return self.x*self.y
    def max(self):
        return max(self.x, self.y)
    def ceilCoords(self): #SUCH AN UGLY IMPLEMENTATION AAAHHAHAHHAHAHA
        tempX = self.x
        tempY = self.y
        if tempX > 1:
            tempX = 1
        if tempX < -1:
            tempX = -1

        if tempY > 1:
            tempY = 1
        if tempY < -1:
            tempY = -1
        return Coords(tempX,tempY)
    __rmul__ = __mul__
    
class CoordConst:
    UP = Coords(0,1)
    DOWN = Coords(0,-1)
    LEFT = Coords(-1,0)
    RIGHT = Coords(1,0)

class RopeSim:
    def __init__(self, tailEndRope=None):
        self.head = Coords(0,0)

        self.tail = Coords(0,0)
        self.tailMovedPos = [self.tail]

        self.tailEndRope = tailEndRope

    def move(self, moveChar):
        if moveChar == "U": #UP
            self.moveHeadAndTail(CoordConst.UP) 
        elif moveChar == "D":
            self.moveHeadAndTail(CoordConst.DOWN) 
        elif moveChar == "L":
            self.moveHeadAndTail(CoordConst.LEFT) 
        elif moveChar == "R":
            self.moveHeadAndTail(CoordConst.RIGHT) 

    def moveHeadAndTail(self, headToCoord: Coords):
        self.head += headToCoord
        diff = self.tail - self.head
        absMaxCoordVal = abs(diff).max() #returns the highest coordinate in positive numbers
        if absMaxCoordVal > 1:
            self.tail += -1*diff.ceilCoords()
            self.tailMovedPos.append(self.tail)
            if self.tailEndRope != None:
                self.tailEndRope.setHeadAndTail(self.tail)


listOfMoves = getFileAsList("9th/data")

rope = RopeSim()

for move in listOfMoves:
    move = move.split(" ")
    for i in range(int(move[1])):
        rope.move(move[0])

nonDuplicatedListOfMoves = []
[nonDuplicatedListOfMoves.append(moveCoord) for moveCoord in rope.tailMovedPos if moveCoord not in nonDuplicatedListOfMoves]

print(len(nonDuplicatedListOfMoves))