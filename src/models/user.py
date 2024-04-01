import uuid

from src.db.database import LibraryDB
from src.utils.validation import *

db = LibraryDB()


class UserModel:
    def __init__(
        self,
        email,
        password,
        username=None,
    ):
        self.ID = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = password

    def get_user(self):
        user = db.execute_query_one(
            "SELECT * FROM user WHERE email LIKE ?", (self.email,)
        )
        return user

    def authenticate(self):
        user = self.get_user()
        is_authenticated = verify_password(self.password, user[3])
        return is_authenticated

    def save(self):
        if self.get_user():
            print(f"User already exists")
            return None

        db.execute_insert_query(
            "INSERT INTO user VALUES(:ID, :username, :email, :password_hash)",
            {
                "ID": self.ID,
                "username": self.username,
                "email": self.email,
                "password_hash": hash_password(self.password),
            },
        )

        user = db.execute_query_one("SELECT * FROM user WHERE ID LIKE ?", (self.ID,))
        return user
