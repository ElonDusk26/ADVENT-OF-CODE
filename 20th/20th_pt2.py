from copy import deepcopy

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList
 
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

def encryptDataIndices(unencryptedData, encryptedDataIndices):
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

    return encryptedDataIndices



unencryptedData = list(map(int, getFileAsList("20th/data"))) #correct ans for data2 is 4224 and the ans 9596 is too high for data3

print(unencryptedData)

unencryptedData = [x*811589153 for x in unencryptedData]#"decryption" key

encryptedDataIndices = list(range(len(unencryptedData)))

for i in range(10):
    encryptedDataIndices = encryptDataIndices(unencryptedData, encryptedDataIndices)
    print(encryptedDataIndices)

encryptedData = [unencryptedData[i] for i in encryptedDataIndices]

startIndex = 0

for i in range(len(encryptedData)):
    if encryptedData[i] == 0:
        startIndex = i
        break

firstCoord = encryptedData[(startIndex+1000) % len(encryptedData)] #data2 startindex 3384. data startindex 3239

secondCoord = encryptedData[(startIndex+2000) % len(encryptedData)]

thirdCoord = encryptedData[(startIndex+3000) % len(encryptedData)]

print(encryptedData, firstCoord, secondCoord, thirdCoord, sum([firstCoord, secondCoord, thirdCoord]))
