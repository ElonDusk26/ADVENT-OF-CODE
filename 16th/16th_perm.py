from copy import deepcopy
from itertools import permutations

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

class Valve:
    def __init__(self, valveName, flowRate: int, connectorValves):
        self.flowRate = flowRate
        self.name = valveName
        self.connectorValves = connectorValves
        self.connectorValveIndices = []
        self.index = 0
    def getIndicesForConnectors(self, valveList):
        for connectorValveName in self.connectorValves:
            for i, valve in enumerate(valveList):
                if valve == connectorValveName:
                    self.connectorValveIndices.append(i)
                    break
        
        for i, valve in enumerate(valveList):
            if valve == self:
                self.index = i

    def __eq__(self, other):
        if isinstance(other, Valve):
            return self.name == other.name
        else:
            return self.name == other

def findShortestDistanceBetweenValves(startValve: Valve, endValve: Valve, valveList):
    if startValve == endValve:
        return 0

    #visitedIndices = [i for i, valve in enumerate(valveList) if valve == startValve]
    visitedIndices = [startValve.index]
    availableMoves = startValve.connectorValveIndices


    moves = 0
    while len(availableMoves) > 0:
        moves += 1
        availableMovesToAppend = []
        for moveIndex in availableMoves:
            if valveList[moveIndex] == endValve:
                return moves
            if moveIndex not in visitedIndices:
                availableMovesToAppend.extend(valveList[moveIndex].connectorValveIndices)
                visitedIndices.append(moveIndex)
        availableMoves = availableMovesToAppend
    return False

def findSummedFlowOfValve(fromValve: Valve, targetValve: Valve, valveList, timeLeft):
    distance = findShortestDistanceBetweenValves(fromValve, targetValve, valveList)
    timeLeft -= distance + 1
    return targetValve.flowRate * timeLeft, timeLeft

def permGen(lst):
    permItr = permutations(lst)
    for perm in permItr:
        yield perm

rawValveData = getFileAsList("16th/data")


valveList = []
for valve in rawValveData:
    valveName = valve.split(" ")[1]
    flowRate = int(valve.split("=")[1].split(";")[0])

    valveConnectorNames = [v.strip(",") for v in valve.split(" ")[9::]]

    valveList.append(Valve(valveName, flowRate, valveConnectorNames))

for valve in valveList:
    valve.getIndicesForConnectors(valveList)

#print(findShortestDistanceBetweenValves(valveList[0], valveList[6], valveList))

valvesWithFlow = [v for v in valveList if v.flowRate > 0]

startValve = [v for v in valveList if v == "AA"][0] #find the start valve with the name AA

flowPermutations = permGen(valvesWithFlow)

highestFlow = 0
bestPerm = valvesWithFlow

for flowPerm in flowPermutations:
    timeLeft = 30
    flow = 0
    currentValve = startValve
    for i, valve in enumerate(flowPerm):
        valveFlow, timeLeft = findSummedFlowOfValve(currentValve, valve, valveList, timeLeft)
        if valveFlow <= 0:
            break
        currentValve = valve
        flow += valveFlow
        #print("opened valve", valve.name, "and got", flow, "and time left:", timeLeft)
    if flow > highestFlow:
        highestFlow = flow
        bestPerm = flowPerm

print("best flow:", highestFlow)
        



#print(findLargestFlow(valveList[0], 30, valveList))

print("end")