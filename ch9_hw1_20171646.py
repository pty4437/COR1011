for i in range(10):
    num = input("Enter a number : ")
    num = int(num)

    if num == 0:
        print("입력 받은 수가 0 입니다")
        break;
    elif num < 0:
        if num % 2 == 0:
            print(num, ": 음수, 짝수")
        else:
            print(num, ": 음수, 홀수")
    elif num > 0:
        if num % 2 == 0:
            print(num, ": 양수, 짝수")
        else:
            print(num, ": 양수, 홀수")


print("프로그램을 종료합니다")
