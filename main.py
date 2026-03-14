import sys, os
from PySide6.QtWidgets import QApplication

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ui.ui_window import ui_window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ui_window()
    window.show()
    sys.exit(app.exec())
