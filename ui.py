# ui.py
from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit,
    QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QLinearGradient, QPalette, QColor, QBrush
from database import Database

class SplitWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()  # Initialize the database

        # Main Window Configuration
        self.setWindowTitle("Modern Split UI")
        self.setGeometry(100, 100, 1200, 600)

        # Gradient Background
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setColorAt(0.0, QColor("#3A6186"))  # Dark blue
        gradient.setColorAt(0.5, QColor("#43C6AC"))  # Midpoint color (greenish)
        gradient.setColorAt(1.0, QColor("#A8E6CE"))  # Light green
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

        # Main Container
        self.main_container = QWidget()
        self.setCentralWidget(self.main_container)

        # Vertical Layout for Panels
        self.main_layout = QVBoxLayout(self.main_container)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Panels
        self.left_panel = self.create_login_panel()
        self.main_layout.addWidget(self.left_panel)

    def create_login_panel(self):
        """Create the login panel."""
        self.login_widget = QWidget()
        layout = QVBoxLayout(self.login_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(15)  # Add spacing between widgets

        # Title
        title = QLabel("Login")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #ffffff;")
        layout.addWidget(title)

        # Username Input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet(self.get_input_style())
        layout.addWidget(self.username_input)

        # Password Input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(self.get_input_style())
        layout.addWidget(self.password_input)

        # Login Button
        login_button = QPushButton("Login")
        login_button.setStyleSheet(self.get_button_style("#4caf50", "#45a049", "#388e3c"))
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        # Register Button
        register_button = QPushButton("Register")
        register_button.setStyleSheet(self.get_button_style("#2196f3", "#1e88e5", "#1565c0"))
        register_button.clicked.connect(self.switch_to_register)
        layout.addWidget(register_button)


        # Forgot Password Link
        forgot_password_link = QLabel('<a href="#">Forgot Password?</a>')
        forgot_password_link.setOpenExternalLinks(True)
        forgot_password_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        forgot_password_link.setStyleSheet("color: #2196f3; text-decoration: underline;")
        layout.addWidget(forgot_password_link)

        return self.login_widget

    def create_register_panel(self):
        """Create the register panel."""
        self.register_widget = QWidget()
        layout = QVBoxLayout(self.register_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title = QLabel("Register")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #ffffff;")
        layout.addWidget(title)

        # Username Input
        self.new_username_input = QLineEdit()
        self.new_username_input.setPlaceholderText("Username")
        self.new_username_input.setStyleSheet(self.get_input_style())
        layout.addWidget(self.new_username_input)

        # Email Input
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet(self.get_input_style())
        layout.addWidget(self.email_input)

        # Password Input
        self.new_password_input = QLineEdit()
        self.new_password_input.setPlaceholderText("Password")
        self.new_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.new_password_input.setStyleSheet(self.get_input_style())
        layout.addWidget(self.new_password_input)

        # Confirm Password Input
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm Password")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setStyleSheet(self.get_input_style())
        layout.addWidget(self.confirm_password_input)

        # Register Button
        register_button = QPushButton("Register")
        register_button.setStyleSheet(self.get_button_style("#4caf50", "#45a049", "#388e3c"))
        register_button.clicked.connect(self.handle_register)
        layout.addWidget(register_button)

        # Switch to Login Button
        switch_to_login = QPushButton("Back to Login")
        switch_to_login.setStyleSheet(self.get_button_style("#2196f3", "#1e88e5", "#1565c0"))
        switch_to_login.clicked.connect(self.switch_to_login)
        layout.addWidget(switch_to_login)

        return self.register_widget

    def get_input_style(self):
        """Reusable style for input fields."""
        return """
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                font-size: 16px;
                padding: 10px;
                border: 2px solid #4caf50;
                border-radius: 10px;
            }
            QLineEdit:focus {
                border-color: #2196f3;
            }
        """

    def get_button_style(self, base_color, hover_color, pressed_color):
        """Reusable style for buttons."""
        return f"""
            QPushButton {{
                background-color: {base_color};
                color: #ffffff;
                font-size: 16px;
                padding: 10px;
                border-radius: 15px;
                border: none;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
            QPushButton:pressed {{
                background-color: {pressed_color};
            }}
        """

    def switch_to_register(self):
        """Switch to the register panel."""
        self.main_layout.replaceWidget(self.left_panel, self.create_register_panel())
        self.left_panel.hide()

    def switch_to_login(self):
        """Switch to the login panel."""
        self.main_layout.replaceWidget(self.left_panel, self.create_login_panel())
        self.left_panel.hide()

    def handle_login(self):
        """Handle the login process."""
        username = self.username_input.text()
        password = self.password_input.text()
        if self.db.validate_user(username, password):
            QMessageBox.information(self, "Login Successful", "Welcome, " + username + "!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def handle_register(self):
        """Handle the register process."""
        username = self.new_username_input.text()
        email = self.email_input.text()
        password = self.new_password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not username or not email or not password or not confirm_password:
            QMessageBox.warning(self, "Error", "All fields are required.")
        elif password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
        else:
            if self.db.add_user(username, email, password):
                QMessageBox.information(self, "Success", "Registration Successful!")
                self.switch_to_login()
            else:
                QMessageBox.warning(self, "Error", "Username already exists.")