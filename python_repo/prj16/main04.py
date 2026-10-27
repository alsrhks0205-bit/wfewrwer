class Coffee:
    def __init__(self,name,price):
        print("init called")
        self.name = name
        self.price = price

    def __str__(self):
        print("str called")
        return f"{self.name} / {self.price}"

    def __eq__(self, other):
        return True
x = Coffee("americano", 1000)
print(x == 1)