# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(480, 265)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddWindow.sizePolicy().hasHeightForWidth())
        AddWindow.setSizePolicy(sizePolicy)
        AddWindow.setMinimumSize(QtCore.QSize(480, 235))
        AddWindow.setMaximumSize(QtCore.QSize(480, 265))
        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setMinimumSize(QtCore.QSize(0, 0))
        self.labelName.setObjectName("labelName")
        self.verticalLayout.addWidget(self.labelName)
        self.labelType = QtWidgets.QLabel(self.centralwidget)
        self.labelType.setObjectName("labelType")
        self.verticalLayout.addWidget(self.labelType)
        self.labelNumber = QtWidgets.QLabel(self.centralwidget)
        self.labelNumber.setObjectName("labelNumber")
        self.verticalLayout.addWidget(self.labelNumber)
        self.labelPlace = QtWidgets.QLabel(self.centralwidget)
        self.labelPlace.setObjectName("labelPlace")
        self.verticalLayout.addWidget(self.labelPlace)
        self.labelYear = QtWidgets.QLabel(self.centralwidget)
        self.labelYear.setObjectName("labelYear")
        self.verticalLayout.addWidget(self.labelYear)
        self.labelDatePov = QtWidgets.QLabel(self.centralwidget)
        self.labelDatePov.setMinimumSize(QtCore.QSize(0, 0))
        self.labelDatePov.setObjectName("labelDatePov")
        self.verticalLayout.addWidget(self.labelDatePov)
        self.labelDateNextPov = QtWidgets.QLabel(self.centralwidget)
        self.labelDateNextPov.setMinimumSize(QtCore.QSize(0, 0))
        self.labelDateNextPov.setObjectName("labelDateNextPov")
        self.verticalLayout.addWidget(self.labelDateNextPov)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setTabletTracking(False)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout_2.addWidget(self.lineEditName)
        self.comboBoxType = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxType.setObjectName("comboBoxType")
        self.verticalLayout_2.addWidget(self.comboBoxType)
        self.lineEditNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNumber.setObjectName("lineEditNumber")
        self.verticalLayout_2.addWidget(self.lineEditNumber)
        self.comboBoxPlace = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxPlace.setObjectName("comboBoxPlace")
        self.verticalLayout_2.addWidget(self.comboBoxPlace)
        self.dateEditYear = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEditYear.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEditYear.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateEditYear.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEditYear.setObjectName("dateEditYear")
        self.verticalLayout_2.addWidget(self.dateEditYear)
        self.dateEditPov = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEditPov.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateEditPov.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEditPov.setObjectName("dateEditPov")
        self.verticalLayout_2.addWidget(self.dateEditPov)
        self.dateEditNextPov = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEditNextPov.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateEditNextPov.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEditNextPov.setObjectName("dateEditNextPov")
        self.verticalLayout_2.addWidget(self.dateEditNextPov)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.btnAdd, 1, 0, 1, 2)
        AddWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "Добавить прибор"))
        self.labelName.setText(_translate("AddWindow", "Название прибора:"))
        self.labelType.setText(_translate("AddWindow", "Тип прибора:"))
        self.labelNumber.setText(_translate("AddWindow", "Заводской номер:"))
        self.labelPlace.setText(_translate("AddWindow", "Место установки:"))
        self.labelYear.setText(_translate("AddWindow", "Год выпуска:"))
        self.labelDatePov.setText(_translate("AddWindow", "Дата поверки:"))
        self.labelDateNextPov.setText(_translate("AddWindow", "Дата следующей поверки:"))
        self.dateEditYear.setDisplayFormat(_translate("AddWindow", "yyyy"))
        self.btnAdd.setText(_translate("AddWindow", "Добавить"))


