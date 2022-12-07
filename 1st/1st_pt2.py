def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

class rank:
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

    

calorieData = getFileAsList("1st/data")

counter = 0
ranker = rank(3)
for calorie in calorieData:
    if calorie != '':
        counter += int(calorie)
    else:
        ranker.insert(counter)
        counter = 0
print(ranker.sum())