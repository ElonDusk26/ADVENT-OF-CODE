import json

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
                if leftElement > rightElement: #left larger than right, which is invalid
                    validity = False
                    return validity
                elif leftElement < rightElement: #LARGE ERROR HAHAHA! forgot to add indexes... see pt2
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

rawData = getFileAsList("12th/data")

#print(rawData[0].strip("][").split(","))

groupedData = [[json.loads(rawData[i-2]), json.loads(rawData[i-1])] for i in range(len(rawData)) if rawData[i] == ""]

indexSum = 0

for i, pair in enumerate(groupedData):
    validity = None
    validity = isValid(pair[0], pair[1], validity)
    print(validity)
    indexSum += (i+1) if validity else 0

print(indexSum)
print("end")