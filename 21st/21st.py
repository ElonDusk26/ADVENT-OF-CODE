import yaml

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

class Monkey:
    def __init__(self, name, jobString):
        self.name = name
        if isinstance(jobString, int):
            self.isJobANumber = True
            self.number = jobString
        else:
            self.isJobANumber = False
            self.jobOperatorLambda, self.targetApes = self.interpretJob(jobString)
            

    def interpretJob(self, jobString): #only run if the job isnt a number
        splitJob = jobString.split(" ")
        jobLambda = None
        if splitJob[1] == "+":
            jobLambda = lambda x, y: (x+y)
        elif splitJob[1] == "-":
            jobLambda = lambda x, y: (x-y)
        elif splitJob[1] == "*":
            jobLambda = lambda x, y: (x*y)
        else:
            jobLambda = lambda x, y: (x/y)
        return jobLambda, [splitJob[0], splitJob[2]]

    def indexMonkeys(self, monkeyList):
        if not self.isJobANumber:
            pass

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