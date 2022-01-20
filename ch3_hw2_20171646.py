price = 3928

fiveHundred = price // 500
remain_1 = price % 500

oneHundred = remain_1 // 100
remain_2 = remain_1 % 100

print('500원짜리 동전 :', fiveHundred, '개')
print('100원짜리 동전 :', oneHundred, '개')
print('남은 금액 :', remain_2, '원')
