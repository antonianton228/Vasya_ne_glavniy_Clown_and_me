import sqlite3

from PIL import Image

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QInputDialog, QErrorMessage, QWidget

from FurnituerWidget import Ui_RurnitureWidget


class WidgetFurn(QWidget):
    def __init__(self, name_furn: str, id_furn: int, parent=None):
        super(WidgetFurn, self).__init__(parent)
        self.ui = Ui_RurnitureWidget()
        self.ui.setupUi(self)
        self.name_furn = name_furn
        self.id_furn = id_furn
        self.initui()

    def initui(self):
        self.ui.groupBox.setTitle(str(self.name_furn))
        self.ui.change_button.clicked.connect(self.change_size)

        self.ui.add_button.setText(self.name_furn)
        self.ui.change_button.setText('Изменить размер ' + self.name_furn)

        con = sqlite3.connect("Furniture_redactor_database.sqlite")
        cur = con.cursor()
        image = cur.execute(f"""SELECT image FROM furniture WHERE title = '{self.name_furn}'""").fetchall()[0][0]
        self.ui.im = Image.open(image)
        self.ui.im = self.ui.im.resize((75, 75))
        self.ui.im.save(image)
        self.ui.img_furniture.setPixmap(QPixmap(image))
        con.close()

    def change_size(self):
        con = sqlite3.connect("Furniture_redactor_database.sqlite")
        cur = con.cursor()
        size, ok_pressed = QInputDialog.getText(self, "Размеры", "Введите размеры через пробел")
        try:
            if ok_pressed:
                cur.execute(
                    f"""UPDATE furniture
                            SET size = '{tuple(map(int, size.split()))}'
                            WHERE title = '{self.sender().text()[16:]}'""")
        except Exception:
            error = QErrorMessage(self)
            error.showMessage('Ошибка, вы внесли неверные данные.')
        con.commit()
        con.close()
