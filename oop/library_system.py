class Book:
    def __init__(self, title, author):
        """Base class for all book types with title and author attributes."""
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        """EBook class that inherits from Book and adds file_size attribute."""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """PrintBook class that inherits from Book and adds page_count attribute."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.page_count}"

class Library:
    def __init__(self):
        """Library class that uses composition to manage a collection of books."""
        self.books = []
    
    def add_book(self, book):
        """Adds a book, ebook, or printbook instance to the library."""
        self.books.append(book)
        print(f"Added: {book.title}")
    
    def list_books(self):
        """Prints details of each book in the library."""
        print("\n--- Library Collection ---")
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)
        print("--------------------------\n")
