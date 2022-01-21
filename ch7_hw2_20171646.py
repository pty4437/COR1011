import math

L = [[1,2,3], [4,5], [6], [7,8]]
newList = []

sum = 0
idx = 0

for tmpList in L:
    for i in tmpList:
        sum += i*i
    newList[len(newList):len(newList)] = [sum]
    sum = 0


print(newList)
