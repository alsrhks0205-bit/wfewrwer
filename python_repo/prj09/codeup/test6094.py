# 이상한 출석 부르기3

n = input()
num_list = input().split()

memo = num_list[0]
for num in num_list:
    memo = int(memo)
    num = int(num)
    if memo > num:
        memo = num

print(memo)
