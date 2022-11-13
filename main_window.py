import sqlite3

from PIL import Image
from PIL.ImageQt import ImageQt

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QMainWindow, QInputDialog

from new_furniture_or_apart_window import NewFurnitureApartClass
from FurnLayuot import WidgetListFurn


class MainWindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        MainWindow = self
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 854)
        MainWindow.setMaximumSize(QtCore.QSize(1009, 854))
        MainWindow.setStyleSheet("background: rgb(195,146,255)")
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
                                       "  background: rgb(252,146,255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "  background: rgb(39,40,255)\n"
                                       "}")
        self.save_button.setObjectName("save_button")
        self.save_load_horisontal_box.addWidget(self.save_button)
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setStyleSheet("QPushButton {\n"
                                       "  background: rgb(252,146,255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "  background: rgb(38, 132, 255)\n"
                                       "}")
        self.load_button.setObjectName("load_button")
        self.save_load_horisontal_box.addWidget(self.load_button)
        self.verticalLayout.addLayout(self.save_load_horisontal_box)
        self.change_make = QtWidgets.QPushButton(self.centralwidget)
        self.change_make.setStyleSheet("QPushButton {\n"
                                       "  background: rgb(252,146,255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "  background: rgb(38, 132, 255)\n"
                                       "}")
        self.change_make.setObjectName("change_make")
        self.verticalLayout.addWidget(self.change_make)
        self.main_plan = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_plan.sizePolicy().hasHeightForWidth())
        self.main_plan.setSizePolicy(sizePolicy)
        self.main_plan.setMinimumSize(QtCore.QSize(700, 750))
        self.main_plan.setStyleSheet("background: rgb(254,220,255)")
        self.main_plan.setText("")
        self.main_plan.setObjectName("main_plan")
        self.verticalLayout.addWidget(self.main_plan)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_furniture = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_furniture.sizePolicy().hasHeightForWidth())
        self.add_furniture.setSizePolicy(sizePolicy)
        self.add_furniture.setMinimumSize(QtCore.QSize(280, 0))
        self.add_furniture.setStyleSheet("QPushButton {\n"
                                         "  background: rgb(224,160,195);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "  background: rgb(255, 255, 0);\n"
                                         "}")
        self.add_furniture.setObjectName("add_furniture")
        self.verticalLayout_3.addWidget(self.add_furniture)
        self.ListFurnButton = QtWidgets.QPushButton(self.centralwidget)
        self.ListFurnButton.setObjectName("ListFurnButton")
        self.ListFurnButton.setStyleSheet("QPushButton {\n"
                                          "  background: rgb(224,160,195);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed{\n"
                                          "  background: rgb(255, 255, 0);\n"
                                          "}")
        self.verticalLayout_3.addWidget(self.ListFurnButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.init_par()
        self.pix_main_plan()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.save_button.setText(_translate("MainWindow", "Сохранить  дизайн"))
        self.load_button.setText(_translate("MainWindow", "Загрузить дизайн"))
        self.change_make.setText(_translate("MainWindow", "Пересоздать макет"))
        self.add_furniture.setText(_translate("MainWindow", "Добавить свою мебель"))
        self.ListFurnButton.setText(_translate("MainWindow", "Открыть список мебели"))
        self.add_furniture.clicked.connect(self.new_furniture)
        self.load_button.clicked.connect(self.new_make)
        self.change_make.clicked.connect(self.open_apart)
        self.save_button.clicked.connect(self.save_apart)
        self.ListFurnButton.clicked.connect(self.open_list_furn)

    def pix_main_plan(self):
        self.im = Image.open('plate.png')
        self.pix = QPixmap.fromImage(ImageQt(self.im.convert("RGBA")))
        self.main_plan.setScaledContents(True)
        self.main_plan.setPixmap(self.pix)

    def init_par(self):
        self.counter_id: int = 0
        self.furn_list_wiew = []
        self.setMouseTracking(True)
        self.moving = False
        self.index = 0
        self.len_list_furn = 0
        self.furn = NewFurnitureApartClass('furniture')

    def open_list_furn(self):
        self.window_list_furns = WidgetListFurn(self)
        self.window_list_furns.show()

    def new_make(self):
        self.apart = NewFurnitureApartClass('apartament')
        self.apart.show()

    def new_furniture(self):
        self.furn = NewFurnitureApartClass('furniture')
        self.furn.show()

    def save_apart(self):
        con = sqlite3.connect("Furniture_redactor_database.sqlite")
        cur = con.cursor()
        name, ok_pressed = QInputDialog.getText(self, "Название квартиры", "Введите название квартиры")
        if ok_pressed:
            list_furn = []
            for i in self.furn_list_wiew:
                list_furn.append(f'{i[1][0]}, {i[2][0]}, {i[-3]}, {i[-2]}, {i[-1]}')
            cur.execute(
                f'''INSERT INTO apartaments(title,list_of_furniture,apart_image) VALUES("{name}",
                        "{"$".join(list_furn)}","images_apart/{self.name}.png")''')
            con.commit()
            con.close()

    def open_apart(self):
        self.con = sqlite3.connect("Furniture_redactor_database.sqlite")
        self.cur = self.con.cursor()
        aparts = tuple(map(lambda x: list(x)[0], self.cur.execute("""SELECT title FROM apartaments""").fetchall()))
        self.name, ok_pressed = QInputDialog.getItem(
            self, "Выберите квартиру", "Какая вам нужна?",
            aparts, 1, False)
        if ok_pressed:
            for i in self.furn_list_wiew:
                i[0].setVisible(False)
            self.furn_list_wiew = []
            apart = list(self.cur.execute(f"""SELECT * FROM apartaments
                    WHERE title = '{self.name}'""").fetchall()[0])
            self.list_of_furn = apart[2].split('$')
            self.im_apart = Image.open(apart[3])
            self.pix_apart = QPixmap.fromImage(ImageQt(self.im_apart.convert("RGBA")))

            self.main_plan.setScaledContents(True)
            self.main_plan.setPixmap(self.pix_apart)
            for furn in self.list_of_furn:
                if furn:
                    x, y, sizex, sizey, title = furn.split(', ')
                    self.add_furn(x=int(x), y=int(y), title=title)
        self.con.close()

    def add_furn(self, title='', x=100, y=100, angle=0):
        f = True
        if not title:
            title = self.sender().text()
            f = False
        self.con = sqlite3.connect("Furniture_redactor_database.sqlite")
        self.cur = self.con.cursor()
        furn = list(self.cur.execute(f"""SELECT * FROM furniture
        WHERE title = '{title}'""").fetchall()[0])
        if not f:
            angle, f = QInputDialog.getItem(
                self, "Выберете угол мебели", "Значение угла",
                ("0", "90", "180", "270"), 0, False)
        if f:
            im1 = QPixmap.fromImage(ImageQt(furn[3]))
            transe = QTransform().rotate(int(angle))
            im1 = QPixmap(im1.transformed(transe))
            self.new_fut = QtWidgets.QLabel(self.centralwidget)
            self.new_fut.setGeometry(
                QtCore.QRect(x, y, int(furn[2].split(', ')[0][1:]), int(furn[2].split(', ')[1][:-1])))
            self.new_fut.setObjectName("label")
            self.new_fut.setScaledContents(True)
            self.new_fut.setPixmap(im1)
            self.new_fut.setAcceptDrops(True)
            self.new_fut.show()

        self.furn_list_wiew.append([self.new_fut, range(x, x + int(furn[2].split(', ')[0][1:])),
                                    range(y, y + int(furn[2].split(', ')[1][:-1])), int(furn[2].split(', ')[0][1:]),
                                    int(furn[2].split(', ')[1][:-1]), title])
        self.setCentralWidget(self.centralwidget)

    def mouseMoveEvent(self, event):
        if self.moving:
            if event.x() + self.furn_list_wiew[self.target][3] < 710 \
                    and event.y() + self.furn_list_wiew[self.target][4] < 810 \
                    and event.x() > 10 and event.y() > 70:
                self.furn_list_wiew[self.target][0].move(event.x(), event.y())
                self.furn_list_wiew[self.target][1] = range(event.x(), event.x() + self.furn_list_wiew[self.target][3])
                self.furn_list_wiew[self.target][2] = range(event.y(), event.y() + self.furn_list_wiew[self.target][4])

    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        for i in range(len(self.furn_list_wiew)):
            if a0.x() in self.furn_list_wiew[i][1] and a0.y() in self.furn_list_wiew[i][2]:
                self.target = i
                self.moving = True

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        self.moving = False

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == Qt.Key_Delete:
            if self.target != '':
                self.furn_list_wiew[self.target][0].setVisible(False)
                self.furn_list_wiew.pop(self.target)