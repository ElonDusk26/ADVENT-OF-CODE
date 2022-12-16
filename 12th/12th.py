from time import sleep
from copy import deepcopy

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

class rowColumnSet:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    def __add__(self, other):
        return rowColumnSet(self.row + other.row, self.column + other.column)
    def __eq__(self, other) -> bool:
        return self.row == other.row and self.column == other.column
        

class directions:
    UP = rowColumnSet(-1,0)
    DOWN = rowColumnSet(1,0)
    LEFT = rowColumnSet(0, -1)
    RIGHT = rowColumnSet(0, 1)
    asList = [UP,DOWN,LEFT,RIGHT]



class maze:
    def __init__(self, mazeAsList):
        self.maze = mazeAsList
        self.start, self.end = self.findStartEnd()

    def findStartEnd(self) -> rowColumnSet:   
        start = 0
        end = 0
        for row in range(len(self.maze)):
            for column in range(len(self.maze[0])):
                if self.maze[row][column] == "S":
                    start = rowColumnSet(row, column)
                if self.maze[row][column] == "E":
                    end = rowColumnSet(row, column)
        return start, end

    def findNeighbor(self, pointToCheck: rowColumnSet, direction: directions):
        updatedPoint = pointToCheck + direction
        try:
            if updatedPoint.row < 0 or updatedPoint.column < 0:
                raise 
            return self.maze[updatedPoint.row][updatedPoint.column]
        except:
            return None

    def findNeighborsAsList(self, pointToCheck: rowColumnSet): #returns a list
        out = []
        for direction in directions.asList:
            neighborInDirection = self.findNeighbor(pointToCheck, direction)
            if neighborInDirection != None:
                out.append(pointToCheck+direction)
        return out

    def isMoveLegal(self, startPoint:rowColumnSet, pointToCheck:rowColumnSet):
        fromPoint = self.maze[startPoint.row][startPoint.column]
        toPoint = self.maze[pointToCheck.row][pointToCheck.column]
        if fromPoint.isupper():
            if fromPoint == "S":
                fromPoint = "a"
            else:
                fromPoint = "z"
        if toPoint.isupper():
            if toPoint == "S":
                toPoint = "a"
            else:
                toPoint = "z"
        a = ord(fromPoint) #to debug
        b = ord(toPoint) #to debug

        return a+1 >= b

    def findNeighbourLegalMovesAsList(self, pointToCheck: rowColumnSet):
        neighborList = self.findNeighborsAsList(pointToCheck)
        if len(neighborList) == 0:
            return None

        neighboursToRemove = [] 
        for neighbour in neighborList:
            if not self.isMoveLegal(pointToCheck, neighbour):
                neighboursToRemove.append(neighbour) #add all legal moves
        [neighborList.remove(n) for n in neighboursToRemove]
        return neighborList

def floodGateSolve(legalMoves, visitedPoints, inputMaze: maze, depthCounter):
    depthCounter += 1
    if len(legalMoves) == 0:
        return False
    legalMovesToAdd = []
    for move in legalMoves:
        if move == inputMaze.end:
            return depthCounter
        if not visitedPoints[move.row][move.column]:
            visitedPoints[move.row][move.column] = True
            legalMovesToAdd.extend(inputMaze.findNeighbourLegalMovesAsList(move))
    return floodGateSolve(legalMovesToAdd, visitedPoints, inputMaze, depthCounter)

        


mazeAsList = getFileAsList("12th/data")
importedMaze = maze(mazeAsList)

visitedPoints = [] 
for i in range(len(importedMaze.maze)):
    visitedPoints.append([False for x in range(len(importedMaze.maze[0]))])

pathList = []

visitedPoints[importedMaze.start.row][importedMaze.start.column] = True
depthCounter = 0

depth = floodGateSolve(importedMaze.findNeighbourLegalMovesAsList(importedMaze.start), visitedPoints, importedMaze, depthCounter)

print("end")
print(depth)