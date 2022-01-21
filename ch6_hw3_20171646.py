a, b = input("두 자리 정수 두개를 입력 : ").split()
a = int(a)
b = int(b)

a_1 = a // 10
a_2 = a % 10

b_1 = b // 10
b_2 = b % 10

if(a_1 == b_1):
    if(a_2 == b_2):
        print("두 정수는 모두 {} 로 같은 정수입니다.".format(a))
    else:
        print("{} , {} : 하나의 숫자만 일치합니다.".format(a,b))
elif(a_2 == b_2):
    print("{} , {} : 하나의 숫자만 일치합니다.".format(a,b))
else:
    if(a_1 == b_2):
        if(a_2 == b_1):
           print("{} , {} : 자리 값만 다른 정수입니다.".format(a,b))
        else:
            print("{} , {} : 하나의 숫자만 일치합니다.".format(a,b))
    elif(a_2 == b_1):
            print("{} , {} : 하나의 숫자만 일치합니다.".format(a,b))
    else:
            print("{} , {} : 일치하지 않는 정수입니다.".format(a,b))
            
    
