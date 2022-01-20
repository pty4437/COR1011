a = 10
print(a, type(a))
print()

import math
b = 5
print("5의 루트 값은: {:.5f}".format(math.sqrt(b)))
print()

c = 'hello'
print(c[::2])
print(c[::-1])
print(c[1::-1])
print(c[2:])
print()

print("과목\t점수")
print("------------")
num1 = 80.3
num2 = 95.7
num3 = 73.2
print("국어:  {:.2f}".format(num1))
print("영어:  {:.2f}".format(num2))
print("수학:  {:.2f}".format(num3))
print("총점: {:.2f}".format(num1+num2+num3))
print("평균:  {:.4f}".format((num1+num2+num3)/3))
print()

str = 'These_functions_cannot_be_used_with_complex_numbers.'
print("원래 문장: {}".format(str))
str = str.replace("_", " ")
print("수정한 문장: {}".format(str))
print("a는 {}번 나왔다.".format(str.count("a")))
print("e는 {}번 나왔다.".format(str.count("e")))
print("u는 {}번 나왔다.".format(str.count("u")))
print("space는 {}번 나왔다.".format(str.count(" ")))
print("모두 대문자로 바꾸면: {}".format(str.upper()))
