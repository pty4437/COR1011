num = input("두 자연수 N1과 N2를 입력하세요(0 < N1 <= N2) : ").split(" ")

idx = 0

for i in num:
    num[idx] = int(i)
    idx += 1

res = 0

for i in range(num[0], num[1]+1):
    if i % 2 == 0:
        res += i


print("크기가 {} 이상이고 {} 이하인 모든 짝수의 합은 {}입니다.".format(num[0], num[1], res))

