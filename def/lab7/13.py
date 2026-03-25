class Book:
    def __init__(self,title, author, pages):
        self.title = title 
        self.author = author 
        self.pages = pages 
    
    def is_long(self):
        if self.pages >= 300:
            return True 
        return False 
    
    def __str__(self):
        return f"Book : {self.title}, Author : {self.author}"

class EBook(Book):
    def __init__(self,title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def is_long(self):
        if (self.pages >= 200):
            return True 
        return False 

    def __str__(self):
        return f"Book : {self.title}, Author : {self.author}, File-size : {self.file_size}"


b1 = Book("War and Peace", "Tolstoy", 1225)
b2 = EBook("Python Basics", "Doe", 150, 2.5)

print(b1)
print(b2)
print(b1.is_long())   # True
print(b2.is_long())   # False)


    

    

