from collections import Counter

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

def getFirstUniqueSequence(inputString):
    for i in range(len(inputString) - 4):
        wordCounter = Counter(inputString[i:i+4])
        unique = True
        for letter, count in wordCounter.items():
            if count > 1:
                unique = False
                break
        if unique:
            return i + 4
    return -1


signal = getFileAsList("6th/data")

for line in signal:
    print(getFirstUniqueSequence(line))