import sqlite3


class LibraryDB:
    def __init__(self, database_file="src/db/library.db"):
        self.database_file = database_file
        self.__conn = sqlite3.connect(self.database_file)
        self.__cur = self.__conn.cursor()

    def close_connection(self):
        self.__conn.close()

    def create_tables(self):
        self.__cur.execute(
            """CREATE TABLE IF NOT EXISTS user (
                ID INT NOT NULL PRIMARY KEY,
                username VARCHAR(150) NOT NULL,
                email VARCHAR(50) NOT NULL,
                password_hash BLOB NOT NULL
            )"""
        )

        self.__cur.execute(
            """CREATE TABLE IF NOT EXISTS book (
                ID INT NOT NULL PRIMARY KEY,
                title VARCHAR(150) NOT NULL,
                author VARCHAR(150) NOT NULL,
                genre VARCHAR(150) NOT NULL,
                available BOOLEAN DEFAULT TRUE,
                added_at VARCHAR(150) NOT NULL
            )"""
        )

        self.__conn.commit()
        self.__conn.close()

    def execute_query(self, query, params=None):
        if params:
            self.__cur.execute(query, params)
        else:
            self.__cur.execute(query)

        result = self.__cur.fetchall()
        self.__conn.commit()
        return result

    def execute_query_one(self, query, params=None):
        if params:
            self.__cur.execute(query, params)
        else:
            self.__cur.execute(query)

        result = self.__cur.fetchone()
        self.__conn.commit()
        return result

    def execute_insert_query(self, query, params=None):
        if params:
            self.__cur.execute(query, params)
        else:
            self.__cur.execute(query)

        result = self.__cur.lastrowid
        self.__conn.commit()
        return result
