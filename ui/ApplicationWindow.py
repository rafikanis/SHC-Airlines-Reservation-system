# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ApplicationWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 730)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.DisplayPage = QWidget(self.centralwidget)
        self.DisplayPage.setObjectName(u"DisplayPage")
        self.verticalLayout_3 = QVBoxLayout(self.DisplayPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.Header = QWidget(self.DisplayPage)
        self.Header.setObjectName(u"Header")
        self.horizontalLayout = QHBoxLayout(self.Header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.HelloMessage = QLabel(self.Header)
        self.HelloMessage.setObjectName(u"HelloMessage")
        font = QFont()
        font.setPointSize(18)
        self.HelloMessage.setFont(font)
        self.HelloMessage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.HelloMessage)

        self.horizontalSpacer = QSpacerItem(693, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.Header)

        self.DisplayStack = QStackedWidget(self.DisplayPage)
        self.DisplayStack.setObjectName(u"DisplayStack")
        font1 = QFont()
        font1.setPointSize(12)
        self.DisplayStack.setFont(font1)
        self.DisplayStack.setStyleSheet(u"\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"")
        self.SearchPage = QWidget()
        self.SearchPage.setObjectName(u"SearchPage")
        self.SearchPage.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"     color: gray;\n"
"     background-color: rgb(224, 238, 249);\n"
"}\n"
"\n"
"QComboBox:hover\n"
"{\n"
"   background-color: rgb(224, 238, 249);\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.SearchPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.SearchPage)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 91, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(25)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Email_13 = QLabel(self.SearchPage)
        self.Email_13.setObjectName(u"Email_13")
        font3 = QFont()
        font3.setPointSize(14)
        self.Email_13.setFont(font3)
        self.Email_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.Email_13)

        self.DepartureAirport = QComboBox(self.SearchPage)
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.setObjectName(u"DepartureAirport")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DepartureAirport.sizePolicy().hasHeightForWidth())
        self.DepartureAirport.setSizePolicy(sizePolicy)
        self.DepartureAirport.setMinimumSize(QSize(400, 0))
        font4 = QFont()
        font4.setPointSize(16)
        self.DepartureAirport.setFont(font4)
        self.DepartureAirport.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.DepartureAirport.setStyleSheet(u"QComboBox {\n"
"     border-radius: 5px;\n"
"     border: 1px solid gray;\n"
"}")

        self.verticalLayout_11.addWidget(self.DepartureAirport)


        self.verticalLayout_7.addLayout(self.verticalLayout_11)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Email_12 = QLabel(self.SearchPage)
        self.Email_12.setObjectName(u"Email_12")
        self.Email_12.setFont(font3)
        self.Email_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.Email_12)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.DepartureDate = QDateEdit(self.SearchPage)
        self.DepartureDate.setObjectName(u"DepartureDate")
        self.DepartureDate.setMinimumSize(QSize(250, 0))
        self.DepartureDate.setFont(font4)
        self.DepartureDate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.DepartureDate)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(25)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Email_10 = QLabel(self.SearchPage)
        self.Email_10.setObjectName(u"Email_10")
        self.Email_10.setFont(font3)
        self.Email_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.Email_10)

        self.ArrivalAirport = QComboBox(self.SearchPage)
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.setObjectName(u"ArrivalAirport")
        sizePolicy.setHeightForWidth(self.ArrivalAirport.sizePolicy().hasHeightForWidth())
        self.ArrivalAirport.setSizePolicy(sizePolicy)
        self.ArrivalAirport.setMinimumSize(QSize(400, 0))
        self.ArrivalAirport.setFont(font4)
        self.ArrivalAirport.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ArrivalAirport.setStyleSheet(u"QComboBox {\n"
"     border-radius: 5px;\n"
"     border: 1px solid gray;\n"
"}")

        self.verticalLayout_8.addWidget(self.ArrivalAirport)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Email_11 = QLabel(self.SearchPage)
        self.Email_11.setObjectName(u"Email_11")
        self.Email_11.setFont(font3)
        self.Email_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.Email_11)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ClassSelect = QComboBox(self.SearchPage)
        self.ClassSelect.addItem("")
        self.ClassSelect.addItem("")
        self.ClassSelect.addItem("")
        self.ClassSelect.setObjectName(u"ClassSelect")
        sizePolicy.setHeightForWidth(self.ClassSelect.sizePolicy().hasHeightForWidth())
        self.ClassSelect.setSizePolicy(sizePolicy)
        self.ClassSelect.setMinimumSize(QSize(250, 0))
        self.ClassSelect.setFont(font4)
        self.ClassSelect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ClassSelect.setStyleSheet(u"QComboBox {\n"
"     border-radius: 5px;\n"
"     border: 1px solid gray;\n"
"}")

        self.horizontalLayout_4.addWidget(self.ClassSelect)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 27, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 3, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.SearchButton = QPushButton(self.SearchPage)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SearchButton.sizePolicy().hasHeightForWidth())
        self.SearchButton.setSizePolicy(sizePolicy1)
        self.SearchButton.setMinimumSize(QSize(100, 30))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(False)
        self.SearchButton.setFont(font5)
        self.SearchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SearchButton.setMouseTracking(False)
        self.SearchButton.setStyleSheet(u" border-radius: 5px;\n"
" border: 1px solid gray;")
        self.SearchButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.SearchButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 170, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 5, 1, 1, 1)

        self.DisplayStack.addWidget(self.SearchPage)
        self.SearchResults = QWidget()
        self.SearchResults.setObjectName(u"SearchResults")
        self.SearchResults.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"color:gray;   \n"
"background-color: rgb(224, 238, 249);\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.SearchResults)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Resulttree = QTreeWidget(self.SearchResults)
        self.Resulttree.setObjectName(u"Resulttree")
        self.Resulttree.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Resulttree.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Resulttree.header().setMinimumSectionSize(49)
        self.Resulttree.header().setDefaultSectionSize(141)
        self.Resulttree.header().setHighlightSections(True)

        self.verticalLayout_15.addWidget(self.Resulttree)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.ReserveSelected = QPushButton(self.SearchResults)
        self.ReserveSelected.setObjectName(u"ReserveSelected")
        self.ReserveSelected.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ReserveSelected.sizePolicy().hasHeightForWidth())
        self.ReserveSelected.setSizePolicy(sizePolicy1)
        self.ReserveSelected.setMinimumSize(QSize(100, 30))
        self.ReserveSelected.setFont(font5)
        self.ReserveSelected.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ReserveSelected.setMouseTracking(False)
        self.ReserveSelected.setStyleSheet(u" border-radius: 5px;\n"
" border: 1px solid gray;\n"
"hover-color: #55aaff;")
        self.ReserveSelected.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.ReserveSelected)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)


        self.verticalLayout_15.addLayout(self.horizontalLayout_6)

        self.DisplayStack.addWidget(self.SearchResults)
        self.HistoryPage = QWidget()
        self.HistoryPage.setObjectName(u"HistoryPage")
        self.gridLayout_4 = QGridLayout(self.HistoryPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Historytree = QTreeWidget(self.HistoryPage)
        self.Historytree.setObjectName(u"Historytree")
        self.Historytree.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Historytree.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Historytree.header().setMinimumSectionSize(49)
        self.Historytree.header().setDefaultSectionSize(141)
        self.Historytree.header().setHighlightSections(True)

        self.gridLayout_4.addWidget(self.Historytree, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.CancelTicket = QPushButton(self.HistoryPage)
        self.CancelTicket.setObjectName(u"CancelTicket")
        self.CancelTicket.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.CancelTicket.sizePolicy().hasHeightForWidth())
        self.CancelTicket.setSizePolicy(sizePolicy1)
        self.CancelTicket.setMinimumSize(QSize(100, 30))
        self.CancelTicket.setFont(font5)
        self.CancelTicket.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CancelTicket.setMouseTracking(False)
        self.CancelTicket.setStyleSheet(u" border-radius: 5px;\n"
" border: 1px solid gray;\n"
"hover-color: #55aaff;")
        self.CancelTicket.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.CancelTicket)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.DisplayStack.addWidget(self.HistoryPage)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.gridLayout_6 = QGridLayout(self.ProfilePage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea = QScrollArea(self.ProfilePage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 950, 605))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(184, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(183, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_9, 1, 4, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 151, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 2, 2, 1, 2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Email_4 = QLabel(self.scrollAreaWidgetContents)
        self.Email_4.setObjectName(u"Email_4")
        font6 = QFont()
        font6.setPointSize(10)
        self.Email_4.setFont(font6)
        self.Email_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.Email_4)

        self.FullName = QLabel(self.scrollAreaWidgetContents)
        self.FullName.setObjectName(u"FullName")
        self.FullName.setMinimumSize(QSize(250, 0))
        self.FullName.setSizeIncrement(QSize(0, 0))
        font7 = QFont()
        font7.setPointSize(13)
        self.FullName.setFont(font7)

        self.verticalLayout_13.addWidget(self.FullName)


        self.verticalLayout_12.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.Email_5 = QLabel(self.scrollAreaWidgetContents)
        self.Email_5.setObjectName(u"Email_5")
        self.Email_5.setFont(font6)
        self.Email_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.Email_5)

        self.Username = QLabel(self.scrollAreaWidgetContents)
        self.Username.setObjectName(u"Username")
        self.Username.setMinimumSize(QSize(250, 0))
        self.Username.setSizeIncrement(QSize(0, 0))
        self.Username.setFont(font7)

        self.verticalLayout_14.addWidget(self.Username)


        self.verticalLayout_12.addLayout(self.verticalLayout_14)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.Password_4 = QLabel(self.scrollAreaWidgetContents)
        self.Password_4.setObjectName(u"Password_4")
        self.Password_4.setFont(font6)
        self.Password_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.Password_4)

        self.NationalID = QLabel(self.scrollAreaWidgetContents)
        self.NationalID.setObjectName(u"NationalID")
        self.NationalID.setMinimumSize(QSize(500, 0))
        self.NationalID.setSizeIncrement(QSize(0, 0))
        self.NationalID.setFont(font7)

        self.verticalLayout_16.addWidget(self.NationalID)


        self.verticalLayout_12.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.Password_9 = QLabel(self.scrollAreaWidgetContents)
        self.Password_9.setObjectName(u"Password_9")
        self.Password_9.setFont(font6)
        self.Password_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_17.addWidget(self.Password_9)

        self.PhoneNumber = QLabel(self.scrollAreaWidgetContents)
        self.PhoneNumber.setObjectName(u"PhoneNumber")
        self.PhoneNumber.setMinimumSize(QSize(500, 0))
        self.PhoneNumber.setSizeIncrement(QSize(0, 0))
        self.PhoneNumber.setFont(font7)

        self.verticalLayout_17.addWidget(self.PhoneNumber)


        self.verticalLayout_12.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.Password_14 = QLabel(self.scrollAreaWidgetContents)
        self.Password_14.setObjectName(u"Password_14")
        self.Password_14.setFont(font6)
        self.Password_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.Password_14)

        self.PassportNumber = QLabel(self.scrollAreaWidgetContents)
        self.PassportNumber.setObjectName(u"PassportNumber")
        self.PassportNumber.setMinimumSize(QSize(500, 0))
        self.PassportNumber.setFont(font7)

        self.verticalLayout_18.addWidget(self.PassportNumber)


        self.verticalLayout_12.addLayout(self.verticalLayout_18)


        self.verticalLayout_10.addLayout(self.verticalLayout_12)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.Password_10 = QLabel(self.scrollAreaWidgetContents)
        self.Password_10.setObjectName(u"Password_10")
        self.Password_10.setFont(font6)
        self.Password_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.Password_10)

        self.BirthDate = QLabel(self.scrollAreaWidgetContents)
        self.BirthDate.setObjectName(u"BirthDate")
        self.BirthDate.setMinimumSize(QSize(500, 0))
        self.BirthDate.setFont(font7)

        self.verticalLayout_20.addWidget(self.BirthDate)


        self.verticalLayout_10.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.Password_12 = QLabel(self.scrollAreaWidgetContents)
        self.Password_12.setObjectName(u"Password_12")
        self.Password_12.setFont(font6)
        self.Password_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_21.addWidget(self.Password_12)

        self.Gender = QLabel(self.scrollAreaWidgetContents)
        self.Gender.setObjectName(u"Gender")
        self.Gender.setMinimumSize(QSize(500, 0))
        self.Gender.setFont(font7)

        self.verticalLayout_21.addWidget(self.Gender)


        self.verticalLayout_10.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.Password_13 = QLabel(self.scrollAreaWidgetContents)
        self.Password_13.setObjectName(u"Password_13")
        self.Password_13.setFont(font6)
        self.Password_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.Password_13)

        self.MainNationality = QLabel(self.scrollAreaWidgetContents)
        self.MainNationality.setObjectName(u"MainNationality")
        self.MainNationality.setMinimumSize(QSize(500, 0))
        self.MainNationality.setFont(font7)

        self.verticalLayout_22.addWidget(self.MainNationality)


        self.verticalLayout_10.addLayout(self.verticalLayout_22)


        self.gridLayout_5.addLayout(self.verticalLayout_10, 1, 3, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.DisplayStack.addWidget(self.ProfilePage)

        self.verticalLayout_3.addWidget(self.DisplayStack)


        self.gridLayout.addWidget(self.DisplayPage, 0, 1, 1, 1)

        self.MenuBar = QWidget(self.centralwidget)
        self.MenuBar.setObjectName(u"MenuBar")
        self.MenuBar.setStyleSheet(u"QWidget{\n"
"background-color: rgb(43, 45, 49);\n"
"}\n"
"\n"
"QPushButton{\n"
"height:30px;\n"
"color:white;\n"
"border:none;\n"
"padding-left:10px;\n"
"text-align:left;\n"
"border-top-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(43, 45, 49);\n"
"font-weight:bold;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.MenuBar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 12, -1, -1)
        self.Menu_2 = QLabel(self.MenuBar)
        self.Menu_2.setObjectName(u"Menu_2")
        font8 = QFont()
        font8.setPointSize(18)
        font8.setKerning(True)
        self.Menu_2.setFont(font8)
        self.Menu_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-right:9px;")
        self.Menu_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Menu_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 140, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.BookingPage = QPushButton(self.MenuBar)
        self.BookingPage.setObjectName(u"BookingPage")
        self.BookingPage.setMinimumSize(QSize(0, 20))
        self.BookingPage.setFont(font1)
        self.BookingPage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BookingPage.setCheckable(True)
        self.BookingPage.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.BookingPage)

        self.History = QPushButton(self.MenuBar)
        self.History.setObjectName(u"History")
        self.History.setMinimumSize(QSize(0, 20))
        self.History.setFont(font1)
        self.History.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.History.setCheckable(True)
        self.History.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.History)

        self.Profile = QPushButton(self.MenuBar)
        self.Profile.setObjectName(u"Profile")
        self.Profile.setMinimumSize(QSize(0, 20))
        self.Profile.setFont(font1)
        self.Profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Profile.setCheckable(True)
        self.Profile.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Profile)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 287, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.LogOut = QPushButton(self.MenuBar)
        self.LogOut.setObjectName(u"LogOut")
        font9 = QFont()
        font9.setPointSize(10)
        font9.setUnderline(False)
        self.LogOut.setFont(font9)
        self.LogOut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.LogOut)


        self.gridLayout.addWidget(self.MenuBar, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.DisplayStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.HelloMessage.setText(QCoreApplication.translate("MainWindow", u"  Hello, User  ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search flights", None))
        self.Email_13.setText(QCoreApplication.translate("MainWindow", u"Departure Airport", None))
        self.DepartureAirport.setItemText(0, "")
        self.DepartureAirport.setItemText(1, QCoreApplication.translate("MainWindow", u"Abu Dhabi International Airport (AUH) \u2013 United Arab Emirates", None))
        self.DepartureAirport.setItemText(2, QCoreApplication.translate("MainWindow", u"Aden International Airport (ADE) \u2013 Yemen", None))
        self.DepartureAirport.setItemText(3, QCoreApplication.translate("MainWindow", u"Algiers Houari Boumediene Airport (ALG) \u2013 Algeria", None))
        self.DepartureAirport.setItemText(4, QCoreApplication.translate("MainWindow", u"Baghdad International Airport (BGW) \u2013 Iraq", None))
        self.DepartureAirport.setItemText(5, QCoreApplication.translate("MainWindow", u"Bahrain International Airport (BAH) \u2013 Bahrain", None))
        self.DepartureAirport.setItemText(6, QCoreApplication.translate("MainWindow", u"Beirut-Rafic Hariri International Airport (BEY) \u2013 Lebanon", None))
        self.DepartureAirport.setItemText(7, QCoreApplication.translate("MainWindow", u"Cairo International Airport (CAI) \u2013 Egypt", None))
        self.DepartureAirport.setItemText(8, QCoreApplication.translate("MainWindow", u"Casablanca Mohammed V International Airport (CMN) \u2013 Morocco", None))
        self.DepartureAirport.setItemText(9, QCoreApplication.translate("MainWindow", u"Djibouti\u2013Ambouli International Airport (JIB) \u2013 Djibouti", None))
        self.DepartureAirport.setItemText(10, QCoreApplication.translate("MainWindow", u"Dubai International Airport (DXB) \u2013 United Arab Emirates", None))
        self.DepartureAirport.setItemText(11, QCoreApplication.translate("MainWindow", u"Damascus International Airport (DAM) \u2013 Syria", None))
        self.DepartureAirport.setItemText(12, QCoreApplication.translate("MainWindow", u"Hamad International Airport (DOH) \u2013 Qatar", None))
        self.DepartureAirport.setItemText(13, QCoreApplication.translate("MainWindow", u"Khartoum International Airport (KRT) \u2013 Sudan", None))
        self.DepartureAirport.setItemText(14, QCoreApplication.translate("MainWindow", u"King Abdulaziz International Airport (JED) \u2013 Jeddah, Saudi Arabia", None))
        self.DepartureAirport.setItemText(15, QCoreApplication.translate("MainWindow", u"King Khalid International Airport (RUH) \u2013 Riyadh, Saudi Arabia", None))
        self.DepartureAirport.setItemText(16, QCoreApplication.translate("MainWindow", u"Kuwait International Airport (KWI) \u2013 Kuwait", None))
        self.DepartureAirport.setItemText(17, QCoreApplication.translate("MainWindow", u"Luxor International Airport (LXR) \u2013 Egypt", None))
        self.DepartureAirport.setItemText(18, QCoreApplication.translate("MainWindow", u"Marsa Alam International Airport (RMF) \u2013 Egypt", None))
        self.DepartureAirport.setItemText(19, QCoreApplication.translate("MainWindow", u"Mitiga International Airport (MJI) \u2013 Tripoli, Libya", None))
        self.DepartureAirport.setItemText(20, QCoreApplication.translate("MainWindow", u"Muscat International Airport (MCT) \u2013 Oman", None))

        self.Email_12.setText(QCoreApplication.translate("MainWindow", u"Date Of Departure", None))
        self.Email_10.setText(QCoreApplication.translate("MainWindow", u"Arrival Airport", None))
        self.ArrivalAirport.setItemText(0, "")
        self.ArrivalAirport.setItemText(1, QCoreApplication.translate("MainWindow", u"Abu Dhabi International Airport (AUH) \u2013 United Arab Emirates", None))
        self.ArrivalAirport.setItemText(2, QCoreApplication.translate("MainWindow", u"Aden International Airport (ADE) \u2013 Yemen", None))
        self.ArrivalAirport.setItemText(3, QCoreApplication.translate("MainWindow", u"Algiers Houari Boumediene Airport (ALG) \u2013 Algeria", None))
        self.ArrivalAirport.setItemText(4, QCoreApplication.translate("MainWindow", u"Baghdad International Airport (BGW) \u2013 Iraq", None))
        self.ArrivalAirport.setItemText(5, QCoreApplication.translate("MainWindow", u"Bahrain International Airport (BAH) \u2013 Bahrain", None))
        self.ArrivalAirport.setItemText(6, QCoreApplication.translate("MainWindow", u"Beirut-Rafic Hariri International Airport (BEY) \u2013 Lebanon", None))
        self.ArrivalAirport.setItemText(7, QCoreApplication.translate("MainWindow", u"Cairo International Airport (CAI) \u2013 Egypt", None))
        self.ArrivalAirport.setItemText(8, QCoreApplication.translate("MainWindow", u"Casablanca Mohammed V International Airport (CMN) \u2013 Morocco", None))
        self.ArrivalAirport.setItemText(9, QCoreApplication.translate("MainWindow", u"Djibouti\u2013Ambouli International Airport (JIB) \u2013 Djibouti", None))
        self.ArrivalAirport.setItemText(10, QCoreApplication.translate("MainWindow", u"Dubai International Airport (DXB) \u2013 United Arab Emirates", None))
        self.ArrivalAirport.setItemText(11, QCoreApplication.translate("MainWindow", u"Damascus International Airport (DAM) \u2013 Syria", None))
        self.ArrivalAirport.setItemText(12, QCoreApplication.translate("MainWindow", u"Hamad International Airport (DOH) \u2013 Qatar", None))
        self.ArrivalAirport.setItemText(13, QCoreApplication.translate("MainWindow", u"Khartoum International Airport (KRT) \u2013 Sudan", None))
        self.ArrivalAirport.setItemText(14, QCoreApplication.translate("MainWindow", u"King Abdulaziz International Airport (JED) \u2013 Jeddah, Saudi Arabia", None))
        self.ArrivalAirport.setItemText(15, QCoreApplication.translate("MainWindow", u"King Khalid International Airport (RUH) \u2013 Riyadh, Saudi Arabia", None))
        self.ArrivalAirport.setItemText(16, QCoreApplication.translate("MainWindow", u"Kuwait International Airport (KWI) \u2013 Kuwait", None))
        self.ArrivalAirport.setItemText(17, QCoreApplication.translate("MainWindow", u"Luxor International Airport (LXR) \u2013 Egypt", None))
        self.ArrivalAirport.setItemText(18, QCoreApplication.translate("MainWindow", u"Marsa Alam International Airport (RMF) \u2013 Egypt", None))
        self.ArrivalAirport.setItemText(19, QCoreApplication.translate("MainWindow", u"Mitiga International Airport (MJI) \u2013 Tripoli, Libya", None))
        self.ArrivalAirport.setItemText(20, QCoreApplication.translate("MainWindow", u"Muscat International Airport (MCT) \u2013 Oman", None))

        self.Email_11.setText(QCoreApplication.translate("MainWindow", u"Seat Class", None))
        self.ClassSelect.setItemText(0, "")
        self.ClassSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"Business Class", None))
        self.ClassSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"Economy", None))

        self.SearchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtreewidgetitem = self.Resulttree.headerItem()
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Available Seats", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Departure time", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Arrival Airport", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Departure Airport", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Flight ID", None));
        self.ReserveSelected.setText(QCoreApplication.translate("MainWindow", u"Reserve", None))
        ___qtreewidgetitem1 = self.Historytree.headerItem()
        ___qtreewidgetitem1.setText(7, QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MainWindow", u"Available Seats", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Departure time", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Arrival Airport", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Departure Airport", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Flight ID", None));
        self.CancelTicket.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.Email_4.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.FullName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Email_5.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Username.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Password_4.setText(QCoreApplication.translate("MainWindow", u"National ID", None))
        self.NationalID.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Password_9.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.PhoneNumber.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Password_14.setText(QCoreApplication.translate("MainWindow", u"Passport Number", None))
        self.PassportNumber.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Password_10.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.BirthDate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Password_12.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.Gender.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Password_13.setText(QCoreApplication.translate("MainWindow", u"Main Nationality", None))
        self.MainNationality.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Menu_2.setText(QCoreApplication.translate("MainWindow", u"Menu ", None))
        self.BookingPage.setText(QCoreApplication.translate("MainWindow", u"Book a flight!     ", None))
        self.History.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.Profile.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.LogOut.setText(QCoreApplication.translate("MainWindow", u"      LogOut!", None))
    # retranslateUi

