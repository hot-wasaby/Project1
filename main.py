class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book removed: {book}")
                return
        print(f"Book with ISBN {isbn} not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

def main():
    library = Library()

    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Display all books")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)

        elif choice == '2':
            isbn_to_remove = input("Enter the ISBN of the book to remove: ")
            library.remove_book(isbn_to_remove)

        elif choice == '3':
            library.display_books()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
