import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from account import Account
from accountManager import AccountManager


qt_creator_file = "mainLayout.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
account_manager = AccountManager()
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.save_account_button.clicked.connect(self.add)
        self.delete_button.clicked.connect(self.delete)
        self.update_button.clicked.connect(self.update)
        self.account_view.itemClicked.connect(self.fill_form)
        self.refresh()
        
    def add(self):
        if str(self.user_name_field.text()) != "" and str(self.password_field.text()) != "" and str(self.description_field.toPlainText()) != "":
            account = Account(str(self.user_name_field.text()),str(self.password_field.text()),str(self.description_field.toPlainText()))
            account_manager.add_account(account)
            self.refresh()
            self.user_name_field.clear()
            self.password_field.clear()
            self.description_field.clear()
            self.info_label.setText("Account Saved")
        else:
            self.info_label.setText("All fields are required")
            
    def refresh(self):
        self.account_view.clear()
        self.__accounts = account_manager.get_all_accounts()
        for i in self.__accounts:
            self.account_view.addItem("Username: "+i.username+"  ||  Description: "+i.description)
    
    
    def delete(self):    
        if(self.account_view.currentRow() != None and len(self.__accounts) > 0):
            account_manager.remove_account(self.__accounts[self.account_view.currentRow()])
            self.username_info_field.clear()
            self.password_info_field.clear()
            self.description_info_field.clear()
            self.refresh()
            
    def fill_form(self):
        if(self.account_view.currentRow() != None):
            account = self.__accounts[self.account_view.currentRow()]
            self.username_info_field.setText(account.username)
            self.password_info_field.setText(account.password)
            self.description_info_field.setText(account.description)
            
    def update(self):
        if(self.account_view.currentRow() != None and len(self.__accounts) > 0):
            old_account = self.__accounts[self.account_view.currentRow()]
            if str(self.username_info_field.text()) != "" and str(self.password_info_field.text()) != "" and str(self.description_info_field.toPlainText()) != "":
                new_account = Account(str(self.username_info_field.text()),str(self.password_info_field.text()),str(self.description_info_field.toPlainText()))
                account_manager.update_account(old_account,new_account)
                self.username_info_field.clear()
                self.password_info_field.clear()
                self.description_info_field.clear()
                self.refresh()
                self.info_label_2.setText("Account updated")
            else:
                self.info_label_2.setText("All fields are required")