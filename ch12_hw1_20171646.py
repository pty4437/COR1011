def cal_sum(op1, op2):
        return op1+op2
def cal_min(op1, op2):
        return op1-op2
def cal_mul(op1, op2):
        return op1*op2
def cal_div(op1, op2):
        return op1/op2





a, cal, b = input("수식 입력(예: 20 * 40) : ").split()

a = float(a)
b = float(b)


if cal == '+':
    res = cal_sum(a,b)
    print("{:.6f} {} {:.6f} = {:.6f}".format(a,cal,b,res))
elif cal == '-':
    res = cal_min(a,b)
    print("{:.6f} {} {:.6f} = {:.6f}".format(a,cal,b,res))
elif cal == '*':
    res = cal_mul(a,b)
    print("{:.6f} {} {:.6f} = {:.6f}".format(a,cal,b,res))
elif cal == '/':
    if b != 0:
        res = cal_div(a,b)
        print("{:.6f} {} {:.6f} = {:.6f}".format(a,cal,b,res))
    else:
        print("{:.6f} 로 나누기를 수행할 수 없습니다".format(b))
else:
    print(cal, "지원하지 않는 연산자입니다")
    

