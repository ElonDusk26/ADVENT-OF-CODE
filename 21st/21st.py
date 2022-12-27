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
    

monkeyDataDict = None
with open("21st/data") as f:
    monkeyDataDict = yaml.full_load(f)

print(evaluateMonkey("root", monkeyDataDict))