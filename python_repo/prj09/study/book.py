# 도서관리
# 도서 :title , price

#비어있는 도서목록 준비
book_list = []

while True:
    # 유저 입력
    print("====도서 등록====")
    t = input("도서 제목:  ")
    p = input("도서 가격:  ")

    # 입력데이터 --> 딕셔너리
    x = {
        "title" : t ,
        "price" : p
    }

    # 딕셔너리를 리스틀에 추가
    book_list.append(x)

    # 도서 추가 여부
    a = input("도서를 더 추가하시겠습니까?(Y/N)")
    if a == "N":
        break


#도서 목록 조회
for d in book_list:
    print(f"{d['title']} ({d["price"]}원)")


