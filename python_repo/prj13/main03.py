class Champ:
    def __init__(self, n, h, a):
        self.name = n
        self.hp = h
        self.atk = a

    def attack(self):
        pass

    def q(self):
        pass

    def w(self):
        pass

    def e(self):
        pass

    def r(self):
        pass

v = Champ("vayne" ,100 , 10)
t = Champ("timo" ,80 , 15)

# vayne -> timo
v.attack()
t.hp = t.hp - v.atk

# timo -> vayne
t.attack()
v.hp = v.hp - t.atk

