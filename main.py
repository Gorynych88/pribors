
import sys
import sqlite3
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsView, QGraphicsItem, QMessageBox, QGraphicsRectItem, QGraphicsPolygonItem, QGraphicsEllipseItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt

sys.path.append("./Design")
import main_window
import add_window
import find_window
import find_result_window


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.showAddWindow)
        self.dialog_add = AddWindow(self)
        self.btnFindWindow.clicked.connect(self.showFindWindow)
        self.dialog_find = FindWindow(self)

    def showAddWindow(self):
        self.dialog_add.show()

    def showFindWindow(self):
        self.dialog_find.show()

class AddWindow(QtWidgets.QMainWindow, add_window.Ui_AddWindow):

    def __init__(self, parent=None):
        super(AddWindow, self).__init__(parent)
        self.db = db
        self.setupUi(self)

        #self.btnAdd.setCheckable(True)
        self.btnAdd.clicked.connect(self.records)

        self.comboBoxAddWindowInit()

    def comboBoxAddWindowInit(self):
        self.comboBoxType.addItems(['Расходомер ультразвуковой',
                                    'Расходомер электромагнитный',
                                    'Уровнемер погружной',
                                    'Расходомер вихревой',
                                    'Уровнемер ультразвуковой',
                                    'Датчик давления',
                                    'Манометр'])
        self.comboBoxPlace.addItems(['12 насосная станция',
                                     '13 насосная станция',
                                     '21 насосная станция',
                                     '22 насосная станция',
                                     '23 насосная станция',
                                     'КП 1',
                                     'КП 2',
                                     'Хлорное хозяйство',
                                     'Реагентное хозяйство',
                                     'Блок 1',
                                     'Блок 2',
                                     'Блок 3',
                                     'Блок 4',
                                     'Блок 5',
                                     '38-1 насосная станция',
                                     '38-2 насосная станция',
                                     '37 насосная станция',
                                     '93 насосная станция',
                                     '17 насосная станция',
                                     'Резервуар 1000 м3 37 насосная станция',
                                     'Резервуар 3000 м3 37 насосная станция',
                                     'Резервуар 750 м3 21 насосная станция',
                                     'Резервуар 1500 м3 21 насосная станция',
                                     'Резервуар 2200 м3 21 насосная станция',
                                     'Резервуар 7000-1 м3 2 блок',
                                     'Резервуар 7000-2 м3 2 блок',
                                     'Резервуар 10000 м3 №1',
                                     'Резервуар 10000 м3 №2',
                                     'Резервуар 10000 м3 №3'])

    def records(self):
        description = self.lineEditName.text()
        description_no_space = description.replace(' ', '')
        type_device = self.comboBoxType.currentText()
        number = self.lineEditNumber.text()
        place = self.comboBoxPlace.currentText()
        temp_year = self.dateEditYear.date()
        year = temp_year.toPyDate()
        # year_temp = QtCore.QDate.fromString(self.dateEditYear, 'yyyy')
        # year = year_temp.yaer()
        temp_data = self.dateEditPov.date()
        data = temp_data.toPyDate()
        temp_data_next = self.dateEditNextPov.date()
        data_next = temp_data_next.toPyDate()

        self.db.insert_data(description_no_space, type_device, number, place, year, data, data_next)


        msg_add = MyMessageBox()
        msg_add.setIcon(QMessageBox.Information)
        # msg_add.setIconPixmap(pixmap)  # Своя картинка

        msg_add.setWindowTitle("Информация")
        msg_add.setText("Успешно!")
        msg_add.setInformativeText("Вы успешно добавили прибор в базу данных")
        # msg_add.setDetailedText("DetailedText")



        okButton = msg_add.addButton('Ок', QMessageBox.AcceptRole)
        # msg_add.addButton('Отмена', QMessageBox.RejectRole)

        msg_add.exec()
        # if msg_add.clickedButton() == okButton:
        #     print("Yes")
        # else:
        #     print("No")

class MyMessageBox(QtWidgets.QMessageBox):
    def __init__(self):
        QtWidgets.QMessageBox.__init__(self)
        self.setSizeGripEnabled(True)

    def event(self, e):
        result = QtWidgets.QMessageBox.event(self, e)

        self.setMinimumHeight(150)
        self.setMaximumHeight(16777215)
        self.setMinimumWidth(150)
        self.setMaximumWidth(16777215)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # textEdit = self.findChild(QtWidgets.QTextEdit)
        # if textEdit != None :
        #     textEdit.setMinimumHeight(0)
        #     textEdit.setMaximumHeight(16777215)
        #     textEdit.setMinimumWidth(0)
        #     textEdit.setMaximumWidth(16777215)
        #     textEdit.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        return result

#-------------------Создание класса для обработки событий для прямоугольников-----------------------
class CustomRectItem(QGraphicsRectItem):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.db = db

        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)

        self.setAcceptHoverEvents(True)

    def select_rect(self, name):
        self.db.select_data_to_place(name)

    def mousePressEvent(self, mouseEvent):
        self.select_rect(self.name)

    def mouseReleaseEvent(self, mouseEvent):
        pass
        # print('mouseReleaseEvent')

    def hoverMoveEvent(self, mouseEvent):
        pass
        # print('hoverMoveEvent')

    def hoverLeaveEvent(self, mouseEvent):
        pass
        # print('hoverLeaveEvent')

    def hoverEnterEvent(self, mouseEvent):
        pass
        # print('hoverEnterEvent')
#------------------------------------------------------------------------------

#-------------------Создание класса для обработки событий для полигонов-----------------------
class CustomPolygonItem(QGraphicsPolygonItem):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.db = db
        self.setAcceptHoverEvents(True)


    def select_polygon(self, name):
        self.db.select_data_to_place(name)


    def mousePressEvent(self, mouseEvent):
        self.select_polygon(self.name)

    def mouseReleaseEvent(self, mouseEvent):
        pass
        # print('mouseReleaseEvent')

    def hoverMoveEvent(self, mouseEvent):
        pass
        # print('hoverMoveEvent')

    def hoverLeaveEvent(self, mouseEvent):
        pass
        # print('hoverLeaveEvent')

    def hoverEnterEvent(self, mouseEvent):
        pass
        # print('hoverEnterEvent')
#------------------------------------------------------------------------------

#-------------------Создание класса для обработки событий для эллипсов-----------------------
class CustomEllipseItem(QGraphicsEllipseItem):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.db = db
        self.setAcceptHoverEvents(True)


    def select_ellipse(self, name):
        self.db.select_data_to_place(name)

    def mousePressEvent(self, mouseEvent):
        self.select_ellipse(self.name)
    
    def mouseReleaseEvent(self, mouseEvent):
        pass
        # print('mouseReleaseEvent')

    def hoverMoveEvent(self, mouseEvent):
        pass
        # print('hoverMoveEvent')

    def hoverLeaveEvent(self, mouseEvent):
        pass
        # print('hoverLeaveEvent')

    def hoverEnterEvent(self, mouseEvent):
        pass
        # print('hoverEnterEvent')
#------------------------------------------------------------------------------

class CustomScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(CustomScene, self).__init__(parent)

        n_st_12 = CustomRectItem('12 насосная станция')
        n_st_12.setRect(194, 33, 60, 30)
        n_st_12.setBrush(Qt.green)
        self.addItem(n_st_12)

        polygon_13_n_st = QPolygonF()
        polygon_13_n_st << QPointF( 83, 172 ) << QPointF( 122, 118 ) \
                        << QPointF( 153, 141 ) << QPointF( 113, 196 )
        n_st_13 = CustomPolygonItem('13 насосная станция')
        n_st_13.setPolygon(polygon_13_n_st)
        n_st_13.setBrush(Qt.green)
        self.addItem(n_st_13)

        cl_st = CustomRectItem('Хлорное хозяйство')
        cl_st.setRect(87, 393, 43, 80)
        cl_st.setBrush(Qt.green)
        self.addItem(cl_st)

        reag_st_3 = CustomRectItem('Реагентное хозяйство')
        reag_st_3.setRect(65, 523, 45, 110)
        reag_st_3.setBrush(Qt.green)
        self.addItem(reag_st_3)

        n_st_17 = CustomRectItem('17 насосная станция')
        n_st_17.setRect(162, 547, 15, 14)
        n_st_17.setBrush(Qt.green)
        self.addItem(n_st_17)

        n_st_38_2 = CustomRectItem('38-2 насосная станция')
        n_st_38_2.setRect(208, 581, 45, 35)
        n_st_38_2.setBrush(Qt.green)
        self.addItem(n_st_38_2)

        n_st_38_1 = CustomRectItem('38-1 насосная станция')
        n_st_38_1.setRect(208, 619, 45, 35)
        n_st_38_1.setBrush(Qt.green)
        self.addItem(n_st_38_1)

        micro_filter_st = CustomRectItem('Микрофильтры')
        micro_filter_st.setRect(197, 342, 45, 110)
        micro_filter_st.setBrush(Qt.green)
        self.addItem(micro_filter_st)

        n_st_21 = CustomRectItem('21 насосная станция')
        n_st_21.setRect(350, 100, 55, 25)
        n_st_21.setBrush(Qt.green)
        self.addItem(n_st_21)

        res_1500_st_21 = CustomRectItem('Резервуар 1500 м3 21 насосная станция')
        res_1500_st_21.setRect(349, 138, 20, 30)
        res_1500_st_21.setBrush(Qt.green)
        self.addItem(res_1500_st_21)

        res_750_st_21 = CustomEllipseItem('Резервуар 750 м3 21 насосная станция')
        res_750_st_21.setRect(385, 142, 25, 25)
        res_750_st_21.setBrush(Qt.green)
        self.addItem(res_750_st_21)

        res_2200_st_21 = CustomEllipseItem('Резервуар 2200 м3 21 насосная станция')
        res_2200_st_21.setRect(283, 174, 40, 40)
        res_2200_st_21.setBrush(Qt.green)
        self.addItem(res_2200_st_21)

        polygon_bl_1 = QPolygonF()
        polygon_bl_1 << QPointF(295, 248) << QPointF(432, 248) \
        << QPointF(433, 302) << QPointF(368, 302) << QPointF(368, 333) \
        << QPointF(348, 333) << QPointF(348, 302) << QPointF(340, 302) \
        << QPointF(340, 333) << QPointF(324, 333) << QPointF(324, 302) \
        << QPointF(314, 302) << QPointF(314, 333) << QPointF(295, 333)
        bl_1 = CustomPolygonItem('Блок 1')
        bl_1.setPolygon(polygon_bl_1)
        bl_1.setBrush(Qt.green)
        self.addItem(bl_1)

        bl_2 = CustomRectItem('Блок 2')
        bl_2.setRect(487, 255, 150, 85)
        bl_2.setBrush(Qt.green)
        self.addItem(bl_2)

        bl_4 = CustomRectItem('Блок 4')
        bl_4.setRect(294, 436, 160, 70)
        bl_4.setBrush(Qt.green)
        self.addItem(bl_4)

        bl_5 = CustomRectItem('Блок 5')
        bl_5.setRect(293, 540, 160, 70)
        bl_5.setBrush(Qt.green)
        self.addItem(bl_5)

        bl_3 = CustomRectItem('Блок 3')
        bl_3.setRect(489, 436, 150, 135)
        bl_3.setBrush(Qt.green)
        self.addItem(bl_3)

        res_7000_1 = CustomRectItem('Резервуар 7000-1 м3 2 блок')
        res_7000_1.setRect(501, 156, 55, 45)
        res_7000_1.setBrush(Qt.green)
        self.addItem(res_7000_1)

        res_7000_2 = CustomRectItem('Резервуар 7000-2 м3 2 блок')
        res_7000_2.setRect(558, 156, 55, 45)
        res_7000_2.setBrush(Qt.green)
        self.addItem(res_7000_2)

        polygon_res_3000_st_37 = QPolygonF()
        polygon_res_3000_st_37 << QPointF(766, 130) << QPointF(817, 92) \
                               << QPointF(839, 122) << QPointF(788, 160)
        res_3000_st_37 = CustomPolygonItem('Резервуар 3000 м3 37 насосная станция')
        res_3000_st_37.setPolygon(polygon_res_3000_st_37)
        res_3000_st_37.setBrush(Qt.green)
        self.addItem(res_3000_st_37)

        polygon_n_st_37 = QPolygonF()
        polygon_n_st_37 << QPointF(804, 168) << QPointF(845, 140) \
                        << QPointF(856, 156) << QPointF(815, 184)
        n_st_37 = CustomPolygonItem('37 насосная станция')
        n_st_37.setPolygon(polygon_n_st_37)
        n_st_37.setBrush(Qt.green)
        self.addItem(n_st_37)

        polygon_res_1000_st_37 = QPolygonF()
        polygon_res_1000_st_37 << QPointF(823, 195) << QPointF(862, 167) \
                               << QPointF(877, 187) << QPointF(838, 215)
        res_1000_st_37 = CustomPolygonItem('Резервуар 1000 м3 37 насосная станция')
        res_1000_st_37.setPolygon(polygon_res_1000_st_37)
        res_1000_st_37.setBrush(Qt.green)
        self.addItem(res_1000_st_37)

        res_10000_3 = CustomRectItem('Резервуар 10000 м3 №3')
        res_10000_3.setRect(705, 250, 55, 115)
        res_10000_3.setBrush(Qt.green)
        self.addItem(res_10000_3)

        res_10000_2 = CustomRectItem('Резервуар 10000 м3 №2')
        res_10000_2.setRect(705, 389, 85, 80)
        res_10000_2.setBrush(Qt.green)
        self.addItem(res_10000_2)

        res_10000_1 = CustomRectItem('Резервуар 10000 м3 №1')
        res_10000_1.setRect(705, 479, 85, 80)
        res_10000_1.setBrush(Qt.green)
        self.addItem(res_10000_1)

        n_st_22 = CustomRectItem('22 насосная станция')
        n_st_22.setRect(833, 305, 45, 110)
        n_st_22.setBrush(Qt.green)
        self.addItem(n_st_22)

        n_st_93 = CustomRectItem('93 насосная станция')
        n_st_93.setRect(843, 424, 35, 25)
        n_st_93.setBrush(Qt.green)
        self.addItem(n_st_93)

        n_st_23 = CustomRectItem('23 насосная станция')
        n_st_23.setRect(835, 465, 45, 110)
        n_st_23.setBrush(Qt.green)
        self.addItem(n_st_23)

        kp_2 = CustomRectItem('КП 2')
        kp_2.setRect(870, 590, 95, 25)
        kp_2.setBrush(Qt.green)
        self.addItem(kp_2)

        kp_1 = CustomRectItem('КП 1')
        kp_1.setRect(126, 233, 60, 30)
        kp_1.setBrush(Qt.green)
        self.addItem(kp_1)

class FindWindow(QtWidgets.QMainWindow, find_window.Ui_FindWindow):

    def __init__(self, parent=None):
        super(FindWindow, self).__init__(parent)
        self.setupUi(self)
        self.createGraphicView()
        self.comboBoxFindWindowInit()
        self.btnFind.clicked.connect(self.showFindWindow)
        self.dialog_find = FindResultWindow(self)


    def showFindWindow(self):
        self.dialog_find.show()

        place_dev = self.comboBoxPlaceFind.currentText()
        type_dev = self.comboBoxTypeFind.currentText()
        year_dev = self.comboBoxYearFind.currentText()
        name_dev = self.lineEditNameFind.text()

        place_dev_pr = place_dev.replace(' ', '')
        type_dev_pr = type_dev.replace(' ', '')
        year_dev_pr = year_dev + '-01-01'
        name_dev_pr = name_dev.replace(' ', '').upper()
        no_find_text = "Приборы не найдены!"

        self.dialog_find.listWidgetFindResult.clear()
        conn = sqlite3.connect('pribors.db')
        cursor = conn.cursor()
        if place_dev_pr.isalnum():    
            cursor.execute("SELECT * FROM pribors WHERE place=?", (place_dev, ))
        if type_dev_pr.isalnum():
            cursor.execute("SELECT * FROM pribors WHERE type=?", (type_dev, ))
        if year_dev.isalnum():
            cursor.execute("SELECT * FROM pribors WHERE year=?", (year_dev_pr, ))
        if name_dev_pr.isalnum():
            cursor.execute("SELECT * FROM pribors WHERE description=?", (name_dev_pr, ))
        if place_dev_pr.isalnum() and type_dev_pr.isalnum():
            cursor.execute("SELECT * FROM pribors WHERE place=? AND type=?", (place_dev, type_dev))
        if place_dev_pr.isalnum() and name_dev_pr.isalnum():
            cursor.execute("SELECT * FROM pribors WHERE place=? AND description=?", (place_dev, name_dev_pr))
        if year_dev.isalnum() and name_dev_pr.isalnum():
            cursor.execute("SELECT * FROM pribors WHERE year=? AND description=?", (year_dev_pr, name_dev_pr))
        if type_dev_pr.isalnum() and name_dev_pr.isalnum():
            cursor.execute("SELECT * FROM pribors WHERE type=? AND description=?", (type_dev, name_dev_pr))
        if place_dev_pr.isalnum() and type_dev_pr.isalnum() and year_dev.isalnum():
            cursor.execute("SELECT * FROM pribors WHERE place=? AND type=? AND year=?", (place_dev, type_dev, year_dev_pr))
        if place_dev_pr.isalnum() and type_dev_pr.isalnum() and year_dev.isalnum() and name_dev_pr.isalnum():
            cursor.execute("SELECT * FROM pribors WHERE type=? AND year=? AND description=?", (type_dev, year_dev_pr, name_dev_pr))
        if place_dev_pr.isalnum() and type_dev_pr.isalnum() and year_dev.isalnum() and name_dev_pr.isalnum():
            cursor.execute("SELECT * FROM pribors WHERE place=? AND type=? AND year=? AND description=?", (place_dev, type_dev, year_dev_pr, name_dev_pr))
        result_find = cursor.fetchall()
        list_elem_find = []

        for i in result_find:
            list_elem_find.append("Прибор: {description} Заводской №: {number} Год выпуска: {year} Место установки: {place}".format(description=i[1], number=i[3], year=i[5][:4], place=i[4]))

 
        for item in list_elem_find:
            self.dialog_find.listWidgetFindResult.addItem(item)

        # print(place_dev_pr.isalnum() and type_dev_pr.isalnum())
        # print(place_dev_pr.isalnum())
        # print(type_dev_pr.isalnum())
        # print(year_dev_pr.isalnum())

    def createGraphicView(self):
        self.scene = CustomScene(self)
        self.graphicsView_Schema.setScene(self.scene)

        self.text_map()


    def text_map(self):
        self.text_12_n_st = self.tr("12 н ст")
        n_st_12_text = self.scene.addText(self.text_12_n_st, QFont('Arial Black', 9))
        n_st_12_text.setPos(200, 37)


        self.text_13_n_st = self.tr("13 н ст")
        n_st_13_text = self.scene.addText(self.text_13_n_st, QFont('Arial Black', 8))
        n_st_13_text.setPos(100, 140)


        self.text_cl_st = self.tr("Хлор.\nхоз-во")
        cl_st_text = self.scene.addText(self.text_cl_st, QFont('Arial Black', 9))
        cl_st_text.setPos(86, 415)


        self.text_reag_st_3 = self.tr("Реаг.\nхоз-во")
        reag_st_3_text = self.scene.addText(self.text_reag_st_3, QFont('Arial Black', 9))
        reag_st_3_text.setPos(65, 555)


        self.text_17_n_st = self.tr("17 н ст")
        n_st_17_text = self.scene.addText(self.text_17_n_st, QFont('Arial Black', 9))
        n_st_17_text.setPos(143, 527)

        self.text_38_2_n_st = self.tr("38-2")
        n_st_38_2_text = self.scene.addText(self.text_38_2_n_st, QFont('Arial Black', 9))
        n_st_38_2_text.setPos(213, 587)

        self.text_38_1_n_st = self.tr("38-1")
        n_st_38_1_text = self.scene.addText(self.text_38_1_n_st, QFont('Arial Black', 9))
        n_st_38_1_text.setPos(213, 626)

        self.text_micro_filter_st = self.tr("Блок \nМ/Ф")
        micro_filter_st_text = self.scene.addText(self.text_micro_filter_st, QFont('Arial Black', 9))
        micro_filter_st_text.setPos(200, 375)

        self.text_21_n_st = self.tr("21 н ст")
        n_st_21_text = self.scene.addText(self.text_21_n_st, QFont('Arial Black', 9))
        n_st_21_text.setPos(353, 102)

        self.text_res_1500_st_21 = self.tr("1500\n  м3")
        res_1500_st_21_text = self.scene.addText(self.text_res_1500_st_21, QFont('Arial Black', 8))
        res_1500_st_21_text.setPos(315, 138)

        self.text_res_750_st_21 = self.tr("750\n м3")
        res_750_st_21_text = self.scene.addText(self.text_res_750_st_21, QFont('Arial Black', 8))
        res_750_st_21_text.setPos(410, 138)

        self.text_res_2200_st_21 = self.tr("2200\n  м3")
        res_2200_st_21_text = self.scene.addText(self.text_res_2200_st_21, QFont('Arial Black', 8))
        res_2200_st_21_text.setPos(286, 180)

        self.text_bl_1 = self.tr("Блок \n  № 1")
        bl_1_text = self.scene.addText(self.text_bl_1, QFont('Arial Black', 9))
        bl_1_text.setPos(340, 255)

        self.text_bl_2 = self.tr("Блок \n  № 2")
        bl_2_text = self.scene.addText(self.text_bl_2, QFont('Arial Black', 9))
        bl_2_text.setPos(540, 280)

        self.text_bl_4 = self.tr("Блок \n  № 4")
        bl_4_text = self.scene.addText(self.text_bl_4, QFont('Arial Black', 9))
        bl_4_text.setPos(352, 450)

        self.text_bl_5 = self.tr("Блок \n  № 5")
        bl_5_text = self.scene.addText(self.text_bl_5, QFont('Arial Black', 9))
        bl_5_text.setPos(352, 555)

        self.text_bl_3 = self.tr("Блок \n  № 3")
        bl_3_text = self.scene.addText(self.text_bl_3, QFont('Arial Black', 9))
        bl_3_text.setPos(545, 487)

        self.text_res_7000_1 = self.tr("7000 м3 \n левый")
        res_7000_1_text = self.scene.addText(self.text_res_7000_1, QFont('Arial Black', 8))
        res_7000_1_text.setPos(502, 160)

        self.text_res_7000_2 = self.tr("7000 м3 \nправый")
        res_7000_2_text = self.scene.addText(self.text_res_7000_2, QFont('Arial Black', 8))
        res_7000_2_text.setPos(560, 160)

        self.text_res_3000_st_37 = self.tr("3000 м3")
        res_3000_st_37_text = self.scene.addText(self.text_res_3000_st_37, QFont('Arial Black', 9))
        res_3000_st_37_text.setPos(830, 90)

        self.text_n_st_37 = self.tr("37 н ст")
        n_st_37_text = self.scene.addText(self.text_n_st_37, QFont('Arial Black', 9))
        n_st_37_text.setPos(855, 132)

        self.text_res_1000_st_37 = self.tr("1000 м3")
        res_1000_st_37_text = self.scene.addText(self.text_res_1000_st_37, QFont('Arial Black', 9))
        res_1000_st_37_text.setPos(875, 165)

        self.text_res_10000_3 = self.tr("РЧВ\n10000м3\n№ 3")
        res_10000_3_text = self.scene.addText(self.text_res_10000_3, QFont('Arial Black', 8))
        res_10000_3_text.setPos(704, 285)

        self.text_res_10000_2 = self.tr("РЧВ\n10000м3\n№ 2")
        res_10000_2_text = self.scene.addText(self.text_res_10000_2, QFont('Arial Black', 8))
        res_10000_2_text.setPos(720, 405)

        self.text_res_10000_1 = self.tr("РЧВ\n10000м3\n№ 1")
        res_10000_1_text = self.scene.addText(self.text_res_10000_1, QFont('Arial Black', 8))
        res_10000_1_text.setPos(720, 495)

        self.text_22_n_st = self.tr("22\nн ст")
        n_st_22_text = self.scene.addText(self.text_22_n_st, QFont('Arial Black', 9))
        n_st_22_text.setPos(842, 345)

        self.text_93_n_st = self.tr("93 н ст")
        n_st_93_text = self.scene.addText(self.text_93_n_st, QFont('Arial Black', 9))
        n_st_93_text.setPos(880, 425)

        self.text_23_n_st = self.tr("23\nн ст")
        n_st_23_text = self.scene.addText(self.text_23_n_st, QFont('Arial Black', 9))
        n_st_23_text.setPos(842, 500)

        self.text_kp2 = self.tr("КП 2")
        kp2_text = self.scene.addText(self.text_kp2, QFont('Arial Black', 9))
        kp2_text.setPos(900, 590)

        self.text_kp1 = self.tr("КП 1")
        kp1_text = self.scene.addText(self.text_kp1, QFont('Arial Black', 9))
        kp1_text.setPos(140, 237)


    def comboBoxFindWindowInit(self):
        self.comboBoxTypeFind.addItems(['',
                                        'Расходомер ультразвуковой',
                                        'Расходомер электромагнитный',
                                        'Уровнемер погружной',
                                        'Расходомер вихревой',
                                        'Уровнемер ультразвуковой',
                                        'Датчик давления',
                                        'Манометр'])
        self.comboBoxPlaceFind.addItems(['',
                                         '12 насосная станция',
                                         '13 насосная станция',
                                         '21 насосная станция',
                                         '22 насосная станция',
                                         '23 насосная станция',
                                         'КП 1',
                                         'КП 2',
                                         'Хлорное хозяйство',
                                         'Реагентное хозяйство',
                                         'Блок 1',
                                         'Блок 2',
                                         'Блок 3',
                                         'Блок 4',
                                         'Блок 5',
                                         '38-1 насосная станция',
                                         '38-2 насосная станция',
                                         '37 насосная станция',
                                         '93 насосная станция',
                                         '17 насосная станция',
                                         'Резервуар 1000 м3 37 насосная станция',
                                         'Резервуар 3000 м3 37 насосная станция',
                                         'Резервуар 750 м3 21 насосная станция',
                                         'Резервуар 1500 м3 21 насосная станция',
                                         'Резервуар 2200 м3 21 насосная станция',
                                         'Резервуар 7000-1 м3 2 блок',
                                         'Резервуар 7000-2 м3 2 блок',
                                         'Резервуар 10000 м3 №1',
                                         'Резервуар 10000 м3 №2',
                                         'Резервуар 10000 м3 №3'])

        self.comboBoxYearFind.addItems(['',
                                        '1990',
                                        '1991',
                                        '1992',
                                        '1993',
                                        '1994',
                                        '1995',
                                        '1996',
                                        '1997',
                                        '1998',
                                        '1999',
                                        '2000',
                                        '2001',
                                        '2002',
                                        '2003',
                                        '2004',
                                        '2005',
                                        '2006',
                                        '2007',
                                        '2008',
                                        '2009',
                                        '2010',
                                        '2011',
                                        '2012',
                                        '2013',
                                        '2014',
                                        '2015',
                                        '2016',
                                        '2017',
                                        '2018',
                                        '2019'])

    def comboboxFindWindowInit(self):
        pass


class FindResultWindow(QtWidgets.QMainWindow, find_result_window.Ui_FindResultWindow):

    def __init__(self, parent=None):
        super(FindResultWindow, self).__init__(parent)
        self.setupUi(self)


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('pribors.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS pribors (id integer primary key, description text, type text, number text,
            place text, year text, data text, data_next text)''')
        self.conn.commit()


    def insert_data(self, description, type_device, number, place, year, data, data_next):
       self.cursor.execute('''INSERT INTO pribors(description, type, number, place, year, data, data_next) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                      (description, type_device, number, place, year, data, data_next))
       self.conn.commit()

    def select_data_to_place(self, name):
        self.cursor.execute("SELECT * FROM pribors WHERE place=?", (name, ))
        items = self.cursor.fetchall()
        list_elem = []
        for i in items:
            list_elem.append("Прибор: {description} Заводской №: {number} Год выпуска: {year}".format(description=i[1], number=i[3], year=i[5][:4])\
                             + "\n -------------------------------------------------------")
        string_list_elem = '\n'.join(list_elem)



        msg_view = MyMessageBox()
        msg_view.setIcon(QMessageBox.Information)
        # msg_add.setIconPixmap(pixmap)  # Своя картинка

        msg_view.setWindowTitle(name)
        msg_view.setText(string_list_elem)
        # msg_view.setInformativeText("В базе данных нет информации о приборах")
        # msg_add.setDetailedText("DetailedText")
        msg_view.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DB()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
