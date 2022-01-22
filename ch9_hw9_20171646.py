score = input("성적들을 입력하세요: ").split(" ")

idx = 0

for i in score:
    score[idx] = int(i)
    idx += 1

num = 1

for i in score:
    if i >= 90:
        print("{}번 학생의 성적은 A입니다.".format(num))
    elif i >= 70:
        print("{}번 학생의 성적은 B입니다.".format(num))
    elif i >= 50:
        print("{}번 학생의 성적은 C입니다.".format(num))
    else:
        print("{}번 학생의 성적은 F입니다.".format(num))

    num += 1
