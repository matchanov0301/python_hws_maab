
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{self.title}' is already borrowed.")
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False


# Member Class
class Member:
    limit = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.limit:
            raise MemberLimitExceededException(f"{self.name} has already borrowed 3 books.")
        book.borrow()
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            print(f"Member '{member_name}' is not registered.")
            return

        try:
            book = self.find_book(book_title)
            member.borrow_book(book)
            print(f"{member_name} successfully borrowed '{book_title}'.")
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(f"Error: {e}")

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            print(f"Member '{member_name}' is not registered.")
            return

        try:
            book = self.find_book(book_title)
            member.return_book(book)
            print(f"{member_name} successfully returned '{book_title}'.")
        except BookNotFoundException as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    library = Library()

    # Adding books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")
    book4 = Book("The Catcher in the Rye", "J.D. Salinger")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    # Adding members
    member1 = Member("Alice")
    member2 = Member("Bob")

    library.add_member(member1)
    library.add_member(member2)

    # Borrowing books
    library.borrow_book("Alice", "1984")  # Alice borrows "1984"
    library.borrow_book("Alice", "The Great Gatsby")  # Alice borrows another book
    library.borrow_book("Alice", "To Kill a Mockingbird")  # Alice borrows third book

    library.borrow_book("Alice", "The Catcher in the Rye")  # Should raise MemberLimitExceededException

    library.borrow_book("Bob", "1984")  # Should raise BookAlreadyBorrowedException

    library.return_book("Alice", "1984")  # Alice returns "1984"
    library.borrow_book("Bob", "1984")  # Now Bob can borrow "1984"

    library.borrow_book("Charlie", "The Great Gatsby")  # Charlie isn't registered (should print error)
