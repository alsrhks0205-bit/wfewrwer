from os import name


class Pokemon:
    def __init__(self , name , hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f"{self.name} / {self.hp}"