

#  Created by "AmaniTech" 

from PyQt5 import QtCore, QtGui, QtWidgets
import images
import pymysql
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox


class Ui_List(object):
        def kotak_pesan(self, judul, pesan):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle(judul)
                msg.setText(pesan)
                msg.exec_()

        def tombol_showall(self): 
                database = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "", 
                        port = 3306, 
                        db = "aplikasi_lapanganbasket",
                        autocommit = True)
                c = database.cursor()
                user = c.execute("select * from tbbooking")
                data = c.fetchall()

                self.tabelpeserta.setRowCount(0)

                for row_number, row_data in enumerate(data):
                        self.tabelpeserta.insertRow(row_number)

                        for coloum_number, waw in enumerate(row_data):
                                self.tabelpeserta.setItem(row_number, coloum_number, QTableWidgetItem(str(waw)))

                self.tabelpeserta.setStyleSheet("background-color : rgb(255, 255, 255)")

        def tombol_search(self):
                try: 
                        id = int(self.lineEdit.text())

                        database = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        port = 3306,
                        db = "aplikasi_lapanganbasket",
                        autocommit = True)

                        c = database.cursor()
                        user = c.execute("select * from tbbooking where no_id = " + str(id))
                        data = c.fetchall()

                        if (data) : 
                                self.tabelpeserta.insertRow(0)

                                for RowNum, RowDATA in enumerate(data):
                                        self.tabelpeserta.insertRow(RowNum)
                                        for ColumnNum, ColumnData in enumerate(RowDATA):
                                                self.tabelpeserta.setItem(RowNum, ColumnNum, QtWidgets.QTableWidgetItem(str(ColumnData)))

                                new = []
                                user2 = c.execute("select * from tbbooking where no_id =" + str(id))
                                data2 = c.fetchall()

                                for RowNum, RowDATA in enumerate(data2):
                                        for ColumnNum, ColumnData in enumerate(RowDATA):
                                                new.append(ColumnData)
                                        
                                self.tabelpeserta.setRowCount(1)

                                ###########################################
                                self.textBrowser.setText(new[3])
                                self.textBrowser_2.setText(new[5])
                                self.textBrowser_3.setText(new[6])
                                self.textBrowser_4.setText(new[8])
                                self.textBrowser_5.setText(new[9])
                                self.textBrowser_6.setText(new[10])

                        else: 
                                self.kotak_pesan("INFO", "Data belum ada")
                        

                except ValueError:
                        self.kotak_pesan("INFO", "Data yang anda masukkan salah, Mohon diperiksa kembali")
                        self.lineEdit.setText("")

        def refresh(self):
                self.lineEdit.setText("")
                self.textBrowser.setText("")
                self.textBrowser_2.setText("")
                self.textBrowser_3.setText("")
                self.textBrowser_4.setText("")
                self.textBrowser_5.setText("")
                self.textBrowser_6.setText("")
                self.tabelpeserta.clearContents()
                self.tabelpeserta.setRowCount(0)
                self.tabelpeserta.setStyleSheet("background-color: rgb(74, 74, 74)")

        def tombol_selesai(self):
                try:
                        id = int(self.lineEdit.text())
                        database = pymysql.connect(
                                host = "localhost",
                                user = "root", 
                                password = "", 
                                port = 3306,
                                db = "aplikasi_lapanganbasket",
                                autocommit = True)
                        o = database.cursor()
                        sql = "delete from tbbooking where no_id = %s" 
                        user = o.execute(sql, id )
                        if (user) : 
                                self.kotak_pesan("INFO", "Data berhasil dihapus")
                                self.refresh()
                        
                        else : 
                                self.kotak_pesan("INFO", "Data gagal dihapus")
                
                except ValueError: 
                        self.kotak_pesan("INFO", "Data yang anda masukkan salah, Mohon diperiksa kembali")
                        self.refresh()

        def tombol_gerbang(self):
                from BMenu import Ui_Beranda
                self.window_about = QtWidgets.QMainWindow()
                self.ui = Ui_Beranda()
                self.ui.setupUi(self.window_about)
                self.window_about.show()

        def tombol_reset(self):
                msgbox = QMessageBox()
                msgbox.setIcon(QMessageBox.Question)
                msgbox.setWindowTitle("Alert")
                msgbox.setText('apakah kamu ingin menghapus semua data ini..?')
                msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                tombol = msgbox.exec_()

                if (tombol) == QMessageBox.Yes : 
                        database = pymysql.connect(
                                host = "localhost",
                                user = "root", 
                                password = "", 
                                port = 3306,
                                db = "aplikasi_lapanganbasket",
                                autocommit = True)
                        c = database.cursor()
                        user = c.execute("delete from tbbooking")
                        ########################
                        self.kotak_pesan("INFO", "semua data telah terhapus")
                        #######################
                        self.refresh()
                
                else : 
                        msgbox = QMessageBox()
                        msgbox.setIcon(QMessageBox.Information)
                        msgbox.setWindowTitle("INFO")
                        msgbox.setText("penghapusan data dibatalkan")
                        msgbox.exec_()



        def setupUi(self, List):
                List.setObjectName("List")
                List.resize(1052, 591)
                self.centralwidget = QtWidgets.QWidget(List)
                self.centralwidget.setObjectName("centralwidget")
                self.tabelpeserta = QtWidgets.QTableWidget(self.centralwidget)
                self.tabelpeserta.setGeometry(QtCore.QRect(40, 140, 531, 411))
                self.tabelpeserta.setStyleSheet("\n"
"\n"
"\n"
"background-color: rgb(74, 74, 74)")
                self.tabelpeserta.setRowCount(0)
                self.tabelpeserta.setColumnCount(11)
                self.tabelpeserta.setObjectName("tabelpeserta")
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(8, item)
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(9, item)
                item = QtWidgets.QTableWidgetItem()
                self.tabelpeserta.setHorizontalHeaderItem(10, item)
                self.tabelpeserta.horizontalHeader().setMinimumSectionSize(50)
                self.tabelpeserta.horizontalHeader().setSortIndicatorShown(True)
                self.tabelpeserta.horizontalHeader().setStretchLastSection(True)
                self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser.setGeometry(QtCore.QRect(730, 160, 271, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.textBrowser.setFont(font)
                self.textBrowser.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.textBrowser.setObjectName("textBrowser")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(610, 160, 91, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_2.setObjectName("label_2")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(610, 220, 111, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
                self.label_4.setObjectName("label_4")
                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(610, 280, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_9.setFont(font)
                self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_9.setObjectName("label_9")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(610, 340, 91, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_6.setObjectName("label_6")
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(840, 340, 61, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_8.setFont(font)
                self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_8.setObjectName("label_8")
                self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_2.setGeometry(QtCore.QRect(730, 220, 271, 32))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.textBrowser_2.setFont(font)
                self.textBrowser_2.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.textBrowser_2.setObjectName("textBrowser_2")
                self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_3.setGeometry(QtCore.QRect(730, 280, 271, 32))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.textBrowser_3.setFont(font)
                self.textBrowser_3.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.textBrowser_3.setObjectName("textBrowser_3")
                self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_4.setGeometry(QtCore.QRect(730, 340, 91, 32))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.textBrowser_4.setFont(font)
                self.textBrowser_4.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.textBrowser_4.setObjectName("textBrowser_4")
                self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_5.setGeometry(QtCore.QRect(910, 340, 91, 32))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.textBrowser_5.setFont(font)
                self.textBrowser_5.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.textBrowser_5.setObjectName("textBrowser_5")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(610, 400, 81, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_7.setFont(font)
                self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_7.setObjectName("label_7")
                self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_6.setGeometry(QtCore.QRect(730, 401, 271, 101))
                self.textBrowser_6.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border : None ; \n"
"border-top : 1px solid rgb(140, 140, 140);\n"
"border-left:1px solid rgb(140, 140, 140);\n"
"border-right:1px solid rgb(140, 140, 140);\n"
"\n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.textBrowser_6.setObjectName("textBrowser_6")
                self.toolButton = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton.setGeometry(QtCore.QRect(910, 520, 111, 33))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.toolButton.setFont(font)
                self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton.setStyleSheet("QToolButton\n"
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
                self.toolButton.setObjectName("toolButton")
                self.toolButton.clicked.connect(self.tombol_reset)

                self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton_2.setGeometry(QtCore.QRect(770, 520, 111, 33))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.toolButton_2.setFont(font)
                self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton_2.setStyleSheet("QToolButton\n"
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
                self.toolButton_2.setObjectName("toolButton_2")
                self.toolButton_2.clicked.connect(self.tombol_selesai)

                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(200, 90, 211, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"background-color: rgb(74, 74, 74);")
                self.label.setObjectName("label")
                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(370, 50, 331, 31))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(0,0,0,0);\n"
"border-top:1px solid rgb(140, 140, 140);\n"
"border-left:1px solid rgb(140, 140, 140);\n"
"border-right:1px solid rgb(140, 140, 140);\n"
"border-bottom: 1px solid rgb(140, 140, 140); \n"
"padding-bottom:7px; \n"
"color: rgb(255, 255, 255);\n"
"")
                self.lineEdit.setText("")
                self.lineEdit.setClearButtonEnabled(True)
                self.lineEdit.setObjectName("lineEdit")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(870, 40, 91, 61))
                font = QtGui.QFont()
                font.setFamily("Brush Script MT")
                font.setPointSize(37)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_3.setObjectName("label_3")
                self.icon_gerbang = QtWidgets.QPushButton(self.centralwidget)
                self.icon_gerbang.setGeometry(QtCore.QRect(40, 20, 51, 51))
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
                self.icon_gerbang.clicked.connect(self.tombol_gerbang)###########################################
                self.icon_gerbang.clicked.connect(List.close)

                self.label_10 = QtWidgets.QLabel(self.centralwidget)
                self.label_10.setGeometry(QtCore.QRect(-280, -110, 1341, 711))
                self.label_10.setText("")
                self.label_10.setPixmap(QtGui.QPixmap(":/LAPBAS/mengenal-penemu-bola-basket-ini-sosoknya-VdY4VLj8hU.jpg"))
                self.label_10.setScaledContents(True)
                self.label_10.setObjectName("label_10")
                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(480, 20, 131, 32))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_11.setFont(font)
                self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_11.setObjectName("label_11")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(710, 40, 51, 41))
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
                self.pushButton.clicked.connect(self.tombol_search)##########################

                self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton_3.setGeometry(QtCore.QRect(450, 100, 91, 31))
                self.toolButton_3.clicked.connect(self.tombol_showall)#################################

                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.toolButton_3.setFont(font)
                self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton_3.setStyleSheet("QToolButton\n"
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
                self.toolButton_3.setObjectName("toolButton_3")
                self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton_4.setGeometry(QtCore.QRect(630, 520, 111, 33))
                self.toolButton_4.clicked.connect(self.refresh)################################

                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.toolButton_4.setFont(font)
                self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton_4.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"color:black;\n"
"border-radius:11px;\n"
"background-color: rgb(85, 255, 0);\n"
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
                self.toolButton_4.setObjectName("toolButton_4")
                self.label_10.raise_()
                self.tabelpeserta.raise_()
                self.textBrowser.raise_()
                self.label_2.raise_()
                self.label_4.raise_()
                self.label_9.raise_()
                self.label_6.raise_()
                self.label_8.raise_()
                self.textBrowser_2.raise_()
                self.textBrowser_3.raise_()
                self.textBrowser_4.raise_()
                self.textBrowser_5.raise_()
                self.label_7.raise_()
                self.textBrowser_6.raise_()
                self.toolButton.raise_()
                self.toolButton_2.raise_()
                self.label.raise_()
                self.lineEdit.raise_()
                self.label_3.raise_()
                self.icon_gerbang.raise_()
                self.label_11.raise_()
                self.pushButton.raise_()
                self.toolButton_3.raise_()
                self.toolButton_4.raise_()
                List.setCentralWidget(self.centralwidget)

                self.retranslateUi(List)
                QtCore.QMetaObject.connectSlotsByName(List)

        def retranslateUi(self, List):
                _translate = QtCore.QCoreApplication.translate
                List.setWindowTitle(_translate("List", "LIST"))
                item = self.tabelpeserta.horizontalHeaderItem(0)
                item.setText(_translate("List", "No.Id"))
                item = self.tabelpeserta.horizontalHeaderItem(1)
                item.setText(_translate("List", "Tanggal"))
                item = self.tabelpeserta.horizontalHeaderItem(2)
                item.setText(_translate("List", "Pilihan"))
                item = self.tabelpeserta.horizontalHeaderItem(3)
                item.setText(_translate("List", "Nama Club "))
                item = self.tabelpeserta.horizontalHeaderItem(4)
                item.setText(_translate("List", "Asal Club "))
                item = self.tabelpeserta.horizontalHeaderItem(5)
                item.setText(_translate("List", "Captain"))
                item = self.tabelpeserta.horizontalHeaderItem(6)
                item.setText(_translate("List", "No.HP"))
                item = self.tabelpeserta.horizontalHeaderItem(7)
                item.setText(_translate("List", "Banyak Pemain"))
                item = self.tabelpeserta.horizontalHeaderItem(8)
                item.setText(_translate("List", "Waktu Mulai"))
                item = self.tabelpeserta.horizontalHeaderItem(9)
                item.setText(_translate("List", "Waktu Akhir"))
                item = self.tabelpeserta.horizontalHeaderItem(10)
                item.setText(_translate("List", "Keterangan"))
                self.label_2.setText(_translate("List", "Nama Club"))
                self.label_4.setText(_translate("List", "Nama Captain"))
                self.label_9.setText(_translate("List", "No.Hp"))
                self.label_6.setText(_translate("List", "Durasi "))
                self.label_8.setText(_translate("List", "Sampai"))
                self.label_7.setText(_translate("List", "Keterangan"))
                self.toolButton.setText(_translate("List", "Reset "))
                self.toolButton_2.setText(_translate("List", "Selesai"))
                self.label.setText(_translate("List", "<html><head/><body><p align=\"center\">Tabel Pesanan</p></body></html>"))
                self.lineEdit.setToolTip(_translate("List", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
                self.label_3.setText(_translate("List", "List "))
                self.label_11.setText(_translate("List", "Masukkan No.Id"))
                self.toolButton_3.setText(_translate("List", "Show All"))
                self.toolButton_4.setText(_translate("List", "Refresh"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    List = QtWidgets.QMainWindow()
    ui = Ui_List()
    ui.setupUi(List)
    List.show()
    sys.exit(app.exec_())
