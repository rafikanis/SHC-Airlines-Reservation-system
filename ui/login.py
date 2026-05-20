# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1084, 672)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"border-image: url(:/wallpaper/images/wallpaperflare.com_wallpaper (2) (1).jpg);\n"
"}\n"
"#widget{\n"
"background-color:white;\n"
"}\n"
"QLabel {\n"
"color: #fff;\n"
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
"QPushButton:hover#LoginButton{\n"
"color:black;\n"
"}\n"
"QPushButton#SignUpButton {\n"
"border: none;\n"
"color: black;\n"
"}\n"
"QLabel#Email_4{\n"
"color:black;\n"
"}\n"
"QLabel#Password_4{\n"
"color:black;\n"
"}\n"
"\n"
"QLabel#LogIn_Label{\n"
"color:black;\n"
"}\n"
"QLabel#SignUpLabel{\n"
"color:black;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_3 = QSpacerItem(464, 56, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 5, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(263, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 4, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"Qlabel#LogIn_Label{\n"
"color:black;\n"
"}\n"
"\n"
"Qpushbutton{\n"
"color:black;\n"
"}")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.LogIn_Label = QLabel(self.widget)
        self.LogIn_Label.setObjectName(u"LogIn_Label")
        font = QFont()
        font.setPointSize(18)
        self.LogIn_Label.setFont(font)
        self.LogIn_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.LogIn_Label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Email_4 = QLabel(self.widget)
        self.Email_4.setObjectName(u"Email_4")
        font1 = QFont()
        font1.setPointSize(10)
        self.Email_4.setFont(font1)
        self.Email_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.Email_4)

        self.UsernameEntry = QLineEdit(self.widget)
        self.UsernameEntry.setObjectName(u"UsernameEntry")
        self.UsernameEntry.setMinimumSize(QSize(250, 0))
        font2 = QFont()
        font2.setPointSize(13)
        self.UsernameEntry.setFont(font2)

        self.verticalLayout.addWidget(self.UsernameEntry)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Password_4 = QLabel(self.widget)
        self.Password_4.setObjectName(u"Password_4")
        self.Password_4.setFont(font1)
        self.Password_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.Password_4)

        self.PasswordEntry = QLineEdit(self.widget)
        self.PasswordEntry.setObjectName(u"PasswordEntry")
        self.PasswordEntry.setFont(font2)
        self.PasswordEntry.setFrame(True)
        self.PasswordEntry.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.PasswordEntry)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.LoginButton = QPushButton(self.widget)
        self.LoginButton.setObjectName(u"LoginButton")
        font3 = QFont()
        font3.setPointSize(12)
        self.LoginButton.setFont(font3)
        self.LoginButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.LoginButton.setCheckable(False)

        self.verticalLayout_4.addWidget(self.LoginButton)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.SignUpLabel = QLabel(self.widget)
        self.SignUpLabel.setObjectName(u"SignUpLabel")
        self.SignUpLabel.setFont(font1)
        self.SignUpLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.SignUpLabel)

        self.SignUpButton = QPushButton(self.widget)
        self.SignUpButton.setObjectName(u"SignUpButton")
        font4 = QFont()
        font4.setUnderline(True)
        self.SignUpButton.setFont(font4)
        self.SignUpButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.SignUpButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 4, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(14)
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)

        self.Welcome = QLabel(self.centralwidget)
        self.Welcome.setObjectName(u"Welcome")
        font6 = QFont()
        font6.setPointSize(26)
        self.Welcome.setFont(font6)
        self.Welcome.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Welcome, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(264, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LogIn_Label.setText(QCoreApplication.translate("MainWindow", u"Already a user?, Log In", None))
        self.Email_4.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Password_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.SignUpLabel.setText(QCoreApplication.translate("MainWindow", u"Don't have an account yet?", None))
        self.SignUpButton.setText(QCoreApplication.translate("MainWindow", u"Sign Up Now!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Travel Anywhere, Anytime.", None))
        self.Welcome.setText(QCoreApplication.translate("MainWindow", u"Welcome to SHC Airlines", None))
    # retranslateUi

