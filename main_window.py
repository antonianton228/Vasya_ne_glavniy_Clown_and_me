import os
import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QApplication, QInputDialog
from new_furniture_or_apart_window import NewFurnitureApartClass


class MainWindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        MainWindow = self
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 854)
        MainWindow.setMaximumSize(QtCore.QSize(1009, 854))
        MainWindow.setStyleSheet("background: rgb(118, 118, 118)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.save_load_horisontal_box = QtWidgets.QHBoxLayout()
        self.save_load_horisontal_box.setObjectName("save_load_horisontal_box")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setStyleSheet("QPushButton {\n"
                                       "  background: rgb(255, 0, 0);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "  background: rgb(38, 132, 255)\n"
                                       "}")
        self.save_button.setObjectName("save_button")
        self.save_load_horisontal_box.addWidget(self.save_button)
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setStyleSheet("QPushButton {\n"
                                       "  background: rgb(255, 0, 0);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "  background: rgb(38, 132, 255)\n"
                                       "}")
        self.load_button.setObjectName("load_button")
        self.save_load_horisontal_box.addWidget(self.load_button)
        self.verticalLayout.addLayout(self.save_load_horisontal_box)
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setStyleSheet("QPushButton {\n"
                                       "  background: rgb(255, 0, 0);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "  background: rgb(38, 132, 255)\n"
                                       "}")
        self.open_button.setObjectName("open_button")
        self.verticalLayout.addWidget(self.open_button)
        self.main_plan = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_plan.sizePolicy().hasHeightForWidth())
        self.main_plan.setSizePolicy(sizePolicy)
        self.main_plan.setMinimumSize(QtCore.QSize(700, 750))
        self.main_plan.setStyleSheet("background: rgb(0, 0, 0)")
        self.main_plan.setText("")
        self.main_plan.setObjectName("main_plan")
        self.verticalLayout.addWidget(self.main_plan)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.scroll_of_furniture = QtWidgets.QScrollArea(self.centralwidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_of_furniture.sizePolicy().hasHeightForWidth())
        self.scroll_of_furniture.setSizePolicy(sizePolicy)
        self.scroll_of_furniture.setMinimumSize(QtCore.QSize(280, 0))
        self.scroll_of_furniture.setWidgetResizable(True)
        self.scroll_of_furniture.setObjectName("scroll_of_furniture")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 278, 760))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.init_scroll()
        self.verticalLayout_4.addWidget(self.scroll_of_furniture)
        self.add_furniture = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_furniture.sizePolicy().hasHeightForWidth())
        self.add_furniture.setSizePolicy(sizePolicy)
        self.add_furniture.setMinimumSize(QtCore.QSize(280, 0))
        self.add_furniture.setStyleSheet("QPushButton {\n"
                                         "  background: rgb(255, 0, 0);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "  background: rgb(255, 255, 0);\n"
                                         "}")
        self.add_furniture.setObjectName("add_furniture")
        self.verticalLayout_4.addWidget(self.add_furniture)

        self.update_list_furn = QtWidgets.QPushButton(self.centralwidget)
        self.update_list_furn.setSizePolicy(sizePolicy)
        self.update_list_furn.setMinimumSize(QtCore.QSize(280, 0))
        self.update_list_furn.setStyleSheet("QPushButton {\n"
                                         "  background: rgb(255, 0, 0);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "  background: rgb(255, 255, 0);\n"
                                         "}")
        self.update_list_furn.setObjectName("update_list_furn")
        self.verticalLayout_4.addWidget(self.update_list_furn)

        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_button.setText(_translate("MainWindow", "Открыть макет квартиры"))
        self.load_button.setText(_translate("MainWindow", "Создать макет квартиры"))
        self.save_button.setText(_translate("MainWindow", "Сохранить дизайн"))
        self.add_furniture.setText(_translate("MainWindow", "Добавить свою мебель"))
        self.update_list_furn.setText(_translate("MainWindow", "Обновить список мебели"))
        self.add_furniture.clicked.connect(self.new_furniture)
        self.load_button.clicked.connect(self.new_make)
        self.update_list_furn.clicked.connect(self.refresh)
        self.open_button.clicked.connect(self.open_apart)

    def new_make(self):
        self.apart = NewFurnitureApartClass('apartament')
        self.apart.show()

    def open_apart(self):
        self.con = sqlite3.connect("Furniture_redactor_database.sqlite")
        self.cur = self.con.cursor()
        aparts = tuple(map(lambda x: list(x)[0], self.cur.execute("""SELECT title FROM apartaments""").fetchall()))
        name, ok_pressed = QInputDialog.getItem(
            self, "Выберите квартиру", "Какая вам нужна?",
            aparts, 1, False)
        if ok_pressed:
            apart = list(self.cur.execute(f"""SELECT * FROM apartaments
            WHERE title = '{name}'""").fetchall()[0])
            self.list_of_furn = apart[2].split('$')
            print(self.list_of_furn)
            self.im_apart = Image.open(apart[3])
            self.im_apart.resize((700, 750))
            self.pix_apart = QPixmap.fromImage(ImageQt(self.im_apart.convert("RGBA")))
            self.main_plan.setPixmap(self.pix_apart)
            for furn in self.list_of_furn:
                x, y, angle = furn.split(', ')
                self.add_furn(x=x, y=y, angle=angle)
        self.con.close()

    def refresh(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

    def init_scroll(self):
        self.layuot_v = QVBoxLayout()
        self.con = sqlite3.connect("Furniture_redactor_database.sqlite")
        self.cur = self.con.cursor()
        self.res = list(map(lambda x: list(x)[0], self.cur.execute('''SELECT image FROM furniture''').fetchall()))
        for i, name in enumerate(map(lambda x: list(x)[0], self.cur.execute('''SELECT title FROM furniture''').fetchall())):
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.img_furniture = QtWidgets.QLabel()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.img_furniture.sizePolicy().hasHeightForWidth())
            self.img_furniture.setSizePolicy(sizePolicy)
            self.img_furniture.setMinimumSize(QtCore.QSize(75, 75))
            self.img_furniture.setStyleSheet("background: rgb(0, 0, 0)")
            self.img_furniture.setObjectName("img_furniture")
            self.im = Image.open(self.res[i])
            self.im = self.im.resize((75, 75))
            self.im.save(self.res[i])
            self.img_furniture.setPixmap(QPixmap(self.res[i]))
            self.horizontalLayout_2.addWidget(self.img_furniture)
            self.verticalLayout_5 = QtWidgets.QVBoxLayout()
            self.verticalLayout_5.setObjectName("verticalLayout_5")
            self.add_button = QtWidgets.QPushButton(name)
            self.add_button.setStyleSheet("QPushButton {\n"
                                          "  background: rgb(255, 0, 0);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed{\n"
                                          "  background: rgb(38, 132, 255)\n"
                                          "}")
            self.add_button.setObjectName("add_button")
            self.verticalLayout_5.addWidget(self.add_button)
            self.change_button = QtWidgets.QPushButton(name + ' change')
            self.change_button.setStyleSheet("QPushButton {\n"
                                             "  background: rgb(255, 0, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed{\n"
                                             "  background: rgb(38, 132, 255)\n"
                                             "}")
            self.change_button.setObjectName("change_button")
            self.verticalLayout_5.addWidget(self.change_button)
            self.horizontalLayout_2.addLayout(self.verticalLayout_5)
            self.layuot_v.addLayout(self.horizontalLayout_2, i)
            self.change_button.clicked.connect(self.change_size)
            self.add_button.clicked.connect(self.add_furn)
        self.scrollAreaWidgetContents.setLayout(self.layuot_v)
        self.scroll_of_furniture.setWidget(self.scrollAreaWidgetContents)
        self.con.close()

    def new_furniture(self):
        self.furn = NewFurnitureApartClass('furniture')
        self.furn.show()

    def add_furn(self, x=1, y=1, angle=0):
        self.con = sqlite3.connect("Furniture_redactor_database.sqlite")
        self.cur = self.con.cursor()
        furn = list(self.cur.execute(f"""SELECT * FROM furniture
        WHERE title = '{self.sender().text()}'""").fetchall()[0])
        print(furn)
        size = list(map(int, furn[2][1:-1].split(', ')))
        self.im_furn = Image.open(furn[3])

    def change_size(self):
        self.con = sqlite3.connect("Furniture_redactor_database.sqlite")
        self.cur = self.con.cursor()
        size, ok_pressed = QInputDialog.getText(self, "Размеры",
                                                "Введите размеры через пробел")
        if ok_pressed:
            self.cur.execute(
                f"""UPDATE furniture
                SET size = '{tuple(map(int, size.split()))}'
                WHERE title = '{self.sender().text()[:-7]}'""")
        self.con.commit()
        self.con.close()