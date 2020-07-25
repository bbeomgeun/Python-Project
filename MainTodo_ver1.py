# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Todolist_Stack.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background : white")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1_login = QtWidgets.QWidget()
        self.page1_login.setObjectName("page1_login")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page1_login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 110, 391, 513))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Page_Login = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Page_Login.setContentsMargins(0, 0, 0, 0)
        self.Page_Login.setObjectName("Page_Login")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setStyleSheet("backgroundcolor : rgba(255, 255, 255, 0)")
        self.textEdit.setObjectName("textEdit")
        self.Page_Login.addWidget(self.textEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.text_ID = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.text_ID.setObjectName("text_ID")
        self.gridLayout.addWidget(self.text_ID, 1, 1, 1, 1)
        self.text_PW = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.text_PW.setText("")
        self.text_PW.setObjectName("text_PW")
        self.gridLayout.addWidget(self.text_PW, 2, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 0, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 2, 0, 1, 1)
        self.Page_Login.addLayout(self.gridLayout)
        self.text_status = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.text_status.setObjectName("text_status")
        self.Page_Login.addWidget(self.text_status)
        self.Button_LogIn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_LogIn.setStyleSheet("background:rgbrgb(127, 127, 127);\n"
"color:rgb(248, 248, 248);")
        self.Button_LogIn.setObjectName("Button_LogIn")
        self.Page_Login.addWidget(self.Button_LogIn)
        self.Button_register = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_register.setStyleSheet("background:rgbrgb(127, 127, 127);\n"
"color:rgb(248, 248, 248);")
        self.Button_register.setObjectName("Button_register")
        self.Page_Login.addWidget(self.Button_register)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setStyleSheet("background:rgbrgb(255, 255, 0)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.Page_Login.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background:rgb(0, 255, 0)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.Page_Login.addWidget(self.pushButton_2)
        self.stackedWidget.addWidget(self.page1_login)
        self.page2_main = QtWidgets.QWidget()
        self.page2_main.setObjectName("page2_main")
        self.scrollArea = QtWidgets.QScrollArea(self.page2_main)
        self.scrollArea.setGeometry(QtCore.QRect(190, 30, 741, 681))
        self.scrollArea.setStyleSheet("background : rgb(48, 48, 48);\n"
"background-attachment: scroll;\n"
"")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 679))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit_7 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_7.setGeometry(QtCore.QRect(560, 140, 151, 51))
        self.textEdit_7.setObjectName("textEdit_7")
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setGeometry(QtCore.QRect(59, 459, 611, 80))
        self.widget_3.setStyleSheet("background : rgb(165, 165, 165)")
        self.widget_3.setObjectName("widget_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_3.setGeometry(QtCore.QRect(560, 10, 41, 61))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.textEdit_11 = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_11.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.textEdit_11.setObjectName("textEdit_11")
        self.progressBar_3 = QtWidgets.QProgressBar(self.widget_3)
        self.progressBar_3.setGeometry(QtCore.QRect(0, 40, 461, 23))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setTextVisible(True)
        self.progressBar_3.setObjectName("progressBar_3")
        self.textEdit_10 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_10.setGeometry(QtCore.QRect(209, 399, 41, 61))
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_9 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_9.setGeometry(QtCore.QRect(59, 399, 151, 61))
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_6 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_6.setGeometry(QtCore.QRect(59, 129, 151, 61))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_5 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_5.setGeometry(QtCore.QRect(209, 129, 41, 61))
        self.textEdit_5.setObjectName("textEdit_5")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(59, 189, 611, 80))
        self.widget.setStyleSheet("background : rgb(165, 165, 165)")
        self.widget.setObjectName("widget")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(560, 10, 41, 61))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.textEdit_4 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(0, 40, 461, 23))
        self.progressBar.setProperty("value", 70)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setGeometry(QtCore.QRect(59, 559, 611, 80))
        self.widget_4.setStyleSheet("background : rgb(165, 165, 165)")
        self.widget_4.setObjectName("widget_4")
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget_4)
        self.checkBox_4.setGeometry(QtCore.QRect(560, 10, 41, 61))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.textEdit_12 = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit_12.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.textEdit_12.setObjectName("textEdit_12")
        self.progressBar_4 = QtWidgets.QProgressBar(self.widget_4)
        self.progressBar_4.setGeometry(QtCore.QRect(0, 40, 461, 23))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setTextVisible(True)
        self.progressBar_4.setObjectName("progressBar_4")
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setGeometry(QtCore.QRect(59, 289, 611, 80))
        self.widget_2.setStyleSheet("background : rgb(165, 165, 165)")
        self.widget_2.setObjectName("widget_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_2.setGeometry(QtCore.QRect(560, 10, 41, 61))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.textEdit_8 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_8.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.textEdit_8.setObjectName("textEdit_8")
        self.progressBar_2 = QtWidgets.QProgressBar(self.widget_2)
        self.progressBar_2.setGeometry(QtCore.QRect(0, 40, 461, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setObjectName("progressBar_2")
        self.textEdit_40 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_40.setGeometry(QtCore.QRect(60, 30, 511, 71))
        self.textEdit_40.setObjectName("textEdit_40")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page2_main)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 29, 160, 681))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text_hello = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.text_hello.setObjectName("text_hello")
        self.verticalLayout_2.addWidget(self.text_hello)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.button_finish = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button_finish.setObjectName("button_finish")
        self.verticalLayout_2.addWidget(self.button_finish)
        self.button_setting = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button_setting.setObjectName("button_setting")
        self.verticalLayout_2.addWidget(self.button_setting)
        self.button_add = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button_add.setObjectName("button_add")
        self.verticalLayout_2.addWidget(self.button_add)
        self.stackedWidget.addWidget(self.page2_main)
        self.page3_finish = QtWidgets.QWidget()
        self.page3_finish.setObjectName("page3_finish")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page3_finish)
        self.scrollArea_2.setGeometry(QtCore.QRect(140, 20, 771, 701))
        self.scrollArea_2.setStyleSheet("background : rgb(48, 48, 48)")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 769, 699))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.textEdit_13 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_13.setGeometry(QtCore.QRect(350, 30, 81, 61))
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_14.setGeometry(QtCore.QRect(310, 30, 41, 61))
        self.textEdit_14.setObjectName("textEdit_14")
        self.textEdit_15 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_15.setGeometry(QtCore.QRect(30, 30, 271, 61))
        self.textEdit_15.setObjectName("textEdit_15")
        self.textEdit_16 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_16.setGeometry(QtCore.QRect(560, 120, 151, 51))
        self.textEdit_16.setObjectName("textEdit_16")
        self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_5.setGeometry(QtCore.QRect(59, 459, 611, 80))
        self.widget_5.setStyleSheet("background : rgb(165, 165, 165)")
        self.widget_5.setObjectName("widget_5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget_5)
        self.checkBox_5.setGeometry(QtCore.QRect(560, 10, 41, 61))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.textEdit_17 = QtWidgets.QTextEdit(self.widget_5)
        self.textEdit_17.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.textEdit_17.setObjectName("textEdit_17")
        self.progressBar_5 = QtWidgets.QProgressBar(self.widget_5)
        self.progressBar_5.setGeometry(QtCore.QRect(0, 40, 461, 23))
        self.progressBar_5.setProperty("value", 100)
        self.progressBar_5.setTextVisible(True)
        self.progressBar_5.setObjectName("progressBar_5")
        self.textEdit_18 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_18.setGeometry(QtCore.QRect(209, 399, 41, 61))
        self.textEdit_18.setObjectName("textEdit_18")
        self.textEdit_19 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_19.setGeometry(QtCore.QRect(59, 399, 151, 61))
        self.textEdit_19.setObjectName("textEdit_19")
        self.textEdit_20 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_20.setGeometry(QtCore.QRect(59, 129, 151, 61))
        self.textEdit_20.setObjectName("textEdit_20")
        self.textEdit_21 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_21.setGeometry(QtCore.QRect(209, 129, 41, 61))
        self.textEdit_21.setObjectName("textEdit_21")
        self.widget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_6.setGeometry(QtCore.QRect(59, 189, 611, 80))
        self.widget_6.setStyleSheet("background : rgb(165, 165, 165)")
        self.widget_6.setObjectName("widget_6")
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget_6)
        self.checkBox_6.setGeometry(QtCore.QRect(560, 10, 41, 61))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.textEdit_22 = QtWidgets.QTextEdit(self.widget_6)
        self.textEdit_22.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.textEdit_22.setObjectName("textEdit_22")
        self.progressBar_6 = QtWidgets.QProgressBar(self.widget_6)
        self.progressBar_6.setGeometry(QtCore.QRect(0, 40, 461, 23))
        self.progressBar_6.setProperty("value", 100)
        self.progressBar_6.setTextVisible(True)
        self.progressBar_6.setObjectName("progressBar_6")
        self.widget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_7.setGeometry(QtCore.QRect(59, 559, 611, 80))
        self.widget_7.setStyleSheet("background : rgb(165, 165, 165)")
        self.widget_7.setObjectName("widget_7")
        self.checkBox_7 = QtWidgets.QCheckBox(self.widget_7)
        self.checkBox_7.setGeometry(QtCore.QRect(560, 10, 41, 61))
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.textEdit_23 = QtWidgets.QTextEdit(self.widget_7)
        self.textEdit_23.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.textEdit_23.setObjectName("textEdit_23")
        self.progressBar_7 = QtWidgets.QProgressBar(self.widget_7)
        self.progressBar_7.setGeometry(QtCore.QRect(0, 40, 461, 23))
        self.progressBar_7.setProperty("value", 100)
        self.progressBar_7.setTextVisible(True)
        self.progressBar_7.setObjectName("progressBar_7")
        self.widget_8 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_8.setGeometry(QtCore.QRect(59, 289, 611, 80))
        self.widget_8.setStyleSheet("background : rgb(165, 165, 165)")
        self.widget_8.setObjectName("widget_8")
        self.checkBox_8 = QtWidgets.QCheckBox(self.widget_8)
        self.checkBox_8.setGeometry(QtCore.QRect(560, 10, 41, 61))
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.textEdit_24 = QtWidgets.QTextEdit(self.widget_8)
        self.textEdit_24.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.textEdit_24.setObjectName("textEdit_24")
        self.progressBar_8 = QtWidgets.QProgressBar(self.widget_8)
        self.progressBar_8.setGeometry(QtCore.QRect(0, 40, 461, 23))
        self.progressBar_8.setProperty("value", 100)
        self.progressBar_8.setTextVisible(True)
        self.progressBar_8.setObjectName("progressBar_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 50, 171, 28))
        self.pushButton_7.setStyleSheet("color : white")
        self.pushButton_7.setObjectName("pushButton_7")
        self.page3_toMain = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.page3_toMain.setGeometry(QtCore.QRect(580, 660, 161, 28))
        self.page3_toMain.setStyleSheet("color : white")
        self.page3_toMain.setObjectName("page3_toMain")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.page3_finish)
        self.page4_setting = QtWidgets.QWidget()
        self.page4_setting.setObjectName("page4_setting")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page4_setting)
        self.scrollArea_3.setGeometry(QtCore.QRect(70, 40, 771, 701))
        self.scrollArea_3.setStyleSheet("background : rgb(48, 48, 48)")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 769, 699))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.textEdit_25 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_25.setGeometry(QtCore.QRect(30, 30, 271, 61))
        self.textEdit_25.setObjectName("textEdit_25")
        self.textEdit_26 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_26.setGeometry(QtCore.QRect(30, 130, 231, 61))
        self.textEdit_26.setObjectName("textEdit_26")
        self.textEdit_28 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_28.setGeometry(QtCore.QRect(30, 230, 231, 51))
        self.textEdit_28.setStyleSheet("color : white")
        self.textEdit_28.setObjectName("textEdit_28")
        self.textEdit_29 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_29.setGeometry(QtCore.QRect(30, 310, 331, 61))
        self.textEdit_29.setStyleSheet("color : white")
        self.textEdit_29.setObjectName("textEdit_29")
        self.textEdit_30 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_30.setGeometry(QtCore.QRect(420, 130, 101, 51))
        self.textEdit_30.setStyleSheet("color:white")
        self.textEdit_30.setObjectName("textEdit_30")
        self.textEdit_31 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_31.setGeometry(QtCore.QRect(560, 130, 121, 51))
        self.textEdit_31.setStyleSheet("color:white")
        self.textEdit_31.setObjectName("textEdit_31")
        self.checkBox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_9.setGeometry(QtCore.QRect(470, 240, 31, 41))
        self.checkBox_9.setText("")
        self.checkBox_9.setIconSize(QtCore.QSize(50, 50))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_10.setGeometry(QtCore.QRect(610, 240, 31, 41))
        self.checkBox_10.setText("")
        self.checkBox_10.setIconSize(QtCore.QSize(50, 50))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_11.setGeometry(QtCore.QRect(470, 310, 31, 41))
        self.checkBox_11.setText("")
        self.checkBox_11.setIconSize(QtCore.QSize(50, 50))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_12.setGeometry(QtCore.QRect(610, 310, 31, 41))
        self.checkBox_12.setText("")
        self.checkBox_12.setIconSize(QtCore.QSize(50, 50))
        self.checkBox_12.setObjectName("checkBox_12")
        self.page4_toMain = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.page4_toMain.setGeometry(QtCore.QRect(480, 420, 161, 28))
        self.page4_toMain.setStyleSheet("color : white")
        self.page4_toMain.setObjectName("page4_toMain")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget.addWidget(self.page4_setting)
        self.page5_add = QtWidgets.QWidget()
        self.page5_add.setObjectName("page5_add")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.page5_add)
        self.scrollArea_4.setGeometry(QtCore.QRect(70, 30, 811, 701))
        self.scrollArea_4.setStyleSheet("background : rgb(48, 48, 48)")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 809, 699))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.textEdit_35 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_35.setGeometry(QtCore.QRect(30, 30, 361, 61))
        self.textEdit_35.setStyleSheet("color : white")
        self.textEdit_35.setObjectName("textEdit_35")
        self.textEdit_36 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_36.setGeometry(QtCore.QRect(30, 120, 121, 61))
        self.textEdit_36.setObjectName("textEdit_36")
        self.textEdit_37 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_37.setGeometry(QtCore.QRect(30, 370, 231, 61))
        self.textEdit_37.setObjectName("textEdit_37")
        self.textEdit_38 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_38.setGeometry(QtCore.QRect(30, 200, 171, 61))
        self.textEdit_38.setObjectName("textEdit_38")
        self.text_subject = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.text_subject.setGeometry(QtCore.QRect(220, 120, 221, 61))
        self.text_subject.setText("")
        self.text_subject.setObjectName("text_subject")
        self.text_date = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.text_date.setGeometry(QtCore.QRect(220, 200, 221, 61))
        self.text_date.setText("")
        self.text_date.setObjectName("text_date")
        self.text_detail = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.text_detail.setGeometry(QtCore.QRect(30, 450, 571, 151))
        self.text_detail.setText("")
        self.text_detail.setObjectName("text_detail")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.scrollAreaWidgetContents_4)
        self.calendarWidget.setGeometry(QtCore.QRect(450, 120, 351, 251))
        self.calendarWidget.setObjectName("calendarWidget")
        self.page5_toMain = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.page5_toMain.setGeometry(QtCore.QRect(610, 620, 161, 28))
        self.page5_toMain.setStyleSheet("color : white")
        self.page5_toMain.setObjectName("page5_toMain")
        self.date_save = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.date_save.setGeometry(QtCore.QRect(420, 620, 161, 28))
        self.date_save.setStyleSheet("color : white")
        self.date_save.setObjectName("date_save")
        self.add_currentDate = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_4)
        self.add_currentDate.setGeometry(QtCore.QRect(420, 30, 361, 61))
        self.add_currentDate.setStyleSheet("color : white")
        self.add_currentDate.setObjectName("add_currentDate")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.stackedWidget.addWidget(self.page5_add)
        self.page6_register = QtWidgets.QWidget()
        self.page6_register.setObjectName("page6_register")
        self.widget_9 = QtWidgets.QWidget(self.page6_register)
        self.widget_9.setGeometry(QtCore.QRect(20, 10, 911, 691))
        self.widget_9.setStyleSheet("")
        self.widget_9.setObjectName("widget_9")
        self.textEdit_32 = QtWidgets.QTextEdit(self.widget_9)
        self.textEdit_32.setGeometry(QtCore.QRect(100, 160, 211, 51))
        self.textEdit_32.setReadOnly(True)
        self.textEdit_32.setObjectName("textEdit_32")
        self.textEdit_27 = QtWidgets.QTextEdit(self.widget_9)
        self.textEdit_27.setGeometry(QtCore.QRect(90, 40, 511, 87))
        self.textEdit_27.setReadOnly(True)
        self.textEdit_27.setObjectName("textEdit_27")
        self.register_ID = QtWidgets.QLineEdit(self.widget_9)
        self.register_ID.setGeometry(QtCore.QRect(330, 160, 261, 51))
        self.register_ID.setObjectName("register_ID")
        self.textEdit_33 = QtWidgets.QTextEdit(self.widget_9)
        self.textEdit_33.setGeometry(QtCore.QRect(100, 260, 211, 51))
        self.textEdit_33.setReadOnly(True)
        self.textEdit_33.setObjectName("textEdit_33")
        self.register_PW = QtWidgets.QLineEdit(self.widget_9)
        self.register_PW.setGeometry(QtCore.QRect(330, 260, 261, 51))
        self.register_PW.setObjectName("register_PW")
        self.register_save = QtWidgets.QPushButton(self.widget_9)
        self.register_save.setGeometry(QtCore.QRect(140, 370, 161, 28))
        self.register_save.setStyleSheet("color : black")
        self.register_save.setObjectName("register_save")
        self.register_cancel = QtWidgets.QPushButton(self.widget_9)
        self.register_cancel.setGeometry(QtCore.QRect(330, 370, 161, 28))
        self.register_cancel.setStyleSheet("color : black")
        self.register_cancel.setObjectName("register_cancel")
        self.id_warning = QtWidgets.QTextEdit(self.widget_9)
        self.id_warning.setGeometry(QtCore.QRect(100, 220, 491, 31))
        self.id_warning.setObjectName("id_warning")
        self.pw_warning = QtWidgets.QTextEdit(self.widget_9)
        self.pw_warning.setGeometry(QtCore.QRect(100, 320, 491, 31))
        self.pw_warning.setObjectName("pw_warning")
        self.stackedWidget.addWidget(self.page6_register)
        self.page7_onedayResult = QtWidgets.QWidget()
        self.page7_onedayResult.setObjectName("page7_onedayResult")
        self.stackedWidget.addWidget(self.page7_onedayResult)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Member Login</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">ID</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">PW</span></p></body></html>"))
        self.Button_LogIn.setText(_translate("MainWindow", "로그인"))
        self.Button_register.setText(_translate("MainWindow", "회원가입"))
        self.pushButton_3.setText(_translate("MainWindow", "카카오 로그인"))
        self.pushButton_2.setText(_translate("MainWindow", "네이버 로그인"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#f9f9f9;\">완료</span></p></body></html>"))
        self.textEdit_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">- 팀 프로젝트 모임</span></p></body></html>"))
        self.progressBar_3.setFormat(_translate("MainWindow", "%p-DAY"))
        self.textEdit_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#fafafa;\">0</span></p></body></html>"))
        self.textEdit_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#fcfcfc;\">● 약속</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#fcfcfc;\">● 과제</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#fafafa;\">0</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">- 파이썬 스터디 과제</span></p></body></html>"))
        self.progressBar.setFormat(_translate("MainWindow", "%p-DAY"))
        self.textEdit_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">- ~~~~~~~~</span></p></body></html>"))
        self.progressBar_4.setFormat(_translate("MainWindow", "%p-DAY"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">- ~~~~~~~~</span></p></body></html>"))
        self.progressBar_2.setFormat(_translate("MainWindow", "%p-DAY"))
        self.textEdit_40.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#f9f9f9;\">To Do LIST</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.button_finish.setText(_translate("MainWindow", "완료한 일"))
        self.button_setting.setText(_translate("MainWindow", "환경설정"))
        self.button_add.setText(_translate("MainWindow", "일정 추가하기"))
        self.textEdit_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#fafafa;\">개</span></p></body></html>"))
        self.textEdit_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#fafafa;\">0</span></p></body></html>"))
        self.textEdit_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#fdfdfd;\">완료한 일</span></p></body></html>"))
        self.textEdit_16.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#f9f9f9;\">완료</span></p></body></html>"))
        self.textEdit_17.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">- 팀 프로젝트 모임</span></p></body></html>"))
        self.progressBar_5.setFormat(_translate("MainWindow", "%p-DAY"))
        self.textEdit_18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#fafafa;\">0</span></p></body></html>"))
        self.textEdit_19.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#fcfcfc;\">● 약속</span></p></body></html>"))
        self.textEdit_20.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#fcfcfc;\">● 과제</span></p></body></html>"))
        self.textEdit_21.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#fafafa;\">0</span></p></body></html>"))
        self.textEdit_22.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">- 파이썬 스터디 과제</span></p></body></html>"))
        self.progressBar_6.setFormat(_translate("MainWindow", "%p-DAY"))
        self.textEdit_23.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">- ~~~~~~~~</span></p></body></html>"))
        self.progressBar_7.setFormat(_translate("MainWindow", "%p-DAY"))
        self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">- ~~~~~~~~</span></p></body></html>"))
        self.progressBar_8.setFormat(_translate("MainWindow", "%p-DAY"))
        self.pushButton_7.setText(_translate("MainWindow", "기간 설정"))
        self.page3_toMain.setText(_translate("MainWindow", "메인으로 돌아가기"))
        self.textEdit_25.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#f8f8f8;\">환경설정</span></p></body></html>"))
        self.textEdit_26.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#fcfcfc;\">- 테마 설정</span></p></body></html>"))
        self.textEdit_28.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">막대 그래프 표시 여부</span></p></body></html>"))
        self.textEdit_29.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">막대 그래프 색 적용</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">(일정에 가까워질수록 차등 색 적용)</span></p></body></html>"))
        self.textEdit_30.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">예</span></p></body></html>"))
        self.textEdit_31.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">아니오</span></p></body></html>"))
        self.page4_toMain.setText(_translate("MainWindow", "메인으로 돌아가기"))
        self.textEdit_35.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">일정 추가 / 수정</span></p></body></html>"))
        self.textEdit_36.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#fcfcfc;\">- 제목</span></p></body></html>"))
        self.textEdit_37.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#fcfcfc;\">- 세부 설명</span></p></body></html>"))
        self.textEdit_38.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#fcfcfc;\">- 마감일</span></p></body></html>"))
        self.page5_toMain.setText(_translate("MainWindow", "메인으로 돌아가기"))
        self.date_save.setText(_translate("MainWindow", "저장하기"))
        self.add_currentDate.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_32.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">아이디</p></body></html>"))
        self.textEdit_27.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">환영합니다!</span></p></body></html>"))
        self.textEdit_33.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">비밀번호</p></body></html>"))
        self.register_save.setText(_translate("MainWindow", "저장하기"))
        self.register_cancel.setText(_translate("MainWindow", "취소"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

