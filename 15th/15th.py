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
    def coordSum(self):
        return self.x + self.y
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
    def manhattanDistance(self, other):
        return abs(self-other).coordSum()
    __rmul__ = __mul__

class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def isOverlapping(self, other):
        return (self.lower <= other.upper and self.upper >= other.lower)

    def mergeOverlappingIntervals(self, other):
        return Interval(min(self.lower, other.lower), max(self.upper, other.upper))

    def __eq__(self, other) -> bool:
        return (self.lower == other.lower and self.upper == other.upper)
    def deletePointInInterval(self, point):
        return Interval(self.lower, point - 1), Interval(point + 1, self.upper)
    def getCount(self):
        return self.upper - self.lower + 1

def checkUnavailableSpots(row, leftMostIndex, rightMostIndex, coordinateDataList):
    xStartPoint = coordinateDataList[leftMostIndex][0].x - coordinateDataList[leftMostIndex][2]
    xStopPoint = coordinateDataList[rightMostIndex][0].x + coordinateDataList[rightMostIndex][2]
    rowPoint = Coords(xStartPoint, row)
    unavailable = 0
    for deltaX in range(xStopPoint-xStartPoint):
        for sensorBeaconCoords in coordinateDataList:
            if sensorBeaconCoords[0].manhattanDistance(rowPoint+Coords(deltaX,0)) <= sensorBeaconCoords[2] and sensorBeaconCoords[1] != rowPoint+Coords(deltaX,0):
                unavailable += 1
                break
    return unavailable

def smartCheckUnavailableSpots(row, coordinateDataList):
    beaconOnlyList = [n[1] for n in coordinateDataList]
    occupiedSpots = []
    for coordinateSet in coordinateDataList:
        if Coords(coordinateSet[0].x, row).manhattanDistance(coordinateSet[0]) <= coordinateSet[2]:
            wingLen = coordinateSet[2] - Coords(coordinateSet[0].x, row).manhattanDistance(coordinateSet[0])
            occupiedSpots.append(Coords(coordinateSet[0].x, row)) if (Coords(coordinateSet[0].x, row) not in occupiedSpots and Coords(coordinateSet[0].x, row) not in beaconOnlyList) else None
            for deltaX in range(wingLen):
                deltaX += 1
                occupiedSpots.append(Coords(coordinateSet[0].x+deltaX, row)) if (Coords(coordinateSet[0].x+deltaX, row) not in occupiedSpots and Coords(coordinateSet[0].x+deltaX, row) not in beaconOnlyList) else None
                occupiedSpots.append(Coords(coordinateSet[0].x-deltaX, row)) if (Coords(coordinateSet[0].x-deltaX, row) not in occupiedSpots and Coords(coordinateSet[0].x-deltaX, row) not in beaconOnlyList) else None
    

    #beaconOnlyList = [n[1] for n in coordinateDataList]
    #uniqueOccupiedSpots = []
    #[uniqueOccupiedSpots.append(x) for x in occupiedSpots if (x not in uniqueOccupiedSpots and x not in beaconOnlyList)]
    return len(occupiedSpots)


def smartIntervalBasedCheckUnavailableSpots(row, coordinateDataList):
    listOfOccupiedIntervals = []
    for coordinateSet in coordinateDataList:
        if Coords(coordinateSet[0].x, row).manhattanDistance(coordinateSet[0]) <= coordinateSet[2]:
            wingLen = coordinateSet[2] - Coords(coordinateSet[0].x, row).manhattanDistance(coordinateSet[0])
            listOfOccupiedIntervals.append(Interval(coordinateSet[0].x-wingLen, coordinateSet[0].x+wingLen))

    while len(listOfOccupiedIntervals) > 1:
        action = False
        for i in range(len(listOfOccupiedIntervals)):
            for j in range(len(listOfOccupiedIntervals)):
                if i == j:
                    continue
                if listOfOccupiedIntervals[i].isOverlapping(listOfOccupiedIntervals[j]):
                    listOfOccupiedIntervals[i] = listOfOccupiedIntervals[i].mergeOverlappingIntervals(listOfOccupiedIntervals[j])
                    del listOfOccupiedIntervals[j]
                    action = True
                    break
            if action:
                break
        if not action:
            break

    return listOfOccupiedIntervals

def getCountOfUnavailableSpotsFromIntervals(row, intervals, coordinateDataList):
    count = 0
    for interval in intervals:
        count += interval.getCount()

    removedBeacons = []
    for coordinate in coordinateDataList:
        for interval in intervals:
            if coordinate[1].y == row and Interval(coordinate[1].x,coordinate[1].x).isOverlapping(interval) and coordinate[1] not in removedBeacons:
                count -= 1
                removedBeacons.append(coordinate[1])
    return count



rawBeaconData = getFileAsList("15th/testData")

coordinateLenData = []
for line in rawBeaconData:
    splitLine = line.split("=")
    sensor = Coords(int(splitLine[1].split(",")[0]), int(splitLine[2].split(":")[0]))
    beacon = Coords(int(splitLine[3].split(",")[0]), int(splitLine[4]))

    dist = sensor.manhattanDistance(beacon)

    coordinateLenData.append([sensor, beacon, dist])
    print("test")

"""
leftMostSensorIndex = 0
rightMostSensorIndex = 0
for i, coordinateData in enumerate(coordinateLenData):
    if coordinateData[0].x < coordinateLenData[leftMostSensorIndex][0].x:
        leftMostSensorIndex = i
    if coordinateData[0].x > coordinateLenData[rightMostSensorIndex][0].x:
        rightMostSensorIndex = i

print(checkUnavailableSpots(10, leftMostSensorIndex, rightMostSensorIndex, coordinateLenData))
"""
listOfOverlappingIntervals = smartIntervalBasedCheckUnavailableSpots(10, coordinateLenData)

print(getCountOfUnavailableSpotsFromIntervals(10, listOfOverlappingIntervals, coordinateLenData))

print("end")