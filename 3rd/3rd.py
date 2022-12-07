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

def splitHalf(string):
    length = int(len(string)/2)
    return string[:length], string[length:]

def convertoPriority(char):
    return priority.find(char.lower()) + (26 if char.isupper() else 0)


listOfBackpacks = getFileAsList("3rd/data")

sumPoints = 0
for backpack in listOfBackpacks:
    splitBackpack = splitHalf(backpack)
    comparison = compareString(splitBackpack[0], splitBackpack[1])
    if comparison[0]:
        sumPoints += convertoPriority(comparison[1])
print(sumPoints) #idk why it dosent wanna print :(