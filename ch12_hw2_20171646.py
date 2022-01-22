import random

def throw_coin(b_time,time):

    a = 0

    for i in range(b_time, time):
        fb = random.randint(0, 1)

        if fb == 0:
            a += 1

    
    return a    


throw = input("동전 던지기 시도 횟수를 입력(1 - 100) : ")
throw = int(throw)

i = 1
b = 0
res = 0

while True:

    if i > throw:
        break

    j = i
    
    if i < 11:
        i += 1

    else:
        i += 10


    res = throw_coin(j, i)

    b += res
    

    if i <= throw+1:
        print("{:3} 번째까지 던지기에서 앞면이 나온 확률 : {:3.0%}".format(i-1, b/i))


print()
print("***********************************************")
print("총 {}번 동전 던지기에서 앞면이 나온 확률 : {:3.0%}".format(throw, b/i))
