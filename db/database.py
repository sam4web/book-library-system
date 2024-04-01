import sqlite3


class Library:
    def __init__(self, database_file="db/library.db"):
        self.database_file = database_file
        self.conn = sqlite3.connect(self.database_file)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS user (
                ID INT NOT NULL PRIMARY KEY,
                username VARCHAR(150) NOT NULL,
                email VARCHAR(50) NOT NULL,
                password_hash VARCHAR(255) NOT NULL
            )"""
        )

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS book (
                ID INT NOT NULL PRIMARY KEY,
                TITLE VARCHAR(150) NOT NULL,
                author VARCHAR(150) NOT NULL,
                genre VARCHAR(150) NOT NULL,
                available BOOLEAN DEFAULT TRUE,
                added_at VARCHAR(150) NOT NULL
            )"""
        )

        self.conn.commit()
        self.conn.close()
