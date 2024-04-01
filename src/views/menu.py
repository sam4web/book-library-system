import getpass

from views.messages import Messages
from controllers.book import BookController
from controllers.user import UserController


class BookMenu:
    def __init__(self):
        self.controller = BookController()

    def display_book_menu(self):
        while True:
            choice = input(Messages.book_menu())
            if choice == "1":
                print("")
                title = input("Title: ")
                author = input("Title: ")
                genre = input("Genre: ")
                self.controller.add_book(title, author, genre)
            elif choice == "2":
                self.controller.get_book_list()
            elif choice == "3":
                self.search_book_menu()
            elif choice == "4":
                print(Messages.goodbye_message())
                break
            else:
                print(Messages.invalid_choice())

    def search_book_menu(self):
        choice = input(Messages.search_book())
        if choice == "1":
            title = input("Title: ")
            self.controller.search_book(title=title)
        elif choice == "2":
            author = input("Author: ")
            self.controller.search_book(author=author)
        elif choice == "3":
            genre = input("Genre: ")
            self.controller.search_book(genre=genre)
        else:
            print(Messages.invalid_choice())


class UserMenu:
    def __init__(self):
        self.controller = UserController()

    def display_login_menu(self):
        while True:
            choice = input(Messages.login_menu())
            if choice == "1":
                email = input("\nEnter email: ")
                password = getpass.getpass(prompt="Enter password: ")
                user = self.controller.login_user(email, password)
                if user:
                    break
            elif choice == "2":
                username = input("\nEnter username: ")
                email = input("Enter email: ")
                password = getpass.getpass(prompt="Enter password: ")
                user = self.controller.register_user(username, email, password)
                if user:
                    break
            else:
                print(Messages.invalid_choice())
