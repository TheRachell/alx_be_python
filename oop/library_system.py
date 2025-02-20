class Book:
    def __init__ (self, title, author):
        self.title = title 
        self.author = author 

    def __str__(self):
        return f"Book: {self.title} ny {self.author}"

class EBook(Book):
    def __init__ (self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File size:{self.file_size}kb"

class PrintBook(Book):
    def __init__ (self, title, author, page_count):
        self().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, page Count:{self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else :
            raise TypeError("only instances of Book, Ebook, or PrintBook")
        
    def list_books(self):
        for book in self.books:
            print(book)
