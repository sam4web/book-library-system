# from src.db.database import LibraryDB
from src.models.user import *


def main():
    library = LibraryDB()
    # library.create_tables()
    # user = User("sam", "sam@gmail.com", "fr34!@rrdF3")
    # user.login_user("sam", "sam@gmail.com")
    # user.save_to_db()
    # print(user.authenticate())
    library.close_connection()


if __name__ == "__main__":
    main()
