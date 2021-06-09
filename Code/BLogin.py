

#  Created by "AmaniTech" 

from PyQt5 import QtCore, QtGui, QtWidgets
import images
import pymysql 


class Ui_BLogin(object):
        def tombol_signup(self):
                from BSignUp import Ui_SIGNUP
                self.window_login = QtWidgets.QMainWindow()
                self.ui = Ui_SIGNUP()
                self.ui.setupUi(self.window_login)
                self.window_login.show()

        def kotak_pesan(self, judul, pesan):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle(judul)
                msg.setText(pesan)
                msg.exec_()
        
        def login(self):
                username = self.lineEdit.text()
                password = self.lineEdit_2.text()

                database = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        port = 3306, 
                        db = "aplikasi_lapanganbasket",
                        autocommit = True)
                
                c = database.cursor()
                sql = "select * from tblogin where username = %s and password = %s"
                user = c.execute(sql, (username, password))
                data = c.fetchall()

                if(len(data)) > 0 : 
                        #self.kotak_pesan("INFO", "berhasil")
                        from BMenu import Ui_Beranda
                        self.window_login = QtWidgets.QMainWindow()
                        self.ui = Ui_Beranda()
                        self.ui.setupUi(self.window_login)
                        self.window_login.show()
                        
                else : 
                        self.kotak_pesan("INFO", "Silahkan Coba Lagi")
                        self.lineEdit.setText("")
                        self.lineEdit_2.setText("")



        def setupUi(self, BLogin):
                BLogin.setObjectName("BLogin")
                BLogin.resize(851, 611)
                self.centralwidget = QtWidgets.QWidget(BLogin)
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(140, 100, 571, 391))
                self.frame.setStyleSheet("background-color: rgb(74, 74, 74);\n"
"")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(20, 10, 141, 41))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(17)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(20, 60, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(20, 140, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_4.setObjectName("label_4")
                self.lineEdit = QtWidgets.QLineEdit(self.frame)
                self.lineEdit.setGeometry(QtCore.QRect(20, 100, 221, 31))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
                self.lineEdit.setText("")
                self.lineEdit.setClearButtonEnabled(True)
                self.lineEdit.setObjectName("lineEdit")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
                self.lineEdit_2.setGeometry(QtCore.QRect(20, 180, 221, 31))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(10)
                self.lineEdit_2.setFont(font)
                self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);")
                self.lineEdit_2.setText("")
                self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
                self.lineEdit_2.setClearButtonEnabled(True)
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.label_6 = QtWidgets.QLabel(self.frame)
                self.label_6.setGeometry(QtCore.QRect(20, 330, 191, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
                self.label_6.setObjectName("label_6")
                self.label_8 = QtWidgets.QLabel(self.frame)
                self.label_8.setGeometry(QtCore.QRect(286, -8, 301, 411))
                self.label_8.setStyleSheet("\n"
"background-image: url(:/LAPBAS/e56b841924ac729935e858cb59535fb7.png);\n"
"")
                self.label_8.setText("")
                self.label_8.setPixmap(QtGui.QPixmap(":/LAPBAS/e56b841924ac729935e858cb59535fb7.png"))
                self.label_8.setScaledContents(False)
                self.label_8.setObjectName("label_8")
                self.Login_button = QtWidgets.QToolButton(self.frame)
                self.Login_button.setGeometry(QtCore.QRect(20, 270, 201, 31))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.Login_button.setFont(font)
                self.Login_button.setStyleSheet("QToolButton\n"
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
"}")
                self.Login_button.setObjectName("Login_button")
                self.Login_button.clicked.connect(self.login)##################################
                self.Login_button.clicked.connect(BLogin.close)

                self.singup_button = QtWidgets.QToolButton(self.frame)
                self.singup_button.setGeometry(QtCore.QRect(150, 340, 51, 20))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.singup_button.setFont(font)
                self.singup_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.singup_button.setStyleSheet("QToolButton\n"
"\n"
"{\n"
"color:white;\n"
"border-radius:11px;\n"
"background-color: rgb(74, 74, 74);\n"
"\n"
"}\n"
"\n"
"QToolButton:hover\n"
"\n"
"{\n"
"color:rgb(208, 208, 208); \n"
"\n"
"text-decoration: underline;\n"
"border-radius: 11px;\n"
"\n"
"\n"
"}")
                self.singup_button.setObjectName("singup_button")
                self.singup_button.clicked.connect(self.tombol_signup)######################
                

                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(0, 0, 851, 591))
                self.label.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"")
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap(":/LAPBAS/8C9445325-michael-jordan-basketball-court.fit-2000w.jpg"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.label.raise_()
                self.frame.raise_()
                BLogin.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(BLogin)
                self.statusbar.setObjectName("statusbar")
                BLogin.setStatusBar(self.statusbar)

                self.retranslateUi(BLogin)
                QtCore.QMetaObject.connectSlotsByName(BLogin)

        def retranslateUi(self, BLogin):
                _translate = QtCore.QCoreApplication.translate
                BLogin.setWindowTitle(_translate("BLogin", "Login"))
                self.label_2.setText(_translate("BLogin", "SIGN IN "))
                self.label_3.setText(_translate("BLogin", "USER NAME"))
                self.label_4.setText(_translate("BLogin", "PASSWORD "))
                self.label_6.setText(_translate("BLogin", "Don\'t Have An Account ? sign up"))
                self.Login_button.setText(_translate("BLogin", "LOGIN"))
                self.singup_button.setText(_translate("BLogin", "sign up"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BLogin = QtWidgets.QMainWindow()
    ui = Ui_BLogin()
    ui.setupUi(BLogin)
    BLogin.show()
    sys.exit(app.exec_())
