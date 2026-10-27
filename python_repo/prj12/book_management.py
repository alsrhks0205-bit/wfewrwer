# 종료하기
# 도서 등록
# 도서 조회

book_list = []

def print_menu():
    print("----- BOOK -----")
    print("0. exit")
    print("1. insert")
    print("2. select")

def insert_book():
    print("----- insert book -----")
    t = input("title : ")
    c = input("price : ")
    d = {
        "title" : t ,
        "price" :  c ,
    }
    book_list.append(d)
    print("~~~insert finished~~~")

def select_book():
    print("----- select book -----")
    for d in book_list:
        print(f"{d['title']} / {d['price']}")


while True:
    print_menu()
    user_input_number = int(input())
    match user_input_number:
        case 0: print("종료하겠습니다"); break
        case 1: insert_book()
        case 2: select_book()


