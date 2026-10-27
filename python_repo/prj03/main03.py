# 나이 입력받고, 연령대 출력하기
# 10대, 20대, 30대, 40대, 기타
age = int(input("당신의 나이는ㅋ"))

if age < 10:
    print("10세 미만")
elif age < 20 :
    print("10대")
elif age < 30 :
    print("20대")
elif age < 40 :
    print("30대")
elif age < 50 :
    print("40대")
else:
    print("기타")
