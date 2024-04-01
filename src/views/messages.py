class Messages:
    @staticmethod
    def welcome_message():
        print("Welcome to Book Library System.")

    @staticmethod
    def book_menu():
        return """\nMain Menu:
    1. Add a Book
    2. View all books
    3. Search Books
    4. Exit
Enter your choice:  """

    @staticmethod
    def login_message():
        return """\nYou need to be logged in to continue. Please choose:
    1. To log in existing account
    2. Create new account (if don't have one)
    Enter your choice: """

    @staticmethod
    def search_book():
        return """\nSearch books by:
    1. Title
    2. Author
    3. Genre
Enter your choice: """

    @staticmethod
    def book_added_successfully(title):
        return f"\nBook '{title}' has been added to the library."

    @staticmethod
    def book_not_found():
        return "\nBook not found in the library."

    @staticmethod
    def goodbye_message():
        return "\nThank you for using the Book Library System. Goodbye!\n"

    @staticmethod
    def invalid_choice():
        return "\nInvalid choice. Please try again."
