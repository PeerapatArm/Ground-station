# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1201, 860)
        MainWindow.setMinimumSize(QtCore.QSize(1201, 860))
        MainWindow.setMaximumSize(QtCore.QSize(1201, 860))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 860))
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 860))
        self.centralwidget.setStyleSheet("background-color: rgb(217, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 25 14pt \"Yu Mincho Light\";")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.T_Can_Humid = QtWidgets.QLabel(self.widget_3)
        self.T_Can_Humid.setObjectName("T_Can_Humid")
        self.gridLayout_5.addWidget(self.T_Can_Humid, 1, 0, 1, 1)
        self.T_Can_rotat = QtWidgets.QLabel(self.widget_3)
        self.T_Can_rotat.setObjectName("T_Can_rotat")
        self.gridLayout_5.addWidget(self.T_Can_rotat, 3, 0, 1, 1)
        self.T_C_R_peek = QtWidgets.QLabel(self.widget_3)
        self.T_C_R_peek.setObjectName("T_C_R_peek")
        self.gridLayout_5.addWidget(self.T_C_R_peek, 4, 0, 1, 1)
        self.T_C_R_posi = QtWidgets.QLabel(self.widget_3)
        self.T_C_R_posi.setObjectName("T_C_R_posi")
        self.gridLayout_5.addWidget(self.T_C_R_posi, 5, 0, 1, 1)
        self.T_Can_PKG = QtWidgets.QLabel(self.widget_3)
        self.T_Can_PKG.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Can_PKG.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can_PKG.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Can_PKG.setObjectName("T_Can_PKG")
        self.gridLayout_5.addWidget(self.T_Can_PKG, 7, 0, 1, 1)
        self.T_Can_2 = QtWidgets.QLabel(self.widget_3)
        self.T_Can_2.setObjectName("T_Can_2")
        self.gridLayout_5.addWidget(self.T_Can_2, 6, 0, 1, 2)
        self.T_Can_ACCX = QtWidgets.QLabel(self.widget_3)
        self.T_Can_ACCX.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Can_ACCX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can_ACCX.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Can_ACCX.setObjectName("T_Can_ACCX")
        self.gridLayout_5.addWidget(self.T_Can_ACCX, 8, 0, 1, 1)
        self.Can_ACCX = QtWidgets.QLabel(self.widget_3)
        self.Can_ACCX.setMinimumSize(QtCore.QSize(50, 0))
        self.Can_ACCX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Can_ACCX.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Can_ACCX.setObjectName("Can_ACCX")
        self.gridLayout_5.addWidget(self.Can_ACCX, 8, 1, 1, 1)
        self.Roc_ACCX = QtWidgets.QLabel(self.widget_3)
        self.Roc_ACCX.setMinimumSize(QtCore.QSize(50, 0))
        self.Roc_ACCX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Roc_ACCX.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_ACCX.setAlignment(QtCore.Qt.AlignCenter)
        self.Roc_ACCX.setObjectName("Roc_ACCX")
        self.gridLayout_5.addWidget(self.Roc_ACCX, 8, 3, 1, 1)
        self.T_Can_ACCY = QtWidgets.QLabel(self.widget_3)
        self.T_Can_ACCY.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Can_ACCY.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can_ACCY.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Can_ACCY.setObjectName("T_Can_ACCY")
        self.gridLayout_5.addWidget(self.T_Can_ACCY, 9, 0, 1, 1)
        self.T_Roc_ACCX = QtWidgets.QLabel(self.widget_3)
        self.T_Roc_ACCX.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Roc_ACCX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc_ACCX.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Roc_ACCX.setObjectName("T_Roc_ACCX")
        self.gridLayout_5.addWidget(self.T_Roc_ACCX, 8, 2, 1, 1)
        self.Can_ACCY = QtWidgets.QLabel(self.widget_3)
        self.Can_ACCY.setMinimumSize(QtCore.QSize(50, 0))
        self.Can_ACCY.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Can_ACCY.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Can_ACCY.setObjectName("Can_ACCY")
        self.gridLayout_5.addWidget(self.Can_ACCY, 9, 1, 1, 1)
        self.Roc_PKG = QtWidgets.QLabel(self.widget_3)
        self.Roc_PKG.setMinimumSize(QtCore.QSize(50, 0))
        self.Roc_PKG.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Roc_PKG.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_PKG.setAlignment(QtCore.Qt.AlignCenter)
        self.Roc_PKG.setObjectName("Roc_PKG")
        self.gridLayout_5.addWidget(self.Roc_PKG, 7, 3, 1, 1)
        self.T_Roc_PKG = QtWidgets.QLabel(self.widget_3)
        self.T_Roc_PKG.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Roc_PKG.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc_PKG.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Roc_PKG.setObjectName("T_Roc_PKG")
        self.gridLayout_5.addWidget(self.T_Roc_PKG, 7, 2, 1, 1)
        self.T_Roc_ACCY = QtWidgets.QLabel(self.widget_3)
        self.T_Roc_ACCY.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Roc_ACCY.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc_ACCY.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Roc_ACCY.setObjectName("T_Roc_ACCY")
        self.gridLayout_5.addWidget(self.T_Roc_ACCY, 9, 2, 1, 1)
        self.T_Can_ACCZ = QtWidgets.QLabel(self.widget_3)
        self.T_Can_ACCZ.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Can_ACCZ.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can_ACCZ.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Can_ACCZ.setObjectName("T_Can_ACCZ")
        self.gridLayout_5.addWidget(self.T_Can_ACCZ, 10, 0, 1, 1)
        self.T_Roc_ACCZ = QtWidgets.QLabel(self.widget_3)
        self.T_Roc_ACCZ.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Roc_ACCZ.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc_ACCZ.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Roc_ACCZ.setObjectName("T_Roc_ACCZ")
        self.gridLayout_5.addWidget(self.T_Roc_ACCZ, 10, 2, 1, 1)
        self.Roc_ACCZ = QtWidgets.QLabel(self.widget_3)
        self.Roc_ACCZ.setMinimumSize(QtCore.QSize(50, 0))
        self.Roc_ACCZ.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Roc_ACCZ.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_ACCZ.setAlignment(QtCore.Qt.AlignCenter)
        self.Roc_ACCZ.setObjectName("Roc_ACCZ")
        self.gridLayout_5.addWidget(self.Roc_ACCZ, 10, 3, 1, 1)
        self.Can_GYRX = QtWidgets.QLabel(self.widget_3)
        self.Can_GYRX.setMinimumSize(QtCore.QSize(50, 0))
        self.Can_GYRX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Can_GYRX.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Can_GYRX.setObjectName("Can_GYRX")
        self.gridLayout_5.addWidget(self.Can_GYRX, 11, 1, 1, 1)
        self.T_Can_GYRX = QtWidgets.QLabel(self.widget_3)
        self.T_Can_GYRX.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Can_GYRX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can_GYRX.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Can_GYRX.setObjectName("T_Can_GYRX")
        self.gridLayout_5.addWidget(self.T_Can_GYRX, 11, 0, 1, 1)
        self.Roc_ACCY = QtWidgets.QLabel(self.widget_3)
        self.Roc_ACCY.setMinimumSize(QtCore.QSize(50, 0))
        self.Roc_ACCY.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Roc_ACCY.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_ACCY.setAlignment(QtCore.Qt.AlignCenter)
        self.Roc_ACCY.setObjectName("Roc_ACCY")
        self.gridLayout_5.addWidget(self.Roc_ACCY, 9, 3, 1, 1)
        self.Can_ACCZ = QtWidgets.QLabel(self.widget_3)
        self.Can_ACCZ.setMinimumSize(QtCore.QSize(50, 0))
        self.Can_ACCZ.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Can_ACCZ.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Can_ACCZ.setObjectName("Can_ACCZ")
        self.gridLayout_5.addWidget(self.Can_ACCZ, 10, 1, 1, 1)
        self.Can_GYRY = QtWidgets.QLabel(self.widget_3)
        self.Can_GYRY.setMinimumSize(QtCore.QSize(50, 0))
        self.Can_GYRY.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Can_GYRY.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Can_GYRY.setObjectName("Can_GYRY")
        self.gridLayout_5.addWidget(self.Can_GYRY, 12, 1, 1, 1)
        self.T_Roc_GYRY = QtWidgets.QLabel(self.widget_3)
        self.T_Roc_GYRY.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Roc_GYRY.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc_GYRY.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Roc_GYRY.setObjectName("T_Roc_GYRY")
        self.gridLayout_5.addWidget(self.T_Roc_GYRY, 12, 2, 1, 1)
        self.T_Roc_GYRX = QtWidgets.QLabel(self.widget_3)
        self.T_Roc_GYRX.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Roc_GYRX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc_GYRX.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Roc_GYRX.setObjectName("T_Roc_GYRX")
        self.gridLayout_5.addWidget(self.T_Roc_GYRX, 11, 2, 1, 1)
        self.Roc_GYRX = QtWidgets.QLabel(self.widget_3)
        self.Roc_GYRX.setMinimumSize(QtCore.QSize(50, 0))
        self.Roc_GYRX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Roc_GYRX.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_GYRX.setAlignment(QtCore.Qt.AlignCenter)
        self.Roc_GYRX.setObjectName("Roc_GYRX")
        self.gridLayout_5.addWidget(self.Roc_GYRX, 11, 3, 1, 1)
        self.T_Can_GYRY = QtWidgets.QLabel(self.widget_3)
        self.T_Can_GYRY.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Can_GYRY.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can_GYRY.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Can_GYRY.setObjectName("T_Can_GYRY")
        self.gridLayout_5.addWidget(self.T_Can_GYRY, 12, 0, 1, 1)
        self.Roc_GYRY = QtWidgets.QLabel(self.widget_3)
        self.Roc_GYRY.setMinimumSize(QtCore.QSize(50, 0))
        self.Roc_GYRY.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Roc_GYRY.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_GYRY.setAlignment(QtCore.Qt.AlignCenter)
        self.Roc_GYRY.setObjectName("Roc_GYRY")
        self.gridLayout_5.addWidget(self.Roc_GYRY, 12, 3, 1, 1)
        self.T_Roc_GYRZ = QtWidgets.QLabel(self.widget_3)
        self.T_Roc_GYRZ.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Roc_GYRZ.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc_GYRZ.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Roc_GYRZ.setObjectName("T_Roc_GYRZ")
        self.gridLayout_5.addWidget(self.T_Roc_GYRZ, 13, 2, 1, 1)
        self.Roc_GYRZ = QtWidgets.QLabel(self.widget_3)
        self.Roc_GYRZ.setMinimumSize(QtCore.QSize(50, 0))
        self.Roc_GYRZ.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Roc_GYRZ.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_GYRZ.setAlignment(QtCore.Qt.AlignCenter)
        self.Roc_GYRZ.setObjectName("Roc_GYRZ")
        self.gridLayout_5.addWidget(self.Roc_GYRZ, 13, 3, 1, 1)
        self.T_Can_GYRZ = QtWidgets.QLabel(self.widget_3)
        self.T_Can_GYRZ.setMinimumSize(QtCore.QSize(50, 0))
        self.T_Can_GYRZ.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can_GYRZ.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.T_Can_GYRZ.setObjectName("T_Can_GYRZ")
        self.gridLayout_5.addWidget(self.T_Can_GYRZ, 13, 0, 1, 1)
        self.Can_GYRZ = QtWidgets.QLabel(self.widget_3)
        self.Can_GYRZ.setMinimumSize(QtCore.QSize(50, 0))
        self.Can_GYRZ.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Can_GYRZ.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Can_GYRZ.setObjectName("Can_GYRZ")
        self.gridLayout_5.addWidget(self.Can_GYRZ, 13, 1, 1, 1)
        self.Humid_graph = PlotWidget(self.widget_3)
        self.Humid_graph.setMinimumSize(QtCore.QSize(350, 150))
        self.Humid_graph.setMaximumSize(QtCore.QSize(350, 16777215))
        self.Humid_graph.setObjectName("Humid_graph")
        self.gridLayout_5.addWidget(self.Humid_graph, 0, 0, 1, 4)
        self.Can_rotat_graph = PlotWidget(self.widget_3)
        self.Can_rotat_graph.setMinimumSize(QtCore.QSize(350, 150))
        self.Can_rotat_graph.setMaximumSize(QtCore.QSize(350, 16777215))
        self.Can_rotat_graph.setObjectName("Can_rotat_graph")
        self.gridLayout_5.addWidget(self.Can_rotat_graph, 2, 0, 1, 4)
        self.Can_PKG = QtWidgets.QLabel(self.widget_3)
        self.Can_PKG.setMinimumSize(QtCore.QSize(50, 0))
        self.Can_PKG.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Can_PKG.setStyleSheet("font: 25 9pt \"Yu Mincho Light\";")
        self.Can_PKG.setObjectName("Can_PKG")
        self.gridLayout_5.addWidget(self.Can_PKG, 7, 1, 1, 1)
        self.T_Roc_2 = QtWidgets.QLabel(self.widget_3)
        self.T_Roc_2.setObjectName("T_Roc_2")
        self.gridLayout_5.addWidget(self.T_Roc_2, 6, 2, 1, 2)
        self.Can_rotat = QtWidgets.QLabel(self.widget_3)
        self.Can_rotat.setAlignment(QtCore.Qt.AlignCenter)
        self.Can_rotat.setObjectName("Can_rotat")
        self.gridLayout_5.addWidget(self.Can_rotat, 3, 2, 1, 2)
        self.C_R_peek = QtWidgets.QLabel(self.widget_3)
        self.C_R_peek.setAlignment(QtCore.Qt.AlignCenter)
        self.C_R_peek.setObjectName("C_R_peek")
        self.gridLayout_5.addWidget(self.C_R_peek, 4, 2, 1, 2)
        self.C_R_posi = QtWidgets.QLabel(self.widget_3)
        self.C_R_posi.setAlignment(QtCore.Qt.AlignCenter)
        self.C_R_posi.setObjectName("C_R_posi")
        self.gridLayout_5.addWidget(self.C_R_posi, 5, 2, 1, 2)
        self.Can_Humid = QtWidgets.QLabel(self.widget_3)
        self.Can_Humid.setAlignment(QtCore.Qt.AlignCenter)
        self.Can_Humid.setObjectName("Can_Humid")
        self.gridLayout_5.addWidget(self.Can_Humid, 1, 2, 1, 2)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.T_Can_Tem = QtWidgets.QLabel(self.widget_2)
        self.T_Can_Tem.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can_Tem.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Can_Tem.setObjectName("T_Can_Tem")
        self.gridLayout_4.addWidget(self.T_Can_Tem, 4, 0, 1, 1)
        self.Can_Alt_graph = PlotWidget(self.widget_2)
        self.Can_Alt_graph.setMinimumSize(QtCore.QSize(300, 150))
        self.Can_Alt_graph.setObjectName("Can_Alt_graph")
        self.gridLayout_4.addWidget(self.Can_Alt_graph, 1, 0, 1, 2)
        self.Can_Tem_graph = PlotWidget(self.widget_2)
        self.Can_Tem_graph.setMinimumSize(QtCore.QSize(300, 150))
        self.Can_Tem_graph.setObjectName("Can_Tem_graph")
        self.gridLayout_4.addWidget(self.Can_Tem_graph, 3, 0, 1, 2)
        self.Roc_Tem_graph = PlotWidget(self.widget_2)
        self.Roc_Tem_graph.setMinimumSize(QtCore.QSize(300, 150))
        self.Roc_Tem_graph.setObjectName("Roc_Tem_graph")
        self.gridLayout_4.addWidget(self.Roc_Tem_graph, 8, 0, 1, 2)
        self.T_Can_Alt = QtWidgets.QLabel(self.widget_2)
        self.T_Can_Alt.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can_Alt.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Can_Alt.setObjectName("T_Can_Alt")
        self.gridLayout_4.addWidget(self.T_Can_Alt, 2, 0, 1, 1)
        self.T_Can = QtWidgets.QLabel(self.widget_2)
        self.T_Can.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can.setObjectName("T_Can")
        self.gridLayout_4.addWidget(self.T_Can, 0, 0, 1, 1)
        self.Can_Lati = QtWidgets.QLabel(self.widget_2)
        self.Can_Lati.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Can_Lati.setObjectName("Can_Lati")
        self.gridLayout_4.addWidget(self.Can_Lati, 1, 2, 1, 1)
        self.Can_Tem = QtWidgets.QLabel(self.widget_2)
        self.Can_Tem.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Can_Tem.setObjectName("Can_Tem")
        self.gridLayout_4.addWidget(self.Can_Tem, 4, 2, 1, 1)
        self.Can_Long = QtWidgets.QLabel(self.widget_2)
        self.Can_Long.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Can_Long.setObjectName("Can_Long")
        self.gridLayout_4.addWidget(self.Can_Long, 3, 2, 1, 1)
        self.Can_Alt = QtWidgets.QLabel(self.widget_2)
        self.Can_Alt.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Can_Alt.setObjectName("Can_Alt")
        self.gridLayout_4.addWidget(self.Can_Alt, 2, 2, 1, 1)
        self.Roc_Long = QtWidgets.QLabel(self.widget_2)
        self.Roc_Long.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Roc_Long.setObjectName("Roc_Long")
        self.gridLayout_4.addWidget(self.Roc_Long, 8, 2, 1, 1)
        self.Roc_Alt = QtWidgets.QLabel(self.widget_2)
        self.Roc_Alt.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Roc_Alt.setObjectName("Roc_Alt")
        self.gridLayout_4.addWidget(self.Roc_Alt, 7, 2, 1, 1)
        self.Roc_Tem = QtWidgets.QLabel(self.widget_2)
        self.Roc_Tem.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Roc_Tem.setObjectName("Roc_Tem")
        self.gridLayout_4.addWidget(self.Roc_Tem, 9, 2, 1, 1)
        self.T_Roc_Tem = QtWidgets.QLabel(self.widget_2)
        self.T_Roc_Tem.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc_Tem.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Roc_Tem.setObjectName("T_Roc_Tem")
        self.gridLayout_4.addWidget(self.T_Roc_Tem, 9, 0, 1, 1)
        self.T_Can_Batt = QtWidgets.QLabel(self.widget_2)
        self.T_Can_Batt.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Can_Batt.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Can_Batt.setObjectName("T_Can_Batt")
        self.gridLayout_4.addWidget(self.T_Can_Batt, 0, 1, 1, 1)
        self.Can_Batt = QtWidgets.QProgressBar(self.widget_2)
        self.Can_Batt.setMinimumSize(QtCore.QSize(120, 25))
        self.Can_Batt.setMaximumSize(QtCore.QSize(120, 25))
        self.Can_Batt.setProperty("value", 24)
        self.Can_Batt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Can_Batt.setTextVisible(True)
        self.Can_Batt.setObjectName("Can_Batt")
        self.gridLayout_4.addWidget(self.Can_Batt, 0, 2, 1, 1)
        self.T_Roc_Alt = QtWidgets.QLabel(self.widget_2)
        self.T_Roc_Alt.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc_Alt.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Roc_Alt.setObjectName("T_Roc_Alt")
        self.gridLayout_4.addWidget(self.T_Roc_Alt, 7, 0, 1, 1)
        self.Roc_Lati = QtWidgets.QLabel(self.widget_2)
        self.Roc_Lati.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Roc_Lati.setObjectName("Roc_Lati")
        self.gridLayout_4.addWidget(self.Roc_Lati, 6, 2, 1, 1)
        self.Roc_Alt_graph = PlotWidget(self.widget_2)
        self.Roc_Alt_graph.setMinimumSize(QtCore.QSize(300, 150))
        self.Roc_Alt_graph.setObjectName("Roc_Alt_graph")
        self.gridLayout_4.addWidget(self.Roc_Alt_graph, 6, 0, 1, 2)
        self.Roc_Batt = QtWidgets.QProgressBar(self.widget_2)
        self.Roc_Batt.setMinimumSize(QtCore.QSize(120, 25))
        self.Roc_Batt.setMaximumSize(QtCore.QSize(120, 25))
        self.Roc_Batt.setProperty("value", 24)
        self.Roc_Batt.setAlignment(QtCore.Qt.AlignCenter)
        self.Roc_Batt.setObjectName("Roc_Batt")
        self.gridLayout_4.addWidget(self.Roc_Batt, 5, 2, 1, 1)
        self.T_Roc_Batt = QtWidgets.QLabel(self.widget_2)
        self.T_Roc_Batt.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc_Batt.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Roc_Batt.setObjectName("T_Roc_Batt")
        self.gridLayout_4.addWidget(self.T_Roc_Batt, 5, 1, 1, 1)
        self.T_Roc = QtWidgets.QLabel(self.widget_2)
        self.T_Roc.setMaximumSize(QtCore.QSize(100, 16777215))
        self.T_Roc.setObjectName("T_Roc")
        self.gridLayout_4.addWidget(self.T_Roc, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.port_box = QtWidgets.QComboBox(self.widget)
        self.port_box.setMinimumSize(QtCore.QSize(0, 30))
        self.port_box.setObjectName("port_box")
        self.gridLayout_2.addWidget(self.port_box, 2, 0, 1, 4)
        self.time = QtWidgets.QLabel(self.widget)
        self.time.setMinimumSize(QtCore.QSize(0, 80))
        self.time.setMaximumSize(QtCore.QSize(16777215, 100))
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.gridLayout_2.addWidget(self.time, 0, 2, 1, 2)
        self.Baud_box = QtWidgets.QComboBox(self.widget)
        self.Baud_box.setMinimumSize(QtCore.QSize(0, 30))
        self.Baud_box.setObjectName("Baud_box")
        self.gridLayout_2.addWidget(self.Baud_box, 3, 0, 1, 4)
        self.elapsed = QtWidgets.QLabel(self.widget)
        self.elapsed.setMinimumSize(QtCore.QSize(0, 80))
        self.elapsed.setMaximumSize(QtCore.QSize(16777215, 100))
        self.elapsed.setAlignment(QtCore.Qt.AlignCenter)
        self.elapsed.setObjectName("elapsed")
        self.gridLayout_2.addWidget(self.elapsed, 1, 2, 1, 2)
        self.clear_bt = QtWidgets.QPushButton(self.widget)
        self.clear_bt.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_bt.setStyleSheet("font: 25 12pt \"Yu Mincho Light\";")
        self.clear_bt.setObjectName("clear_bt")
        self.gridLayout_2.addWidget(self.clear_bt, 4, 1, 1, 1)
        self.refresh_bt = QtWidgets.QPushButton(self.widget)
        self.refresh_bt.setMinimumSize(QtCore.QSize(0, 30))
        self.refresh_bt.setStyleSheet("font: 25 12pt \"Yu Mincho Light\";")
        self.refresh_bt.setObjectName("refresh_bt")
        self.gridLayout_2.addWidget(self.refresh_bt, 4, 2, 1, 1)
        self.start_bt = QtWidgets.QPushButton(self.widget)
        self.start_bt.setMinimumSize(QtCore.QSize(0, 30))
        self.start_bt.setStyleSheet("font: 25 12pt \"Yu Mincho Light\";")
        self.start_bt.setObjectName("start_bt")
        self.gridLayout_2.addWidget(self.start_bt, 4, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_4.setObjectName("widget_4")
        self.T_file_name = QtWidgets.QLabel(self.widget_4)
        self.T_file_name.setGeometry(QtCore.QRect(10, 59, 121, 41))
        self.T_file_name.setMinimumSize(QtCore.QSize(0, 0))
        self.T_file_name.setObjectName("T_file_name")
        self.comboBox = QtWidgets.QComboBox(self.widget_4)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.send_CMD_bt = QtWidgets.QPushButton(self.widget_4)
        self.send_CMD_bt.setGeometry(QtCore.QRect(210, 0, 111, 41))
        self.send_CMD_bt.setMinimumSize(QtCore.QSize(0, 30))
        self.send_CMD_bt.setStyleSheet("font: 25 12pt \"Yu Mincho Light\";")
        self.send_CMD_bt.setObjectName("send_CMD_bt")
        self.file_name = QtWidgets.QLabel(self.widget_4)
        self.file_name.setGeometry(QtCore.QRect(130, 59, 201, 41))
        self.file_name.setMinimumSize(QtCore.QSize(0, 0))
        self.file_name.setAlignment(QtCore.Qt.AlignCenter)
        self.file_name.setObjectName("file_name")
        self.gridLayout_2.addWidget(self.widget_4, 5, 0, 1, 4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LOS = QtWidgets.QLabel(self.widget_5)
        self.LOS.setMinimumSize(QtCore.QSize(0, 80))
        self.LOS.setMaximumSize(QtCore.QSize(16777215, 80))
        self.LOS.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.LOS.setAlignment(QtCore.Qt.AlignCenter)
        self.LOS.setObjectName("LOS")
        self.gridLayout_3.addWidget(self.LOS, 6, 1, 1, 1)
        self.T_LOS = QtWidgets.QLabel(self.widget_5)
        self.T_LOS.setMinimumSize(QtCore.QSize(0, 80))
        self.T_LOS.setMaximumSize(QtCore.QSize(16777215, 80))
        self.T_LOS.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_LOS.setObjectName("T_LOS")
        self.gridLayout_3.addWidget(self.T_LOS, 6, 0, 1, 1)
        self.T_Alt = QtWidgets.QLabel(self.widget_5)
        self.T_Alt.setMinimumSize(QtCore.QSize(0, 80))
        self.T_Alt.setMaximumSize(QtCore.QSize(16777215, 80))
        self.T_Alt.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Alt.setObjectName("T_Alt")
        self.gridLayout_3.addWidget(self.T_Alt, 4, 0, 1, 1)
        self.T_Lng = QtWidgets.QLabel(self.widget_5)
        self.T_Lng.setMinimumSize(QtCore.QSize(0, 80))
        self.T_Lng.setMaximumSize(QtCore.QSize(16777215, 80))
        self.T_Lng.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Lng.setObjectName("T_Lng")
        self.gridLayout_3.addWidget(self.T_Lng, 3, 0, 1, 1)
        self.T_Lat = QtWidgets.QLabel(self.widget_5)
        self.T_Lat.setMinimumSize(QtCore.QSize(0, 80))
        self.T_Lat.setMaximumSize(QtCore.QSize(16777215, 80))
        self.T_Lat.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Lat.setObjectName("T_Lat")
        self.gridLayout_3.addWidget(self.T_Lat, 2, 0, 1, 1)
        self.T_GS_posi_Alt = QtWidgets.QLabel(self.widget_5)
        self.T_GS_posi_Alt.setMinimumSize(QtCore.QSize(0, 80))
        self.T_GS_posi_Alt.setMaximumSize(QtCore.QSize(16777215, 80))
        self.T_GS_posi_Alt.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_GS_posi_Alt.setObjectName("T_GS_posi_Alt")
        self.gridLayout_3.addWidget(self.T_GS_posi_Alt, 7, 0, 1, 1)
        self.T_GD = QtWidgets.QLabel(self.widget_5)
        self.T_GD.setMinimumSize(QtCore.QSize(0, 80))
        self.T_GD.setMaximumSize(QtCore.QSize(16777215, 80))
        self.T_GD.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_GD.setObjectName("T_GD")
        self.gridLayout_3.addWidget(self.T_GD, 5, 0, 1, 1)
        self.Alt = QtWidgets.QLabel(self.widget_5)
        self.Alt.setMinimumSize(QtCore.QSize(0, 80))
        self.Alt.setMaximumSize(QtCore.QSize(16777215, 80))
        self.Alt.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Alt.setAlignment(QtCore.Qt.AlignCenter)
        self.Alt.setObjectName("Alt")
        self.gridLayout_3.addWidget(self.Alt, 4, 1, 1, 1)
        self.GS_posi_Alt = QtWidgets.QLabel(self.widget_5)
        self.GS_posi_Alt.setMinimumSize(QtCore.QSize(0, 80))
        self.GS_posi_Alt.setMaximumSize(QtCore.QSize(16777215, 80))
        self.GS_posi_Alt.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.GS_posi_Alt.setAlignment(QtCore.Qt.AlignCenter)
        self.GS_posi_Alt.setObjectName("GS_posi_Alt")
        self.gridLayout_3.addWidget(self.GS_posi_Alt, 7, 1, 1, 1)
        self.GD = QtWidgets.QLabel(self.widget_5)
        self.GD.setMinimumSize(QtCore.QSize(0, 80))
        self.GD.setMaximumSize(QtCore.QSize(16777215, 80))
        self.GD.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.GD.setAlignment(QtCore.Qt.AlignCenter)
        self.GD.setObjectName("GD")
        self.gridLayout_3.addWidget(self.GD, 5, 1, 1, 1)
        self.Ele = QtWidgets.QLabel(self.widget_5)
        self.Ele.setMinimumSize(QtCore.QSize(0, 80))
        self.Ele.setMaximumSize(QtCore.QSize(16777215, 80))
        self.Ele.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Ele.setAlignment(QtCore.Qt.AlignCenter)
        self.Ele.setObjectName("Ele")
        self.gridLayout_3.addWidget(self.Ele, 1, 1, 1, 1)
        self.Lng = QtWidgets.QLabel(self.widget_5)
        self.Lng.setMinimumSize(QtCore.QSize(0, 80))
        self.Lng.setMaximumSize(QtCore.QSize(16777215, 80))
        self.Lng.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Lng.setAlignment(QtCore.Qt.AlignCenter)
        self.Lng.setObjectName("Lng")
        self.gridLayout_3.addWidget(self.Lng, 3, 1, 1, 1)
        self.Lat = QtWidgets.QLabel(self.widget_5)
        self.Lat.setMinimumSize(QtCore.QSize(0, 80))
        self.Lat.setMaximumSize(QtCore.QSize(16777215, 80))
        self.Lat.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Lat.setAlignment(QtCore.Qt.AlignCenter)
        self.Lat.setObjectName("Lat")
        self.gridLayout_3.addWidget(self.Lat, 2, 1, 1, 1)
        self.T_Ele = QtWidgets.QLabel(self.widget_5)
        self.T_Ele.setMinimumSize(QtCore.QSize(0, 80))
        self.T_Ele.setMaximumSize(QtCore.QSize(16777215, 80))
        self.T_Ele.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Ele.setObjectName("T_Ele")
        self.gridLayout_3.addWidget(self.T_Ele, 1, 0, 1, 1)
        self.Azi = QtWidgets.QLabel(self.widget_5)
        self.Azi.setMinimumSize(QtCore.QSize(0, 80))
        self.Azi.setMaximumSize(QtCore.QSize(16777215, 80))
        self.Azi.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.Azi.setAlignment(QtCore.Qt.AlignCenter)
        self.Azi.setObjectName("Azi")
        self.gridLayout_3.addWidget(self.Azi, 0, 1, 1, 1)
        self.T_Azi = QtWidgets.QLabel(self.widget_5)
        self.T_Azi.setMinimumSize(QtCore.QSize(0, 80))
        self.T_Azi.setMaximumSize(QtCore.QSize(16777215, 80))
        self.T_Azi.setStyleSheet("font: 25 10pt \"Yu Mincho Light\";")
        self.T_Azi.setObjectName("T_Azi")
        self.gridLayout_3.addWidget(self.T_Azi, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_5, 6, 0, 1, 4)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setStyleSheet("image: url(:/newPrefix/logo.png);\n"
"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2.addWidget(self.frame, 0, 0, 2, 2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.T_Can_Humid.setText(_translate("MainWindow", "Humidity"))
        self.T_Can_rotat.setText(_translate("MainWindow", "Rotation rate"))
        self.T_C_R_peek.setText(_translate("MainWindow", "Peek Alt"))
        self.T_C_R_posi.setText(_translate("MainWindow", "Position"))
        self.T_Can_PKG.setText(_translate("MainWindow", "PKG count"))
        self.T_Can_2.setText(_translate("MainWindow", "CanSat"))
        self.T_Can_ACCX.setText(_translate("MainWindow", "ACCX"))
        self.Can_ACCX.setText(_translate("MainWindow", "0"))
        self.Roc_ACCX.setText(_translate("MainWindow", "0"))
        self.T_Can_ACCY.setText(_translate("MainWindow", "ACCY"))
        self.T_Roc_ACCX.setText(_translate("MainWindow", "ACCX"))
        self.Can_ACCY.setText(_translate("MainWindow", "0"))
        self.Roc_PKG.setText(_translate("MainWindow", "0"))
        self.T_Roc_PKG.setText(_translate("MainWindow", "PKG count"))
        self.T_Roc_ACCY.setText(_translate("MainWindow", "ACCY"))
        self.T_Can_ACCZ.setText(_translate("MainWindow", "ACCZ"))
        self.T_Roc_ACCZ.setText(_translate("MainWindow", "ACCZ"))
        self.Roc_ACCZ.setText(_translate("MainWindow", "0"))
        self.Can_GYRX.setText(_translate("MainWindow", "0"))
        self.T_Can_GYRX.setText(_translate("MainWindow", "GYRX"))
        self.Roc_ACCY.setText(_translate("MainWindow", "0"))
        self.Can_ACCZ.setText(_translate("MainWindow", "0"))
        self.Can_GYRY.setText(_translate("MainWindow", "0"))
        self.T_Roc_GYRY.setText(_translate("MainWindow", "GYRY"))
        self.T_Roc_GYRX.setText(_translate("MainWindow", "GYRX"))
        self.Roc_GYRX.setText(_translate("MainWindow", "0"))
        self.T_Can_GYRY.setText(_translate("MainWindow", "GYRY"))
        self.Roc_GYRY.setText(_translate("MainWindow", "0"))
        self.T_Roc_GYRZ.setText(_translate("MainWindow", "GYRZ"))
        self.Roc_GYRZ.setText(_translate("MainWindow", "0"))
        self.T_Can_GYRZ.setText(_translate("MainWindow", "GYRZ"))
        self.Can_GYRZ.setText(_translate("MainWindow", "0"))
        self.Can_PKG.setText(_translate("MainWindow", "0"))
        self.T_Roc_2.setText(_translate("MainWindow", "Rocket"))
        self.Can_rotat.setText(_translate("MainWindow", "0"))
        self.C_R_peek.setText(_translate("MainWindow", "0"))
        self.C_R_posi.setText(_translate("MainWindow", "0"))
        self.Can_Humid.setText(_translate("MainWindow", "0"))
        self.T_Can_Tem.setText(_translate("MainWindow", "Temperature"))
        self.T_Can_Alt.setText(_translate("MainWindow", "Altitude"))
        self.T_Can.setText(_translate("MainWindow", "CanSat"))
        self.Can_Lati.setText(_translate("MainWindow", "Latitude"))
        self.Can_Tem.setText(_translate("MainWindow", "0.0000000"))
        self.Can_Long.setText(_translate("MainWindow", "Longitude"))
        self.Can_Alt.setText(_translate("MainWindow", "0.0000000"))
        self.Roc_Long.setText(_translate("MainWindow", "Longitude"))
        self.Roc_Alt.setText(_translate("MainWindow", "0.0000000"))
        self.Roc_Tem.setText(_translate("MainWindow", "0.0000000"))
        self.T_Roc_Tem.setText(_translate("MainWindow", "Temperature"))
        self.T_Can_Batt.setText(_translate("MainWindow", "Battery"))
        self.T_Roc_Alt.setText(_translate("MainWindow", "Altitude"))
        self.Roc_Lati.setText(_translate("MainWindow", "Latitude"))
        self.T_Roc_Batt.setText(_translate("MainWindow", "Battery"))
        self.T_Roc.setText(_translate("MainWindow", "Rocket"))
        self.time.setText(_translate("MainWindow", "00:00:00"))
        self.elapsed.setText(_translate("MainWindow", "00:00:00"))
        self.clear_bt.setText(_translate("MainWindow", "Clear"))
        self.refresh_bt.setText(_translate("MainWindow", "Refresh"))
        self.start_bt.setText(_translate("MainWindow", "Start"))
        self.T_file_name.setText(_translate("MainWindow", "File name :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "CMDCX,ON$"))
        self.comboBox.setItemText(1, _translate("MainWindow", "CMDCX,OFF$"))
        self.comboBox.setItemText(2, _translate("MainWindow", "CMDSP1,ON$"))
        self.comboBox.setItemText(3, _translate("MainWindow", "CMDSP2,ON$"))
        self.comboBox.setItemText(4, _translate("MainWindow", "CMDSP1,OFF$"))
        self.comboBox.setItemText(5, _translate("MainWindow", "CMDSP2,OFF$"))
        self.send_CMD_bt.setText(_translate("MainWindow", "Send CMD"))
        self.file_name.setText(_translate("MainWindow", "???"))
        self.LOS.setText(_translate("MainWindow", "0"))
        self.T_LOS.setText(_translate("MainWindow", "Line of sight"))
        self.T_Alt.setText(_translate("MainWindow", "ALT"))
        self.T_Lng.setText(_translate("MainWindow", "LNG"))
        self.T_Lat.setText(_translate("MainWindow", "LAT"))
        self.T_GS_posi_Alt.setText(_translate("MainWindow", "GS position and Alt"))
        self.T_GD.setText(_translate("MainWindow", "Ground distance"))
        self.Alt.setText(_translate("MainWindow", "0"))
        self.GS_posi_Alt.setText(_translate("MainWindow", "0"))
        self.GD.setText(_translate("MainWindow", "0"))
        self.Ele.setText(_translate("MainWindow", "0"))
        self.Lng.setText(_translate("MainWindow", "0"))
        self.Lat.setText(_translate("MainWindow", "0"))
        self.T_Ele.setText(_translate("MainWindow", "ELEVATION"))
        self.Azi.setText(_translate("MainWindow", "0"))
        self.T_Azi.setText(_translate("MainWindow", "AZIMUTH"))
from pyqtgraph import PlotWidget
import logo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
