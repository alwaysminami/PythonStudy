coffee = 5

while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피가 나옵니다.")
        coffee -= 1
        print("현재 남은 커피 잔 수: %s\n" % coffee)
    elif money > 300:
        print("거스름돈 %d과 커피가 나옵니다." % (money - 300))
        coffee -= 1
        print("현재 남은 커피 잔 수: %s\n" % coffee)
    else:
        print("금액이 부족합니다.")
        print("남은 커피는 %d잔 입니다." % coffee)
        print("현재 남은 커피 잔 수: %s\n" % coffee)
    if coffee == 0:
        print("커피가 매진되었습니다. 판매를 중지합니다.")
        break