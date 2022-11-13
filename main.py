import sys

from PyQt5.QtWidgets import QApplication

from main_window import MainWindowClass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindowClass()
    ui.show()
    sys.exit(app.exec_())
