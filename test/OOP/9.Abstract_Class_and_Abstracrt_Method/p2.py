"""
Class => Library
Layers of abstraction => display available books, to lend a book, to add a book

Class => Customer
Layers of abstraction => request for a book, return a book
"""


class Library:
    def __init__(self, list_of_books):
        self.available_books = list_of_books

    def display_available_books(self):
        print()
        print('Available Books: ')
        for book in self.available_books:
            print(book)

    def lend_book(self, request_book):
        if request_book in self.available_books:
            print('You have now borrowed the book')
            self.available_books.remove(request_book)
        else:
            print('Sorry, the book is not available in our list.')

    def add_book(self, return_book):
        self.available_books.append(return_book)
        print('You have returned the book. Thank you!')


class Customer:
    def request_book(self):
        print('Enter the name of a book you would like to borrow: ')
        self.book = input()
        return self.book

    def return_book(self):
        print('Enter the name of the book which you are returning: ')
        self.book = input()
        return self.book


library = Library(['Game of Thrones', 'Fools Die', 'The Godfather'])
customer = Customer()
while True:
    print('Enter 1 to display the available books')
    print('Enter 2 to request for a book')
    print('Enter 3 to return a book')
    print('Enter 4 to exit')
    user_choice = int(input())
    if user_choice is 1:
        library.display_available_books()
    elif user_choice is 2:
        request_book = customer.request_book()
        library.lend_book(request_book)
    elif user_choice is 3:
        returned_book = customer.request_book()
        library.add_book(returned_book)
    elif user_choice is 4:
        quit()
