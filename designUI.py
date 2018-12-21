# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\edupt\Documents\Raspberry Pi Stuff\first.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, WindowSize):
        MainWindow.resize(WindowSize[0], WindowSize[1])
        MainWindow.showFullScreen()
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setMinimumSize(QtCore.QSize(WindowSize[0], WindowSize[1]))
        self.CentralWidget.setMaximumSize(QtCore.QSize(WindowSize[0], WindowSize[1]))
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
        self.weatherGridLayout = QtWidgets.QGridLayout()
        self.weatherWidget.setStyleSheet("color:rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(40)
        font.setBold(True)
        font.setKerning(True)
        self.weatherLabelA1 = QLabel()
        self.weatherGridLayout.addWidget(self.weatherLabelA1,0,0)
        self.weatherGridLayout.addWidget(QLabel(),0,1)
        self.weatherGridLayout.addWidget(QLabel(),0,2)
        self.weatherGridLayout.addWidget(QLabel(),0,3)
        self.weatherGridLayout.addWidget(QLabel(),0,4)
        self.weatherGridLayout.addWidget(QLabel(),0,5)
        self.weatherGridLayout.addWidget(QLabel(),1,0)
        self.weatherGridLayout.addWidget(QLabel(),1,1)
        self.weatherGridLayout.addWidget(QLabel(),1,2)
        self.weatherGridLayout.addWidget(QLabel(),1,3)
        self.weatherGridLayout.addWidget(QLabel(),1,4)
        self.weatherGridLayout.addWidget(QLabel(),1,5)
        self.weatherWidget.setLayout(self.weatherGridLayout)


    
    def calendar(self):
        pass

    