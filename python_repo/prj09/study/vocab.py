# 영어단어 나오면, 한국어 뜻 말하기

words = {
    "apple" : "사과" ,
    "book" : "책" ,
    "orange" : "오렌지" ,
}
for k,v in words.items():
    x = input(f"{k} : ").strip()
    if x == v:
        print("정답입니다")
    else:
        print("오답입니다")