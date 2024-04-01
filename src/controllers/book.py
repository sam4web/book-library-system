from db.database import LibraryDB
from models.book import BookModel
from views.messages import Messages


db = LibraryDB()


class BookController:

    @staticmethod
    def add_book(title, author, genre):
        book = BookModel(title, author, genre).save()
        if book:
            print(Messages.book_added_successfully(title))

    @staticmethod
    def remove_book(book_id):
        book = BookModel.get_book(book_id)
        if book:
            db.execute_insert_query("DELETE FROM book WHERE ID LIKE ?", (book_id,))
            print(Messages.book_removed_successfully(book[1]))
        else:
            print(Messages.book_not_found())

    @staticmethod
    def get_book_list():
        book_list = db.execute_query("SELECT * FROM book")
        print("")
        for book in book_list:
            print(
                f"Title: {book[1].ljust(15, ' ')}Author: {book[2].ljust(6, ' ')}\tGenre: {book[3]}"
            )

    @staticmethod
    def search_book(**kwargs):
        book_list = []
        if kwargs.get("title"):
            books = db.execute_query(
                "SELECT * FROM book WHERE title = ?", (kwargs.get("title"),)
            )
            book_list.extend(books)

        if kwargs.get("author"):
            books = db.execute_query(
                "SELECT * FROM book WHERE author = ?", (kwargs.get("author"),)
            )
            book_list.extend(books)

        if kwargs.get("genre"):
            books = db.execute_query(
                "SELECT * FROM book WHERE genre = ?", (kwargs.get("genre"),)
            )
            book_list.extend(books)

        if len(book_list) == 0:
            print(Messages.book_not_found())
        else:
            print("\n")
            for book in book_list:
                print(
                    f"Title: {book[1].ljust(15, ' ')}Author: {book[2].ljust(6, ' ')}\tGenre: {book[3]}"
                )
