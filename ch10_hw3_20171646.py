print("정수들을 입력:")

numList = list(map(int, input().split()))

i = 0
pos = 0
neg = 0
sumOfList = 0
while i < len(numList):
    
    if numList[i] > 0:
        pos += 1
        sumOfList += numList[i]
    elif numList[i] < 0:
        neg += 1
        sumOfList += numList[i]

    i+=1


if pos == 0 and neg == 0:
    print("입력한 숫자가 없습니다")

print("양수: {} 개, 음수 : {} 개, 합계 : {}".format(pos,neg,sumOfList))

