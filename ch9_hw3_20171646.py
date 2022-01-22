A = [4, 8, 2, 3, 4, 2]
B = [7, 2, 5, 2, 3, 6, 5]
tmp = set()
L = []

for i in B:
    if i in A:
        tmp.add(i)


for i in tmp:
    L.append(i)

L.sort()
print(L)
