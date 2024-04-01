from src.db.database import LibraryDB
from src.models.book import BookModel
from src.models.user import UserModel
from src.services.book import Book
from src.services.user import User


def main():
    library = LibraryDB()
    library.create_tables()

    sam = User()
    # sam.register_user("sam", "sam@gmail.com", "Fe42@fewe12")

    # print(UserModel("sam", "sam@gmail.com", "Fe42@fewe12").authenticate())
    sam.login_user("sam@gmail.com", "Fe42@fewe12")
    sam.logout_user()

    Book.search_book(author="No author")
    library.close_connection()


if __name__ == "__main__":
    main()
