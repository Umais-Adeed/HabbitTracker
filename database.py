# database.py
import sqlite3

class Database:
    def __init__(self, db_name="users.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_user_table()

    def create_user_table(self):
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )
                """
            )

    def add_user(self, username, email, password):
        try:
            with self.connection:
                self.connection.execute(
                    "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                    (username, email, password),
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def validate_user(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        return cursor.fetchone() is not None