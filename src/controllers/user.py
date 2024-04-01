from db.database import LibraryDB
from views.messages import Messages
from models.user import UserModel
from utils.validation import *

db = LibraryDB()


class UserController:
    def __init__(self):
        self.user = None

    @staticmethod
    def validate(email, password):
        if not validate_email(email):
            print("\nEnter a valid email.")
            return False
        if not validate_password(password):
            print("\nEnter a valid password.")
            return False
        return True

    def register_user(self, username, email, password):
        if not self.validate(email, password):
            return

        user = UserModel(email, password, username)
        if user.get_user():
            print(Messages.user_exists(username))
            return
        user.save()
        if user:
            self.user = user
            print(Messages.user_created(username))
            return user

    def login_user(self, email, password):
        if not self.validate(email, password):
            return

        user = UserModel(email, password)
        if user.authenticate():
            self.user = user.get_user()
            print(Messages.login_successfully(self.user[1]))
            return self.user
        else:
            print("Invalid Password")
