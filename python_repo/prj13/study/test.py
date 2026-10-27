# study.person 파일에 가보면 class 만들어놓은거 있어
from study.person import Person
# 모듈 전체 가져오기
# import study.person # 모듈명. 이름 형태로 접근
# study.person.Person()

# 특정 요소만 가져오기
from person import f03
# from person import x , f01 as f04
# f04()
# 이름이 겹치면 덮어쓰기 됨

# def f01(): pass

x = Person("hong",  20)
y = Person("kim",  30)
z = Person("lee",  40)
print(x.name)
print(x.age)

print(y.name)
print(y.age)

print(z.name)
print(z.age)
