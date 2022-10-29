import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from main_window import MainWindowClass
from new_plat_window import NewPlatClass
from new_furniture_window import NewFurnitureClass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainWindowClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())