def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line) #NOT STRIPPED
    return rList

def importStack(inputList):
    outList = [[] for i in range(9)]

    for line in inputList:
        for i in range(9):
            bit = line[i*4 + 1]
            if bit != " ":
                outList[i].append(bit)
    return outList

def moveStack(stack, amount, fromIndex, toIndex):
    buffer = []
    for i in range(amount):
        buffer.append(stack[fromIndex].pop(0))
    [stack[toIndex].insert(0, subBuffer) for subBuffer in buffer]
        
def extractMoveCommands(moveCommandList):
    out = []
    for line in moveCommandList:
        toAppend = []
        toAppend.append(line.split(" ")[1])
        toAppend.append(line.split(" ")[3])
        toAppend.append(line.strip().split(" ")[5])
        toAppend = list(map(int, toAppend))
        out.append(toAppend)
    return out


stackData = getFileAsList("5th/stack")

stack = importStack(stackData)

moveCommandList = getFileAsList("5th/moveCommands")

moveCommands = extractMoveCommands(moveCommandList)

for command in moveCommands:
    moveStack(stack, command[0], command[1]-1, command[2]-1)

for stackFile in stack:
    print(stackFile[0], end="")
print("\nend")