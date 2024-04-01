from src.db.database import LibraryDB
from src.models.book import BookModel
from src.models.user import UserModel
from src.services.book import Book
from src.services.user import User


def main():
    library = LibraryDB()
    library.create_tables()

    # sam = User()
    # sam.register_user("sam", "sam@gmail.com", "Fe42@fewe12")

    # print(UserModel("sam", "sam@gmail.com", "Fe42@fewe12").authenticate())
    # sam.login_user("sam@gmail.com", "Fe42@fewe12")
    # sam.logout_user()

    # Book.add_book("Great Book", "Jim", "Fiction")
    # Book.remove_book("2151fc80-a8df-4183-8723-5ce94cd73454")
    # print(Book.get_book_list())

    Book.search_book(title="Book1")

    library.close_connection()


if __name__ == "__main__":
    main()
