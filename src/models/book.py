import uuid

from src.db.database import LibraryDB
from src.utils.date import get_current_time

db = LibraryDB()


class BookModel:
    def __init__(self, title, author, genre, available=True):
        self.book_data = {
            "ID": str(uuid.uuid4()),
            "title": title,
            "author": author,
            "genre": genre,
            "available": available,
            "added_at": get_current_time(),
        }

    @staticmethod
    def get_book(book_id):
        book = db.execute_query_one("SELECT * FROM book WHERE ID LIKE ?", (book_id,))
        return book

    def save(self):
        db.execute_insert_query(
            "INSERT INTO book VALUES (:ID, :title, :author, :genre, :available, :added_at)",
            self.book_data,
        )

        book = db.execute_query_one(
            "SELECT * FROM book WHERE ID LIKE ?", (self.book_data["ID"],)
        )
        return book
