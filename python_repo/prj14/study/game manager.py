class GameManager:
    def start_updown_game(self):
        print("=====up down======")
    def start_baseball_game(self):
        print("=====base ball======")

    def print_menu(self):
        print("0. exit")
        print("1. updown game")
        print("2. baseball game")

    def game_start(self):
        while True:
            self.print_menu()
            n = input("menu : ")
            match n:
                case "0":
                    print("exit game");break
                case "1":
                    self.start_updown_game()
                case "2":
                    self.start_baseball_game()
                case _:
                    print("enter your choice")