# 이상한 출석부르기 1

# 선생님이 부른 출석번호 n개를 리스트에 잘 받아놓움
n = input() #출석 몇번 부를거임?
x = input()
num_list = x.split()

memo = [0] * 24         # memo gt rdy

#출석 부른거 보고 메모장 업데이트 수정을 해줍니다
for student_num in num_list:
    student_num = int(student_num)
    memo[student_num] = int(memo[student_num]) + 1

#결과확인
for x in memo[1:24]:
    print(x , end=" ")


