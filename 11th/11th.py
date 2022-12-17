import math
from copy import copy

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

class rank: #copied from the first challenge day
    def __init__(self, rankLen):
        self.rankings = [0] * rankLen
        self.len = rankLen

    def insert(self,number):
        for i in range(len(self.rankings)): #go backwards to find the point at which the inserted number is larger
            if(self.rankings[-i - 1] < number): #if its larger
                for c in range(self.len - 1 - i): #from the front shift the list: 2nd becomes 3rd and 1st becomes 2nd
                    self.rankings[c] = self.rankings[c+1]
                self.rankings[-i-1] = number #finally update number 1 (largest)
                break

    def sum(self):
        return sum(self.rankings)

class Monkey:
    def __init__(self, listOfItemsToStart, operationList, testCondition, ifConditionTrueIndex, ifConditionFalseIndex):
        self.items = listOfItemsToStart
        self.testCondition = testCondition
        self.conditionTrueIndex = ifConditionTrueIndex
        self.conditionFalseIndex = ifConditionFalseIndex

        self.operationList = operationList

        if operationList[1] == "+":
            self.operationLambda = lambda old: (old + int(operationList[2]))
        else:
            if operationList[2] == "old":
                self.operationLambda = lambda old: (old * old)
            else:
                self.operationLambda = lambda old: (old * int(operationList[2]))

        self.activity = 0

    def playTurn(self, monkeyList):
        for item in self.items:
            self.activity += 1
            item = math.floor(self.operationLambda(item) / 3)
            if item % self.testCondition == 0:
                monkeyList[self.conditionTrueIndex].items.append(item)
            else:
                monkeyList[self.conditionFalseIndex].items.append(item)
        self.items = []



def loadMonkeys(rawMonkeyList):
    monkeyListOut = []
    for i in range(int(len(rawMonkeyList)/7)):
        #get the items first
        listOfMonkeyItemsString = rawMonkeyList[i*7+1]
        rawItemNumbersList = listOfMonkeyItemsString.split(":")[-1].strip(" ").split(",")
        monkeyItems = [int(rawItemString) for rawItemString in rawItemNumbersList]

        #get the operation
        operationList = rawMonkeyList[i*7+2].split("=")[-1].strip().split(" ")
        
        #getting the test condition
        testCondition = int(rawMonkeyList[i*7+3].split(" ")[-1])

        #getting the condition body
        ifConditionTrue = int(rawMonkeyList[i*7+4].split(" ")[-1])
        ifConditionFalse = int(rawMonkeyList[i*7+5].split(" ")[-1])

        #creating and appending the monkey class to the list
        monkeyListOut.append(Monkey(monkeyItems, operationList, testCondition, ifConditionTrue, ifConditionFalse))

        print(monkeyListOut[0].operationLambda(10))
    return monkeyListOut

            

rawMonkeyData = getFileAsList("11th/data")

monkeyData = loadMonkeys(rawMonkeyData)

for i in range(20):
    for monkey in monkeyData:
        monkey.playTurn(monkeyData)

monkeyBusinessRank = rank(2)

for monkey in monkeyData:
    monkeyBusinessRank.insert(monkey.activity)

print(monkeyBusinessRank.rankings[0] * monkeyBusinessRank.rankings[1])


print("end")