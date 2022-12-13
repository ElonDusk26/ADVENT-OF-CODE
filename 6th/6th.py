from collections import Counter

def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

def find_first_index_of_n_consecutive_repeating_chars(s, n): #chatgpt
  # Loop through the string, starting from the nth character
  for i in range(n-1, len(s)):
    # Check if the current character is the same as the previous n-1 characters
    if all(s[i] == s[i-j] for j in range(1, n)):
      # If so, return the index of the current character
      return i
  # If no n consecutive repeating characters are found, return -1
  return -1


def getFirstUniqueSequence(inputString):
    for i in range(len(inputString) - 4):
        wordCounter = Counter(inputString[i:i+4])
        unique = True
        for letter, count in wordCounter.items():
            if count > 1:
                unique = False
                break
        if unique:
            return i + 4
    return -1


signal = getFileAsList("6th/data")

print(find_first_index_of_n_consecutive_repeating_chars("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4))

for line in signal:
    print(find_first_index_of_n_consecutive_repeating_chars(line, 4))