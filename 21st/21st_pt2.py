import yaml

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

def evaluateMonkey(targetMonkey, monkeyDict):
    targetMonkeyVal = monkeyDict[targetMonkey]
    if isinstance(targetMonkeyVal, int):
        return targetMonkeyVal

    splitJob = targetMonkeyVal.split(" ")

    if splitJob[1] == "+":
        return evaluateMonkey(splitJob[0],monkeyDict) + evaluateMonkey(splitJob[2],monkeyDict)
    elif splitJob[1] == "-":
        return evaluateMonkey(splitJob[0],monkeyDict) - evaluateMonkey(splitJob[2],monkeyDict)
    elif splitJob[1] == "*":
        return evaluateMonkey(splitJob[0],monkeyDict) * evaluateMonkey(splitJob[2],monkeyDict)
    else:
        return evaluateMonkey(splitJob[0],monkeyDict) / evaluateMonkey(splitJob[2],monkeyDict)


def evaluateMonkeyWithHUMN(targetMonkey, monkeyDict, humn):
    targetMonkeyVal = monkeyDict[targetMonkey]
    if isinstance(targetMonkeyVal, int):
        if targetMonkey == "humn":
            return humn
        return targetMonkeyVal

    splitJob = targetMonkeyVal.split(" ")

    if splitJob[1] == "+":
        return evaluateMonkeyWithHUMN(splitJob[0],monkeyDict,humn) + evaluateMonkeyWithHUMN(splitJob[2],monkeyDict,humn)
    elif splitJob[1] == "-":
        return evaluateMonkeyWithHUMN(splitJob[0],monkeyDict,humn) - evaluateMonkeyWithHUMN(splitJob[2],monkeyDict,humn)
    elif splitJob[1] == "*":
        return evaluateMonkeyWithHUMN(splitJob[0],monkeyDict,humn) * evaluateMonkeyWithHUMN(splitJob[2],monkeyDict,humn)
    else:
        return evaluateMonkeyWithHUMN(splitJob[0],monkeyDict,humn) / evaluateMonkeyWithHUMN(splitJob[2],monkeyDict,humn)

def calculateGradientAtVal(startMonkey, val, monkeyDict):
    y1 = evaluateMonkeyWithHUMN(startMonkey, monkeyDict, val)
    y2 = evaluateMonkeyWithHUMN(startMonkey, monkeyDict, val+1)
    slope = y2-y1
    return y1, slope

def computeHumn(startMonkey, targetVal, monkeyDict):
    original = monkeyDataDict["humn"]
    humn = original
    while True:
        out, gradient = calculateGradientAtVal(startMonkey,humn,monkeyDataDict)
        diff = hasToEqual - out
        humn = (diff / gradient) + humn
        print("current iteration:", evaluateMonkeyWithHUMN(startMonkey, monkeyDataDict, humn))
        print("difference:", diff)
        if evaluateMonkeyWithHUMN(startMonkey, monkeyDataDict, humn) == targetVal:
            break
    return int(humn)


    
def findHumn(targetMonkey, monkeyDict):
    targetMonkeyVal = monkeyDict[targetMonkey]
    if isinstance(targetMonkeyVal, int):
        return targetMonkey == "humn"
    splitJob = targetMonkeyVal.split(" ")
    return findHumn(splitJob[0],monkeyDict) or findHumn(splitJob[2],monkeyDict)

monkeyDataDict = None
with open("21st/data") as f:
    monkeyDataDict = yaml.full_load(f)

rootVal = monkeyDataDict["root"]

if findHumn(rootVal.split(" ")[0], monkeyDataDict):
    hasToEqual = evaluateMonkey(rootVal.split(" ")[2], monkeyDataDict)
    print("has to equal", hasToEqual)
    print("humn equals", computeHumn(rootVal.split(" ")[0],hasToEqual, monkeyDataDict)) #calculating humn by using some sort of gradient descent ahahahahahaha

