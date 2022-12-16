def find_largest_sum(lst):
  # Initialize the current group and the largest sum to 0
  current_group = []
  largest_sum = 0

  # Iterate through the list
  for s in lst:
    # If the current string is not empty, add it to the current group
    if s:
      current_group.append(int(s))
    # If the current string is empty, check if the sum of the current group is larger than the largest sum
    # If it is, update the largest sum
    # Then reset the current group
    else:
      current_sum = sum(current_group)
      if current_sum > largest_sum:
        largest_sum = current_sum
      current_group = []

  # Check if the sum of the final group is larger than the largest sum
  # If it is, update the largest sum
  final_sum = sum(current_group)
  if final_sum > largest_sum:
    largest_sum = final_sum

  # Return the largest sum
  return largest_sum


def getFileAsList(filename):
    rList = []
    with open(filename, "r") as fileObj:
        for line in fileObj.readlines():
            rList.append(line.strip())
    return rList

calorieData = getFileAsList("1st/data")

print(find_largest_sum(calorieData))