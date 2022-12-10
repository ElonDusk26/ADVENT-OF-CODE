def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

def addToRegister(registerList, toAdd):
    registerList.append(registerList[-1])
    registerList.append(registerList[-1] + toAdd)

def noOperation(registerList):
    registerList.append(registerList[-1])


operationList = []
cycleRegisterList = [1] #startValue


operationList = getFileAsList("10th/data")

for operation in operationList:
    splitOperation = operation.split(" ")
    if splitOperation[0] == "addx":
        addToRegister(cycleRegisterList, int(splitOperation[1]))
    else:
        noOperation(cycleRegisterList)


#order of operations:
#first a pixel is drawn, then the register change is detected.
#the sprite is 3 wide ###



spriteIndex = 1
crtScreenList = []

for crtRow in range(6): #6 is the amount of rows on the screen
    crtScreenRow = [""]*40
    for pixelIndex in range(40): #40 is the screen length
        spriteIndex = cycleRegisterList[(crtRow*40)+pixelIndex]

        written = False
        for pixelOffset in range(3):
            try: #ignores if the index is out of bounds
                if crtScreenRow[spriteIndex - 1 + pixelOffset] == "" and spriteIndex - 1 + pixelOffset == pixelIndex: #pixel goes from 0, 1, 2
                    crtScreenRow[pixelIndex] = "#"
                    written = True
                    break
            except:
                continue
        if not written:
            crtScreenRow[pixelIndex] = "."
    crtScreenList.append(crtScreenRow)
    




for screenRow in crtScreenList:
    print("".join(str(x) for x in screenRow))    
