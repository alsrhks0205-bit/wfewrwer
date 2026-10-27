# 클래스 : 객체 만들기 위함
# 객체 : data + function


class Book:
    def __init__(self):
        self.a = 10
        self.b = 20

    def f01(self):
        print("f01")
    def f02(self):
        print("f02")
    def f03(self):
        print("f03")

book = Book()
book.f01()
book.f02()
book.f03()
print(book.a)
print(book.b)

