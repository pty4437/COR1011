print("***** if조건문으로 작성 *****")
mon = input("월을 입력하세요: ")

mon = int(mon)

if mon == 1:
    print("1월은 January입니다")
elif mon == 2:
    print("2월은 Feburary입니다")
elif mon == 3:
    print("3월은 March입니다")
elif mon == 4:
    print("4월은 April입니다")
elif mon == 5:
    print("5월은 May입니다")
elif mon == 6:
    print("6월은 June입니다")
elif mon == 7:
    print("7월은 July입니다")
elif mon == 8:
    print("8월은 August입니다")
elif mon == 9:
    print("9월은 September입니다")
elif mon == 10:
    print("10월은 October입니다")
elif mon == 11:
    print("11월은 November입니다")
elif mon == 12:
    print("12월은 December입니다")

print("***** 리스트로 작성 *****")
mon = input("월을 입력하세요: ")

mon = int(mon)

monList = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print("%d월은 %s입니다" % (mon, monList[mon-1]))
