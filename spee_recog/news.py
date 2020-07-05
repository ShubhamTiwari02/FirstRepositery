# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'news.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newswindow(object):
    def setupUi(self, newswindow):
        newswindow.setObjectName("newswindow")
        newswindow.resize(726, 607)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newswindow.sizePolicy().hasHeightForWidth())
        newswindow.setSizePolicy(sizePolicy)
        newswindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(newswindow)
        self.centralwidget.setObjectName("centralwidget")
        self.news = QtWidgets.QLabel(self.centralwidget)
        self.news.setGeometry(QtCore.QRect(-60, -170, 1121, 781))
        self.news.setText("")
        self.news.setPixmap(QtGui.QPixmap("../../IMAGES/altitude-clouds-daylight-1450082.jpg"))
        self.news.setScaledContents(True)
        self.news.setObjectName("news")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 391, 31))
        self.label.setStyleSheet("font: 14pt \"Ravie\";\n"
"font: 81 14pt \"Rockwell Extra Bold\";")
        self.label.setObjectName("label")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 110, 671, 61))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.title.setText("")
        self.title.setScaledContents(True)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 671, 341))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 530, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 530, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.postname = QtWidgets.QLabel(self.centralwidget)
        self.postname.setGeometry(QtCore.QRect(20, 40, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.postname.setFont(font)
        self.postname.setText("")
        self.postname.setAlignment(QtCore.Qt.AlignCenter)
        self.postname.setObjectName("postname")
        self.postauthor = QtWidgets.QLabel(self.centralwidget)
        self.postauthor.setGeometry(QtCore.QRect(350, 40, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.postauthor.setFont(font)
        self.postauthor.setText("")
        self.postauthor.setAlignment(QtCore.Qt.AlignCenter)
        self.postauthor.setObjectName("postauthor")
        newswindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(newswindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 21))
        self.menubar.setObjectName("menubar")
        self.menuGO_BACK = QtWidgets.QMenu(self.menubar)
        self.menuGO_BACK.setObjectName("menuGO_BACK")
        newswindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(newswindow)
        self.statusBar.setObjectName("statusBar")
        newswindow.setStatusBar(self.statusBar)
        self.actionGO_BACK = QtWidgets.QAction(newswindow)
        self.actionGO_BACK.setObjectName("actionGO_BACK")
        self.actionEXIT = QtWidgets.QAction(newswindow)
        self.actionEXIT.setObjectName("actionEXIT")
        self.menuGO_BACK.addAction(self.actionGO_BACK)
        self.menuGO_BACK.addSeparator()
        self.menuGO_BACK.addAction(self.actionEXIT)
        self.menuGO_BACK.addSeparator()
        self.menubar.addAction(self.menuGO_BACK.menuAction())

        self.retranslateUi(newswindow)
        QtCore.QMetaObject.connectSlotsByName(newswindow)

    def retranslateUi(self, newswindow):
        _translate = QtCore.QCoreApplication.translate
        newswindow.setWindowTitle(_translate("newswindow", "MainWindow"))
        self.label.setText(_translate("newswindow", "See The Latest News Here........."))
        self.textEdit.setPlaceholderText(_translate("newswindow", "Read News Description Here..."))
        self.pushButton.setText(_translate("newswindow", "Previous"))
        self.pushButton_2.setText(_translate("newswindow", "Next"))
        self.menuGO_BACK.setTitle(_translate("newswindow", "Menu"))
        self.actionGO_BACK.setText(_translate("newswindow", "GoToMain!"))
        self.actionEXIT.setText(_translate("newswindow", "Exit!"))
