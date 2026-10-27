# 이상한 출석 부르기 2

n = input()
x = input()
num_list = x.split()

for i in range(len(num_list) - 1, -1, -1):
    print(num_list[i], end=" ")

# i = len(num_list) - 1
# while i >= 0:
#     print(num_list[i], end=" ")
#     i -= 1

# n = input()
# x = input()
# num_list = x.split()
#
# for i in  range(9, -1, -1):
#     print(num_list[i], end=" ")
#
# for i in range(len(num_list) -1, -1, -1):
#     print(num_list[i], end=" ")





