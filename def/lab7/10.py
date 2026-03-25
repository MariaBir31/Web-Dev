class Student:
    def __init__(self, name, grade, subject):
        self.name = name 
        self.grade = grade
        self.subject = subject 
    
    def is_passing(self):
        if (self.grade >= 60):
            return True
        return False

    def __str__(self):
        return f"Student: {self.name}, Subject: {self.subject}"

class ExcellentStudent(Student):
    def __init__(self, name, grade, subject, scholarship):
        super().__init__(name, grade, subject)
        self.scholarship = scholarship

    def is_passing(self):
        return True
    
    def __str__(self):
        return f"Student: {self.name}, Subject: {self.subject}, Scholarship : {self.scholarship}"

s1 = Student("Maria", 55, "Math")
s2 = ExcellentStudent("Anna", 98, "Physics", 500)

print(s1)
print(s2)
print(s1.is_passing())   # False
print(s2.is_passing())   # True
