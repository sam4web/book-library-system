from db.database import LibraryDB

from models.book import BookModel

db = LibraryDB()


class Book:

    @staticmethod
    def add_book(title, author, genre):
        book = BookModel(title, author, genre).save()
        if book:
            print(book)

    @staticmethod
    def remove_book(book_id):
        book = BookModel.get_book(book_id)
        if book:
            db.execute_insert_query("DELETE FROM book WHERE ID LIKE ?", (book_id,))
        print(f'"{book[1]}" book successfully deleted.')

    @staticmethod
    def get_book_list():
        book_list = db.execute_query("SELECT * FROM book")
        return book_list

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
            print("No books found")
        elif len(book_list) == 1:
            print(book_list[0])
        else:
            for book in book_list:
                print(book)
