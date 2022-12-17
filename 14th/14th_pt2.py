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
    def manhattanNormalizedCoord(self): #SUCH AN UGLY IMPLEMENTATION AAAHHAHAHHAHAHA
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


class ExpandingCoordsystem:
    def __init__(self, defVal):
        self.defaultVal = defVal
        self.coordMap = [[self.defaultVal]]

    def addRow(self):
        rowToAdd = [self.defaultVal] * len(self.coordMap[0])
        self.coordMap.append(rowToAdd)

    def addColumn(self):
        for row in self.coordMap:
            row.append(self.defaultVal)

    def insertItem(self, coord:Coords, item):
        try:
            self.coordMap[coord.y][coord.x] = item
        except:
            if len(self.coordMap) < coord.y+1:
                while len(self.coordMap) < coord.y+1:
                    self.addRow()
            if len(self.coordMap[0]) < coord.x+1:
                while len(self.coordMap[0]) < coord.x+1:
                    self.addColumn()
            self.insertItem(coord, item)

class SandSimulator:
    def __init__(self, eCoordSystem: ExpandingCoordsystem):
        self.expandingCoordSystem = eCoordSystem
    
    def addWalls(self, wallCoordList):
        for i in range(len(wallCoordList) - 1):
            diff = wallCoordList[i+1] - wallCoordList[i]
            for x in range(abs(diff).x + 1 if diff.x != 0 else 0):
                insertCoord = Coords(wallCoordList[i].x + x * diff.manhattanNormalizedCoord().x, wallCoordList[i].y)
                self.expandingCoordSystem.insertItem(insertCoord, True)
            for y in range(abs(diff).y + 1 if diff.y != 0 else 0):
                insertCoord = Coords(wallCoordList[i].x, wallCoordList[i].y + y * diff.manhattanNormalizedCoord().y)
                self.expandingCoordSystem.insertItem(insertCoord, True)

    def addSand(self, sandCoord):
        sand = sandCoord
        if self.expandingCoordSystem.coordMap[0][500] == True:
            return False
        while True:
            sandNextStepCoords = sand + Coords(0, 1) #down
            try:
                if self.expandingCoordSystem.coordMap[sandNextStepCoords.y][sandNextStepCoords.x] == False:
                    sand = sandNextStepCoords #sand stepped down once
                    continue

                sandNextStepCoords = sandNextStepCoords + Coords(-1, 0) #left
                if self.expandingCoordSystem.coordMap[sandNextStepCoords.y][sandNextStepCoords.x] == False:
                    sand = sandNextStepCoords #sand stepped down once
                    continue

                sandNextStepCoords = sandNextStepCoords + Coords(2, 0) #right twice
                if self.expandingCoordSystem.coordMap[sandNextStepCoords.y][sandNextStepCoords.x] == False:
                    sand = sandNextStepCoords #sand stepped down once
                    continue
            except:
                #sand is out of bounds.
                if sandNextStepCoords.y > len(self.expandingCoordSystem.coordMap)-1:
                    self.expandingCoordSystem.insertItem(sand, True)
                    return True
                else:
                    self.expandingCoordSystem.addColumn()
                    return self.addSand(sandCoord)
            #no free spaces left
            self.expandingCoordSystem.insertItem(sand, True)
            return True
            
        

def getCoordsFromString(coordString, sep=","):
    return Coords(int(coordString.split(sep)[0]), int(coordString.split(sep)[1]))

def loadCoordsFromFile(rawCoordFile):
    coordOutList = []
    for line in rawCoordFile:
        listToAppend = []
        for coordString in line.split(" -> "):
            listToAppend.append(getCoordsFromString(coordString))
        coordOutList.append(listToAppend)
    return coordOutList

def normalizeXVals(coordList):
    smallestX = coordList[0][0].x
    for coordGroup in coordList:
        for coord in coordGroup:
            if coord.x < smallestX:
                smallestX = coord.x

    for coordGroup in coordList:
        for coord in coordGroup:
            coord.x = coord.x - smallestX
    return coordList, smallestX




rawCoordFile = getFileAsList("14th/data")

coordList = loadCoordsFromFile(rawCoordFile)

#normalizedCoordList,normalizerValue = normalizeXVals(coordList)

expandingCoord = ExpandingCoordsystem(False)

sandSim = SandSimulator(expandingCoord)

for wallList in coordList:
    sandSim.addWalls(wallList)

#add a row 
sandSim.expandingCoordSystem.addRow()

i = 0
while True:
    if sandSim.addSand(Coords(500, 0)):
        i += 1
    else:
        break

print(i)

print("end")