num = input("Enter N (0 < N < 10) : ")
num = int(num)

if num <= 0 or num >= 10:
    print("ERROR: N must be 0 < N < 10.")
else:
    if num % 2 == 0:
        for i in range(1, num+1):
            for j in range(1, i+1):
                print(j, end = "")
            print()
        for i in range(1, num+1):
            print(i, end = "")
        print()
        for i in range(1, num):
            for j in range(1, num-i+1):
                print(j, end = "")
            print()

    elif num % 2 == 1:
        for i in range(1, num+1):
            for j in range(1, i+1):
                print(j, end = "")
                
            print()
        for i in range(1, num):
            for j in range(1, num-i+1):
                print(j, end = "")
            print()
