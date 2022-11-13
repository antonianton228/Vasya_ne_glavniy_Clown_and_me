import sqlite3

from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QColorDialog
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap


class NewFurnitureApartClass(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj
        self.setupUi()

    def setupUi(self):
        Form = self
        Form.setObjectName("Form")
        Form.resize(739, 626)
        Form.setStyleSheet("background: rgb(195,146,255)")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.furniture_plan = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.furniture_plan.sizePolicy().hasHeightForWidth())
        self.furniture_plan.setSizePolicy(sizePolicy)
        self.furniture_plan.setMinimumSize(QtCore.QSize(600, 600))
        self.furniture_plan.setStyleSheet("background: rgb(254,220,255)")
        self.furniture_plan.setObjectName("furniture_plan")
        self.furniture_plan.setMouseTracking(True)
        self.horizontalLayout_2.addWidget(self.furniture_plan)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rendo_button = QtWidgets.QPushButton(Form)
        self.rendo_button.setStyleSheet("QPushButton {\n"
                                        "  background: rgb(224,160,195);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "  background: rgb(38, 132, 255)\n"
                                        "}")
        self.rendo_button.setObjectName("rendo_button")
        self.verticalLayout.addWidget(self.rendo_button)
        self.undo_button = QtWidgets.QPushButton(Form)
        self.undo_button.setStyleSheet("QPushButton {\n"
                                       "  background: rgb(224,160,195);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "  background: rgb(38, 132, 255)\n"
                                       "}")
        self.undo_button.setObjectName("undo_button")
        self.verticalLayout.addWidget(self.undo_button)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.color_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_button.sizePolicy().hasHeightForWidth())
        self.color_button.setSizePolicy(sizePolicy)
        self.color_button.setStyleSheet("QPushButton {\n"
                                        "  background: rgb(224,160,195);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "  background: rgb(38, 132, 255)\n"
                                        "}")
        self.color_button.setObjectName("color_button")
        self.verticalLayout_2.addWidget(self.color_button)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.apply_button = QtWidgets.QPushButton(Form)
        self.apply_button.setStyleSheet("QPushButton {\n"
                                        "  background: rgb(224,160,195);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "  background: rgb(255, 255, 0);\n"
                                        "}")
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout.addWidget(self.apply_button)
        self.exit_button = QtWidgets.QPushButton(Form)
        self.exit_button.setStyleSheet("QPushButton {\n"
                                       "  background: rgb(224,160,195);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "  background: rgb(255, 255, 0);\n"
                                       "}")
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout.addWidget(self.exit_button)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.initui()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rendo_button.setText(_translate("Form", "Вернуть"))
        self.undo_button.setText(_translate("Form", "Стереть"))
        self.color_button.setText(_translate("Form", "Цвет"))
        self.apply_button.setText(_translate("Form", "Применить"))
        self.exit_button.setText(_translate("Form", "Выйти"))
        self.undo_button.clicked.connect(self.undo)
        self.rendo_button.clicked.connect(self.rendo)
        self.apply_button.clicked.connect(self.apply)
        self.color_button.clicked.connect(self.pick_color)
        self.exit_button.clicked.connect(self.close)

    def initui(self):
        self.drawing = False
        self.draw_flag = False
        self.brushSize = 2
        self.brushColor = (255, 255, 255)
        self.lastPoint = QPoint()

        if self.obj == 'apartament':
            self.im = Image.open('plate.png')
            self.pix = QPixmap.fromImage(ImageQt(self.im.convert("RGBA")))
            self.furniture_plan.setScaledContents(True)
            self.furniture_plan.setPixmap(self.pix)

        if self.obj == 'apartament':
            self.im = Image.open('plate.png')
            self.old_im = Image.open('plate.png')
        else:
            self.im = Image.new('RGB', (self.furniture_plan.size().width(), self.furniture_plan.size().height()),
                                (254, 220, 255))
            self.old_im = Image.new('RGB', (self.furniture_plan.size().width(), self.furniture_plan.size().height()),
                                    'black')

    def pick_color(self):
        self.brushColor = QColorDialog.getColor().getRgb()

    def undo(self):
        self.im, self.old_im = Image.new('RGB',
                                         (self.furniture_plan.size().width(), self.furniture_plan.size().height()),
                                         'black'), self.old_im.copy()
        self.pix = QPixmap.fromImage(ImageQt(self.im.convert("RGBA")))
        self.furniture_plan.setPixmap(self.pix)

    def rendo(self):
        self.im = self.old_im.copy()
        self.pix = QPixmap.fromImage(ImageQt(self.im.convert("RGBA")))
        self.furniture_plan.setPixmap(self.pix)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.draw_flag = False

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.draw_flag:
                pencil = ImageDraw.Draw(self.im)
                if abs(self.draw_flag.x() - event.pos().x()) > abs(self.draw_flag.y() - event.pos().y()):
                    pencil.line((self.draw_flag.x() - 10, self.draw_flag.y() - 10, event.pos().x() - 10,
                                 self.draw_flag.y() - 10),
                                fill=self.brushColor, width=5)
                    self.draw_flag = QPoint(event.pos().x(), self.draw_flag.y())
                else:
                    pencil.line(
                        (self.draw_flag.x() - 10, self.draw_flag.y() - 10, self.draw_flag.x() - 10,
                         event.pos().y() - 10),
                        fill=self.brushColor, width=5)
                    self.draw_flag = QPoint(self.draw_flag.x(), event.pos().y())
                self.pix = QPixmap.fromImage(ImageQt(self.im.convert("RGBA")))
                self.furniture_plan.setPixmap(self.pix)
                self.update()
            else:
                self.draw_flag = event.pos()
            self.drawing = False
            self.old_im = self.im.copy()

    def apply(self):
        con = sqlite3.connect("Furniture_redactor_database.sqlite")
        cur = con.cursor()
        if self.obj == 'furniture':
            if self.lineEdit.text() != '' and (self.lineEdit.text(),) not in cur.execute(
                    '''SELECT title FROM furniture''').fetchall() and self.im != Image.new('RGB', (
                    self.furniture_plan.size().width(), self.furniture_plan.size().height()), 'black'):
                self.crop(self.im).save(f'images_furn/{self.lineEdit.text()}.png')
                cur.execute(
                    f'''INSERT INTO furniture(title,size,image) VALUES("{self.lineEdit.text()}",
                     "(100, 100)","images_furn/{self.lineEdit.text()}.png")''')
                con.commit()
                con.close()
        else:
            if self.lineEdit.text() != '' and (self.lineEdit.text(),) not in cur.execute(
                    '''SELECT title FROM apartaments''').fetchall() and self.im != Image.new('RGB', (
                    self.furniture_plan.size().width(), self.furniture_plan.size().height()), 'black'):
                self.crop(self.im).save(f'images_apart/{self.lineEdit.text()}.png')
                cur.execute(
                    f'''INSERT INTO apartaments(title,list_of_furniture,apart_image) VALUES("{self.lineEdit.text()}",
                    "","images_apart/{self.lineEdit.text()}.png")''')
                con.commit()
                con.close()
        self.close()

    def crop(self, im):
        pixels = im.load()
        x, y = im.size
        def_pix = pixels[0, 0]
        max_coorg_i = 0
        min_coorg_i = 1000000000000
        max_coorg_j = 0
        min_coorg_j = 1000000000000
        for i in range(x):
            for j in range(y):
                if pixels[i, j] != def_pix:
                    if max_coorg_i < i:
                        max_coorg_i = i
                    if min_coorg_i > i:
                        min_coorg_i = i
                    if max_coorg_j < j:
                        max_coorg_j = j
                    if min_coorg_j > j:
                        min_coorg_j = j
        return im.crop((min_coorg_i, min_coorg_j, max_coorg_i + 1, max_coorg_j + 1))