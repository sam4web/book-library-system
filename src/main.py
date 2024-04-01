from db.database import LibraryDB
from models.book import BookModel
from models.user import UserModel
from controllers.book import BookController
from controllers.user import UserController
from views.messages import Messages
from views.menu import *


def main():
    library = LibraryDB()
    library.create_tables()

    UserMenu().display_login_menu()
    BookMenu().display_book_menu()

    library.close_connection()


if __name__ == "__main__":
    main()
