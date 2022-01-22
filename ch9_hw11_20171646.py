num = 0

for i in range(1, 6):
    num = 5 - i
    for j in range(1, num+1):
        print(" ", end = "")
    for j in range(1, i + (i-1) + 1):
        print("*", end = "")
    for j in range(1, num+1):
        print(" ", end = "")
    print()
        
        
