# 4. Simple Library System
# The Goal: Create a class Book that accepts title and author.
# Create a child class Ebook that also accepts file_size.
# Create a method in Ebook called get_details() that prints all three pieces of information in a clean format.
# Key concept: Managing multiple parameters through inheritance.

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class Ebook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size = file_size

    def get_details(self):
        print(f"Book Details is {self.title} by {self.author} and file size is {self.file_size} MB")

e1=Ebook("Ethics and Values","Sardarji",23)
e1.get_details()