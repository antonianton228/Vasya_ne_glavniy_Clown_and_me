import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtWidgets

from main_window import MainWindowClass


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        ui = MainWindowClass()
        ui.show()
        sys.exit(app.exec_())
    except Exception as a:
        print(a)
