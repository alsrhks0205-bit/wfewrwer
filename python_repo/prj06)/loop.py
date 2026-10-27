# 중첩 반복문
# 구구단

# print("2 x 1 = 2")
# print("2 x 2 = 4")
# print("2 x 3 = 6")
# print("2 x 4 = 8")
# print("2 x 5 = 10")
# print("2 x 6 = 12")
# print("2 x 7 = 14")
# print("2 x 8 = 16")
# print("2 x 9 = 18")
# print("2 x 10 = 20")
#
# print(f"{2} x {1} = {2*1}")
# print(f"{2} x {2} = {2*2}")
# print(f"{2} x {3} = {2*3}")
# print(f"{2} x {4} = {2*4}")
# print(f"{2} x {5} = {2*5}")
# print(f"{2} x {6} = {2*6}")
# print(f"{2} x {7} = {2*7}")
# print(f"{2} x {8} = {2*8}")
# print(f"{2} x {9} = {2*9}")


# print(f"{2} x {num} = {2*num}")


dan = 2
while dan < 10:
    num = 1

    while num < 10:
        print(f"{dan} x {num} = {dan * num}")
        num = num + 1
    dan = dan + 1


