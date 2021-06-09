

#  Created by "AmaniTech" 

#from PyQt5 import QtCore, QtGui, QtWidgets, QTime
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import images
from random import randint
import pymysql



class Ui_sewa(object):
        def kotak_pesan(self, judul, pesan):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle(judul)
                msg.setText(pesan)
                msg.exec_()

        def tombol_nomorid(self):

                random = randint(1,999999999999)

                id_r = self.textBrowser.setText(str(random))

                database = pymysql.connect(
                     host = "localhost",
                     user = "root",
                     password = "",
                     port = 3306,
                     db = "aplikasi_lapanganbasket",
                     autocommit = True)

                a = database.cursor()
                sql = "select * from tbbooking " 
                user = a.execute(sql)
                data = a.fetchall()

                if (data) == id_r :
                        self.kotak_pesan("INFO", "No.Id sudah ada, Mohon coba lagi")
                          
        
        def tombol_masukkan(self):
                id_r = self.textBrowser.toPlainText()
                tanggal = self.dateEdit.text()
                pilihan = self.comboBox.currentText()
                nama_club = self.lineEdit.text()
                asal_club = self.lineEdit_2.text()
                captain = self.lineEdit_3.text()
                nohp = self.lineEdit_4.text()
                banyak_pemain = self.spinBox.value()
                waktu_awal = self.timeEdit.text()
                waktu_akhir = self.timeEdit_2.text()
                keterangan = self.plainTextEdit_2.toPlainText()

                try : 
                        insert = (int(id_r), tanggal, pilihan, nama_club, asal_club, captain, int(nohp), int(banyak_pemain), waktu_awal, waktu_akhir, keterangan)

                        database = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        port = 3306,
                        db = "aplikasi_lapanganbasket",
                        autocommit = True)

                        b = database.cursor()
                        sql = "insert into tbbooking (`no_id`, `tanggal`, `pilihan`, `nama_club`, `asal_club`, `captain`, `no_hp`,`banyak_pemain`, `waktu_mulai`, `waktu_akhir`, `keterangan`) values" + str(insert)
                        user = b.execute(sql)
                        
                        if (user) :
                                self.kotak_pesan("INFO", "Berhasil menyimpan data")
                        else : 
                                self.kotak_pesan("INFO", "Data gagal disimpan")

                except ValueError: 
                        self.kotak_pesan("INFO", "Data yang anda masukkan salah, mohon diperiksa kembali")

        
        def reset_all(self):       
                self.textBrowser.setPlainText("")
                self.dateEdit.setDate(QDate(2000,1,1))
                self.comboBox.setCurrentText("")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                self.timeEdit.setTime(QTime(0,0))
                self.timeEdit_2.setTime(QTime(0,0))
                self.plainTextEdit_2.setPlainText("")
                self.spinBox.setValue(0)

        def tombol_gerbang(self):
                from BMenu import Ui_Beranda
                self.window_about = QtWidgets.QMainWindow()
                self.ui = Ui_Beranda()
                self.ui.setupUi(self.window_about)
                self.window_about.show()

        def setupUi(self, sewa):
                sewa.setObjectName("sewa")
                sewa.resize(875, 618)
                self.centralwidget = QtWidgets.QWidget(sewa)
                self.centralwidget.setObjectName("centralwidget")
                self.save = QtWidgets.QToolButton(self.centralwidget)
                self.save.setGeometry(QtCore.QRect(700, 300, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                font.setWeight(75)
                self.save.setFont(font)
                self.save.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"color:black;\n"
"border-radius:11px;\n"
"background-color: rgb(208, 208, 208);\n"
"\n"
"}\n"
"\n"
"QToolButton:hover\n"
"\n"
"{\n"
"color:white;\n"
"border-radius: 11px;\n"
"    background-color: rgb(162, 162, 162);\n"
"\n"
"}\n"
"")
                self.save.setObjectName("save")
                self.save.clicked.connect(self.tombol_masukkan)###################################
                self.save.clicked.connect(self.reset_all)

                self.icon_gerbang = QtWidgets.QPushButton(self.centralwidget)
                self.icon_gerbang.setGeometry(QtCore.QRect(20, 20, 51, 51))
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
                self.icon_gerbang.clicked.connect(self.tombol_gerbang)###########################
                self.icon_gerbang.clicked.connect(sewa.close)
                
                self.comboBox = QtWidgets.QComboBox(self.centralwidget)
                self.comboBox.setGeometry(QtCore.QRect(510, 140, 141, 32))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.comboBox.setFont(font)
                self.comboBox.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.comboBox.setPlaceholderText("")
                self.comboBox.setDuplicatesEnabled(False)
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.setItemText(0, "")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(230, 190, 421, 32))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.lineEdit.setObjectName("lineEdit")
                self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
                self.timeEdit.setGeometry(QtCore.QRect(230, 390, 118, 32))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.timeEdit.setFont(font)
                self.timeEdit.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.timeEdit.setObjectName("timeEdit")
                self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
                self.timeEdit_2.setGeometry(QtCore.QRect(440, 390, 118, 32))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.timeEdit_2.setFont(font)
                self.timeEdit_2.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.timeEdit_2.setObjectName("timeEdit_2")
                self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
                self.plainTextEdit_2.setGeometry(QtCore.QRect(230, 440, 421, 131))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.plainTextEdit_2.setFont(font)
                self.plainTextEdit_2.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px ; \n"
"border-top:1px solid rgb(140, 140, 140);\n"
"border-left:1px solid rgb(140, 140, 140);\n"
"border-right:1px solid rgb(140, 140, 140);\n"
"color: rgb(255, 255, 255);\n"
"")
                self.plainTextEdit_2.setObjectName("plainTextEdit_2")
                self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
                self.spinBox.setGeometry(QtCore.QRect(610, 340, 42, 32))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.spinBox.setFont(font)
                self.spinBox.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.spinBox.setObjectName("spinBox")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(100, 140, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("color: rgb(255, 255, 255);")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(100, 190, 91, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(100, 240, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(100, 290, 111, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(410, 150, 91, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(100, 390, 91, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(100, 440, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_7.setFont(font)
                self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(370, 390, 61, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_8.setFont(font)
                self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(100, 340, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_9.setFont(font)
                self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_9.setObjectName("label_9")
                self.label_10 = QtWidgets.QLabel(self.centralwidget)
                self.label_10.setGeometry(QtCore.QRect(480, 340, 111, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_10.setFont(font)
                self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_10.setObjectName("label_10")
                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(-10, -10, 901, 651))
                self.label_11.setText("")
                self.label_11.setPixmap(QtGui.QPixmap(":/LAPBAS/black-doff-wallpaper-33.jpg"))
                self.label_11.setScaledContents(True)
                self.label_11.setObjectName("label_11")
                self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser.setGeometry(QtCore.QRect(230, 140, 181, 31))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(11)
                self.textBrowser.setFont(font)
                self.textBrowser.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.textBrowser.setObjectName("textBrowser")
                self.save_2 = QtWidgets.QToolButton(self.centralwidget)
                self.save_2.setGeometry(QtCore.QRect(700, 180, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                font.setWeight(75)
                self.save_2.setFont(font)
                self.save_2.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"color:black;\n"
"border-radius:11px;\n"
"background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"\n"
"QToolButton:hover\n"
"\n"
"{\n"
"color:white;\n"
"border-radius: 11px;\n"
"    background-color: rgb(162, 162, 162);\n"
"\n"
"}\n"
"")
                self.save_2.setObjectName("save_2")
                self.save_2.clicked.connect(self.tombol_nomorid)###########################

                self.label_12 = QtWidgets.QLabel(self.centralwidget)
                self.label_12.setGeometry(QtCore.QRect(710, 220, 141, 21))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_12.setFont(font)
                self.label_12.setStyleSheet("color: rgb(214, 214, 214);")
                self.label_12.setObjectName("label_12")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_2.setGeometry(QtCore.QRect(230, 240, 421, 32))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.lineEdit_2.setFont(font)
                self.lineEdit_2.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_3.setGeometry(QtCore.QRect(230, 290, 421, 32))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.lineEdit_3.setFont(font)
                self.lineEdit_3.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_4.setGeometry(QtCore.QRect(230, 340, 241, 32))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.lineEdit_4.setFont(font)
                self.lineEdit_4.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.lineEdit_4.setObjectName("lineEdit_4")
                self.label_13 = QtWidgets.QLabel(self.centralwidget)
                self.label_13.setGeometry(QtCore.QRect(350, 30, 231, 91))
                font = QtGui.QFont()
                font.setFamily("Brush Script MT")
                font.setPointSize(50)
                self.label_13.setFont(font)
                self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_13.setObjectName("label_13")
                self.label_14 = QtWidgets.QLabel(self.centralwidget)
                self.label_14.setGeometry(QtCore.QRect(720, 420, 111, 121))
                self.label_14.setStyleSheet("image: url(:/LAPBAS/1.jpg);\n"
"\n"
"")
                self.label_14.setText("")
                self.label_14.setObjectName("label_14")
                self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
                self.dateEdit.setGeometry(QtCore.QRect(740, 70, 110, 22))
                self.dateEdit.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"border-top:1px solid rgb(140, 140, 140);\n"
"border-left:1px solid rgb(140, 140, 140);\n"
"border-right:1px solid rgb(140, 140, 140);\n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.dateEdit.setObjectName("dateEdit")
                self.label_15 = QtWidgets.QLabel(self.centralwidget)
                self.label_15.setGeometry(QtCore.QRect(760, 40, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Brush Script MT")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_15.setFont(font)
                self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_15.setObjectName("label_15")
                self.label_11.raise_()
                self.save.raise_()
                self.icon_gerbang.raise_()
                self.comboBox.raise_()
                self.lineEdit.raise_()
                self.timeEdit.raise_()
                self.timeEdit_2.raise_()
                self.plainTextEdit_2.raise_()
                self.spinBox.raise_()
                self.label.raise_()
                self.label_2.raise_()
                self.label_3.raise_()
                self.label_4.raise_()
                self.label_5.raise_()
                self.label_6.raise_()
                self.label_7.raise_()
                self.label_8.raise_()
                self.label_9.raise_()
                self.label_10.raise_()
                self.textBrowser.raise_()
                self.save_2.raise_()
                self.label_12.raise_()
                self.lineEdit_2.raise_()
                self.lineEdit_3.raise_()
                self.lineEdit_4.raise_()
                self.label_13.raise_()
                self.label_14.raise_()
                self.dateEdit.raise_()
                self.label_15.raise_()
                sewa.setCentralWidget(self.centralwidget)

                self.retranslateUi(sewa)
                QtCore.QMetaObject.connectSlotsByName(sewa)

        def retranslateUi(self, sewa):
                _translate = QtCore.QCoreApplication.translate
                sewa.setWindowTitle(_translate("sewa", "BOOKING"))
                self.save.setText(_translate("sewa", "Masukkan"))
                self.comboBox.setItemText(1, _translate("sewa", "Lapangan 1 - Surya"))
                self.comboBox.setItemText(2, _translate("sewa", "Lapangan 2 - Kaguya "))
                self.comboBox.setItemText(3, _translate("sewa", "Lapangan 3 - Kamiu"))
                self.plainTextEdit_2.setPlainText(_translate("sewa", "-"))
                self.label.setText(_translate("sewa", "No.Id"))
                self.label_2.setText(_translate("sewa", "Nama Club"))
                self.label_3.setText(_translate("sewa", "Asal Club "))
                self.label_4.setText(_translate("sewa", "Nama Captain"))
                self.label_5.setText(_translate("sewa", "<html><head/><body><p align=\"center\">Pilihan</p></body></html>"))
                self.label_6.setText(_translate("sewa", "Durasi "))
                self.label_7.setText(_translate("sewa", "Keterangan"))
                self.label_8.setText(_translate("sewa", "Sampai"))
                self.label_9.setText(_translate("sewa", "No.Hp"))
                self.label_10.setText(_translate("sewa", "Banyak Pemain"))
                self.save_2.setText(_translate("sewa", "Nomor ID "))
                self.label_12.setText(_translate("sewa", "<html><head/><body><p><span style=\" font-weight:600;\">* klik untuk nomor id </span></p></body></html>"))
                self.label_13.setText(_translate("sewa", "<html><head/><body><p align=\"center\">Booking</p></body></html>"))
                self.label_15.setText(_translate("sewa", "Tanggal"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sewa = QtWidgets.QMainWindow()
    ui = Ui_sewa()
    ui.setupUi(sewa)
    sewa.show()
    sys.exit(app.exec_())
