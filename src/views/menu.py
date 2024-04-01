from views.messages import Messages


class Menu:
    def __init__(self, controller):
        self.controller = controller

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
