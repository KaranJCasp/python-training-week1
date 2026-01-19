'''
4. Library Management System (Main Project)
Create a complete Library Management System using classes:

Class: Book
Attributes: book_id, title, author, is_available, borrowed_by
Methods:
  get_info() - return formatted book details
  mark_borrowed(member_name) - set availability to False
  mark_returned() - set availability to True

Class: Member
Attributes: member_id, name, borrowed_books (list of book_ids), max_books (limit: 3)
Methods:
  borrow_book(book) - add book to borrowed list if under limit
  return_book(book) - remove book from borrowed list
  get_borrowed_books() - return list of currently borrowed books

Class: Library
Manages collections of Book and Member objects
Methods:
  add_book(title, author) - add new book with unique ID
  register_member(name) - register new member with unique ID
  issue_book(member_id, book_id) - handle book borrowing
  receive_book(member_id, book_id) - handle book returns
  search_books(keyword) - search by title or author
  get_available_books() - list all books currently available

Requirements:
Use proper exception handling (book not found, member limit exceeded, etc.)
Validate all inputs
Generate unique IDs for books and members
Create a menu-driven interface

Bonus: Save/load library data to/from file
'''

import uuid
import uuid

class Book:
    def __init__(self, title, author, book_id=None, is_available=True, borrowed_by=None):
        self.book_id = book_id or str(uuid.uuid4())[:8] 
        self.title = title
        self.author = author
        self.is_available = is_available
        self.borrowed_by = borrowed_by

    def get_info(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}"

    def mark_borrowed(self, member_name):
        self.is_available = False
        self.borrowed_by = member_name

    def mark_returned(self):
        self.is_available = True
        self.borrowed_by = None

class Member:
    def __init__(self, name, member_id=None, borrowed_books=None, max_books=3):
        self.member_id = member_id or str(uuid.uuid4())[:8] 
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []
        self.max_books = max_books

    def borrow_book(self, book_id):
        if len(self.borrowed_books) >= self.max_books:
            raise Exception(f"Limit reached ({self.max_books} books).")
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
        else:
            raise Exception(f"Member does not have this book.")

    def get_borrowed_books(self):
        return self.borrowed_books

class Library:
    def __init__(self):
        self.books = {} 
        self.members = {} 

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books[new_book.book_id] = new_book
        return new_book.book_id

    def register_member(self, name):
        new_member = Member(name)
        self.members[new_member.member_id] = new_member
        return new_member.member_id

    def issue_book(self, member_id, book_id):
        if member_id not in self.members:
            raise Exception("Member ID not found.")
        if book_id not in self.books:
            raise Exception("Book ID not found.")
        book = self.books[book_id]
        member = self.members[member_id]
        if not book.is_available:
            raise Exception("Book is already borrowed.")
        member.borrow_book(book_id)
        book.mark_borrowed(member.name)

    def receive_book(self, member_id, book_id):
        if member_id not in self.members:
            raise Exception("Member ID not found.")
        if book_id not in self.books:
            raise Exception("Book ID not found.")
        member = self.members[member_id]
        book = self.books[book_id]
        member.return_book(book_id)
        book.mark_returned()

    def search_books(self, keyword):
        keyword = keyword.lower()
        results = [b.get_info() for b in self.books.values() if keyword in b.title.lower() or keyword in b.author.lower()]
        return results

    
    def get_available_books(self):
        return [b.get_info() for b in self.books.values() if b.is_available]
    
    
def main():
    lib = Library()
    while True:
        print("--- Library Management System ---")
        print("1. Add Book\n2. Register Member\n3. Issue Book\n4. Return Book")
        print("5. Search Books\n6. List Available Books\n7. Exit")
        choice = input("Select an option: ")

        try:
            if choice == '1':
                t = input("Title: ")
                a = input("Author: ")
                bid = lib.add_book(t, a)
                print(f"Book added! ID: {bid}")

            elif choice == '2':
                n = input("Member Name: ")
                mid = lib.register_member(n)
                print(f"Member registered! ID: {mid}")

            elif choice == '3':
                mid = input("Member ID: ")
                bid = input("Book ID: ")
                lib.issue_book(mid, bid)
                print("Book issued successfully!")

            elif choice == '4':
                mid = input("Member ID: ")
                bid = input("Book ID: ")
                lib.receive_book(mid, bid)
                print("Book returned successfully!")

            elif choice == '5':
                kw = input("Enter title or author keyword: ")
                results = lib.search_books(kw)
                print("\n".join(results) if results else "No books found.")

            elif choice == '6':
                books = lib.get_available_books()
                if(len(books)!=0):
                 for book in books:
                   print(book)
                else:
                 print("No books available.")

            elif choice == '7':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

        


