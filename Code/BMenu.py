

#  Created by "AmaniTech" 

from PyQt5 import QtCore, QtGui, QtWidgets
import images 
import sys


class Ui_Beranda(object):

        def tombol_edit(self):
                from BEdit import Ui_edit_data
                self.window_menu = QtWidgets.QMainWindow()
                self.ui = Ui_edit_data()
                self.ui.setupUi(self.window_menu)
                self.window_menu.show()
        
        def tombol_booking(self):
                from BBooking import Ui_sewa
                self.window_menu = QtWidgets.QMainWindow()
                self.ui = Ui_sewa()
                self.ui.setupUi(self.window_menu)
                self.window_menu.show()

        def tombol_exit(self):
                sys.exit()

        def tombol_about(self):
                from BAbout import Ui_about
                self.window_menu = QtWidgets.QMainWindow()
                self.ui = Ui_about()
                self.ui.setupUi(self.window_menu)
                self.window_menu.show()
        
        def tombol_list(self):
                from BList import Ui_List
                self.window_menu = QtWidgets.QMainWindow()
                self.ui = Ui_List()
                self.ui.setupUi(self.window_menu)
                self.window_menu.show()

        def setupUi(self, Beranda):
                Beranda.setObjectName("Beranda")
                Beranda.resize(1018, 653)
                Beranda.setStyleSheet("")
                self.centralwidget = QtWidgets.QWidget(Beranda)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(340, 80, 91, 91))
                self.label.setStyleSheet("image: url(:/LAPBAS/04283530121635article-icon.png);\n"
"background-color: rgb(0,0,0,0);")
                self.label.setText("")
                self.label.setObjectName("label")
                self.toolButton = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton.setGeometry(QtCore.QRect(390, 110, 291, 91))
                font = QtGui.QFont()
                font.setFamily("Brush Script MT")
                font.setPointSize(28)
                font.setBold(False)
                font.setWeight(50)
                self.toolButton.setFont(font)
                self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton.setStyleSheet("QToolButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0,0,0,0);\n"
"border : 3px solid rgb(0, 159, 159);\n"
"border-radius : 20px\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QToolButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"background-color:  rgb(0, 227, 227);\n"
"border : 3px solid rgb(0, 227, 227);\n"
"border-radius : 20px\n"
"}\n"
"")
                self.toolButton.setObjectName("toolButton")
                self.toolButton.clicked.connect(self.tombol_booking)#####################
                self.toolButton.clicked.connect(Beranda.close)
                
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(50, 230, 131, 131))
                self.label_2.setStyleSheet("\n"
"background-color: rgb(0,0,0,0);")
                self.label_2.setText("")
                self.label_2.setPixmap(QtGui.QPixmap(":/LAPBAS/icons8-list-100.png"))
                self.label_2.setScaledContents(True)
                self.label_2.setObjectName("label_2")
                self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton_2.setGeometry(QtCore.QRect(120, 280, 291, 91))
                font = QtGui.QFont()
                font.setFamily("Brush Script MT")
                font.setPointSize(28)
                font.setBold(False)
                font.setWeight(50)
                self.toolButton_2.setFont(font)
                self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton_2.setStyleSheet("QToolButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(0,0,0,0);\n"
"border : 3px solid  rgb(82, 190, 160);\n"
"border-radius : 20px}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QToolButton:hover{\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(104, 240, 201);\n"
"border : 3px solid rgb(104, 240, 201);\n"
"border-radius : 20px\n"
"\n"
"}\n"
"")
                self.toolButton_2.setObjectName("toolButton_2")
                self.toolButton_2.clicked.connect(self.tombol_list)#####################################
                self.toolButton_2.clicked.connect(Beranda.close)

                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(630, 250, 91, 91))
                self.label_3.setStyleSheet("background-color: rgb(0,0,0,0);")
                self.label_3.setText("")
                self.label_3.setPixmap(QtGui.QPixmap(":/LAPBAS/user.png"))
                self.label_3.setScaledContents(True)
                self.label_3.setObjectName("label_3")
                self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton_3.setGeometry(QtCore.QRect(690, 280, 291, 91))
                font = QtGui.QFont()
                font.setFamily("Brush Script MT")
                font.setPointSize(28)
                font.setBold(False)
                font.setWeight(50)
                self.toolButton_3.setFont(font)
                self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton_3.setStyleSheet("\n"
"\n"
"QToolButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(0,0,0,0);\n"
"border : 3px solid  rgb(26, 136, 217);\n"
"border-radius : 20px\n"
"}\n"
"\n"
"\n"
"QToolButton:hover{\n"
"color: rgb(0,0,0);\n"
"background-color:rgb(31, 162, 255);\n"
"border : 3px solid rgb(31, 162, 255);\n"
"border-radius : 20px\n"
"}\n"
"")
                self.toolButton_3.setObjectName("toolButton_3")
                self.toolButton_3.clicked.connect(self.tombol_about)########################
                self.toolButton_3.clicked.connect(Beranda.close)

                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(30, 570, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(22)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("background-color: rgb(0, 0, 0,0);")
                self.label_4.setText("")
                self.label_4.setPixmap(QtGui.QPixmap(":/LAPBAS/logging-out-2355227_960_720.webp"))
                self.label_4.setScaledContents(True)
                self.label_4.setObjectName("label_4")
                self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton_4.setGeometry(QtCore.QRect(70, 580, 141, 51))
                font = QtGui.QFont()
                font.setFamily("Brush Script MT")
                font.setPointSize(22)
                font.setBold(False)
                font.setWeight(50)
                self.toolButton_4.setFont(font)
                self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton_4.setStyleSheet("\n"
"\n"
"QToolButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(0,0,0,0);\n"
"border : 3px solid rgb(28, 138, 219);\n"
"border-radius : 20px\n"
"}\n"
"\n"
"\n"
"QToolButton:hover{\n"
"color: rgb(0,0,0);\n"
"background-color:rgb(23, 112, 176);\n"
"border : 3px solid rgb(23, 112, 176);\n"
"border-radius : 20px\n"
"}\n"
"")
                self.toolButton_4.setObjectName("toolButton_4")
                self.toolButton_4.clicked.connect(self.tombol_exit)################
                self.toolButton_4.clicked.connect(Beranda.close)

                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(-10, -20, 1051, 681))
                self.label_5.setText("")
                self.label_5.setPixmap(QtGui.QPixmap(":/LAPBAS/Bola-Basket.jpg"))
                self.label_5.setScaledContents(True)
                self.label_5.setObjectName("label_5")
                self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton_5.setGeometry(QtCore.QRect(810, 580, 141, 51))
                font = QtGui.QFont()
                font.setFamily("Brush Script MT")
                font.setPointSize(22)
                font.setBold(False)
                font.setWeight(50)
                self.toolButton_5.setFont(font)
                self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton_5.setStyleSheet("\n"
"\n"
"QToolButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(0,0,0,0);\n"
"border : 3px solid rgb(255, 214, 252);\n"
"border-radius : 20px\n"
"}\n"
"\n"
"\n"
"QToolButton:hover{\n"
"color: rgb(0,0,0);\n"
"background-color:rgb(199, 83, 255);\n"
"border : 3px solid rgb(199, 83, 255);\n"
"border-radius : 20px\n"
"}\n"
"")
                self.toolButton_5.setObjectName("toolButton_5")
                self.toolButton_5.clicked.connect(self.tombol_edit)########################
                self.toolButton_5.clicked.connect(Beranda.close)
                
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(920, 570, 71, 71))
                font = QtGui.QFont()
                font.setPointSize(22)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("background-color: rgb(0, 0, 0,0);")
                self.label_6.setText("")
                self.label_6.setPixmap(QtGui.QPixmap(":/LAPBAS/bill.png"))
                self.label_6.setScaledContents(True)
                self.label_6.setObjectName("label_6")
                self.label_5.raise_()
                self.toolButton_4.raise_()
                self.label_4.raise_()
                self.toolButton_3.raise_()
                self.toolButton_2.raise_()
                self.toolButton.raise_()
                self.label.raise_()
                self.label_2.raise_()
                self.label_3.raise_()
                self.toolButton_5.raise_()
                self.label_6.raise_()
                Beranda.setCentralWidget(self.centralwidget)

                self.retranslateUi(Beranda)
                QtCore.QMetaObject.connectSlotsByName(Beranda)

        def retranslateUi(self, Beranda):
                _translate = QtCore.QCoreApplication.translate
                Beranda.setWindowTitle(_translate("Beranda", "Beranda"))
                self.toolButton.setText(_translate("Beranda", "Booking"))
                self.toolButton_2.setText(_translate("Beranda", "List"))
                self.toolButton_3.setText(_translate("Beranda", "About"))
                self.toolButton_4.setText(_translate("Beranda", "Exit"))
                self.toolButton_5.setText(_translate("Beranda", "Edit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Beranda = QtWidgets.QMainWindow()
    ui = Ui_Beranda()
    ui.setupUi(Beranda)
    Beranda.show()
    sys.exit(app.exec_())
