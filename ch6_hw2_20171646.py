a, sik, b = input("수식 입력(예: 20 * 40) : ").split()

a = float(a)
b = float(b)

if(sik == '+'):
    print('{:.6f} + {:.6f} = {:.6f}'.format(a,b,a+b))
elif(sik == '-'):
    print('{:.6f} - {:.6f} = {:.6f}'.format(a,b,a-b))
elif(sik == '*'):
    print('{:.6f} * {:.6f} = {:.6f}'.format(a,b,a*b))
elif(sik == '/'):
    if(b == 0.0):
        print("0.000000 로 나누기를 수행할 수 없습니다.")
    else:
        print('{:.6f} / {:.6f} = {:.6f}'.format(a,b,a/b))
else:
    print("{} 지원하지 않는 연산자입니다.".format(sik))
