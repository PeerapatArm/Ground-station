# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QWidget)

from pyqtgraph import PlotWidget
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1201, 860)
        MainWindow.setMinimumSize(QSize(1201, 860))
        MainWindow.setMaximumSize(QSize(1201, 860))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1200, 860))
        self.centralwidget.setMaximumSize(QSize(1200, 860))
        self.centralwidget.setStyleSheet(u"background-color: rgb(217, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 25 14pt \"Yu Mincho Light\";")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.T_Can_Humid = QLabel(self.widget_3)
        self.T_Can_Humid.setObjectName(u"T_Can_Humid")

        self.gridLayout_5.addWidget(self.T_Can_Humid, 1, 0, 1, 1)

        self.T_Can_rotat = QLabel(self.widget_3)
        self.T_Can_rotat.setObjectName(u"T_Can_rotat")

        self.gridLayout_5.addWidget(self.T_Can_rotat, 3, 0, 1, 1)

        self.T_C_R_peek = QLabel(self.widget_3)
        self.T_C_R_peek.setObjectName(u"T_C_R_peek")

        self.gridLayout_5.addWidget(self.T_C_R_peek, 4, 0, 1, 1)

        self.T_C_R_posi = QLabel(self.widget_3)
        self.T_C_R_posi.setObjectName(u"T_C_R_posi")

        self.gridLayout_5.addWidget(self.T_C_R_posi, 5, 0, 1, 1)

        self.T_Can_PKG = QLabel(self.widget_3)
        self.T_Can_PKG.setObjectName(u"T_Can_PKG")
        self.T_Can_PKG.setMinimumSize(QSize(50, 0))
        self.T_Can_PKG.setMaximumSize(QSize(100, 16777215))
        self.T_Can_PKG.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Can_PKG, 7, 0, 1, 1)

        self.T_Can_2 = QLabel(self.widget_3)
        self.T_Can_2.setObjectName(u"T_Can_2")

        self.gridLayout_5.addWidget(self.T_Can_2, 6, 0, 1, 2)

        self.T_Can_ACCX = QLabel(self.widget_3)
        self.T_Can_ACCX.setObjectName(u"T_Can_ACCX")
        self.T_Can_ACCX.setMinimumSize(QSize(50, 0))
        self.T_Can_ACCX.setMaximumSize(QSize(100, 16777215))
        self.T_Can_ACCX.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Can_ACCX, 8, 0, 1, 1)

        self.Can_ACCX = QLabel(self.widget_3)
        self.Can_ACCX.setObjectName(u"Can_ACCX")
        self.Can_ACCX.setMinimumSize(QSize(50, 0))
        self.Can_ACCX.setMaximumSize(QSize(100, 16777215))
        self.Can_ACCX.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.Can_ACCX, 8, 1, 1, 1)

        self.Roc_ACCX = QLabel(self.widget_3)
        self.Roc_ACCX.setObjectName(u"Roc_ACCX")
        self.Roc_ACCX.setMinimumSize(QSize(50, 0))
        self.Roc_ACCX.setMaximumSize(QSize(100, 16777215))
        self.Roc_ACCX.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_ACCX.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Roc_ACCX, 8, 3, 1, 1)

        self.T_Can_ACCY = QLabel(self.widget_3)
        self.T_Can_ACCY.setObjectName(u"T_Can_ACCY")
        self.T_Can_ACCY.setMinimumSize(QSize(50, 0))
        self.T_Can_ACCY.setMaximumSize(QSize(100, 16777215))
        self.T_Can_ACCY.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Can_ACCY, 9, 0, 1, 1)

        self.T_Roc_ACCX = QLabel(self.widget_3)
        self.T_Roc_ACCX.setObjectName(u"T_Roc_ACCX")
        self.T_Roc_ACCX.setMinimumSize(QSize(50, 0))
        self.T_Roc_ACCX.setMaximumSize(QSize(100, 16777215))
        self.T_Roc_ACCX.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Roc_ACCX, 8, 2, 1, 1)

        self.Can_ACCY = QLabel(self.widget_3)
        self.Can_ACCY.setObjectName(u"Can_ACCY")
        self.Can_ACCY.setMinimumSize(QSize(50, 0))
        self.Can_ACCY.setMaximumSize(QSize(100, 16777215))
        self.Can_ACCY.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.Can_ACCY, 9, 1, 1, 1)

        self.Roc_PKG = QLabel(self.widget_3)
        self.Roc_PKG.setObjectName(u"Roc_PKG")
        self.Roc_PKG.setMinimumSize(QSize(50, 0))
        self.Roc_PKG.setMaximumSize(QSize(100, 16777215))
        self.Roc_PKG.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_PKG.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Roc_PKG, 7, 3, 1, 1)

        self.T_Roc_PKG = QLabel(self.widget_3)
        self.T_Roc_PKG.setObjectName(u"T_Roc_PKG")
        self.T_Roc_PKG.setMinimumSize(QSize(50, 0))
        self.T_Roc_PKG.setMaximumSize(QSize(100, 16777215))
        self.T_Roc_PKG.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Roc_PKG, 7, 2, 1, 1)

        self.T_Roc_ACCY = QLabel(self.widget_3)
        self.T_Roc_ACCY.setObjectName(u"T_Roc_ACCY")
        self.T_Roc_ACCY.setMinimumSize(QSize(50, 0))
        self.T_Roc_ACCY.setMaximumSize(QSize(100, 16777215))
        self.T_Roc_ACCY.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Roc_ACCY, 9, 2, 1, 1)

        self.T_Can_ACCZ = QLabel(self.widget_3)
        self.T_Can_ACCZ.setObjectName(u"T_Can_ACCZ")
        self.T_Can_ACCZ.setMinimumSize(QSize(50, 0))
        self.T_Can_ACCZ.setMaximumSize(QSize(100, 16777215))
        self.T_Can_ACCZ.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Can_ACCZ, 10, 0, 1, 1)

        self.T_Roc_ACCZ = QLabel(self.widget_3)
        self.T_Roc_ACCZ.setObjectName(u"T_Roc_ACCZ")
        self.T_Roc_ACCZ.setMinimumSize(QSize(50, 0))
        self.T_Roc_ACCZ.setMaximumSize(QSize(100, 16777215))
        self.T_Roc_ACCZ.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Roc_ACCZ, 10, 2, 1, 1)

        self.Roc_ACCZ = QLabel(self.widget_3)
        self.Roc_ACCZ.setObjectName(u"Roc_ACCZ")
        self.Roc_ACCZ.setMinimumSize(QSize(50, 0))
        self.Roc_ACCZ.setMaximumSize(QSize(100, 16777215))
        self.Roc_ACCZ.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_ACCZ.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Roc_ACCZ, 10, 3, 1, 1)

        self.Can_GYRX = QLabel(self.widget_3)
        self.Can_GYRX.setObjectName(u"Can_GYRX")
        self.Can_GYRX.setMinimumSize(QSize(50, 0))
        self.Can_GYRX.setMaximumSize(QSize(100, 16777215))
        self.Can_GYRX.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.Can_GYRX, 11, 1, 1, 1)

        self.T_Can_GYRX = QLabel(self.widget_3)
        self.T_Can_GYRX.setObjectName(u"T_Can_GYRX")
        self.T_Can_GYRX.setMinimumSize(QSize(50, 0))
        self.T_Can_GYRX.setMaximumSize(QSize(100, 16777215))
        self.T_Can_GYRX.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Can_GYRX, 11, 0, 1, 1)

        self.Roc_ACCY = QLabel(self.widget_3)
        self.Roc_ACCY.setObjectName(u"Roc_ACCY")
        self.Roc_ACCY.setMinimumSize(QSize(50, 0))
        self.Roc_ACCY.setMaximumSize(QSize(100, 16777215))
        self.Roc_ACCY.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_ACCY.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Roc_ACCY, 9, 3, 1, 1)

        self.Can_ACCZ = QLabel(self.widget_3)
        self.Can_ACCZ.setObjectName(u"Can_ACCZ")
        self.Can_ACCZ.setMinimumSize(QSize(50, 0))
        self.Can_ACCZ.setMaximumSize(QSize(100, 16777215))
        self.Can_ACCZ.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.Can_ACCZ, 10, 1, 1, 1)

        self.Can_GYRY = QLabel(self.widget_3)
        self.Can_GYRY.setObjectName(u"Can_GYRY")
        self.Can_GYRY.setMinimumSize(QSize(50, 0))
        self.Can_GYRY.setMaximumSize(QSize(100, 16777215))
        self.Can_GYRY.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.Can_GYRY, 12, 1, 1, 1)

        self.T_Roc_GYRY = QLabel(self.widget_3)
        self.T_Roc_GYRY.setObjectName(u"T_Roc_GYRY")
        self.T_Roc_GYRY.setMinimumSize(QSize(50, 0))
        self.T_Roc_GYRY.setMaximumSize(QSize(100, 16777215))
        self.T_Roc_GYRY.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Roc_GYRY, 12, 2, 1, 1)

        self.T_Roc_GYRX = QLabel(self.widget_3)
        self.T_Roc_GYRX.setObjectName(u"T_Roc_GYRX")
        self.T_Roc_GYRX.setMinimumSize(QSize(50, 0))
        self.T_Roc_GYRX.setMaximumSize(QSize(100, 16777215))
        self.T_Roc_GYRX.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Roc_GYRX, 11, 2, 1, 1)

        self.Roc_GYRX = QLabel(self.widget_3)
        self.Roc_GYRX.setObjectName(u"Roc_GYRX")
        self.Roc_GYRX.setMinimumSize(QSize(50, 0))
        self.Roc_GYRX.setMaximumSize(QSize(100, 16777215))
        self.Roc_GYRX.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_GYRX.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Roc_GYRX, 11, 3, 1, 1)

        self.T_Can_GYRY = QLabel(self.widget_3)
        self.T_Can_GYRY.setObjectName(u"T_Can_GYRY")
        self.T_Can_GYRY.setMinimumSize(QSize(50, 0))
        self.T_Can_GYRY.setMaximumSize(QSize(100, 16777215))
        self.T_Can_GYRY.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Can_GYRY, 12, 0, 1, 1)

        self.Roc_GYRY = QLabel(self.widget_3)
        self.Roc_GYRY.setObjectName(u"Roc_GYRY")
        self.Roc_GYRY.setMinimumSize(QSize(50, 0))
        self.Roc_GYRY.setMaximumSize(QSize(100, 16777215))
        self.Roc_GYRY.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_GYRY.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Roc_GYRY, 12, 3, 1, 1)

        self.T_Roc_GYRZ = QLabel(self.widget_3)
        self.T_Roc_GYRZ.setObjectName(u"T_Roc_GYRZ")
        self.T_Roc_GYRZ.setMinimumSize(QSize(50, 0))
        self.T_Roc_GYRZ.setMaximumSize(QSize(100, 16777215))
        self.T_Roc_GYRZ.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Roc_GYRZ, 13, 2, 1, 1)

        self.Roc_GYRZ = QLabel(self.widget_3)
        self.Roc_GYRZ.setObjectName(u"Roc_GYRZ")
        self.Roc_GYRZ.setMinimumSize(QSize(50, 0))
        self.Roc_GYRZ.setMaximumSize(QSize(100, 16777215))
        self.Roc_GYRZ.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")
        self.Roc_GYRZ.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Roc_GYRZ, 13, 3, 1, 1)

        self.T_Can_GYRZ = QLabel(self.widget_3)
        self.T_Can_GYRZ.setObjectName(u"T_Can_GYRZ")
        self.T_Can_GYRZ.setMinimumSize(QSize(50, 0))
        self.T_Can_GYRZ.setMaximumSize(QSize(100, 16777215))
        self.T_Can_GYRZ.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.T_Can_GYRZ, 13, 0, 1, 1)

        self.Can_GYRZ = QLabel(self.widget_3)
        self.Can_GYRZ.setObjectName(u"Can_GYRZ")
        self.Can_GYRZ.setMinimumSize(QSize(50, 0))
        self.Can_GYRZ.setMaximumSize(QSize(100, 16777215))
        self.Can_GYRZ.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.Can_GYRZ, 13, 1, 1, 1)

        self.Humid_graph = PlotWidget(self.widget_3)
        self.Humid_graph.setObjectName(u"Humid_graph")
        self.Humid_graph.setMinimumSize(QSize(350, 150))
        self.Humid_graph.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.Humid_graph, 0, 0, 1, 4)

        self.Can_rotat_graph = PlotWidget(self.widget_3)
        self.Can_rotat_graph.setObjectName(u"Can_rotat_graph")
        self.Can_rotat_graph.setMinimumSize(QSize(350, 150))
        self.Can_rotat_graph.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.Can_rotat_graph, 2, 0, 1, 4)

        self.Can_PKG = QLabel(self.widget_3)
        self.Can_PKG.setObjectName(u"Can_PKG")
        self.Can_PKG.setMinimumSize(QSize(50, 0))
        self.Can_PKG.setMaximumSize(QSize(100, 16777215))
        self.Can_PKG.setStyleSheet(u"font: 25 9pt \"Yu Mincho Light\";")

        self.gridLayout_5.addWidget(self.Can_PKG, 7, 1, 1, 1)

        self.T_Roc_2 = QLabel(self.widget_3)
        self.T_Roc_2.setObjectName(u"T_Roc_2")

        self.gridLayout_5.addWidget(self.T_Roc_2, 6, 2, 1, 2)

        self.Can_rotat = QLabel(self.widget_3)
        self.Can_rotat.setObjectName(u"Can_rotat")
        self.Can_rotat.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Can_rotat, 3, 2, 1, 2)

        self.C_R_peek = QLabel(self.widget_3)
        self.C_R_peek.setObjectName(u"C_R_peek")
        self.C_R_peek.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_R_peek, 4, 2, 1, 2)

        self.C_R_posi = QLabel(self.widget_3)
        self.C_R_posi.setObjectName(u"C_R_posi")
        self.C_R_posi.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_R_posi, 5, 2, 1, 2)

        self.Can_Humid = QLabel(self.widget_3)
        self.Can_Humid.setObjectName(u"Can_Humid")
        self.Can_Humid.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Can_Humid, 1, 2, 1, 2)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(500, 16777215))
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.T_Can_Tem = QLabel(self.widget_2)
        self.T_Can_Tem.setObjectName(u"T_Can_Tem")
        self.T_Can_Tem.setMaximumSize(QSize(100, 16777215))
        self.T_Can_Tem.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.T_Can_Tem, 4, 0, 1, 1)

        self.Can_Alt_graph = PlotWidget(self.widget_2)
        self.Can_Alt_graph.setObjectName(u"Can_Alt_graph")
        self.Can_Alt_graph.setMinimumSize(QSize(300, 150))

        self.gridLayout_4.addWidget(self.Can_Alt_graph, 1, 0, 1, 2)

        self.Can_Tem_graph = PlotWidget(self.widget_2)
        self.Can_Tem_graph.setObjectName(u"Can_Tem_graph")
        self.Can_Tem_graph.setMinimumSize(QSize(300, 150))

        self.gridLayout_4.addWidget(self.Can_Tem_graph, 3, 0, 1, 2)

        self.Roc_Tem_graph = PlotWidget(self.widget_2)
        self.Roc_Tem_graph.setObjectName(u"Roc_Tem_graph")
        self.Roc_Tem_graph.setMinimumSize(QSize(300, 150))

        self.gridLayout_4.addWidget(self.Roc_Tem_graph, 8, 0, 1, 2)

        self.T_Can_Alt = QLabel(self.widget_2)
        self.T_Can_Alt.setObjectName(u"T_Can_Alt")
        self.T_Can_Alt.setMaximumSize(QSize(100, 16777215))
        self.T_Can_Alt.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.T_Can_Alt, 2, 0, 1, 1)

        self.T_Can = QLabel(self.widget_2)
        self.T_Can.setObjectName(u"T_Can")
        self.T_Can.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.T_Can, 0, 0, 1, 1)

        self.Can_Lati = QLabel(self.widget_2)
        self.Can_Lati.setObjectName(u"Can_Lati")
        self.Can_Lati.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.Can_Lati, 1, 2, 1, 1)

        self.Can_Tem = QLabel(self.widget_2)
        self.Can_Tem.setObjectName(u"Can_Tem")
        self.Can_Tem.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.Can_Tem, 4, 2, 1, 1)

        self.Can_Long = QLabel(self.widget_2)
        self.Can_Long.setObjectName(u"Can_Long")
        self.Can_Long.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.Can_Long, 3, 2, 1, 1)

        self.Can_Alt = QLabel(self.widget_2)
        self.Can_Alt.setObjectName(u"Can_Alt")
        self.Can_Alt.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.Can_Alt, 2, 2, 1, 1)

        self.Roc_Long = QLabel(self.widget_2)
        self.Roc_Long.setObjectName(u"Roc_Long")
        self.Roc_Long.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.Roc_Long, 8, 2, 1, 1)

        self.Roc_Alt = QLabel(self.widget_2)
        self.Roc_Alt.setObjectName(u"Roc_Alt")
        self.Roc_Alt.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.Roc_Alt, 7, 2, 1, 1)

        self.Roc_Tem = QLabel(self.widget_2)
        self.Roc_Tem.setObjectName(u"Roc_Tem")
        self.Roc_Tem.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.Roc_Tem, 9, 2, 1, 1)

        self.T_Roc_Tem = QLabel(self.widget_2)
        self.T_Roc_Tem.setObjectName(u"T_Roc_Tem")
        self.T_Roc_Tem.setMaximumSize(QSize(100, 16777215))
        self.T_Roc_Tem.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.T_Roc_Tem, 9, 0, 1, 1)

        self.T_Can_Batt = QLabel(self.widget_2)
        self.T_Can_Batt.setObjectName(u"T_Can_Batt")
        self.T_Can_Batt.setMaximumSize(QSize(100, 16777215))
        self.T_Can_Batt.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.T_Can_Batt, 0, 1, 1, 1)

        self.Can_Batt = QProgressBar(self.widget_2)
        self.Can_Batt.setObjectName(u"Can_Batt")
        self.Can_Batt.setMinimumSize(QSize(120, 25))
        self.Can_Batt.setMaximumSize(QSize(120, 25))
        self.Can_Batt.setValue(24)
        self.Can_Batt.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Can_Batt.setTextVisible(True)

        self.gridLayout_4.addWidget(self.Can_Batt, 0, 2, 1, 1)

        self.T_Roc_Alt = QLabel(self.widget_2)
        self.T_Roc_Alt.setObjectName(u"T_Roc_Alt")
        self.T_Roc_Alt.setMaximumSize(QSize(100, 16777215))
        self.T_Roc_Alt.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.T_Roc_Alt, 7, 0, 1, 1)

        self.Roc_Lati = QLabel(self.widget_2)
        self.Roc_Lati.setObjectName(u"Roc_Lati")
        self.Roc_Lati.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.Roc_Lati, 6, 2, 1, 1)

        self.Roc_Alt_graph = PlotWidget(self.widget_2)
        self.Roc_Alt_graph.setObjectName(u"Roc_Alt_graph")
        self.Roc_Alt_graph.setMinimumSize(QSize(300, 150))

        self.gridLayout_4.addWidget(self.Roc_Alt_graph, 6, 0, 1, 2)

        self.Roc_Batt = QProgressBar(self.widget_2)
        self.Roc_Batt.setObjectName(u"Roc_Batt")
        self.Roc_Batt.setMinimumSize(QSize(120, 25))
        self.Roc_Batt.setMaximumSize(QSize(120, 25))
        self.Roc_Batt.setValue(24)
        self.Roc_Batt.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.Roc_Batt, 5, 2, 1, 1)

        self.T_Roc_Batt = QLabel(self.widget_2)
        self.T_Roc_Batt.setObjectName(u"T_Roc_Batt")
        self.T_Roc_Batt.setMaximumSize(QSize(100, 16777215))
        self.T_Roc_Batt.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_4.addWidget(self.T_Roc_Batt, 5, 1, 1, 1)

        self.T_Roc = QLabel(self.widget_2)
        self.T_Roc.setObjectName(u"T_Roc")
        self.T_Roc.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.T_Roc, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.port_box = QComboBox(self.widget)
        self.port_box.setObjectName(u"port_box")
        self.port_box.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.port_box, 2, 0, 1, 4)

        self.time = QLabel(self.widget)
        self.time.setObjectName(u"time")
        self.time.setMinimumSize(QSize(0, 80))
        self.time.setMaximumSize(QSize(16777215, 100))
        self.time.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.time, 0, 2, 1, 2)

        self.Baud_box = QComboBox(self.widget)
        self.Baud_box.setObjectName(u"Baud_box")
        self.Baud_box.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.Baud_box, 3, 0, 1, 4)

        self.elapsed = QLabel(self.widget)
        self.elapsed.setObjectName(u"elapsed")
        self.elapsed.setMinimumSize(QSize(0, 80))
        self.elapsed.setMaximumSize(QSize(16777215, 100))
        self.elapsed.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.elapsed, 1, 2, 1, 2)

        self.clear_bt = QPushButton(self.widget)
        self.clear_bt.setObjectName(u"clear_bt")
        self.clear_bt.setMinimumSize(QSize(0, 30))
        self.clear_bt.setStyleSheet(u"font: 25 12pt \"Yu Mincho Light\";")

        self.gridLayout_2.addWidget(self.clear_bt, 4, 1, 1, 1)

        self.refresh_bt = QPushButton(self.widget)
        self.refresh_bt.setObjectName(u"refresh_bt")
        self.refresh_bt.setMinimumSize(QSize(0, 30))
        self.refresh_bt.setStyleSheet(u"font: 25 12pt \"Yu Mincho Light\";")

        self.gridLayout_2.addWidget(self.refresh_bt, 4, 2, 1, 1)

        self.start_bt = QPushButton(self.widget)
        self.start_bt.setObjectName(u"start_bt")
        self.start_bt.setMinimumSize(QSize(0, 30))
        self.start_bt.setStyleSheet(u"font: 25 12pt \"Yu Mincho Light\";")

        self.gridLayout_2.addWidget(self.start_bt, 4, 0, 1, 1)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 100))
        self.widget_4.setMaximumSize(QSize(16777215, 100))
        self.T_file_name = QLabel(self.widget_4)
        self.T_file_name.setObjectName(u"T_file_name")
        self.T_file_name.setGeometry(QRect(10, 59, 121, 41))
        self.T_file_name.setMinimumSize(QSize(0, 0))
        self.comboBox = QComboBox(self.widget_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(0, 0, 201, 41))
        self.send_CMD_bt = QPushButton(self.widget_4)
        self.send_CMD_bt.setObjectName(u"send_CMD_bt")
        self.send_CMD_bt.setGeometry(QRect(210, 0, 111, 41))
        self.send_CMD_bt.setMinimumSize(QSize(0, 30))
        self.send_CMD_bt.setStyleSheet(u"font: 25 12pt \"Yu Mincho Light\";")
        self.file_name = QLabel(self.widget_4)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(130, 59, 201, 41))
        self.file_name.setMinimumSize(QSize(0, 0))
        self.file_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.widget_4, 5, 0, 1, 4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 50))
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.LOS = QLabel(self.widget_5)
        self.LOS.setObjectName(u"LOS")
        self.LOS.setMinimumSize(QSize(0, 80))
        self.LOS.setMaximumSize(QSize(16777215, 80))
        self.LOS.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")
        self.LOS.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.LOS, 6, 1, 1, 1)

        self.T_LOS = QLabel(self.widget_5)
        self.T_LOS.setObjectName(u"T_LOS")
        self.T_LOS.setMinimumSize(QSize(0, 80))
        self.T_LOS.setMaximumSize(QSize(16777215, 80))
        self.T_LOS.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_3.addWidget(self.T_LOS, 6, 0, 1, 1)

        self.T_Alt = QLabel(self.widget_5)
        self.T_Alt.setObjectName(u"T_Alt")
        self.T_Alt.setMinimumSize(QSize(0, 80))
        self.T_Alt.setMaximumSize(QSize(16777215, 80))
        self.T_Alt.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_3.addWidget(self.T_Alt, 4, 0, 1, 1)

        self.T_Lng = QLabel(self.widget_5)
        self.T_Lng.setObjectName(u"T_Lng")
        self.T_Lng.setMinimumSize(QSize(0, 80))
        self.T_Lng.setMaximumSize(QSize(16777215, 80))
        self.T_Lng.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_3.addWidget(self.T_Lng, 3, 0, 1, 1)

        self.T_Lat = QLabel(self.widget_5)
        self.T_Lat.setObjectName(u"T_Lat")
        self.T_Lat.setMinimumSize(QSize(0, 80))
        self.T_Lat.setMaximumSize(QSize(16777215, 80))
        self.T_Lat.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_3.addWidget(self.T_Lat, 2, 0, 1, 1)

        self.T_GS_posi_Alt = QLabel(self.widget_5)
        self.T_GS_posi_Alt.setObjectName(u"T_GS_posi_Alt")
        self.T_GS_posi_Alt.setMinimumSize(QSize(0, 80))
        self.T_GS_posi_Alt.setMaximumSize(QSize(16777215, 80))
        self.T_GS_posi_Alt.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_3.addWidget(self.T_GS_posi_Alt, 7, 0, 1, 1)

        self.T_GD = QLabel(self.widget_5)
        self.T_GD.setObjectName(u"T_GD")
        self.T_GD.setMinimumSize(QSize(0, 80))
        self.T_GD.setMaximumSize(QSize(16777215, 80))
        self.T_GD.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_3.addWidget(self.T_GD, 5, 0, 1, 1)

        self.Alt = QLabel(self.widget_5)
        self.Alt.setObjectName(u"Alt")
        self.Alt.setMinimumSize(QSize(0, 80))
        self.Alt.setMaximumSize(QSize(16777215, 80))
        self.Alt.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")
        self.Alt.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Alt, 4, 1, 1, 1)

        self.GS_posi_Alt = QLabel(self.widget_5)
        self.GS_posi_Alt.setObjectName(u"GS_posi_Alt")
        self.GS_posi_Alt.setMinimumSize(QSize(0, 80))
        self.GS_posi_Alt.setMaximumSize(QSize(16777215, 80))
        self.GS_posi_Alt.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")
        self.GS_posi_Alt.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.GS_posi_Alt, 7, 1, 1, 1)

        self.GD = QLabel(self.widget_5)
        self.GD.setObjectName(u"GD")
        self.GD.setMinimumSize(QSize(0, 80))
        self.GD.setMaximumSize(QSize(16777215, 80))
        self.GD.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")
        self.GD.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.GD, 5, 1, 1, 1)

        self.Ele = QLabel(self.widget_5)
        self.Ele.setObjectName(u"Ele")
        self.Ele.setMinimumSize(QSize(0, 80))
        self.Ele.setMaximumSize(QSize(16777215, 80))
        self.Ele.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")
        self.Ele.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Ele, 1, 1, 1, 1)

        self.Lng = QLabel(self.widget_5)
        self.Lng.setObjectName(u"Lng")
        self.Lng.setMinimumSize(QSize(0, 80))
        self.Lng.setMaximumSize(QSize(16777215, 80))
        self.Lng.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")
        self.Lng.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Lng, 3, 1, 1, 1)

        self.Lat = QLabel(self.widget_5)
        self.Lat.setObjectName(u"Lat")
        self.Lat.setMinimumSize(QSize(0, 80))
        self.Lat.setMaximumSize(QSize(16777215, 80))
        self.Lat.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")
        self.Lat.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Lat, 2, 1, 1, 1)

        self.T_Ele = QLabel(self.widget_5)
        self.T_Ele.setObjectName(u"T_Ele")
        self.T_Ele.setMinimumSize(QSize(0, 80))
        self.T_Ele.setMaximumSize(QSize(16777215, 80))
        self.T_Ele.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_3.addWidget(self.T_Ele, 1, 0, 1, 1)

        self.Azi = QLabel(self.widget_5)
        self.Azi.setObjectName(u"Azi")
        self.Azi.setMinimumSize(QSize(0, 80))
        self.Azi.setMaximumSize(QSize(16777215, 80))
        self.Azi.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")
        self.Azi.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Azi, 0, 1, 1, 1)

        self.T_Azi = QLabel(self.widget_5)
        self.T_Azi.setObjectName(u"T_Azi")
        self.T_Azi.setMinimumSize(QSize(0, 80))
        self.T_Azi.setMaximumSize(QSize(16777215, 80))
        self.T_Azi.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";")

        self.gridLayout_3.addWidget(self.T_Azi, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_5, 6, 0, 1, 4)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"image: url(:/newPrefix/logo.png);\n"
"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 2, 2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.T_Can_Humid.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.T_Can_rotat.setText(QCoreApplication.translate("MainWindow", u"Rotation rate", None))
        self.T_C_R_peek.setText(QCoreApplication.translate("MainWindow", u"Peek Alt", None))
        self.T_C_R_posi.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.T_Can_PKG.setText(QCoreApplication.translate("MainWindow", u"PKG count", None))
        self.T_Can_2.setText(QCoreApplication.translate("MainWindow", u"CanSat", None))
        self.T_Can_ACCX.setText(QCoreApplication.translate("MainWindow", u"ACCX", None))
        self.Can_ACCX.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Roc_ACCX.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Can_ACCY.setText(QCoreApplication.translate("MainWindow", u"ACCY", None))
        self.T_Roc_ACCX.setText(QCoreApplication.translate("MainWindow", u"ACCX", None))
        self.Can_ACCY.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Roc_PKG.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Roc_PKG.setText(QCoreApplication.translate("MainWindow", u"PKG count", None))
        self.T_Roc_ACCY.setText(QCoreApplication.translate("MainWindow", u"ACCY", None))
        self.T_Can_ACCZ.setText(QCoreApplication.translate("MainWindow", u"ACCZ", None))
        self.T_Roc_ACCZ.setText(QCoreApplication.translate("MainWindow", u"ACCZ", None))
        self.Roc_ACCZ.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Can_GYRX.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Can_GYRX.setText(QCoreApplication.translate("MainWindow", u"GYRX", None))
        self.Roc_ACCY.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Can_ACCZ.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Can_GYRY.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Roc_GYRY.setText(QCoreApplication.translate("MainWindow", u"GYRY", None))
        self.T_Roc_GYRX.setText(QCoreApplication.translate("MainWindow", u"GYRX", None))
        self.Roc_GYRX.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Can_GYRY.setText(QCoreApplication.translate("MainWindow", u"GYRY", None))
        self.Roc_GYRY.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Roc_GYRZ.setText(QCoreApplication.translate("MainWindow", u"GYRZ", None))
        self.Roc_GYRZ.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Can_GYRZ.setText(QCoreApplication.translate("MainWindow", u"GYRZ", None))
        self.Can_GYRZ.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Can_PKG.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Roc_2.setText(QCoreApplication.translate("MainWindow", u"Rocket", None))
        self.Can_rotat.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C_R_peek.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C_R_posi.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Can_Humid.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Can_Tem.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.T_Can_Alt.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.T_Can.setText(QCoreApplication.translate("MainWindow", u"CanSat", None))
        self.Can_Lati.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.Can_Tem.setText(QCoreApplication.translate("MainWindow", u"0.0000000", None))
        self.Can_Long.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.Can_Alt.setText(QCoreApplication.translate("MainWindow", u"0.0000000", None))
        self.Roc_Long.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.Roc_Alt.setText(QCoreApplication.translate("MainWindow", u"0.0000000", None))
        self.Roc_Tem.setText(QCoreApplication.translate("MainWindow", u"0.0000000", None))
        self.T_Roc_Tem.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.T_Can_Batt.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.T_Roc_Alt.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.Roc_Lati.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.T_Roc_Batt.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.T_Roc.setText(QCoreApplication.translate("MainWindow", u"Rocket", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.elapsed.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.clear_bt.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.refresh_bt.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.start_bt.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.T_file_name.setText(QCoreApplication.translate("MainWindow", u"File name :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CMDCX,ON$", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CMDCX,OFF$", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CMDSP1,ON$", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"CMDSP2,ON$", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"CMDSP1,OFF$", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"CMDSP2,OFF$", None))

        self.send_CMD_bt.setText(QCoreApplication.translate("MainWindow", u"Send CMD", None))
        self.file_name.setText(QCoreApplication.translate("MainWindow", u"???", None))
        self.LOS.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_LOS.setText(QCoreApplication.translate("MainWindow", u"Line of sight", None))
        self.T_Alt.setText(QCoreApplication.translate("MainWindow", u"ALT", None))
        self.T_Lng.setText(QCoreApplication.translate("MainWindow", u"LNG", None))
        self.T_Lat.setText(QCoreApplication.translate("MainWindow", u"LAT", None))
        self.T_GS_posi_Alt.setText(QCoreApplication.translate("MainWindow", u"GS position and Alt", None))
        self.T_GD.setText(QCoreApplication.translate("MainWindow", u"Ground distance", None))
        self.Alt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.GS_posi_Alt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.GD.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Ele.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Lng.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Lat.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Ele.setText(QCoreApplication.translate("MainWindow", u"ELEVATION", None))
        self.Azi.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_Azi.setText(QCoreApplication.translate("MainWindow", u"AZIMUTH", None))
    # retranslateUi

