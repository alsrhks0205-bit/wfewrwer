# method override

class Drink:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("self.name) : " , self.name)

class Coffee(Drink):
    pass
    def print_info(self):
        print("<Coffee>self.name : " , self.name)


d = Drink("포카리")
c = Coffee("라떼")

d.print_info()
c.print_info()

