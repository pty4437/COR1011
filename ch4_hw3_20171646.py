sample = "abcABCdEFaBCDeFAbC"

sample = sample.lower()

print("\"abc 문자열 : %d 인덱스, %d 번 존재\"" % (sample.find("abc"), sample.count("abc")))
print("\"def 문자열 : %d 인덱스, %d 번 존재\"" % (sample.find("def"), sample.count("def")))
