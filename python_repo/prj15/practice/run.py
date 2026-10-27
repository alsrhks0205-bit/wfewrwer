from practice.assignment import AssetManager

AM = AssetManager(500000)
x = AM.print_Menu()
print(x)

while True:
    n = input("메뉴를 선택하세요: ")

    match n:
        case "1":
            AM.add_income()

        case "2":
            AM.add_expense()

        case "3":
            AM.show_assets()

        case "0":
            print("프로그램을 종료합니다.")
            break

        case _:
            print("잘못된 메뉴입니다.")