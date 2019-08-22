# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find_result_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FindResultWindow(object):
    def setupUi(self, FindResultWindow):
        FindResultWindow.setObjectName("FindResultWindow")
        FindResultWindow.resize(801, 546)
        self.centralwidget = QtWidgets.QWidget(FindResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setEnabled(False)
        self.btnEdit.setGeometry(QtCore.QRect(330, 470, 151, 51))
        self.btnEdit.setCheckable(False)
        self.btnEdit.setAutoDefault(False)
        self.btnEdit.setObjectName("btnEdit")
        self.listWidgetFindResult = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetFindResult.setGeometry(QtCore.QRect(10, 10, 781, 441))
        self.listWidgetFindResult.setObjectName("listWidgetFindResult")
        FindResultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FindResultWindow)
        QtCore.QMetaObject.connectSlotsByName(FindResultWindow)

    def retranslateUi(self, FindResultWindow):
        _translate = QtCore.QCoreApplication.translate
        FindResultWindow.setWindowTitle(_translate("FindResultWindow", "Информация о приборах"))
        self.btnEdit.setText(_translate("FindResultWindow", "Изменить данные"))


