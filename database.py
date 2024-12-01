import sqlite3
import bcrypt  # Import bcrypt for password hashing

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
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            with self.connection:
                self.connection.execute(
                    "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                    (username, email, hashed_password),
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def validate_user(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT password FROM users WHERE username = ?",
            (username,),
        )
        row = cursor.fetchone()
        if row and bcrypt.checkpw(password.encode('utf-8'), row[0]):
            return True
        return False