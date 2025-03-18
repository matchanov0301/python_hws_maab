class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}!"

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Moo")

    def produce_milk(self):
        return f"{self.name} is producing milk."


class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cluck")

    def lay_egg(self):
        return f"{self.name} laid an egg."


class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Baa")

    def shear_wool(self):
        return f"{self.name} is being sheared for wool."


# Example Usage
cow = Cow("Bessie", 5)
chicken = Chicken("Clucky", 2)
sheep = Sheep("Wooly", 4)

animals = [cow, chicken, sheep]

for animal in animals:
    print(animal.make_sound())
    print(animal.eat())
    print(animal.sleep())

print(cow.produce_milk())
print(chicken.lay_egg())
print(sheep.shear_wool())
