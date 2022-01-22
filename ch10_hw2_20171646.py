num = input("구하려는 소수의 개수를 입력 : ")

num = int(num)

count = 1
sosu = 2
tmp = 3
flag = 0

while True:

    if num == 1 or num == 0:
        break

    
    for j in range(2, tmp):
        if  tmp % j == 0:
            tmp += 1
            flag = -1
            break

    if flag == -1:
        flag = 0
        continue


    print(sosu)
    sosu = tmp
    tmp += 1
    count += 1
    

    if count == num:
        break


if num != 0:
    print(sosu)


print(num, "개의 소수를 찾았습니다")
