

#  Created by "AmaniTech" 

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import images
import pymysql


class Ui_SIGNUP(object):
        def kotak_pesan(self, judul, pesan):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle(judul)
                msg.setText(pesan)
                msg.exec_()
        def tombol_signup(self):
                nama_lengkap = self.input_nama.text()
                username = self.input_username.text()
                email = self.input_email.text()
                password = self.input_password.text()
                lahir = self.tanggal_lahir.text()

                try : 
                        insert = (username , nama_lengkap, lahir, password, email )

                        database = pymysql.connect(
                                host = "localhost",
                                user = "root",
                                password = "",
                                db = "aplikasi_lapanganbasket",
                                port = 3306,
                                autocommit = True)

                        c = database.cursor()
                        sql = "insert into tblogin (`username`, `nama_lengkap`, `tanggal_lahir`, `password`, `email`) values" + str(insert)
                        user = c.execute(sql)

                        if (user) : 
                                self.kotak_pesan("INFO", "Data berhasil disimpan")
                                #################################################
                                
                                self.input_nama.setText("")
                                self.input_username.setText("")
                                self.input_email.setText("")
                                self.input_password.setText("")
                                self.tanggal_lahir.setTime(QTime(0,0,0))
                                
                        else : 
                                self.kotak_pesan("INFO", "Gagal menyimpan data")
                                #################################################
                                
                                self.input_nama.setText("")
                                self.input_username.setText("")
                                self.input_email.setText("")
                                self.input_password.setText("")
                                self.tanggal_lahir.setTime(QTime(0,0,0))

                except ValueError:
                        self.kotak_pesan("INFO", "Data yang anda masukkan salah , mohon diperiksa kembali")
                        ###################################################################################
                         
                        self.input_nama.setText("")
                        self.input_username.setText("")
                        self.input_email.setText("")
                        self.input_password.setText("")
                        self.tanggal_lahir.setTime(QTime(0,0,0))


        
        def setupUi(self, SIGNUP):
                SIGNUP.setObjectName("SIGNUP")
                SIGNUP.resize(830, 585)
                self.centralwidget = QtWidgets.QWidget(SIGNUP)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(0, 0, 841, 621))
                self.label.setStyleSheet("background-image: url(:/LAPBAS/8C9445325-michael-jordan-basketball-court.fit-2000w.jpg);")
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap(":/LAPBAS/DEPORTES-basquet.jpg"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(120, 90, 611, 461))
                self.frame.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.login_button_2 = QtWidgets.QPushButton(self.frame)
                self.login_button_2.setGeometry(QtCore.QRect(260, 410, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.login_button_2.setFont(font)
                self.login_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.login_button_2.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"color:black;\n"
"border-radius:14px;\n"
"background:WHITE;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"\n"
"{\n"
"color:white;\n"
"border-radius: 14px;\n"
"background:SILVER;\n"
"\n"
"}")
                self.login_button_2.setObjectName("login_button_2")
                self.login_button_2.clicked.connect(self.tombol_signup)####################
                
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(20, 10, 191, 51))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(17)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
                self.label_3.setObjectName("label_3")
                self.label_5 = QtWidgets.QLabel(self.frame)
                self.label_5.setGeometry(QtCore.QRect(70, 60, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.frame)
                self.label_6.setGeometry(QtCore.QRect(70, 130, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.frame)
                self.label_7.setGeometry(QtCore.QRect(70, 270, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.label_7.setFont(font)
                self.label_7.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(self.frame)
                self.label_8.setGeometry(QtCore.QRect(70, 200, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.label_8.setFont(font)
                self.label_8.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(self.frame)
                self.label_9.setGeometry(QtCore.QRect(70, 340, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.label_9.setFont(font)
                self.label_9.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
                self.label_9.setObjectName("label_9")
                self.input_nama = QtWidgets.QLineEdit(self.frame)
                self.input_nama.setGeometry(QtCore.QRect(70, 90, 331, 31))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.input_nama.setFont(font)
                self.input_nama.setStyleSheet("color: rgb(255, 255, 255);")
                self.input_nama.setText("")
                self.input_nama.setObjectName("input_nama")
                self.input_username = QtWidgets.QLineEdit(self.frame)
                self.input_username.setGeometry(QtCore.QRect(70, 160, 331, 31))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.input_username.setFont(font)
                self.input_username.setStyleSheet("color: rgb(255, 255, 255);")
                self.input_username.setText("")
                self.input_username.setObjectName("input_username")
                self.input_email = QtWidgets.QLineEdit(self.frame)
                self.input_email.setGeometry(QtCore.QRect(70, 230, 331, 31))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.input_email.setFont(font)
                self.input_email.setStyleSheet("color: rgb(255, 255, 255);")
                self.input_email.setText("")
                self.input_email.setObjectName("input_email")
                self.input_password = QtWidgets.QLineEdit(self.frame)
                self.input_password.setGeometry(QtCore.QRect(70, 300, 331, 31))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.input_password.setFont(font)
                self.input_password.setStyleSheet("color:rgb(255, 255, 255)")
                self.input_password.setText("")
                self.input_password.setObjectName("input_password")
                self.tanggal_lahir = QtWidgets.QDateEdit(self.frame)
                self.tanggal_lahir.setGeometry(QtCore.QRect(70, 370, 110, 22))
                self.tanggal_lahir.setStyleSheet("color: rgb(255, 255, 255);")
                self.tanggal_lahir.setObjectName("tanggal_lahir")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(400, 50, 61, 61))
                self.label_4.setText("")
                self.label_4.setPixmap(QtGui.QPixmap(":/LAPBAS/round-account-button-with-user-inside.png"))
                self.label_4.setScaledContents(True)
                self.label_4.setObjectName("label_4")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(390, 40, 81, 81))
                self.pushButton.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"\n"
"    background-color: rgb(85, 85, 85);\n"
"border-radius:40px;\n"
"\n"
"}")
                self.pushButton.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/lapbas/C:/Users/HP/Downloads/round-account-button-with-user-inside.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton.setIcon(icon)
                self.pushButton.setIconSize(QtCore.QSize(100, 100))
                self.pushButton.setObjectName("pushButton")
                self.icon_gerbang = QtWidgets.QPushButton(self.centralwidget)
                self.icon_gerbang.setGeometry(QtCore.QRect(30, 30, 51, 51))
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
                
                self.icon_gerbang.clicked.connect(SIGNUP.close)

                self.label.raise_()
                self.pushButton.raise_()
                self.frame.raise_()
                self.label_4.raise_()
                self.icon_gerbang.raise_()
                SIGNUP.setCentralWidget(self.centralwidget)

                self.retranslateUi(SIGNUP)
                QtCore.QMetaObject.connectSlotsByName(SIGNUP)

        def retranslateUi(self, SIGNUP):
                _translate = QtCore.QCoreApplication.translate
                SIGNUP.setWindowTitle(_translate("SIGNUP", "SIGN UP"))
                self.login_button_2.setText(_translate("SIGNUP", "LOGIN"))
                self.label_3.setText(_translate("SIGNUP", " SIGN UP"))
                self.label_5.setText(_translate("SIGNUP", "NAMA  LENGKAP"))
                self.label_6.setText(_translate("SIGNUP", "USERNAME"))
                self.label_7.setText(_translate("SIGNUP", "PASSWORD"))
                self.label_8.setText(_translate("SIGNUP", "EMAIL"))
                self.label_9.setText(_translate("SIGNUP", "TANGGAL LAHIR"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SIGNUP = QtWidgets.QMainWindow()
    ui = Ui_SIGNUP()
    ui.setupUi(SIGNUP)
    SIGNUP.show()
    sys.exit(app.exec_())
