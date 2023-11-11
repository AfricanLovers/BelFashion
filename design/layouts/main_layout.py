# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design\ui\main_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.mainLayout.addWidget(self.titleLabel)
        self.containerLayout = QtWidgets.QHBoxLayout()
        self.containerLayout.setObjectName("containerLayout")
        self.leftMenuLayout = QtWidgets.QVBoxLayout()
        self.leftMenuLayout.setObjectName("leftMenuLayout")
        self.searchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBar.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; padding: 10px; border: 2px solid #aaa; border-radius: 5px;")
        self.searchBar.setObjectName("searchBar")
        self.leftMenuLayout.addWidget(self.searchBar)
        self.categoriesList = QtWidgets.QListWidget(self.centralwidget)
        self.categoriesList.setStyleSheet("\n"
"               font: 16pt \"MS Shell Dlg 2\"; \n"
"               border: 1px solid #ddd;\n"
"\n"
"               QListWidget::item {\n"
"                   padding: 10px 20px; \n"
"                   margin: 5px 0; \n"
"                   border-radius: 4px;\n"
"                   color: #555;\n"
"               }\n"
"\n"
"               QListWidget::item:hover {\n"
"                   background-color: #ddd;\n"
"                   color: #333;\n"
"               }\n"
"\n"
"               QListWidget::item:selected {\n"
"                   background-color: #5a9;\n"
"                   color: white;\n"
"               }\n"
"           ")
        self.categoriesList.setObjectName("categoriesList")
        self.leftMenuLayout.addWidget(self.categoriesList)
        self.deleteFiltersBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteFiltersBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deleteFiltersBtn.setFont(font)
        self.deleteFiltersBtn.setObjectName("deleteFiltersBtn")
        self.leftMenuLayout.addWidget(self.deleteFiltersBtn)
        self.cartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cartBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cartBtn.setFont(font)
        self.cartBtn.setObjectName("cartBtn")
        self.leftMenuLayout.addWidget(self.cartBtn)
        self.exitAccountBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitAccountBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exitAccountBtn.setFont(font)
        self.exitAccountBtn.setObjectName("exitAccountBtn")
        self.leftMenuLayout.addWidget(self.exitAccountBtn)
        self.containerLayout.addLayout(self.leftMenuLayout)
        self.productsScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.productsScrollArea.setWidgetResizable(True)
        self.productsScrollArea.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.productsScrollArea.setObjectName("productsScrollArea")
        self.productsContainer = QtWidgets.QWidget()
        self.productsContainer.setGeometry(QtCore.QRect(0, 0, 438, 737))
        self.productsContainer.setObjectName("productsContainer")
        self.productsVerticalLayout = QtWidgets.QVBoxLayout(self.productsContainer)
        self.productsVerticalLayout.setSpacing(10)
        self.productsVerticalLayout.setObjectName("productsVerticalLayout")
        self.productsScrollArea.setWidget(self.productsContainer)
        self.containerLayout.addWidget(self.productsScrollArea)
        self.mainLayout.addLayout(self.containerLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.action.setFont(font)
        self.action.setObjectName("action")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clothesstore"))
        self.titleLabel.setText(_translate("MainWindow", "store"))
        self.searchBar.setPlaceholderText(_translate("MainWindow", "Поиск..."))
        self.deleteFiltersBtn.setText(_translate("MainWindow", "Убрать Фильтрацию"))
        self.cartBtn.setText(_translate("MainWindow", "Корзина"))
        self.exitAccountBtn.setText(_translate("MainWindow", "Выйти С Аккаунта"))
        self.action.setText(_translate("MainWindow", "Выйти"))
