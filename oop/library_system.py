class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} is written by {self.author}"
        
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} is written by {self.author} and is {self.file_size}MB"
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} is written by {self.author} and has {self.page_count} pages"
        
class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        for self.book in self.books:
            if isinstance(self.book, PrintBook):
                print(f"PrintBook: {self.book.title} is written by {self.book.author}")
            elif isinstance(self.book, EBook):
                print(f"EBook: {self.book.title} is written by {self.book.author}")
            elif isinstance(self.book, Book):
                print(f"Book: {self.book.title} is written by {self.book.author}")
