class Food:
    def __init__(self , menu , price , check):
        self.menu = menu
        self.price = price
        self.check = check
    def __str__(self):
        return f"{self.menu} / {self.price} / {self.check}"