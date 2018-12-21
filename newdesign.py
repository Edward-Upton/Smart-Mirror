from PyQt5 import QtCore, QtSvg
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QGridLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
import sys
import time
from weather import Weather, Unit
import json

WINDOW_SIZE = [1024,1280]
with open("weatherDisplay.json", "r") as fp:
    WEATHER_DISPLAY_DICT = json.load(fp)

with open("defaultFonts.json", "r") as fp:
    DEFAULT_FONTS = json.load(fp)

class SmartMirrorApp(QMainWindow):
    def __init__(self, parent=None):
        # Initialising Super Class
        super(SmartMirrorApp, self).__init__(parent)
        # Window Initialisation
        self.mainWindow = QMainWindow()
        self.mainWindow.resize(WINDOW_SIZE[0], WINDOW_SIZE[1])
        self.mainWindow.showFullScreen()
        self.centralWidget = QWidget(self.mainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        self.centralWidget.setMaximumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        self.centralWidget.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralGridLayout = QGridLayout(self.centralWidget)
        # Creating 4 Widgets in Grid Layout
        self.TopLeft = QWidget(self.centralWidget)
        self.TopRight = QWidget(self.centralWidget)
        self.BottomLeft = QWidget(self.centralWidget)
        self.BottomRight = QWidget(self.centralWidget)
        self.centralGridLayout.addWidget(self.TopLeft, 0, 0)
        self.centralGridLayout.addWidget(self.TopRight, 0, 1)
        self.centralGridLayout.addWidget(self.BottomLeft, 1, 0)
        self.centralGridLayout.addWidget(self.BottomRight, 1, 1)
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
        # Final Setup Steps
        self.mainWindow.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)

    def create_time_widget(self):
        self.timeWidget = QWidget()
        self.timeLabel = QLabel(self.timeWidget)
        self.timeLabel.setGeometry(QRect(0,0,400,65))
        self.timeLabel.setStyleSheet("color:rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(50)
        font.setBold(True)
        font.setKerning(True)
        self.timeLabel.setFont(font)
    
    def create_weather_widget(self):
        self.weatherWidget = QWidget()
        self.weatherGridLayout = QGridLayout(self.weatherWidget)
        self.weatherWidget.setStyleSheet("color:rgb(255, 255, 255)")
        self.weatherLabelA1 = QLabel()
        self.weatherGridLayout.addWidget(self.weatherLabelA1, 0, 0)
        self.weatherLabelB1 = QLabel()
        self.weatherGridLayout.addWidget(self.weatherLabelB1, 1, 0)
        font = QtGui.QFont("Century Gothic", 20, QtGui.QFont.Bold)
        self.weatherLabelB1.setFont(font)
        self.weatherLabelB1.move(0,0)


def move_top_left(widget, form):
    w_widget = widget.geometry().width()
    h_widget = widget.geometry().height()
    geometryRect = QRect(0, 0, w_widget, h_widget)
    widget.setParent(form.TopLeft)
    widget.setGeometry(geometryRect)
def move_top_right(widget, form):
    w_widget = widget.geometry().width()
    h_widget = widget.geometry().height()
    x_2 = (WINDOW_SIZE[0]/2) - widget.geometry().width()
    geometryRect = QRect(x_2, 0, w_widget, h_widget)
    widget.setParent(form.TopRight)
    widget.setGeometry(geometryRect)
def move_bottom_left(widget, form):
    w_widget = widget.geometry().width()
    h_widget = widget.geometry().height()
    y_2 = (WINDOW_SIZE[1]/2) - widget.geometry().height()
    geometryRect = QRect(0, y_2, w_widget, h_widget)
    widget.setParent(form.BottomLeft)
    widget.setGeometry(geometryRect)
def move_bottom_right(widget, form):
    w_widget = widget.geometry().width()
    h_widget = widget.geometry().height()
    x_2 = (WINDOW_SIZE[0]/2) - widget.geometry().width()
    y_2 = (WINDOW_SIZE[1]/2) - widget.geometry().height()
    geometryRect = QRect(x_2, y_2, w_widget, h_widget)
    widget.setParent(form.BottomRight)
    widget.setGeometry(geometryRect)

def update_time_label(timeLabel):
    curTime = time.strftime("%H:%M:%S")
    timeLabel.setText(curTime)

def update_weather_widget(form, weather):
    WeatherInfo = weather.lookup(30076)
    weatherInfoDict = WeatherInfo.print_obj
    weatherImageFilename = WEATHER_DISPLAY_DICT["images"][weatherInfoDict["item"]["condition"]["code"]] + ".png"
    weatherPixmap = QPixmap("MirrorFiles/1x/%s" % weatherImageFilename).scaled(150,150, QtCore.Qt.KeepAspectRatio)
    form.weatherLabelA1.setPixmap(weatherPixmap)
    weatherText = weatherInfoDict["item"]["condition"]["text"]
    form.weatherLabelB1.setText(weatherText)
    with open("weatherTempData.json", "w") as fp:
        json.dump(weatherInfoDict, fp)


def main():
    app = QApplication(sys.argv)
    form = SmartMirrorApp()
    weather = Weather(unit=Unit.CELSIUS)
    form.create_time_widget()
    move_top_left(form.timeWidget, form)
    form.create_weather_widget()
    form.weatherWidget.setGeometry(QRect(0,0,500,300))
    
    move_top_right(form.weatherWidget, form)
    update_weather_widget(form, weather)
    weatherUpdateTimer = QtCore.QTimer()
    weatherUpdateTimer.timeout.connect(lambda: update_weather_widget(form, weather))
    weatherUpdateTimer.start(60000)
    timeUpdateTimer = QtCore.QTimer()
    timeUpdateTimer.timeout.connect(lambda: update_time_label(form.timeLabel))
    timeUpdateTimer.start(500)

    form.show()
    app.exec_()

if __name__ == '__main__':
    main()