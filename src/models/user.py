import uuid

from src.db.database import LibraryDB
from src.utils.validation import *

db = LibraryDB()


class User:
    def __init__(self, username, email, password):
        self.ID = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = password

    def authenticate(self):
        user = db.execute_query_one(
            "SELECT * FROM user WHERE username LIKE ?", (self.username,)
        )
        is_authenticated = verify_password(self.password, user[3])
        return is_authenticated

    def save_to_db(self):
        existing_user = db.execute_query_one(
            "SELECT * FROM user WHERE email LIKE ?", (self.email,)
        )
        if existing_user:
            print(f"User already exists")
            return

        db.execute_insert_query(
            "INSERT INTO user VALUES(:ID, :username, :email, :password_hash)",
            (
                {
                    "ID": self.ID,
                    "username": self.username,
                    "email": self.email,
                    "password_hash": hash_password(self.password),
                }
            ),
        )
