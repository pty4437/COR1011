numList = []

while True:
    a = input("정수를 입력 (0을 입력하면 종료) : ")
    a = int(a)

    if a == 0:
        break

    numList.append(a)

print("입력한 정수 리스트 :", numList)

sumOfList = 0

for i in numList:
    sumOfList += i

if len(numList) == 0:
    print("합계 : ")
    print("평균 : ")
else:
    print("합계 :", sumOfList)
    print("평균 :", sumOfList / len(numList))
