def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList



def compare(elf1, elf2, recursed=False) -> bool: #checks whether any of the two elves fully overlap
    if (elf1[0] <= elf2[0]) and (elf1[1] >= elf2[1]): #if lower bound is less and upper bound is greater
        return True
    elif not recursed:
        return compare(elf2, elf1, True)
    return False



listOfElves = getFileAsList("4th/data")

overlaps = 0
for unsplitElfPair in listOfElves:
    elfPair = [list(map(int, splitElf.split("-"))) for splitElf in unsplitElfPair.split(",")]
    if compare(elfPair[0], elfPair[1]):
        overlaps += 1

print(overlaps)
