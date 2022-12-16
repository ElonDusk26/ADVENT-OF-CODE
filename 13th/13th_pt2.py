import json
from functools import cmp_to_key

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

def isValid(leftElement, rightElement, validity):
    for i in range(max(len(leftElement), len(rightElement))):
        if validity != None:
            break
        try:
            if isinstance(leftElement[i], int) and isinstance(rightElement[i], int): #if both are ints
                if leftElement[i] > rightElement[i]: #left larger than right, which is invalid
                    validity = False
                    return validity
                elif leftElement[i] < rightElement[i]:
                    validity = True
                    return validity
                continue
            if isinstance(leftElement[i], list) and isinstance(rightElement[i], list):#both are lists: recursively call itself
                validity = isValid(leftElement[i], rightElement[i], validity)
                continue

            #now either int and int || list and list is exhausted. 
            if isinstance(leftElement[i], list): #if the left is a list and right is an int
                validity = isValid(leftElement[i], [rightElement[i]], validity) #right element is made a list
                continue

            if isinstance(rightElement[i], list): #if the right is a list and left is an int
                validity = isValid([leftElement[i]], rightElement[i], validity) #left element is made a list
                continue
        except:
            if len(rightElement) < len(leftElement): #if the right list runs out first (has fewer items) then its invalid
                validity = False
                return validity
            elif len(rightElement) > len(leftElement): #left side runs out first is valid
                validity = True
                return validity
            break
    return validity

def bubbleSort(unsortedList, cmpFunc):
    while True:
        change = False
        for i in range(len(unsortedList)-1):
            i += 1
            if cmpFunc(unsortedList[i-1], unsortedList[i], None):
                pass
            else:
                buffer = unsortedList[i]
                unsortedList[i] = unsortedList[i-1]
                unsortedList[i-1] = buffer
                change = True
        if not change:
            break
    return unsortedList

def isValidToCMP(leftItem, rightItem):
    validity = isValid(leftItem, rightItem, None)
    if validity:
        return -1
    else:
        return 1

rawData = getFileAsList("13th/data")

#print(rawData[0].strip("][").split(","))

groupedData = [[json.loads(rawData[i-2]), json.loads(rawData[i-1])] for i in range(len(rawData)) if rawData[i] == ""]

indexSum = 0

unsortedData = []
for group in groupedData:
    unsortedData.append(group[0])
    unsortedData.append(group[1])

firstDivider = [[2]]
secondDivider = [[6]]

unsortedData.extend([firstDivider, secondDivider])

sortedData = sorted(unsortedData, key=cmp_to_key(isValidToCMP))

result = 1
for i, data in enumerate(sortedData):
    if data == firstDivider or data == secondDivider:
        result *= i+1

#index 4 and 5
print(result)
print("end")