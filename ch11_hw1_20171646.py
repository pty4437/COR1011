def password(string):
    """string이 유효한 password인지 판별"""
    if len(string) < 8:
        print("error! 8 글자 이상이어야 함")
        return False
    elif string.isnumeric() == True:
        print("error! 영문도 포함되어야 함")
        return False
    elif string.isalpha() == True:
        print("error! 숫자도 포함되어야 함")
        return False
    elif string.isalnum() == False:
        print("error! 영문자, 숫자로만 구성되어야 함")
        return False
    else:
        cnt = 0
        for i in range(0, 9):
            i = str(i)
            cnt += string.count(i)

        if cnt < 2:
            print("error! 최소한 2개의 숫자를 포함해야 함")
            return False
        else:
            return True


for i in range(0, 5):
    string = input("Enter password: ")
    res = password(string)
    if res == False:
        print("Invalid password")
    elif res == True:
        print("Valid password")
        break
