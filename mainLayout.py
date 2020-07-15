# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Cherif\Documents\Cours\Projet\Projet_Python\Python-Projet\MainLayout.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from account import Account
from accountManager import AccountManager

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 561, 381))
        self.tabWidget.setMaximumSize(QtCore.QSize(561, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.addAccount = QtWidgets.QWidget()
        self.addAccount.setObjectName("addAccount")
        self.descriptionField = QtWidgets.QTextEdit(self.addAccount)
        self.descriptionField.setGeometry(QtCore.QRect(120, 150, 291, 71))
        self.descriptionField.setObjectName("descriptionField")
        self.userNameField = QtWidgets.QLineEdit(self.addAccount)
        self.userNameField.setGeometry(QtCore.QRect(120, 50, 291, 31))
        self.userNameField.setObjectName("userNameField")
        self.label = QtWidgets.QLabel(self.addAccount)
        self.label.setGeometry(QtCore.QRect(50, 50, 71, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.addAccount)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.addAccount)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 51, 21))
        self.label_2.setObjectName("label_2")
        self.saveAccountButton = QtWidgets.QPushButton(self.addAccount)
        self.saveAccountButton.setGeometry(QtCore.QRect(210, 240, 101, 51))
        self.saveAccountButton.setObjectName("saveAccountButton")
        self.passwordField = QtWidgets.QLineEdit(self.addAccount)
        self.passwordField.setGeometry(QtCore.QRect(120, 100, 291, 31))
        self.passwordField.setObjectName("passwordField")
        self.tabWidget.addTab(self.addAccount, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listView = QtWidgets.QListView(self.tab_2)
        self.listView.setGeometry(QtCore.QRect(10, 50, 256, 241))
        self.listView.setObjectName("listView")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.saveAccountButton.clicked.connect(self.isClicked)
        
    def isClicked(self):
        account = Account(str(self.userNameField.text()),str(self.passwordField.text()),str(self.descriptionField.toPlainText()))
        account_manager = AccountManager()
        account_manager.add_account(account)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "UserName"))
        self.label_3.setText(_translate("MainWindow", "Description"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.saveAccountButton.setStatusTip(_translate("MainWindow", "Save a new account"))
        self.saveAccountButton.setText(_translate("MainWindow", "Save Account"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addAccount), _translate("MainWindow", "Add account"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Account List"))
