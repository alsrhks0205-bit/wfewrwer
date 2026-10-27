# 게시글

board_list = []

def insert_board():
    print("=====게시글 작성=====")
    t = input("제목 : ")
    c = input("내용 : ")
    d = {
        "title": t,
        "content": c,
    }
    board_list.append(d)
    print("게시글 작성 완료 !")

def select_board():
    print("----게시글 목록 조회-----")
    for x in board_list:
        print(x["title"], "/" , x["content"])

def print_menu():
    print("=====BOARD=====")
    print("1. 게시글 작성")
    print("2. 게시글 목록 조회")
    n = int(input("메뉴번호 : "))
    return n

while True:
    n = print_menu()
    if n == 0:
        break
    match n:
        case 1:
            insert_board()
        case 2:
            select_board()

