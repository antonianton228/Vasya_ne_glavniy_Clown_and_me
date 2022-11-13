import sqlite3

from PyQt5.QtWidgets import QWidget

from ListOfFurn import Ui_Form
from FurnWidget import WidgetFurn


class WidgetListFurn(QWidget):
    def __init__(self, main_window):
        super(WidgetListFurn, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_scroll()
        self.main_window = main_window

    def init_scroll(self):
        con = sqlite3.connect("Furniture_redactor_database.sqlite")
        cur = con.cursor()
        for id, name in (cur.execute('''SELECT id, title FROM furniture''').fetchall()):
            self.widget_furn = WidgetFurn(name, id, self.ui.scrollAreaWidgetContents)
            self.ui.layout_of_furns.addWidget(self.widget_furn)
            self.widget_furn.ui.add_button.clicked.connect(self.press_add)
        con.close()

    def press_add(self):
        self.main_window.add_furn()
        self.close()
