words_lev1 = {
        "apple" : "사과" ,
        "book" : "책" ,
        "orange" : "오렌지" ,
    }
words_lev2 = {
        "cluster": "무리",
        "tremendous": "엄청난",
        "catastrophic": "재앙적인",
    }
while True:
    for k,v in words_lev1.items():
        for attempt in range(3):
            x = input(f"{k} : ").strip()
            if x == v:
                print("정답입니다")
                break
            else:
                print(f"오답입니다 (남은기회: {2 - attempt}번)")
        else:
            print(f"3번 모두 틀렸습니다. 정답: {v}")

    while True:
        choice = input("press y for play harder mode or press n for exit: ").strip().lower()
        if choice == "y" or choice == "n":
            break
        print("y 또는 n만 입력해주세요")
    if choice == "y":
        for k, v in words_lev2.items():
            for attempt in range(3):
                x = input(f"{k} : ").strip()
                if x == v:
                    print("정답입니다")
                    break
                else:
                    print(f"오답입니다 (남은 기회: {2 - attempt}번)")
            else:
                print(f"3번 모두 틀렸습니다. 정답: {v}")
    elif x == "n":
        break
print("exited...")

