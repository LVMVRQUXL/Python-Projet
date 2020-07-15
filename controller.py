import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from account import Account
from accountManager import AccountManager


qt_creator_file = "mainLayout.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.saveAccountButton.clicked.connect(self.isClicked)
        
    def isClicked(self):
        if((str(self.userNameField.text()) != "" and str(self.passwordField.text()) != "" and str(self.descriptionField.toPlainText()) != "" )):
            account = Account(str(self.userNameField.text()),str(self.passwordField.text()),str(self.descriptionField.toPlainText()))
            account_manager = AccountManager()
            account_manager.add_account(account)
            self.infoLabel.setText("Account Saved")
        else:
            self.infoLabel.setText("All fields are required")