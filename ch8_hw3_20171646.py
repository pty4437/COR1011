fruit = {'배' : [2, 1000], '자몽' : [1, 2000], '메론' : [1, 8000], '감' : [6, 800]}

eat = input("먹고 싶은 과일은? : ")

if eat not in fruit :
    print(eat, "준비되어 있지 않습니다.")
elif fruit[eat][0] == 0:
    print(eat, "준비되어 있지 않습니다.")
else :
    print(eat, "맛있게 드세요")
    fruit[eat][0] = fruit[eat][0]-1

print()

print("각 과일 당 최소 5개는 되도록 구입합니다")

price = 0
keyList = list(fruit.keys())

for i in range (0, len(fruit)):
    if (5-fruit[keyList[i]][0]) >= 0:
        price += (5-fruit[keyList[i]][0]) * (fruit[keyList[i]][1])


print("구입에 필요한 총 금액은 :", price, "원 입니다")

