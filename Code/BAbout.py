

#  Created by "AmaniTech" 

from PyQt5 import QtCore, QtGui, QtWidgets
import images


class Ui_about(object):

    def tombol_gerbang(self):
        from BMenu import Ui_Beranda
        self.window_about = QtWidgets.QMainWindow()
        self.ui = Ui_Beranda()
        self.ui.setupUi(self.window_about)
        self.window_about.show()

    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(971, 584)
        self.centralwidget = QtWidgets.QWidget(about)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 991, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/LAPBAS/barthelemy-de-mazenod-bbIrw_Phz9g-unsplash-1030x683.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 10, 451, 551))
        self.label_2.setStyleSheet("background-color: rgb(74, 74, 74);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 30, 91, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/LAPBAS/user.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 150, 431, 331))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.icon_gerbang = QtWidgets.QPushButton(self.centralwidget)
        self.icon_gerbang.setGeometry(QtCore.QRect(40, 30, 61, 51))
        self.icon_gerbang.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_gerbang.setMouseTracking(False)
        self.icon_gerbang.setTabletTracking(False)
        self.icon_gerbang.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    image: url(:/LAPBAS/logging-out-2355227_960_720.webp);\n"
"\n"
"background-color: rgb(0,0,0,0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"\n"
"{\n"
"image: url(:/LAPBAS/logging-out-2355227_960_720.webp);\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.icon_gerbang.setText("")
        self.icon_gerbang.setAutoDefault(False)
        self.icon_gerbang.setFlat(False)
        self.icon_gerbang.setObjectName("icon_gerbang")
        self.icon_gerbang.clicked.connect(self.tombol_gerbang)###############
        self.icon_gerbang.clicked.connect(about.close)

        about.setCentralWidget(self.centralwidget)

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "ABOUT"))
        self.label_4.setText(_translate("about", "Programmer"))
        self.label_5.setText(_translate("about", "<html><head/><body><p align=\"center\">@AmaniTech</p><p align=\"center\"><span style=\" font-size:12pt;\">Lekok - Pasuruan</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about = QtWidgets.QMainWindow()
    ui = Ui_about()
    ui.setupUi(about)
    about.show()
    sys.exit(app.exec_())
