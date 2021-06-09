

#  Created by "AmaniTech" 

from PyQt5 import QtCore, QtGui, QtWidgets
import images
import pymysql


class Ui_edit_data(object):
        def kotak_pesan(self, judul, pesan):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle(judul)
                msg.setText(pesan)
                msg.exec_()

        def tombol_refresh(self):
                self.lineEdit_6.setText("")
                self.lineEdit_5.setText("")
                self.comboBox.setCurrentText("")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                self.spinBox.setValue(0)
                self.lineEdit_7.setText("")
                self.lineEdit_8.setText("")
                self.lineEdit_9.setText("")
                self.plainTextEdit_2.setPlainText("")

        def tombol_search(self):
                try : 
                        masuk_id = int(self.lineEdit_6.text())

                        database = pymysql.connect(host = "localhost", user = "root", password = "", port = 3306, db = "aplikasi_lapanganbasket", autocommit = True)

                        c = database.cursor()
                        user = c.execute("select * from tbbooking where no_id =" + str(masuk_id) )
                        data = c.fetchall()

                        if (data) : 
                                for x in data :
                                        self.lineEdit_5.setText(x[0])
                                        self.comboBox.setCurrentText(x[2])
                                        self.lineEdit.setText(x[3])
                                        self.lineEdit_2.setText(x[4])
                                        self.lineEdit_3.setText(x[5])
                                        self.lineEdit_4.setText(x[6])
                                        self.spinBox.setValue(int(x[7]))
                                        self.lineEdit_7.setText(x[8])
                                        self.lineEdit_8.setText(x[9])
                                        self.lineEdit_9.setText(x[1])
                                        self.plainTextEdit_2.setPlainText(x[10])

                        else : 
                                self.kotak_pesan("INFO", "Data belum ada")
                                self.tombol_refresh()

                except ValueError:
                        self.kotak_pesan("INFO", "Data yang anda masukaan salah, mohon diperiksa kembali")
                        self.lineEdit_6.setText("")

        def tombol_update(self):
                try:
                        id = self.lineEdit_5.text()
                        pilihan = self.comboBox.currentText()
                        club = self.lineEdit.text()
                        asal_club = self.lineEdit_2.text()
                        captain = self.lineEdit_3.text()
                        hp = self.lineEdit_4.text()
                        pemain = self.spinBox.value()
                        waktu_awal = self.lineEdit_7.text()
                        waktu_akhir = self.lineEdit_8.text()
                        keterangan = self.plainTextEdit_2.toPlainText()
                        tanggal = self.lineEdit_9.text()

                        database = pymysql.connect(host = "localhost",user = "root", password = "", port = 3306, db = "aplikasi_lapanganbasket",autocommit = True)

                        c = database.cursor()
                        sql = "update tbbooking set `tanggal`=%s,`pilihan`=%s,`nama_club`=%s,`asal_club`=%s,`captain`=%s,`no_hp`=%s,`banyak_pemain`=%s,`waktu_mulai`=%s,`waktu_akhir`=%s,`keterangan`=%s where `no_id`= %s"
                        user = c.execute(sql, (tanggal, pilihan, club, asal_club, captain, hp , pemain, waktu_awal, waktu_akhir, keterangan, id ))
                        
                        if (user) : 
                                self.kotak_pesan("INFO", "Data berhasil di update")
                                self.tombol_refresh()
                        else  :
                                self.kotak_pesan("INFO", "Data gagal disimpan")
                
                except ValueError:
                        self.kotak_pesan("INFO", "Data yang anda masukaan salah, mohon diperiksa kembali")

        def tombol_gerbang(self):
                from BMenu import Ui_Beranda
                self.window_about = QtWidgets.QMainWindow()
                self.ui = Ui_Beranda()
                self.ui.setupUi(self.window_about)
                self.window_about.show()

        
        def setupUi(self, edit_data):
                edit_data.setObjectName("edit_data")
                edit_data.resize(904, 663)
                self.centralwidget = QtWidgets.QWidget(edit_data)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(-10, 0, 931, 671))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap(":/LAPBAS/black-doff-wallpaper-33.jpg"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(100, 400, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_9.setFont(font)
                self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_9.setObjectName("label_9")
                self.label_15 = QtWidgets.QLabel(self.centralwidget)
                self.label_15.setGeometry(QtCore.QRect(760, 170, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Brush Script MT")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_15.setFont(font)
                self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_15.setObjectName("label_15")
                self.save = QtWidgets.QToolButton(self.centralwidget)
                self.save.setGeometry(QtCore.QRect(700, 340, 141, 41))
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
                self.save.clicked.connect(self.tombol_refresh)#########################

                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(100, 350, 111, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_4.setObjectName("label_4")
                self.label_10 = QtWidgets.QLabel(self.centralwidget)
                self.label_10.setGeometry(QtCore.QRect(480, 400, 111, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_10.setFont(font)
                self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_10.setObjectName("label_10")
                self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
                self.spinBox.setGeometry(QtCore.QRect(610, 400, 42, 32))
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
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(100, 500, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_7.setFont(font)
                self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_7.setObjectName("label_7")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_2.setGeometry(QtCore.QRect(230, 300, 421, 32))
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
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(100, 300, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_3.setObjectName("label_3")
                self.label_14 = QtWidgets.QLabel(self.centralwidget)
                self.label_14.setGeometry(QtCore.QRect(720, 480, 111, 121))
                self.label_14.setStyleSheet("image: url(:/LAPBAS/1.jpg);\n"
"\n"
"\n"
"\n"
"")
                self.label_14.setText("")
                self.label_14.setObjectName("label_14")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(100, 250, 91, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_2.setObjectName("label_2")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(100, 200, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(410, 210, 91, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_6.setObjectName("label_6")
                self.save_2 = QtWidgets.QToolButton(self.centralwidget)
                self.save_2.setGeometry(QtCore.QRect(700, 260, 141, 41))
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
                self.save_2.clicked.connect(self.tombol_update)######################

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
                self.icon_gerbang.clicked.connect(self.tombol_gerbang)#####################
                self.icon_gerbang.clicked.connect(edit_data.close)

                self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
                self.plainTextEdit_2.setGeometry(QtCore.QRect(230, 500, 421, 131))
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
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(100, 450, 91, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_8.setFont(font)
                self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_8.setObjectName("label_8")
                self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_3.setGeometry(QtCore.QRect(230, 350, 421, 32))
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
                self.lineEdit_4.setGeometry(QtCore.QRect(230, 400, 241, 32))
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
                self.comboBox = QtWidgets.QComboBox(self.centralwidget)
                self.comboBox.setGeometry(QtCore.QRect(510, 200, 141, 32))
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
                self.lineEdit.setGeometry(QtCore.QRect(230, 250, 421, 32))
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
                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(370, 450, 61, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_11.setFont(font)
                self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_11.setObjectName("label_11")
                self.label_13 = QtWidgets.QLabel(self.centralwidget)
                self.label_13.setGeometry(QtCore.QRect(320, 0, 231, 91))
                font = QtGui.QFont()
                font.setFamily("Brush Script MT")
                font.setPointSize(50)
                self.label_13.setFont(font)
                self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_13.setObjectName("label_13")
                self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_5.setGeometry(QtCore.QRect(230, 200, 181, 32))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.lineEdit_5.setFont(font)
                self.lineEdit_5.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.lineEdit_5.setObjectName("lineEdit_5")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(610, 110, 51, 41))
                self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton.setStyleSheet("\n"
"QPushButton\n"
"\n"
"{\n"
"    image: url(:/LAPBAS/zoom-icon-png-9.png);\n"
"\n"
"background-color: rgb(0,0,0,0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"\n"
"{\n"
"image: url(:/LAPBAS/zoom-icon-png-9.png);\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}")
                self.pushButton.setText("")
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.tombol_search)###################

                self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_6.setGeometry(QtCore.QRect(270, 120, 331, 31))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.lineEdit_6.setFont(font)
                self.lineEdit_6.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(0,0,0,0);\n"
"border-top:1px solid rgb(140, 140, 140);\n"
"border-left:1px solid rgb(140, 140, 140);\n"
"border-right:1px solid rgb(140, 140, 140);\n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.lineEdit_6.setText("")
                self.lineEdit_6.setClearButtonEnabled(True)
                self.lineEdit_6.setObjectName("lineEdit_6")
                self.label_12 = QtWidgets.QLabel(self.centralwidget)
                self.label_12.setGeometry(QtCore.QRect(380, 90, 131, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_12.setFont(font)
                self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_12.setObjectName("label_12")
                self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_7.setGeometry(QtCore.QRect(230, 450, 131, 32))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.lineEdit_7.setFont(font)
                self.lineEdit_7.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.lineEdit_7.setObjectName("lineEdit_7")
                self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_8.setGeometry(QtCore.QRect(440, 450, 131, 32))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.lineEdit_8.setFont(font)
                self.lineEdit_8.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.lineEdit_8.setObjectName("lineEdit_8")
                self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_9.setGeometry(QtCore.QRect(740, 200, 101, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.lineEdit_9.setFont(font)
                self.lineEdit_9.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"border-top : 1px solid rgb(140, 140, 140); \n"
"border-left:1px solid rgb(140, 140, 140); \n"
"border-right:1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.lineEdit_9.setObjectName("lineEdit_9")
                self.label.raise_()
                self.label_9.raise_()
                self.label_15.raise_()
                self.save.raise_()
                self.label_4.raise_()
                self.label_10.raise_()
                self.spinBox.raise_()
                self.label_7.raise_()
                self.lineEdit_2.raise_()
                self.label_3.raise_()
                self.label_2.raise_()
                self.label_5.raise_()
                self.label_6.raise_()
                self.save_2.raise_()
                self.icon_gerbang.raise_()
                self.plainTextEdit_2.raise_()
                self.label_8.raise_()
                self.lineEdit_3.raise_()
                self.lineEdit_4.raise_()
                self.comboBox.raise_()
                self.lineEdit.raise_()
                self.label_11.raise_()
                self.label_13.raise_()
                self.lineEdit_5.raise_()
                self.label_14.raise_()
                self.pushButton.raise_()
                self.lineEdit_6.raise_()
                self.label_12.raise_()
                self.lineEdit_7.raise_()
                self.lineEdit_8.raise_()
                self.lineEdit_9.raise_()
                edit_data.setCentralWidget(self.centralwidget)

                self.retranslateUi(edit_data)
                QtCore.QMetaObject.connectSlotsByName(edit_data)

        def retranslateUi(self, edit_data):
                _translate = QtCore.QCoreApplication.translate
                edit_data.setWindowTitle(_translate("edit_data", "EDIT "))
                self.label_9.setText(_translate("edit_data", "No.Hp"))
                self.label_15.setText(_translate("edit_data", "Tanggal"))
                self.save.setText(_translate("edit_data", "Refresh"))
                self.label_4.setText(_translate("edit_data", "Nama Captain"))
                self.label_10.setText(_translate("edit_data", "Banyak Pemain"))
                self.label_7.setText(_translate("edit_data", "Keterangan"))
                self.label_3.setText(_translate("edit_data", "Asal Club "))
                self.label_2.setText(_translate("edit_data", "Nama Club"))
                self.label_5.setText(_translate("edit_data", "No.Id"))
                self.label_6.setText(_translate("edit_data", "<html><head/><body><p align=\"center\">Pilihan</p></body></html>"))
                self.save_2.setText(_translate("edit_data", "Update"))
                self.plainTextEdit_2.setPlainText(_translate("edit_data", "-"))
                self.label_8.setText(_translate("edit_data", "Durasi "))
                self.comboBox.setItemText(1, _translate("edit_data", "Lapangan 1 - Surya"))
                self.comboBox.setItemText(2, _translate("edit_data", "Lapangan 2 - Kaguya "))
                self.comboBox.setItemText(3, _translate("edit_data", "Lapangan 3 - Kamiu"))
                self.label_11.setText(_translate("edit_data", "Sampai"))
                self.label_13.setText(_translate("edit_data", "<html><head/><body><p align=\"center\">Edit Data</p></body></html>"))
                self.lineEdit_6.setToolTip(_translate("edit_data", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
                self.label_12.setText(_translate("edit_data", "Masukkan No.Id"))
                self.lineEdit_9.setToolTip(_translate("edit_data", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_data = QtWidgets.QMainWindow()
    ui = Ui_edit_data()
    ui.setupUi(edit_data)
    edit_data.show()
    sys.exit(app.exec_())
