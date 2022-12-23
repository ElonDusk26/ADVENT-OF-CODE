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

    def isNeighbor(self, other):
        return 1 == abs(self - other).coordSum()


rawCoordinates = getFileAsList("18th/data")

coordList = []

for coords in rawCoordinates:
    x, y, z = tuple(map(int, coords.split(",")))
    coordList.append(Coord3D(x,y,z))


faces = len(coordList) * 6

for coords in coordList:
    for coordToCompare in coordList:
        faces -= 1 if coords.isNeighbor(coordToCompare) else 0

print(faces)