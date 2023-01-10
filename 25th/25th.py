def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

snafuConvTable=["0","1","2","=","-"]
def decimalToSNAFU(decNumber):
    snafuOut = ""
    i = 1
    while True:
        remainder = decNumber % 5*i
        snafuOut = snafuConvTable[remainder] + snafuOut
        remainder *= -1 if remainder > 2 else 1
        decNumber = int((decNumber-remainder) / 5*i)

        if decNumber == 0:
            return snafuOut

snafuToDecimalDict = {"0":0, "1":1, "2":2, "=":-2, "-":-1}
def snafuToDecimal(snafuNumber):
    decimalOut = 0
    for i, snafuPoint in enumerate(snafuNumber[::-1]):
        decimalOut += snafuToDecimalDict[snafuPoint] * 5**i
    return decimalOut



snafuData = getFileAsList("25th/data")

result = 0
for snafuNum in snafuData:
    result += snafuToDecimal(snafuNum)

print(result, decimalToSNAFU(result))