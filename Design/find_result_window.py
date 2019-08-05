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
        FindResultWindow.resize(705, 542)
        self.centralwidget = QtWidgets.QWidget(FindResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name_object = QtWidgets.QLabel(self.centralwidget)
        self.label_name_object.setGeometry(QtCore.QRect(300, 30, 67, 17))
        self.label_name_object.setObjectName("label_name_object")
        self.tableWidget_result = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_result.setGeometry(QtCore.QRect(10, 80, 681, 331))
        self.tableWidget_result.setObjectName("tableWidget_result")
        self.tableWidget_result.setColumnCount(0)
        self.tableWidget_result.setRowCount(0)
        FindResultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FindResultWindow)
        QtCore.QMetaObject.connectSlotsByName(FindResultWindow)

    def retranslateUi(self, FindResultWindow):
        _translate = QtCore.QCoreApplication.translate
        FindResultWindow.setWindowTitle(_translate("FindResultWindow", "Информация об объекте"))
        self.label_name_object.setText(_translate("FindResultWindow", "TextLabel"))


