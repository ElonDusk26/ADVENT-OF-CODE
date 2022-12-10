def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

def checkHorizontalTree(treeMapRow, treeString):
    highestTree = -1
    #forwards
    for i, treeVal in enumerate(treeString):
        if int(treeVal) > highestTree:
            highestTree = int(treeVal)
            treeMapRow[i] = True
    #backwards
    highestTree = -1
    for i in range(len(treeString)):
        if highestTree < int(treeString[-i-1]):
            highestTree = int(treeString[-i-1])
            treeMapRow[-i-1] = True

def checkVerticalTree(treeMap, treeDataList):
    #up to down
    for j in range(len(treeDataList[0])):
        highestTree = -1
        for i in range(len(treeDataList)):
            if int(treeDataList[i][j]) > highestTree:
                highestTree = int(treeDataList[i][j])
                treeMap[i][j] = True
    #down to up
    for j in range(len(treeDataList[0])):
        highestTree = -1
        for i in range(len(treeDataList)):
            if int(treeDataList[-i-1][j]) > highestTree:
                highestTree = int(treeDataList[-i-1][j])
                treeMap[-i-1][j] = True
    
def getTreeScenicScore(treeDataList, treeRow, treeColumn):
    treeToCheck = int(treeDataList[treeRow][treeColumn])
    returnScore = 0

    
    #right
    scoreIncrementer = 1
    offset = 1
    while treeColumn+offset < len(treeDataList[treeRow]) - 1:
        if int(treeDataList[treeRow][treeColumn+offset]) < treeToCheck: #if the tree is less than the scenic tree
            scoreIncrementer += 1
            offset += 1
        else:
            break

    returnScore += scoreIncrementer

    #left
    scoreIncrementer = 1
    offset = 1
    while treeColumn-offset > 0:
        if int(treeDataList[treeRow][treeColumn-offset]) < treeToCheck: #if the tree is less than the scenic tree
            scoreIncrementer += 1
            offset += 1
        else:
            break

    returnScore *= scoreIncrementer

    #down
    scoreIncrementer = 1
    offset = 1
    while treeRow+offset < len(treeDataList) - 1:
        if int(treeDataList[treeRow + offset][treeColumn]) < treeToCheck: #if the tree is less than the scenic tree
            scoreIncrementer += 1
            offset += 1
        else:
            break

    returnScore *= scoreIncrementer

    #up
    scoreIncrementer = 1
    offset = 1
    while treeRow-offset > 0:
        if int(treeDataList[treeRow - offset][treeColumn]) < treeToCheck: #if the tree is less than the scenic tree
            scoreIncrementer += 1
            offset += 1
        else:
            break

    returnScore *= scoreIncrementer

    return returnScore


def countTrees(treeMap):
    treeSum = 0
    for row in treeMap:
        row = list(map(int, row))
        treeSum += sum(row)
    return treeSum


treeData = getFileAsList("8th/data")

print(getTreeScenicScore(treeData, 3, 2))

largestScore = 0
for row in range(len(treeData)):
    for column in range(len(treeData)):
        treeScoreBuffer = getTreeScenicScore(treeData, row, column)
        if treeScoreBuffer > largestScore:
            largestScore = treeScoreBuffer

print(largestScore)
