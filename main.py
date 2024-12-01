import sys
from PyQt6.QtWidgets import QApplication
from ui import SplitWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplitWindow()
    window.show()
    sys.exit(app.exec())