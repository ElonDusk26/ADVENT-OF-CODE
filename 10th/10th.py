def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

def addToRegister(registerList, toAdd):
    registerList.append(registerList[-1])
    registerList.append(registerList[-1] + toAdd)

def noOperation(registerList):
    registerList.append(registerList[-1])


operationList = []
cycleRegisterList = [1] #startValue

operationList = getFileAsList("10th/data")

for operation in operationList:
    splitOperation = operation.split(" ")
    if splitOperation[0] == "addx":
        addToRegister(cycleRegisterList, int(splitOperation[1]))
    else:
        noOperation(cycleRegisterList)

summedVals = 0
for i in range(6):
    print(cycleRegisterList[i*40+20-1]*(i*40+20))
    summedVals += cycleRegisterList[i*40+20-1]*(i*40+20)
print(summedVals)
