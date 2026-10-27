class AssetManager:
    def __init__ (self, asset):
        self.asset = asset
        self.income = 0
        self.expense = 0 #클랴스 자산 관리 매니저 생성

    def print_Menu(self):
        print("====자산관리 프로그램====")
        print("1. 수입 추가하기")
        print("2. 지출추가하기")
        print("3. 자산 현황보기")
        print("0. 종료하기")
# add income 함수 amount 변수 만들고 와일문 한번 돌때마다 수
    def add_income(self):
        amount = int(input("수입 금액: "))

        if amount <= 0:
            print("0보다 큰 금액을 입력하세요.")
            return

        self.income += amount
        self.asset += amount

        print("수입이 추가되었습니다.")
        print("현재 자산:", self.asset, "원")

# 지출
    def add_expense(self):
        amount = int(input("지출 금액: "))

        if amount <= 0:
            print("0보다 큰 금액을 입력하세요.")
            return

        if amount > self.asset:
            print("현재 자산보다 지출이 많습니다.")
            return

        self.expense += amount
        self.asset -= amount

        print("지출이 추가되었습니다.")
        print("현재 자산:", self.asset, "원")

# 현재 자산 확인
    def show_assets(self):
        print("===== 현재 자산 =====")
        print("현재 자산:", self.asset, "원")
        print("총수입:", self.income, "원")
        print("총지출:", self.expense, "원")