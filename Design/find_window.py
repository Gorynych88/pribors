# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FindWindow(object):
    def setupUi(self, FindWindow):
        FindWindow.setObjectName("FindWindow")
        FindWindow.resize(1004, 710)
        self.centralwidget = QtWidgets.QWidget(FindWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelPlaceFind = QtWidgets.QLabel(self.centralwidget)
        self.labelPlaceFind.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlaceFind.setObjectName("labelPlaceFind")
        self.gridLayout.addWidget(self.labelPlaceFind, 0, 0, 1, 1)
        self.labelTypeFind = QtWidgets.QLabel(self.centralwidget)
        self.labelTypeFind.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTypeFind.setObjectName("labelTypeFind")
        self.gridLayout.addWidget(self.labelTypeFind, 0, 1, 1, 1)
        self.labelYearFind = QtWidgets.QLabel(self.centralwidget)
        self.labelYearFind.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYearFind.setObjectName("labelYearFind")
        self.gridLayout.addWidget(self.labelYearFind, 0, 2, 1, 1)
        self.labelNameFind = QtWidgets.QLabel(self.centralwidget)
        self.labelNameFind.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNameFind.setObjectName("labelNameFind")
        self.gridLayout.addWidget(self.labelNameFind, 0, 3, 1, 1)
        self.comboBoxPlaceFind = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxPlaceFind.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxPlaceFind.setObjectName("comboBoxPlaceFind")
        self.gridLayout.addWidget(self.comboBoxPlaceFind, 1, 0, 1, 1)
        self.comboBoxTypeFind = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTypeFind.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxTypeFind.setObjectName("comboBoxTypeFind")
        self.gridLayout.addWidget(self.comboBoxTypeFind, 1, 1, 1, 1)
        self.comboBoxYearFind = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxYearFind.setMinimumSize(QtCore.QSize(80, 0))
        self.comboBoxYearFind.setObjectName("comboBoxYearFind")
        self.gridLayout.addWidget(self.comboBoxYearFind, 1, 2, 1, 1)
        self.lineEditNameFind = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNameFind.sizePolicy().hasHeightForWidth())
        self.lineEditNameFind.setSizePolicy(sizePolicy)
        self.lineEditNameFind.setObjectName("lineEditNameFind")
        self.gridLayout.addWidget(self.lineEditNameFind, 1, 3, 1, 1)
        self.btnFind = QtWidgets.QPushButton(self.centralwidget)
        self.btnFind.setObjectName("btnFind")
        self.gridLayout.addWidget(self.btnFind, 1, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 5)
        self.graphicsView_Schema = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Schema.setObjectName("graphicsView_Schema")
        self.gridLayout.addWidget(self.graphicsView_Schema, 3, 0, 1, 5)
        FindWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FindWindow)
        QtCore.QMetaObject.connectSlotsByName(FindWindow)

    def retranslateUi(self, FindWindow):
        _translate = QtCore.QCoreApplication.translate
        FindWindow.setWindowTitle(_translate("FindWindow", "Поиск"))
        self.labelPlaceFind.setText(_translate("FindWindow", "Место установки"))
        self.labelTypeFind.setText(_translate("FindWindow", "Тип прибора"))
        self.labelYearFind.setText(_translate("FindWindow", "Год выпуска"))
        self.labelNameFind.setText(_translate("FindWindow", "Название прибора"))
        self.btnFind.setText(_translate("FindWindow", "Найти"))


