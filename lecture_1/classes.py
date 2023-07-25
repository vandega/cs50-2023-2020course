class Human():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __gt__(self, other):
        if isinstance(other, Human):
            return self.age > other.age

        else:
            raise ValueError('error')


me = Human('joni', 25)
someone = Human('petre', 30)

print(me < someone)
