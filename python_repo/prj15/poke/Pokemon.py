class Pokemon:
    def __init__(self, name, hp, atk, arm):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.arm = arm

    def __str__(self):
        return f"name={self.name} hp={self.hp} atk={self.atk} arm={self.arm}"

