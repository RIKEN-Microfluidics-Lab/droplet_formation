# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'droplet_gui_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Droplet_formation(object):
    def setupUi(self, Droplet_formation):
        Droplet_formation.setObjectName("Droplet_formation")
        Droplet_formation.resize(796, 669)
        self.centralwidget = QtWidgets.QWidget(Droplet_formation)
        self.centralwidget.setObjectName("centralwidget")
        self.recordButton = QtWidgets.QPushButton(self.centralwidget)
        self.recordButton.setGeometry(QtCore.QRect(90, 560, 90, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recordButton.setFont(font)
        self.recordButton.setObjectName("recordButton")
        self.valveLcd_1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.valveLcd_1.setGeometry(QtCore.QRect(200, 480, 120, 50))
        self.valveLcd_1.setObjectName("valveLcd_1")
        self.valveLcd_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.valveLcd_2.setGeometry(QtCore.QRect(540, 480, 120, 50))
        self.valveLcd_2.setObjectName("valveLcd_2")
        self.valveButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.valveButton_1.setGeometry(QtCore.QRect(90, 480, 90, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valveButton_1.setFont(font)
        self.valveButton_1.setObjectName("valveButton_1")
        self.valveButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.valveButton_2.setGeometry(QtCore.QRect(440, 480, 90, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valveButton_2.setFont(font)
        self.valveButton_2.setObjectName("valveButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 510, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 510, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        Droplet_formation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Droplet_formation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        Droplet_formation.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Droplet_formation)
        self.statusbar.setObjectName("statusbar")
        Droplet_formation.setStatusBar(self.statusbar)

        self.retranslateUi(Droplet_formation)
        self.recordButton.clicked.connect(Droplet_formation.slot1)
        self.valveButton_1.clicked.connect(Droplet_formation.slot2)
        self.valveButton_2.clicked.connect(Droplet_formation.slot3)
        QtCore.QMetaObject.connectSlotsByName(Droplet_formation)
        

    def retranslateUi(self, Droplet_formation):
        _translate = QtCore.QCoreApplication.translate
        Droplet_formation.setWindowTitle(_translate("Droplet_formation", "MainWindow"))
        self.recordButton.setText(_translate("Droplet_formation", "Record"))
        self.valveButton_1.setText(_translate("Droplet_formation", "Valve1"))
        self.valveButton_2.setText(_translate("Droplet_formation", "Valve2"))
        self.label.setText(_translate("Droplet_formation", "kPa"))
        self.label_2.setText(_translate("Droplet_formation", "kPa"))

