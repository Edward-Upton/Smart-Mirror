# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\edupt\Documents\Raspberry Pi Stuff\first.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1024, 1280)
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setMinimumSize(QtCore.QSize(1024, 1239))
        self.CentralWidget.setMaximumSize(QtCore.QSize(1024, 1239))
        self.CentralWidget.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.GridLayout = QtWidgets.QGridLayout(self.CentralWidget)

        # Creating 4 Widgets in Grid Layout
        self.TopLeft = QtWidgets.QWidget(self.CentralWidget)
        self.TopRight = QtWidgets.QWidget(self.CentralWidget)
        self.BottomLeft = QtWidgets.QWidget(self.CentralWidget)
        self.BottomRight = QtWidgets.QWidget(self.CentralWidget)
        self.GridLayout.addWidget(self.TopLeft, 0, 0, 1, 1)
        self.GridLayout.addWidget(self.TopRight, 0, 1, 1, 1)
        self.GridLayout.addWidget(self.BottomLeft, 1, 0, 1, 1)
        self.GridLayout.addWidget(self.BottomRight, 1, 1, 1, 1)

        # Default Font Settings
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.TopLeft.setFont(font)
        self.TopRight.setFont(font)
        self.BottomLeft.setFont(font)
        self.BottomRight.setFont(font)
       
        MainWindow.setCentralWidget(self.CentralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label.setText(_translate("MainWindow", "10:50"))
        # self.label_2.setText(_translate("MainWindow", "TextLabel"))

    def createTimeWidget(self):
        self.timeLabel = QLabel()
        self.timeLabel.setStyleSheet("color:rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(50)
        font.setBold(True)
        font.setKerning(True)
        self.timeLabel.setFont(font)
    
    def createWeatherWidget(self):
        self.weatherWidget = QWidget()
        self.weatherWidget.setStyleSheet("color:rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(40)
        font.setBold(True)
        font.setKerning(True)
        self.weatherWidget.setFont(font)
    
    def calendar(self):
        pass

    