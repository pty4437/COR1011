def countKey(string, ch):
    """string문자열에서 ch문자가 몇 개 있는지 반환"""
    return string.count(ch)

string = input("문자열 입력 : ")
string = string.lower()
searchList = []

for i in range(0, len(string)):
    if string[i] == ' ':
        continue
    if string[i] in searchList:
        continue

    cnt = countKey(string, string[i])
    print(string[i], ":", cnt)

    searchList.append(string[i])
    
