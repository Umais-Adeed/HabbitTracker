
# **Modern Split UI - Login and Registration Application**

### **Overview**
The **Modern Split UI** is a sleek and user-friendly graphical user interface (GUI) application built with **PyQt6**. It offers a seamless login and registration experience with a visually stunning gradient background, modern design, and responsive layout. This application leverages **SQLite** to securely manage user credentials, making it an ideal starting point for desktop applications requiring authentication features.

---

### **✨ Features**
- **User Authentication**:
  - Secure login and registration functionality.
  - Ensures unique usernames and password validation during registration.
- **Responsive Split Design**:
  - A split layout with a login panel on one side and a dynamic right panel, providing balance and modern aesthetics.
- **Gradient Background**:
  - Eye-catching gradient background transitioning from `#43C6AC` (light green) to `#3A6186` (dark blue).
- **Input Validation**:
  - Enforces required fields and matching passwords for a seamless registration experience.
- **Database Integration**:
  - Backed by an **SQLite** database for secure and efficient storage of user data.
- **Forgot Password Link**:
  - Placeholder for implementing future password recovery functionality.
- **Extensible Architecture**:
  - Modular code structure for adding more features with ease.

---

### **🛠️ Technologies Used**
- **Python**: Core programming language for the application logic.
- **PyQt6**: Framework for building the responsive and visually appealing GUI.
- **SQLite**: Lightweight database for managing user credentials.

---

### **📦 Installation**
To set up and run the application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/modern-split-ui.git
   cd modern-split-ui
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install PyQt6
   ```

3. **Run the Application**:
   Start the application by executing the main script:
   ```bash
   python main.py
   ```

---

### **🚀 Usage**
1. **Login**:
   - Enter your username and password to log in.
   - If you don't have an account, click on the "Register" button.
2. **Register**:
   - Fill in the required fields (username, email, password) and click "Register".
   - Ensure the username is unique and passwords match.
3. **Forgot Password**:
   - A placeholder link for future password recovery functionality.

---

### **📂 Code Structure**
- **`main.py`**: Entry point for launching the application.
- **`ui.py`**: Manages the split UI layout and gradient design.
- **`database.py`**: Handles SQLite database connections and operations (e.g., user registration, validation).
- **`user.py`**: Defines the `User` class to manage user-related data.

---

### **📈 Contribution**
We welcome contributions! If you'd like to improve this project or add new features:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make changes and commit:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push your changes:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

---

### **📚 Acknowledgments**
- [PyQt6 Documentation](https://www.riverbankcomputing.com/software/pyqt/intro)
- [SQLite Documentation](https://sqlite.org/docs.html)
