class Dog :
    species = "jmmcfe"

    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def description(self):
        return f"{self.name} is {self.age} years old dog"

    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 5)

print(miles.description())
print(miles.speak("Awooo"))