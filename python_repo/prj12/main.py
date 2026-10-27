class Board:
    def __init__(self , t , c):
        self.title = t
        self.content = c
    def __repr__(self) -> str:
        return f'{self.title} | {self.content}'

x = Board("title" , 'content')
# print(x.title)
# print(x.content)
print(x)