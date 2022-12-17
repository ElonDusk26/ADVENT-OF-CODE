testNumber = 123
unAlteredTest = testNumber
modOperator1 = 5
modOperator2 = 16

modMultiplier = modOperator1 * modOperator2

print(testNumber % modOperator1)
print(testNumber % modOperator2)
print(unAlteredTest % modOperator1)
print(unAlteredTest % modOperator2)

testNumber *= 10
testNumber -= modMultiplier
unAlteredTest *= 10

print(testNumber % modOperator1)
print(testNumber % modOperator2)
print(unAlteredTest % modOperator1)
print(unAlteredTest % modOperator2)

testNumber *= 12
testNumber -= modMultiplier*100
unAlteredTest *= 12

print(testNumber % modOperator1)
print(testNumber % modOperator2)
print(unAlteredTest % modOperator1)
print(unAlteredTest % modOperator2)

testNumber += 7
testNumber -= modMultiplier * 100
unAlteredTest += 7

print(testNumber % modOperator1)
print(testNumber % modOperator2)
print(unAlteredTest % modOperator1)
print(unAlteredTest % modOperator2)