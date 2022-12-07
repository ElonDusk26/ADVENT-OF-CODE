#ROCK = 1 point
#PAPER = 2 points
#SCISSORS = 3 points

#A = ROCK
#B = PAPER
#C = SCISSORS

#X = LOSE
#Y = DRAW
#Z = WIN

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
        if encodedHand in "A":
            self.hand = self.ROCK
        elif encodedHand in "B":
            self.hand = self.PAPER
        elif encodedHand in "C":
            self.hand = self.SCISSOR

    def __eq__(self, toCompare):
        if isinstance(toCompare, gesture):
            return self.hand == toCompare.hand
        else:
            return self.hand == toCompare

def calculatePoint(opponentsHand: gesture, desiredOutcome):
    pointsOut = 0
    if desiredOutcome == "X": #loss
        pointsOut += LOSS
        if opponentsHand.hand == gesture.ROCK:
            return pointsOut + gesture.SCISSOR
        if opponentsHand.hand == gesture.PAPER:
            return pointsOut + gesture.ROCK
        if opponentsHand.hand == gesture.SCISSOR:
            return pointsOut + gesture.PAPER

    if desiredOutcome == "Y": #draw
        pointsOut += DRAW
        pointsOut += opponentsHand.hand
        return pointsOut
    if desiredOutcome == "Z": #win
        pointsOut += WIN
        if opponentsHand.hand == gesture.ROCK:
            return pointsOut + gesture.PAPER
        if opponentsHand.hand == gesture.PAPER:
            return pointsOut + gesture.SCISSOR
        if opponentsHand.hand == gesture.SCISSOR:
            return pointsOut + gesture.ROCK

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
    points += calculatePoint(gesture(seperatedPosition[0]), seperatedPosition[1])
print(points)