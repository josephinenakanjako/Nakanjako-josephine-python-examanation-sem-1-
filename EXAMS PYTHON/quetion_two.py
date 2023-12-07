class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Creating an instance of the Book class
book_instance = Book(" Programming in python", "kayinga joseph", 567)

book_instance.display_info()



#(iv) a
Classes are fundamental in object-oriented programming as they allow for creating reusable code, and abstraction by bundling data and methods together within a single structure.
#(iv)b
Objects allow you to store data specific to that instance and perform actions using the methods defined in their class. 


