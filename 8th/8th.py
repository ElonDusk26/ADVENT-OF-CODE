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

def countTrees(treeMap):
    treeSum = 0
    for row in treeMap:
        row = list(map(int, row))
        treeSum += sum(row)
    return treeSum


treeData = getFileAsList("8th/data")

rowLen = len(treeData[0])
columnLen = len(treeData)

treeMap = []
for i in range(rowLen):
    treeMap.append([])
    for j in range(columnLen):
        treeMap[i].append(False)

for treeMapRow, treeStringRow in zip(treeMap, treeData):
    checkHorizontalTree(treeMapRow, treeStringRow)

checkVerticalTree(treeMap, treeData)

print(countTrees(treeMap))