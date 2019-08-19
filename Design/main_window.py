# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 271)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setEnabled(True)
        self.btnAdd.setMinimumSize(QtCore.QSize(100, 60))
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnFindWindow = QtWidgets.QPushButton(self.centralwidget)
        self.btnFindWindow.setMinimumSize(QtCore.QSize(100, 60))
        self.btnFindWindow.setBaseSize(QtCore.QSize(0, 0))
        self.btnFindWindow.setObjectName("btnFindWindow")
        self.horizontalLayout.addWidget(self.btnFindWindow)
        self.btnNear = QtWidgets.QPushButton(self.centralwidget)
        self.btnNear.setMinimumSize(QtCore.QSize(100, 60))
        self.btnNear.setObjectName("btnNear")
        self.horizontalLayout.addWidget(self.btnNear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelInfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.verticalLayout.addWidget(self.labelInfo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Программа учёта приборов КИП"))
        self.btnAdd.setText(_translate("MainWindow", "Добавить\n"
"прибор"))
        self.btnFindWindow.setText(_translate("MainWindow", "Найти"))
        self.btnNear.setText(_translate("MainWindow", "Поверка"))
        self.labelInfo.setText(_translate("MainWindow", "В ближайшие полгода поверки приборов не требуется"))


