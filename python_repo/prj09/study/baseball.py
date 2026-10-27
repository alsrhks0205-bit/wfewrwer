import random

answer = random.sample(range(1,10), 3)
x = ""
x += str(answer[0])
x += str(answer[1])
x += str(answer[2])
answer = x

while True:
    #입력받기
    pred_num = input("숫자 예측: ")

    # S, B 판단
    s = 0
    b = 0
    for i in range(3):
        if pred_num[i] == answer[i]:
            s += 1
        elif pred_num[i] in answer:
            b += 1
    #결과 출력
    if s == 3:
        print("정답 !!!")
        break
    elif s == 0 and b == 0:
        print("아웃 !!!")
    else:
        print(f"{s}S. {b}B")
