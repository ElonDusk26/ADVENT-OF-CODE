from copy import deepcopy

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

def getRecursiveFlow(fromValve: Valve, timeLeft, valvesWithFlow, openedValves, valveList, totalFlow, fullPathFlows, openedValvePath, flowList, returnFlowList):
    moved = False
    for valve in valvesWithFlow:
        if timeLeft <= 0:
            break
        if valve not in openedValves:
            moveFlow, moveTimeLeft = findSummedFlowOfValve(fromValve, valve, valveList, timeLeft)
            if moveTimeLeft <= 0:
                continue
            moved = True
            moveOpenedValves = deepcopy(openedValves)
            moveOpenedValves.append(valve)
            moveFlowList = deepcopy(flowList)
            moveFlowList.append(moveFlow+totalFlow)
            getRecursiveFlow(valve, moveTimeLeft, valvesWithFlow, moveOpenedValves, valveList, totalFlow + moveFlow,fullPathFlows,openedValvePath,moveFlowList,returnFlowList)
    if not moved:
        #print(totalFlow)
        fullPathFlows.append(totalFlow)
        openedValvePath.append(openedValves)
        returnFlowList.append(flowList)
    return fullPathFlows, openedValvePath, returnFlowList


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

flowPaths = []
flowPathways = []
flowList = []

startValve = [v for v in valveList if v == "AA"][0] #find the start valve with the name AA

flowPaths, flowPathways, flowList = getRecursiveFlow(startValve, 30, valvesWithFlow, [], valveList, 0,flowPaths,flowPathways,[], flowList)

highestFlow = 0
highestFlowIndex = 0
for i, flowNum in enumerate(flowPaths):
    if flowNum > highestFlow:
        highestFlow = flowNum
        highestFlowIndex = i

timeLeft = 30
flow = 0
currentValve = startValve
for i, valve in enumerate(flowPathways[highestFlowIndex]):
    valveFlow, timeLeft = findSummedFlowOfValve(currentValve, valve, valveList, timeLeft)
    currentValve = valve
    flow += valveFlow
    print("opened valve", valve.name, "and got", flow, "and time left:", timeLeft, "and recursive current flow", flowList[highestFlowIndex][i])
    



#print(findLargestFlow(valveList[0], 30, valveList))

print("end")