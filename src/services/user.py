from src.db.database import LibraryDB

from src.models.user import UserModel
from src.utils.validation import *

db = LibraryDB()


class User:
    def __init__(self):
        self.user = None

    @staticmethod
    def validate(email, password):
        if not validate_email(email):
            print("Enter a valid email.")
            return False
        if not validate_password(password):
            print("Enter a valid password.")
            return False
        return True

    def register_user(self, username, email, password):
        if not self.validate(email, password):
            return

        user = UserModel(email, password, username).save()
        if user:
            self.user = user
            print(f'User "{username}" successfully created.')

    def login_user(self, email, password):
        if not self.validate(email, password):
            return
        user = UserModel(email, password)
        if user.authenticate():
            self.user = user.get_user()
            print("Valid")
        else:
            print("Invalid")

    def logout_user(self):
        if not self.user:
            print("No user")
            return
        self.user = None
