from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit,
    QPushButton, QMessageBox, QProgressBar, QListWidget, QHBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import random


class MainActivityWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
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
        self.progress_bar.setValue(0)  # Initial progress value
        self.progress_bar.setFormat("Daily Progress: %p%")
        layout.addWidget(self.progress_bar)

        # Habit List
        habits_label = QLabel("Your Habits for Today:")
        habits_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        layout.addWidget(habits_label)

        self.habit_list = QListWidget()
        self.habit_list.addItems(["Drink Water", "Exercise", "Read a Book", "Meditate"])  # Static habit list
        layout.addWidget(self.habit_list)

        # Add Habit Input and Button
        add_habit_layout = QHBoxLayout()
        self.add_habit_input = QLineEdit()
        self.add_habit_input.setPlaceholderText("Enter a new habit")
        add_habit_button = QPushButton("Add Habit")
        add_habit_button.clicked.connect(self.add_habit)
        add_habit_layout.addWidget(self.add_habit_input)
        add_habit_layout.addWidget(add_habit_button)
        layout.addLayout(add_habit_layout)

        # Example Habit Tracker Button
        habit_button = QPushButton("Mark Habit as Done")
        habit_button.setFont(QFont("Arial", 16))
        habit_button.clicked.connect(self.handle_habit_tracking)
        layout.addWidget(habit_button)

        # Initialize tracked habits
        self.completed_habits = 0
        self.total_habits = self.habit_list.count()

    def add_habit(self):
        new_habit = self.add_habit_input.text().strip()
        if new_habit:
            self.habit_list.addItem(new_habit)
            self.total_habits += 1
            self.add_habit_input.clear()
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid habit.")

    def handle_habit_tracking(self):
        selected_items = self.habit_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select a habit to mark as done.")
            return

        for item in selected_items:
            self.habit_list.takeItem(self.habit_list.row(item))
            self.completed_habits += 1

        # Update progress bar
        progress = int((self.completed_habits / self.total_habits) * 100)
        self.progress_bar.setValue(progress)

        if self.completed_habits == self.total_habits:
            QMessageBox.information(self, "Habit Tracker", "Congratulations! You've completed all your habits for today.")
        else:
            QMessageBox.information(self, "Habit Tracker", f"Habit marked as done! {self.total_habits - self.completed_habits} habits remaining.")

    def get_motivational_quote(self):
        quotes = [
            "The journey of a thousand miles begins with one step.",
            "Success is the sum of small efforts, repeated day in and day out.",
            "Don't watch the clock; do what it does. Keep going.",
            "Start where you are. Use what you have. Do what you can.",
        ]
        return random.choice(quotes)


# To run the app, this class would need to be invoked in a PyQt6 application loop.
from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit,
    QPushButton, QMessageBox, QProgressBar, QListWidget, QHBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import random


class MainActivityWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
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
        self.progress_bar.setValue(0)  # Initial progress value
        self.progress_bar.setFormat("Daily Progress: %p%")
        layout.addWidget(self.progress_bar)

        # Habit List
        habits_label = QLabel("Your Habits for Today:")
        habits_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        layout.addWidget(habits_label)

        self.habit_list = QListWidget()
        self.habit_list.addItems(["Drink Water", "Exercise", "Read a Book", "Meditate"])  # Static habit list
        layout.addWidget(self.habit_list)

        # Add Habit Input and Button
        add_habit_layout = QHBoxLayout()
        self.add_habit_input = QLineEdit()
        self.add_habit_input.setPlaceholderText("Enter a new habit")
        add_habit_button = QPushButton("Add Habit")
        add_habit_button.clicked.connect(self.add_habit)
        add_habit_layout.addWidget(self.add_habit_input)
        add_habit_layout.addWidget(add_habit_button)
        layout.addLayout(add_habit_layout)

        # Example Habit Tracker Button
        habit_button = QPushButton("Mark Habit as Done")
        habit_button.setFont(QFont("Arial", 16))
        habit_button.clicked.connect(self.handle_habit_tracking)
        layout.addWidget(habit_button)

        # Initialize tracked habits
        self.completed_habits = 0
        self.total_habits = self.habit_list.count()

    def add_habit(self):
        new_habit = self.add_habit_input.text().strip()
        if new_habit:
            self.habit_list.addItem(new_habit)
            self.total_habits += 1
            self.add_habit_input.clear()
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid habit.")

    def handle_habit_tracking(self):
        selected_items = self.habit_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select a habit to mark as done.")
            return

        for item in selected_items:
            self.habit_list.takeItem(self.habit_list.row(item))
            self.completed_habits += 1

        # Update progress bar
        progress = int((self.completed_habits / self.total_habits) * 100)
        self.progress_bar.setValue(progress)

        if self.completed_habits == self.total_habits:
            QMessageBox.information(self, "Habit Tracker", "Congratulations! You've completed all your habits for today.")
        else:
            QMessageBox.information(self, "Habit Tracker", f"Habit marked as done! {self.total_habits - self.completed_habits} habits remaining.")

    def get_motivational_quote(self):
        quotes = [
            "The journey of a thousand miles begins with one step.",
            "Success is the sum of small efforts, repeated day in and day out.",
            "Don't watch the clock; do what it does. Keep going.",
            "Start where you are. Use what you have. Do what you can.",
        ]
        return random.choice(quotes)


# To run the app, this class would need to be invoked in a PyQt6 application loop.
