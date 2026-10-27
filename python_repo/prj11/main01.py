# 함수 형태
'''
def 함수이름(매개변수):
    실행할코드
    실행할코드
    실행할코드
    return 값
'''
# 파라미터(parameter) ㄴㄴ, 리턴(return) ㄴㄴ
def hello():
    print("hello" "world", end=" ")

# hello()

# 매개변수(parameter) ㅇㅇ, 리턴(return) ㄴㄴ
def hello(x):
    print(f"{x} 님 welcome ~")

# hello("hong gil dong")

def print_plus_result(a,b):
    result = a + b
    print(result)


# print_plus_result(3, 4)

# 파라미터(parameter) ㄴㄴ, 리던(return) ㅇㅇ
def get_number():
    return 10

# x = get_number()
# print(x)

# 파라미터(parameter) ㅇㅇ, 리턴(return) ㅇㅇ
def plus_ten(x):
    result = x + 10
    return result

a = plus_ten(3)
print(a)