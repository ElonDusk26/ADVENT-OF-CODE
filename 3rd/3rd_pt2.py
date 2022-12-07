priority = "_abcdefghijklmnopqrstuvwxyz"

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

def compareString(string1, string2):
    for char in string1:
        if char in string2:
            return True, char
    return False, ""

def compareString3(string1, string2, string3):
    for char in string1:
        if char in string2 and char in string3:
            return True, char
    return False, ""

def splitHalf(string):
    length = int(len(string)/2)
    return string[:length], string[length:]

def convertoPriority(char):
    return priority.find(char.lower()) + (26 if char.isupper() else 0)


listOfBackpacks = getFileAsList("3rd/data")

sumPoints = 0
for i in range(int(len(listOfBackpacks)/3)):
    backpackTrio = listOfBackpacks[i*3:i*3+3]
    sumPoints += convertoPriority(compareString3(backpackTrio[0], backpackTrio[1], backpackTrio[2])[1])

print(sumPoints)