# 도서관리 프로그램

class Book:
    def __init__(self, a , b):
        self.title = a
        self.price = b

book_list = []

def print_menu():
    print("0. exit")
    print("1. insert")
    print("2. select")


def insert():
    t = input("title :")
    p = input("price :")
    x = Book(t, p)
    book_list.append(x)

def select():
    for x in book_list:
        print(f"{x.title} / {x.price}")

while True:
    print_menu()
    n = int(input("menu : "))
    match n:
        case 0:
            print("exit......")
            break
        case 1:
            insert()
        case 2:
            select()

