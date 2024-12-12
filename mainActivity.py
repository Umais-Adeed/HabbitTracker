from sys import exception

from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel,
    QPushButton, QMessageBox, QProgressBar, QListWidget
)
from PyQt6.QtCore import Qt
from datetime import date, timedelta
from PyQt6.QtGui import QFont
import random
from database import Database


class MainActivityWindow(QMainWindow):
    def __init__(self, username, db, habit_id, frequency):
        super().__init__()
        try:
            self.db = Database()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to initialize database: {str(e)}")
            self.close()
            return
        self.habit_id = habit_id


        self.setWindowTitle("Habit Tracker - Main Activity")
        self.setGeometry(100, 100, 800, 600)

        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        layout = QVBoxLayout(self.central_widget)

        # Welcome Message
        welcome_label = QLabel(f"Welcome to your Habit Tracker, {username}!")
        welcome_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(welcome_label)

        # Motivational Quote
        quote_label = QLabel(self.get_motivational_quote())
        quote_label.setFont(QFont("Arial", 14))
        quote_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        quote_label.setStyleSheet("color: gray;")
        layout.addWidget(quote_label)

        # Habit Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(1)  # Placeholder progress value
        self.progress_bar.setFormat("Daily Progress: %p%")
        layout.addWidget(self.progress_bar)

        # Habit List
        habits_label = QLabel("Your Habits for Today:")
        habits_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        layout.addWidget(habits_label)

        self.habit_list = QListWidget()
        self.habit_list.addItems(["Drink Water", "Exercise", "Read a Book", "Meditate"])  # Static habit list
        layout.addWidget(self.habit_list)

        # Example Habit Tracker Button
        habit_button = QPushButton("Mark Habit as Done")
        habit_button.setFont(QFont("Arial", 16))
        habit_button.clicked.connect(self.handle_habit_tracking)
        layout.addWidget(habit_button)

    def mark_habit_complete(self):
        today = date.today().isoformat()
        if self.db.mark_habit(self.habit_id, today):
            QMessageBox.information(self, "Success","Habit Marked")
            self.update_progress()
        else:
            QMessageBox.warning(self, "Error", "Failed To Mark Habit")

    def get_target_frequency(self,frequency):
        if frequency == "daily":
            return 1
        elif frequency == "weekly":
            return 7
        elif frequency == "monthly":
            return 30
        return 1
    def update_progress(self):
        completions = self.db.get_habit_completions(self.habit_id, self.habit_frequency)
        target = self.get_frequency_target(self.frequency)
        progress = min((completions/target) *100, 100) if target > 0 else 0
        self.progress_bar.setValue(int(progress))

    def get_motivational_quote(self):
        quotes = [
            "The journey of a thousand miles begins with one step.",
            "Success is the sum of small efforts, repeated day in and day out.",
            "Don't watch the clock; do what it does. Keep going.",
            "Start where you are. Use what you have. Do what you can.",
        ]
        return random.choice(quotes)


# To run the app, this class would need to be invoked in a PyQt6 application loop.
