# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1101, 870)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"border-image: url(:/wallpaper/images/wallpaperflare.com_wallpaper (2) (1).jpg);\n"
"}\n"
"\n"
"#widget {\n"
"background-color: #fff;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel#Welcome {\n"
"color: #fff;\n"
"}\n"
"\n"
"QLabel#label_4 {\n"
"color: #fff;\n"
"}\n"
"QLabel#Started {\n"
"color: black;\n"
"}\n"
"QLabel#SignUp {\n"
"color: black;\n"
"}\n"
"\n"
"QLineEdit {\n"
"border: none;\n"
"border-bottom: 2px solid #cccccc\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border-bottom: 2px solid #295ba4\n"
"}\n"
"\n"
"QScrollArea {\n"
"background-color: #fff;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover#LoginNow\n"
"{\n"
"     color: gray;\n"
"     background-color: rgb(224, 238, 249);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.Welcome = QLabel(self.centralwidget)
        self.Welcome.setObjectName(u"Welcome")
        font = QFont()
        font.setPointSize(26)
        self.Welcome.setFont(font)
        self.Welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.Welcome)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.verticalSpacer_5 = QSpacerItem(20, 105, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.SignUp = QLabel(self.widget)
        self.SignUp.setObjectName(u"SignUp")
        font2 = QFont()
        font2.setPointSize(10)
        self.SignUp.setFont(font2)
        self.SignUp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.SignUp)

        self.LoginNow = QPushButton(self.widget)
        self.LoginNow.setObjectName(u"LoginNow")
        self.LoginNow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.LoginNow)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.Started = QLabel(self.widget)
        self.Started.setObjectName(u"Started")
        font3 = QFont()
        font3.setPointSize(18)
        self.Started.setFont(font3)
        self.Started.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Started, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 518, 747))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Email_4 = QLabel(self.scrollAreaWidgetContents)
        self.Email_4.setObjectName(u"Email_4")
        self.Email_4.setFont(font2)
        self.Email_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.Email_4)

        self.FullName = QLineEdit(self.scrollAreaWidgetContents)
        self.FullName.setObjectName(u"FullName")
        self.FullName.setMinimumSize(QSize(250, 0))
        font4 = QFont()
        font4.setPointSize(13)
        self.FullName.setFont(font4)

        self.verticalLayout.addWidget(self.FullName)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Email_5 = QLabel(self.scrollAreaWidgetContents)
        self.Email_5.setObjectName(u"Email_5")
        self.Email_5.setFont(font2)
        self.Email_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.Email_5)

        self.Username = QLineEdit(self.scrollAreaWidgetContents)
        self.Username.setObjectName(u"Username")
        self.Username.setMinimumSize(QSize(250, 0))
        self.Username.setFont(font4)
        self.Username.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_7.addWidget(self.Username)


        self.verticalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Password_5 = QLabel(self.scrollAreaWidgetContents)
        self.Password_5.setObjectName(u"Password_5")
        self.Password_5.setFont(font2)
        self.Password_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.Password_5)

        self.Password = QLineEdit(self.scrollAreaWidgetContents)
        self.Password.setObjectName(u"Password")
        self.Password.setFont(font4)
        self.Password.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_8.addWidget(self.Password)


        self.verticalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Password_4 = QLabel(self.scrollAreaWidgetContents)
        self.Password_4.setObjectName(u"Password_4")
        self.Password_4.setFont(font2)
        self.Password_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.Password_4)

        self.NationalID = QLineEdit(self.scrollAreaWidgetContents)
        self.NationalID.setObjectName(u"NationalID")
        self.NationalID.setFont(font4)
        self.NationalID.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_2.addWidget(self.NationalID)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Password_9 = QLabel(self.scrollAreaWidgetContents)
        self.Password_9.setObjectName(u"Password_9")
        self.Password_9.setFont(font2)
        self.Password_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.Password_9)

        self.PhoneNumber = QLineEdit(self.scrollAreaWidgetContents)
        self.PhoneNumber.setObjectName(u"PhoneNumber")
        self.PhoneNumber.setFont(font4)
        self.PhoneNumber.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_11.addWidget(self.PhoneNumber)


        self.verticalLayout_3.addLayout(self.verticalLayout_11)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.Password_14 = QLabel(self.scrollAreaWidgetContents)
        self.Password_14.setObjectName(u"Password_14")
        self.Password_14.setFont(font2)
        self.Password_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.Password_14)

        self.PassportNumber = QLineEdit(self.scrollAreaWidgetContents)
        self.PassportNumber.setObjectName(u"PassportNumber")
        self.PassportNumber.setFont(font4)
        self.PassportNumber.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_16.addWidget(self.PassportNumber)


        self.verticalLayout_3.addLayout(self.verticalLayout_16)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.Password_10 = QLabel(self.scrollAreaWidgetContents)
        self.Password_10.setObjectName(u"Password_10")
        self.Password_10.setFont(font2)
        self.Password_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.Password_10)

        self.BirthDate = QDateEdit(self.scrollAreaWidgetContents)
        self.BirthDate.setObjectName(u"BirthDate")
        self.BirthDate.setMinimumSize(QSize(0, 40))
        self.BirthDate.setFont(font4)

        self.verticalLayout_12.addWidget(self.BirthDate)


        self.verticalLayout_4.addLayout(self.verticalLayout_12)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.Password_12 = QLabel(self.scrollAreaWidgetContents)
        self.Password_12.setObjectName(u"Password_12")
        self.Password_12.setFont(font2)
        self.Password_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.Password_12)

        self.Gender = QComboBox(self.scrollAreaWidgetContents)
        self.Gender.addItem("")
        self.Gender.addItem("")
        self.Gender.addItem("")
        self.Gender.setObjectName(u"Gender")
        self.Gender.setFont(font4)

        self.verticalLayout_14.addWidget(self.Gender)


        self.verticalLayout_4.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Password_13 = QLabel(self.scrollAreaWidgetContents)
        self.Password_13.setObjectName(u"Password_13")
        self.Password_13.setFont(font2)
        self.Password_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.Password_13)

        self.Nationality = QComboBox(self.scrollAreaWidgetContents)
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.addItem("")
        self.Nationality.setObjectName(u"Nationality")
        self.Nationality.setFont(font4)

        self.verticalLayout_15.addWidget(self.Nationality)


        self.verticalLayout_4.addLayout(self.verticalLayout_15)

        self.CreateAccount = QPushButton(self.scrollAreaWidgetContents)
        self.CreateAccount.setObjectName(u"CreateAccount")
        font5 = QFont()
        font5.setPointSize(12)
        self.CreateAccount.setFont(font5)
        self.CreateAccount.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CreateAccount.setCheckable(False)

        self.verticalLayout_4.addWidget(self.CreateAccount)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 2, 1)

        self.horizontalSpacer_5 = QSpacerItem(184, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(183, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 1, 4, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 151, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 2, 2, 1, 2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Welcome.setText(QCoreApplication.translate("MainWindow", u"Welcome to SHC Airlines", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Travel Anywhere, Anytime.", None))
        self.SignUp.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.LoginNow.setText(QCoreApplication.translate("MainWindow", u"Log In Now!", None))
        self.Started.setText(QCoreApplication.translate("MainWindow", u"Let's Get Started!", None))
        self.Email_4.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.Email_5.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Password_5.setText(QCoreApplication.translate("MainWindow", u"Create Password (Don't share it with anyone)", None))
        self.Password.setText("")
        self.Password_4.setText(QCoreApplication.translate("MainWindow", u"National ID", None))
        self.NationalID.setText("")
        self.Password_9.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.Password_14.setText(QCoreApplication.translate("MainWindow", u"Passport Number", None))
        self.Password_10.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.Password_12.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.Gender.setItemText(0, "")
        self.Gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.Gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.Password_13.setText(QCoreApplication.translate("MainWindow", u"Main Nationality", None))
        self.Nationality.setItemText(0, "")
        self.Nationality.setItemText(1, QCoreApplication.translate("MainWindow", u"Afghan (Afghanistan)", None))
        self.Nationality.setItemText(2, QCoreApplication.translate("MainWindow", u"Albanian (Albania)", None))
        self.Nationality.setItemText(3, QCoreApplication.translate("MainWindow", u"Algerian (Algeria)", None))
        self.Nationality.setItemText(4, QCoreApplication.translate("MainWindow", u"American (United States)", None))
        self.Nationality.setItemText(5, QCoreApplication.translate("MainWindow", u"Argentine (Argentina)", None))
        self.Nationality.setItemText(6, QCoreApplication.translate("MainWindow", u"Australian (Australia)", None))
        self.Nationality.setItemText(7, QCoreApplication.translate("MainWindow", u"Austrian (Austria)", None))
        self.Nationality.setItemText(8, QCoreApplication.translate("MainWindow", u"Bahraini (Bahrain)", None))
        self.Nationality.setItemText(9, QCoreApplication.translate("MainWindow", u"Belgian (Belgium)", None))
        self.Nationality.setItemText(10, QCoreApplication.translate("MainWindow", u"Brazilian (Brazil)", None))
        self.Nationality.setItemText(11, QCoreApplication.translate("MainWindow", u"British (United Kingdom)", None))
        self.Nationality.setItemText(12, QCoreApplication.translate("MainWindow", u"Canadian (Canada)", None))
        self.Nationality.setItemText(13, QCoreApplication.translate("MainWindow", u"Chinese (China)", None))
        self.Nationality.setItemText(14, QCoreApplication.translate("MainWindow", u"Colombian (Colombia)", None))
        self.Nationality.setItemText(15, QCoreApplication.translate("MainWindow", u"Croatian (Croatia)", None))
        self.Nationality.setItemText(16, QCoreApplication.translate("MainWindow", u"Cypriot (Cyprus)", None))
        self.Nationality.setItemText(17, QCoreApplication.translate("MainWindow", u"Czech (Czech Republic)", None))
        self.Nationality.setItemText(18, QCoreApplication.translate("MainWindow", u"Danish (Denmark)", None))
        self.Nationality.setItemText(19, QCoreApplication.translate("MainWindow", u"Dutch (Netherlands)", None))
        self.Nationality.setItemText(20, QCoreApplication.translate("MainWindow", u"Egyptian (Egypt)", None))
        self.Nationality.setItemText(21, QCoreApplication.translate("MainWindow", u"Emirati (United Arab Emirates - UAE)", None))
        self.Nationality.setItemText(22, QCoreApplication.translate("MainWindow", u"Finnish (Finland)", None))
        self.Nationality.setItemText(23, QCoreApplication.translate("MainWindow", u"French (France)", None))
        self.Nationality.setItemText(24, QCoreApplication.translate("MainWindow", u"German (Germany)", None))
        self.Nationality.setItemText(25, QCoreApplication.translate("MainWindow", u"Greek (Greece)", None))
        self.Nationality.setItemText(26, QCoreApplication.translate("MainWindow", u"Hungarian (Hungary)", None))
        self.Nationality.setItemText(27, QCoreApplication.translate("MainWindow", u"Indian (India)", None))
        self.Nationality.setItemText(28, QCoreApplication.translate("MainWindow", u"Iraqi (Iraq)", None))
        self.Nationality.setItemText(29, QCoreApplication.translate("MainWindow", u"Italian (Italy)", None))
        self.Nationality.setItemText(30, QCoreApplication.translate("MainWindow", u"Japanese (Japan)", None))
        self.Nationality.setItemText(31, QCoreApplication.translate("MainWindow", u"Jordanian (Jordan)", None))
        self.Nationality.setItemText(32, QCoreApplication.translate("MainWindow", u"Kuwaiti (Kuwait)", None))
        self.Nationality.setItemText(33, QCoreApplication.translate("MainWindow", u"Lebanese (Lebanon)", None))
        self.Nationality.setItemText(34, QCoreApplication.translate("MainWindow", u"Libyan (Libya)", None))
        self.Nationality.setItemText(35, QCoreApplication.translate("MainWindow", u"Mauritanian (Mauritania)", None))
        self.Nationality.setItemText(36, QCoreApplication.translate("MainWindow", u"Mexican (Mexico)", None))
        self.Nationality.setItemText(37, QCoreApplication.translate("MainWindow", u"Moroccan (Morocco)", None))
        self.Nationality.setItemText(38, QCoreApplication.translate("MainWindow", u"New Zealander (New Zealand)", None))
        self.Nationality.setItemText(39, QCoreApplication.translate("MainWindow", u"Omani (Oman)", None))
        self.Nationality.setItemText(40, QCoreApplication.translate("MainWindow", u"Palestinian (Palestine)", None))
        self.Nationality.setItemText(41, QCoreApplication.translate("MainWindow", u"Polish (Poland)", None))
        self.Nationality.setItemText(42, QCoreApplication.translate("MainWindow", u"Portuguese (Portugal)", None))
        self.Nationality.setItemText(43, QCoreApplication.translate("MainWindow", u"Qatari (Qatar)", None))
        self.Nationality.setItemText(44, QCoreApplication.translate("MainWindow", u"Russian (Russia)", None))
        self.Nationality.setItemText(45, QCoreApplication.translate("MainWindow", u"Saudi (Saudi Arabia)", None))
        self.Nationality.setItemText(46, QCoreApplication.translate("MainWindow", u"Spanish (Spain)", None))
        self.Nationality.setItemText(47, QCoreApplication.translate("MainWindow", u"Syrian (Syria)", None))
        self.Nationality.setItemText(48, QCoreApplication.translate("MainWindow", u"Turkish (Turkey)", None))
        self.Nationality.setItemText(49, QCoreApplication.translate("MainWindow", u"Yemeni (Yemen)", None))

        self.CreateAccount.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
    # retranslateUi

