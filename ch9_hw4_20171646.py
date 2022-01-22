print("Enter data :")

numList = []

num = input().split(" ")
idx = 0

M2 = 0
E2 = 0

for i in num:
    num[idx] = float(i)
    idx += 1

for i in num:
    M2 += i ** 2
    E2 += i

M2 = M2 / len(num)
E2 = (E2 / len(num)) ** 2

import math as m

std_dev = m.sqrt(M2 - E2)
print("{:.5f}".format(std_dev))
    
    
