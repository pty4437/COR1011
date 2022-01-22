score = [82, 98, 100, 40, 75, 55, 73, 24, 10, 64]

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
