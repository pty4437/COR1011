a,b,c = input("세 개의 정수를 입력하시오 : ").split()
a = int(a)
b = int(b)
c = int(c)

print("내림차순 정렬: ",end='')

if(a < b):
    if(a < c):
        if(b < c):
            print(c, b, a)
        else:
            print(b,c,a)
    else:
        print(b,a,c)
else:
    if(b < c):
        if(c < a):
            print(a,c,b)
        else:
            print(c,a,b)
    else:
        print(a,b,c)
