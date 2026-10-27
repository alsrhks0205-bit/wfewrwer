class Athlete():
    def __init__(self, name, height, weight,):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return f'name={self.name},height={self.height},weight={self.weight}'

    def eat(self):
        print("오이쉬이")