from account import Account
from accountManager import AccountManager
from PyQt5 import QtCore, QtGui, QtWidgets
from controller import MainWindow

import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
