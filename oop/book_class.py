class Book:
    def __init__ (self, title, author, year):
        self.title = title
        self.author = author
        self.year = year  

    def __del__(self):
        print (f"deleting {author}")

    def __str__ (self):
        return "{title} by {auhtor}. published in {year}"
    
    def __repr__ (self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    