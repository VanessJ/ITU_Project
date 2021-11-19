# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerOKdtxc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(190, 80, 241, 61))
        font = QFont()
        font.setPointSize(24)
        self.label_name.setFont(font)
        self.label_temperature = QLabel(self.centralwidget)
        self.label_temperature.setObjectName(u"label_temperature")
        self.label_temperature.setGeometry(QRect(200, 190, 241, 61))
        self.label_temperature.setFont(font)
        self.label_nas = QLabel(self.centralwidget)
        self.label_nas.setObjectName(u"label_nas")
        self.label_nas.setGeometry(QRect(210, 250, 241, 61))
        self.label_nas.setFont(font)
        self.label_time = QLabel(self.centralwidget)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(190, 130, 241, 61))
        self.label_time.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"N\u00e1zov stroja", None))
        self.label_temperature.setText(QCoreApplication.translate("MainWindow", u"Teplota", None))
        self.label_nas.setText(QCoreApplication.translate("MainWindow", u"NAS", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"Doba be\u017eania", None))
    # retranslateUi

