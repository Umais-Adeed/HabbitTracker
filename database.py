import sqlite3
from datetime import timedelta, date

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
    def create_habit_table(self):
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS habit (
                    habit_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    habit_name TEXT NOT NULL,
                    habit_category TEXT NOT NULL,
                    habit_frequency TEXT NOT NULL check(habit_frequency in ('daily','weekly','monthly')),
                    foreign key (user_id) references users(id)
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

    def add_habit(self,habit_name, habit_category, habit_frequency):
        try:
            with self.connection:
                self.connection.execute("insert into habit(user_id,habit_name, habit_category, habit_frequency) VALUES (?, ?, ?,?)")
            return True,"Habit Added Successfully!"
        except sqlite3.IntegrityError:
            return False

    def get_all_habits(self):
        cursor = self.connection.cursor()
        cursor.execute("Select habit_name, habit_category, habit_frequency from habit")
        rows = cursor.fetchall()

        habits = [{"habit_name":row[0], "habit_category": rows[1], "habit_frequency": rows[2]} for row in rows]

    def mark_habit(self, habit_id, completion_date):
        try:
            with self.connection:
                self.connection.execute(
                    "INSERT INTO habit_progress (habit_id, completion_date) VALUES (?, ?)",
                    (habit_id, completion_date),
                )
                return True
        except sqlite3.IntegrityError:
            return False
    def get_completed_habits(self, habit_id, frequency):
        cursor = self.connection.cursor()
        today = date.today()
        if frequency == 'daily':
            cutoff = today.isoformat()
        elif frequency == 'weekly':
            cutoff = (today - timedelta(days=today.weekday())).isoformat()
        elif frequency == 'monthly':
            cutoff = today.replace(day=1).isoformat()
        else:
            return 0
        cursor.execute(
            "SELECT COUNT(*) FROM habit_progress WHERE habit_id = ? AND date_completed >= ?",
            (habit_id, cutoff),
        )
        return cursor.fetchone()[0]