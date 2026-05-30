class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> str:
        return "generic sound"

    def describe(self) -> str:
        return f"Tôi là {self.name}, tiếng kêu: {self.make_sound()}"


class Dog(Animal):
    def make_sound(self) -> str:
        return "Gâu!"


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meo!"