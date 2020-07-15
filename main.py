from account import Account
from accountManager import AccountManager
from mainLayout import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from controller import MainWindow
import sys
def main():
    acc = Account('test', 'ozef', 'No website')
    account_manager = AccountManager()
    account_manager.add_account(acc)
    accounts = account_manager.get_all_accounts()
    if len(accounts) == 0:
        print('No accounts to print!\n')
    else:
        [print(acc) for acc in accounts]
        print('\n')

    new_acc = Account('test', 'password_updated', 'No description')
    account_manager.update_account(acc, new_acc)
    accounts = account_manager.get_all_accounts()
    if len(accounts) == 0:
        print('No accounts to print!\n')
    else:
        [print(acc) for acc in accounts]
        print('\n')

    account_manager.remove_account(acc)
    accounts = account_manager.get_all_accounts()
    if len(accounts) == 0:
        print('No accounts to print!\n')
    else:
        [print(acc) for acc in accounts]
        print('\n')


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()  
    window.show()
    sys.exit(app.exec_())
