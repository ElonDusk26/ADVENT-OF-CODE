def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

calorieData = getFileAsList("1st/data")


counter = 0
maxCount = 0
for calorie in calorieData:
    if calorie != '':
        counter += int(calorie)
    else:
        if counter >= maxCount:
            maxCount = counter
        counter = 0
print(maxCount)