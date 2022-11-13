from PyQt5 import QtCore, QtWidgets


class Ui_RurnitureWidget(object):
    def setupUi(self, RurnitureWidget):
        RurnitureWidget.setObjectName("RurnitureWidget")
        RurnitureWidget.resize(410, 129)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RurnitureWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(RurnitureWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_furniture = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_furniture.sizePolicy().hasHeightForWidth())
        self.img_furniture.setSizePolicy(sizePolicy)
        self.img_furniture.setMinimumSize(QtCore.QSize(75, 0))
        self.img_furniture.setStyleSheet("background: rgb(0, 0, 0)")
        self.img_furniture.setText("")
        self.img_furniture.setObjectName("img_furniture")
        self.horizontalLayout_2.addWidget(self.img_furniture)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.add_button = QtWidgets.QPushButton(self.groupBox)
        self.add_button.setStyleSheet("QPushButton {\n"
                                      "  background: rgb(224,160,195);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "  background: rgb(255, 255, 0);\n"
                                      "}")
        self.add_button.setText("")
        self.add_button.setObjectName("add_button")
        self.verticalLayout_5.addWidget(self.add_button)
        self.change_button = QtWidgets.QPushButton(self.groupBox)
        self.change_button.setStyleSheet("QPushButton {\n"
                                         "  background: rgb(224,160,195);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "  background: rgb(255, 255, 0);\n"
                                         "}")
        self.change_button.setText("")
        self.change_button.setObjectName("change_button")
        self.verticalLayout_5.addWidget(self.change_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(RurnitureWidget)
        QtCore.QMetaObject.connectSlotsByName(RurnitureWidget)

    def retranslateUi(self, RurnitureWidget):
        _translate = QtCore.QCoreApplication.translate
        RurnitureWidget.setWindowTitle(_translate("RurnitureWidget", "Form"))
        self.groupBox.setTitle(_translate("RurnitureWidget", "GroupBox"))
