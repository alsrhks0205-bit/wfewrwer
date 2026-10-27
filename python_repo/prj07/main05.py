# for i in range(1, 11):
#     print(i, end="")
#
# result = 0
# for i in range(1, 11):
#     result = result + i
#     result += i
# print(result)

n = int(input())
result = 0
for i in range(3, n+1):
    if i%2 != 0:
        result += i
print(result)