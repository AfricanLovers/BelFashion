# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design\ui\registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton, 0, QtCore.Qt.AlignRight)
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.horizontalLayout.addWidget(self.usernameLabel)
        self.usernameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameEdit.setMinimumSize(QtCore.QSize(380, 0))
        self.usernameEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usernameEdit.setFont(font)
        self.usernameEdit.setObjectName("usernameEdit")
        self.horizontalLayout.addWidget(self.usernameEdit, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.horizontalLayout_2.addWidget(self.passwordLabel)
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setMinimumSize(QtCore.QSize(380, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.horizontalLayout_2.addWidget(self.passwordEdit, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.repeatPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.repeatPasswordLineEdit.setMinimumSize(QtCore.QSize(380, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.repeatPasswordLineEdit.setFont(font)
        self.repeatPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeatPasswordLineEdit.setObjectName("repeatPasswordLineEdit")
        self.horizontalLayout_3.addWidget(self.repeatPasswordLineEdit, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.showPasswordCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.showPasswordCheckBox.setFont(font)
        self.showPasswordCheckBox.setObjectName("showPasswordCheckBox")
        self.verticalLayout.addWidget(self.showPasswordCheckBox)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.registerButton.setFont(font)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Войти"))
        self.titleLabel.setText(_translate("MainWindow", "Регистрация"))
        self.usernameLabel.setText(_translate("MainWindow", "Логин:"))
        self.passwordLabel.setText(_translate("MainWindow", "Пароль:"))
        self.label.setText(_translate("MainWindow", "Повторите пароль:"))
        self.showPasswordCheckBox.setText(_translate("MainWindow", "Показать пароль"))
        self.registerButton.setText(_translate("MainWindow", "Зарегистрироваться"))