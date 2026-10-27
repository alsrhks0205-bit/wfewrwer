# 모기잡는게임
import random

# 난이도 설정
x = ["□"] * 10
def mode():
    print("=====난이도를 설정하세요.=====\n")
    print("0. exit")
    print("1. easy mode")
    print("2. normal mode")
    print("3. hard mode")

mode()

def catch():
    print("대단하군요. 모기를 잡았습니다!")
def lost():
    print("오우..도망갔어요. 이래서 잠은 잘수 있겠어요?")


m = int(input("선택하신 난이도를 입력하세요 :   "))
while True:
    match m:
        case 0 :
            print("프로그램을 종료합니다.")
            break
    # easy mode
        case 1:
            while True:
                print("-----모기를 잡으세요-----(1~3)")
                result = random.randint(1,3)
                print(x[1:4])
                n = int(input("모기가 있는 위치는?    \n(숫자로 적어주세요.)"))
                if n == result:
                    catch()
                    break
                else:
                    lost()
            break
    # normal mode
        case 2:
            while True:
                print("-----모기를 잡으세요-----(1~5)")
                result = random.randint(1, 5)
                print(x[1:6])
                n = int(input("모기가 있는 위치는?    \n(숫자로 적어주세요.)"))
                if n == result:
                    catch()
                    break
                else:
                    lost()

    # hard mode
        case 3:
            while True:
                print("-----모기를 잡으세요-----(1~10)")
                result = random.randint(1, 10)
                print(x[1:11])
                n = int(input("모기가 있는 위치는?    \n(숫자로 적어주세요.)"))
                if n == result:
                    catch()
                    break
                else:
                    lost()