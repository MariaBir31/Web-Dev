class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def speak(self):
        return "Some sound"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    def speak(self):
        return ("Woof!")


class Cat(Animal):
    def speak(self):
        return ("Meow!")

d = Dog("Loki", 5)
c = Cat("Barsik", 4)

animals = [d, c]

for animal in animals:
    print(animal)
    print(animal.speak())

