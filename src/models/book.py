import uuid

from db.database import LibraryDB
from utils.date import get_current_time

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

    def save(self):
        existing_book = db.execute_query_one(
            "SELECT * FROM book WHERE title=:title AND author=:author",
            {"title": self.book_data["title"], "author": self.book_data["author"]},
        )
        if existing_book:
            print("Book already exists.")
            return

        db.execute_insert_query(
            "INSERT INTO book VALUES (:ID, :title, :author, :genre, :available, :added_at)",
            self.book_data,
        )

        book = db.execute_query_one(
            "SELECT * FROM book WHERE ID LIKE ?", (self.book_data["ID"],)
        )
        return book
