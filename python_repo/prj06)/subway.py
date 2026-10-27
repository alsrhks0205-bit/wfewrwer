# 서브웨이 키오스크 #서브웨이 (빵, 야채 -> 금액)

print("====서브웨이 키오스크====")
print("----빵을 1개 고르고, 야채를 자유롭게 추가하세요")

print("\n----- 빵 선택 ------\n")            # 빵 메뉴판

print("1. 플렛 브래드(1000원)")
print("2, 호밀빵(2000원)")
print("3 식빵(3000원)")

bread_num = input("빵 번호: ")               # 빵 선택, 금액 업데이트

if bread_num == "1":
    price = 1000
elif bread_num == "2":
    price = 2000
elif bread_num == "3":
    price = 3000

while True:                                 # 야채 메뉴판
    print("0. 야채 선택 종료")
    print("1. 야채 오이 (500원)")
    print("2. 야채 버섯 (700원)")
    print("3. 야채 당근 (800원)")

    veg_num = input("야채 번호: ")            # 야채 선택, 금액 업데이트

    if veg_num == "1":
        price = 1000 + 500
    elif veg_num == "2":
        price = 2000 + 700
    elif veg_num == "3":
        price = 3000 + 800
    elif veg_num == "0":
        break

print(f"총 결제하실 금액은 {price}원 입니다")       #금액