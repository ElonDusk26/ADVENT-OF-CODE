def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList


class FileDirectory:

    def __init__(self, directoryName, parent = None):
        self.fileDirectory = []
        self.directoryName = directoryName
        self.parent = parent

    def addFile(self, filename, size):
        self.fileDirectory.append(self.File(filename, size))

    def addDirectory(self, directoryName):
        self.fileDirectory.append(FileDirectory(directoryName, self))

    def findItem(self, filename):
        for item in self.fileDirectory:
            if item == filename:
                return item
        return None

    def goToParent(self):
        return self.parent

    def __eq__(self, directoryName):
        return self.directoryName == directoryName

    class File:
        def __init__(self, filename, size):
            self.filename = filename
            self.size = size
        def __eq__(self, filename) -> bool:
            return self.filename == filename

def getSumOfDirectory(directory):
    directorySum = 0
    for item in directory.fileDirectory:
        if isinstance(item, FileDirectory.File):
            directorySum += item.size 
        else:
            directorySum += getSumOfDirectory(item) 
    return directorySum

def getSumOfAllDirectories(directory):
    out = 0
    for item in directory.fileDirectory:
        if isinstance(item, FileDirectory):
            sumOfDirectory = getSumOfDirectory(item)
            out += sumOfDirectory if sumOfDirectory <= 100000 else 0
            out += getSumOfAllDirectories(item)
    return out
            
        
cmdLines = getFileAsList("7th/data")

currentDir = FileDirectory("/")

i = 0
while i < len(cmdLines):
    strippedLines = cmdLines[i].split(" ")
    if strippedLines[1] == "ls":
        while True:
            i += 1

            if i >= len(cmdLines):
                break

            strippedOperation = cmdLines[i].split(" ")

            if strippedOperation[0] == "$": #if its a command then escape from the sequence
                break
        
            if currentDir.findItem(strippedOperation[1]) != None:
                continue #already exists and just go to the next item

            if strippedOperation[0] == "dir": #if ls shows a dir
                currentDir.addDirectory(strippedOperation[1])
            else:
                currentDir.addFile(strippedOperation[1], int(strippedOperation[0]))
    else:
        if strippedLines[2] == "..":
            currentDir = currentDir.goToParent()
            i += 1
        else:
            currentDir = currentDir.findItem(strippedLines[2])
            i += 1

while True: #go to root directory
    if currentDir.directoryName != "/":
        currentDir = currentDir.goToParent()
    else:
        break

print(getSumOfAllDirectories(currentDir))