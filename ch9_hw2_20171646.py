L = []

for i in range(1,101):
    L.append(i)


for i in range(0,100):
    if L[i] % 8 == 0:
        print(L[i], end = " ")
