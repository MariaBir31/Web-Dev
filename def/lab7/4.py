class Dog:
    species = " German sheperd"

    def __init__(self, name, age, breed):
        self.name = name 
        self.age = age 
        self.breed = breed 

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speaks(self, sound):
        return f"{self.name} says {sound}"

brown = Dog("Brown", 3, "Sheperd")

print(brown.__str__())
print(brown.speaks("Wooof "))

     


