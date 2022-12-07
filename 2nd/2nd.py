#ROCK = 1 point
#PAPER = 2 points
#SCISSORS = 3 points

#A or X = ROCK
#B or Y = PAPER
#C or Z = SCISSORS

#WIN = 6 points
#DRAW = 3 points
#LOSS = 0 points

WIN = 6
DRAW = 3
LOSS = 0

class gesture:
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    def __init__(self, encodedHand):
        self.hand = 0
        if encodedHand in "A X":
            self.hand = self.ROCK
        elif encodedHand in "B Y":
            self.hand = self.PAPER
        elif encodedHand in "C Z":
            self.hand = self.SCISSOR

    def __eq__(self, toCompare):
        if isinstance(toCompare, gesture):
            return self.hand == toCompare.hand
        else:
            return self.hand == toCompare

def evaluatePositionPoints(first: gesture, second: gesture):#first is the "main player"
    if first == second:#draw
        return DRAW + first.hand
    else:
        if first == gesture.ROCK and second == gesture.SCISSOR:
            return WIN + first.hand
        if first == gesture.PAPER and second == gesture.ROCK:
            return WIN + first.hand
        if first == gesture.SCISSOR and second == gesture.PAPER:
            return WIN + first.hand
        return LOSS + first.hand


def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

rockPaperScissorsData = getFileAsList("2nd/data")

points = 0
for position in rockPaperScissorsData:
    seperatedPosition = position.split(' ')
    points += evaluatePositionPoints(gesture(seperatedPosition[1]), gesture(seperatedPosition[0]))
print(points)