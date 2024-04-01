from db.database import LibraryDB
from models.book import BookModel
from models.user import UserModel


def main():
    library = LibraryDB()
    # library.create_tables()
    # user = UserModel("jim", "jim@gmail.com", "fr34!@rrd33")
    # user.login_user("sam", "sam@gmail.com")
    # user.save()
    # print(user.authenticate())

    great_gatsby = BookModel(
        title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction"
    )
    jane_eyre = BookModel(
        title="Jane Eyre", author="Charlotte Brontë", genre="Gothic romance"
    )
    # great_gatsby.save()
    # jane_eyre.save()

    library.close_connection()


if __name__ == "__main__":
    main()
