from practice.animal import Animal
from practice.athlete import Athlete
from practice.pokemon import Pokemon

# x = Animal("진돗게" , 50 , "전기타입")
# print(x.name)
# print(x.weight)
# print(x.type)
# print(type(x))
#
# y = Animal("잉어" , 3 , "불속성")
# print(y.name)
# print(y.weight)
# print(y.type)
# print(type(y))
#
# z = Animal(n="말미잘" ,w=0.5 , t="땅속성")
# print(z.name)
# print(z.weight)
# print(z.type)
# print(type(z))

# p1 = Pokemon("피카츄", 100)
# p2 = Pokemon("파이리", 90)
# p3 = Pokemon("꼬부기", 110)
#
# print(p1.__str__())
# print(p2)
# print(p3)


# baverage_01 = Baverage("라떼", 3000)
# baverage_02 = Baverage("아메리카노", 2000)
# baverage_03 = Baverage("아이스티", 2000)
#
# print (baverage_01)
# print (baverage_02)
# print (baverage_03)
x = Athlete(name="홍길동" , height="180", weight="70")
print(x)
x.eat()
