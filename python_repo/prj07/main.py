
# 숫자 1 ~ 12 입력받아서
# 해당 월의 마지막 일 출력

# n = int(input("Enter a number: "))
# if n == 1: print("31")
# if n == 2: print("28")
# if n == 3: print("31")
# if n == 4: print("30")
# if n == 5: print("31")
# if n == 6: print("31")
# if n == 7: print("30")
# if n == 8: print("31")
# if n == 9: print("30")
# if n == 10: print("31")
# if n == 11: print("30")
# if n == 12: print("31")

x = int(input("month?"))
match x:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31")
    case 2:
        print("28")
    case 4 | 6 | 9 | 11:
        print("30")
    case _:
        print(f"입력하신 {_}월은 존재하지 않습니다")



