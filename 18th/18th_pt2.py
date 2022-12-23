from copy import deepcopy

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList


class Coord3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Coord3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def coordSum(self):
        return self.x + self.y + self.z

    def __abs__(self):
        return Coord3D(abs(self.x), abs(self.y), abs(self.z))

    def findAllNeighbors(self):
        neighborList = []
        neighborList.append(Coord3D(self.x+1, self.y, self.z))
        neighborList.append(Coord3D(self.x-1, self.y, self.z))
        neighborList.append(Coord3D(self.x, self.y+1, self.z))
        neighborList.append(Coord3D(self.x, self.y-1, self.z))
        neighborList.append(Coord3D(self.x, self.y, self.z+1))
        neighborList.append(Coord3D(self.x, self.y, self.z-1))
        return neighborList

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

def isCoordWithinBounds(point:Coord3D, lowerBound:Coord3D, upperBound:Coord3D) -> bool:
    if point.x < lowerBound.x or point.y < lowerBound.y or point.z < lowerBound.z:
        return False
    if point.x > upperBound.x or point.y > upperBound.y or point.z > upperBound.z:
        return False
    return True



def findEdgesByFloodFill(lowerBound, upperBound, coordList):
    upperBound = Coord3D(upperBound.x+1, upperBound.y+1, upperBound.z+1)
    lowerBound = Coord3D(lowerBound.x-1, lowerBound.y-1, lowerBound.z-1)
    
    possibleMoves = lowerBound.findAllNeighbors()
    visitedPoints = []

    faces = 0

    for move in possibleMoves:
        if isCoordWithinBounds(move, lowerBound, upperBound) and move not in visitedPoints:
            if move in coordList:
                faces += 1
            else:
                possibleMoves.extend(move.findAllNeighbors())
                visitedPoints.append(move)
    return faces

    
    
rawCoordinates = getFileAsList("18th/data")

coordList = []

for coords in rawCoordinates:
    x, y, z = tuple(map(int, coords.split(",")))
    coordList.append(Coord3D(x,y,z))

#faces = len(coordList) * 6
faces = 0

upperBound = deepcopy(coordList[0])
lowerBound = deepcopy(coordList[0])

for coord in coordList:
    if coord.x < lowerBound.x:
        lowerBound.x = coord.x
    if coord.y < lowerBound.y:
        lowerBound.y = coord.y
    if coord.z < lowerBound.z:
        lowerBound.z = coord.z

    if coord.x > upperBound.x:
        upperBound.x = coord.x
    if coord.y > upperBound.y:
        upperBound.y = coord.y
    if coord.z > upperBound.z:
        upperBound.z = coord.z

print(findEdgesByFloodFill(lowerBound, upperBound, coordList))

print(faces)