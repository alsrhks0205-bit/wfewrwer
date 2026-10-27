# 가위바위보 연산 게임 (사용자 VS컴퓨터)# 간단한 게임 소개
print("간단한 게임 소개: 3판 2선 승의 가위바위보 게임을 진행합니다 개임에서 지면 평생 코딩지옥에 갇힙니다..")
# "가위바위보"출력

user_score = 0
com_score = 0  # 사용자가 가위,바위,보 입력 ---> 숫자로 치완해주고 가위(1) 바위(2) 보(3)

import random

while user_score < 3 and com_score < 3:
    user = int(input("가위(1) 바위(2) 보(3)무엇을 내겠습니까?"))
    if not (1 <= user <= 3):  # 예측불가 사용자 사전방지
        print("다시 입력하세요 -.-")
        continue  # 컴퓨터가 랜덤하게 정수를 가져오고
    com = random.randint(1, 3)
    if com == 1:
        print("컴퓨터: 가위")
    elif com == 2:
        print("컴퓨터: 바위")
    elif com == 3:
        print("컴퓨터: 보")
# 사용자랑 컴퓨터 비교연산
# #사용자가 이기면 사용자 점수 +1 else 컴퓨터 +1///// 3판 2선승이니까 < 3 로 루프 돌리기
    if user == com:
        print("비김 다시!!")
        continue

    elif user == 1 and com == 2:
        print("컴퓨터 승..")
        com_score = com_score + 1
    elif user == 2 and com == 3:
        print("컴퓨터 승..")
        com_score = com_score + 1
    elif user == 3 and com == 1:
        print("컴퓨터 승..")
        com_score = com_score + 1

# 점수판print("=====점수판=====")
    else:
        print("사용자 승!!")
    user_score = user_score + 1
    print(" 사용자:", user_score)
    print(" 컴퓨터:", com_score)
    print("================")
    if user_score == 2 or com_score == 2:
        break

if user_score > com_score:
    print("--------------------")
    print("당신은 살아남으셨습니다")
    print("-------------------")
else:
    print("------------------------------")
    print("이런.. 당신은 코딩지옥에 빠졌습니다..")
    print("------------------------------")
