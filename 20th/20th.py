from copy import deepcopy

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

def moveItemFromIndexToIndexByOffsetInList(list, fromIndex, offset):
    item = list[fromIndex]
    if offset < 0:
        offset %= -len(list)
        offset = len(list) + offset - 1
    else:
        offset %= len(list)
    if (offset + fromIndex) > (len(list) - 1):
        offset = len(list) - offset - 1
        for i in range(offset):
            list[(fromIndex-i)%len(list)] = list[(fromIndex-i-1)%len(list)]
        list[(fromIndex - offset)%len(list)] = item
        return list


    for i in range(offset):
        list[(fromIndex+i)%len(list)] = list[(fromIndex+i+1)%len(list)]
    list[(fromIndex + offset)%len(list)] = item
    return list

def moveItemByOffsetFromIndex(list, fromIndex, offset):
    item = list[fromIndex]
    offset %= len(list)

    if offset + fromIndex > len(list) - 1:
        offset+=1
        reverseFromIndex = fromIndex - len(list) + offset
        moveInterval = list[reverseFromIndex:fromIndex]

        list[reverseFromIndex] = item

        for i,reverseItem in enumerate(moveInterval):
            list[reverseFromIndex + i + 1] = reverseItem
        return list

    moveInterval = list[fromIndex+1:fromIndex+offset+1]
    for i, intervalItem in enumerate(moveInterval):
        if offset < 0:
            list[fromIndex-offset+i] = intervalItem
        else:
            list[fromIndex+i] = intervalItem 

    list[fromIndex+offset] = item


    return list

 
def slowSwapByOffset(list, fromIndex, offset):
    direction = 1 if offset > 0 else -1
    offset %= ((len(list)-1) * direction) #was before: (len(list) * direction) -1 
                                          #which is incorrect, and causes errors, 
                                          #when the offset is equal (len(list) -1)*2
                                          #dosent cause errors if either 9998 og -9998 is present in the list
                                          #which is the case for the "data2" list

    currentIndex = fromIndex
    while offset != 0:
        nextIndex = currentIndex + direction
        if nextIndex == len(list):
            nextIndex = 0

        buffer = list[nextIndex]
        list[nextIndex] = list[currentIndex]
        list[currentIndex] = buffer
        currentIndex = nextIndex
        offset -= direction
    return list

        


def encryptData(unencryptedData):
    encryptedDataIndices = list(range(len(unencryptedData)))

    for i in range(len(unencryptedData)):
        offsetIndex = 0
        for j in range(len(encryptedDataIndices)):
            if encryptedDataIndices[j] == i:
                offsetIndex = j
                break
        offset = unencryptedData[i]

        encryptedDataIndices = slowSwapByOffset(encryptedDataIndices, offsetIndex, offset)
        #encryptedData = [unencryptedData[i] for i in encryptedDataIndices]  
        #print(encryptedData)
        pass

    return [unencryptedData[i] for i in encryptedDataIndices]    

def checkDuplicateCount(list):
    return len(list) - len(set(list))

test = [4, -2, 5, 6, 7, 8, 9]


#exit()

unencryptedData = list(map(int, getFileAsList("20th/data"))) #correct ans for data2 is 4224 and the ans 9596 is too high for data3

print(checkDuplicateCount(unencryptedData))

print(unencryptedData)

encrypted = encryptData(unencryptedData)

startIndex = 0

for i in range(len(encrypted)):
    if encrypted[i] == 0:
        startIndex = i
        break

firstCoord = encrypted[(startIndex+1000) % len(encrypted)] #data2 startindex 3384. data startindex 3239

secondCoord = encrypted[(startIndex+2000) % len(encrypted)]

thirdCoord = encrypted[(startIndex+3000) % len(encrypted)]

print(encrypted, firstCoord, secondCoord, thirdCoord, sum([firstCoord, secondCoord, thirdCoord]))
