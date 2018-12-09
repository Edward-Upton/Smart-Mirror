from PyQt5 import QtCore, QtSvg
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
import sys
import time
from weather import Weather, Unit
import json

import designUI

WINDOW_SIZE = [1024,1280]

class ExampleApp(QMainWindow, designUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self, WINDOW_SIZE)

def moveTopLeft(widget, form):
    w_widget = widget.geometry().width()
    h_widget = widget.geometry().height()
    geometryRect = QRect(0, 0, 400, 65)
    widget.setParent(form.TopLeft)
    widget.setGeometry(geometryRect)
def moveTopRight(widget, form):
    w_widget = widget.geometry().width()
    h_widget = widget.geometry().height()
    x_2 = (WINDOW_SIZE[0]/2) - widget.geometry().width()
    geometryRect = QRect(x_2, 0, w_widget, h_widget)
    widget.setParent(form.TopRight)
    widget.setGeometry(geometryRect)
def moveBottomLeft(widget, form):
    w_widget = widget.geometry().width()
    h_widget = widget.geometry().height()
    y_2 = (WINDOW_SIZE[1]/2) - widget.geometry().height()
    geometryRect = QRect(0, y_2, w_widget, h_widget)
    widget.setParent(form.BottomLeft)
    widget.setGeometry(geometryRect)
def moveBottomRight(widget, form):
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

def update_weather_widget(weatherWidget, weather):
    WeatherInfo = weather.lookup(30076)
    weatherInfoDict = WeatherInfo.print_obj
    with open("weatherTempData.json", "w") as fp:
        json.dump(weatherInfoDict, fp)


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    weather = Weather(unit=Unit.CELSIUS)
    form.createTimeWidget()
    moveTopLeft(form.timeLabel, form)
    form.createWeatherWidget()
    form.weatherWidget.setGeometry(QRect(0,0,500,300))
    pixmap = QPixmap("MirrorFiles/1x/Sunny.png").scaled(200,200, QtCore.Qt.KeepAspectRatio)
    sunnyIcon = QLabel(form.weatherWidget)
    sunnyIcon.setPixmap(pixmap)
    moveTopRight(form.weatherWidget, form)
    update_weather_widget(form.weatherWidget, weather)
    weatherUpdateTimer = QtCore.QTimer()
    weatherUpdateTimer.timeout.connect(lambda: update_weather_widget(form.weatherWidget, weather))
    weatherUpdateTimer.start(900000)
    timeUpdateTimer = QtCore.QTimer()
    timeUpdateTimer.timeout.connect(lambda: update_time_label(form.timeLabel))
    timeUpdateTimer.start(500)

    form.show()
    app.exec_()

if __name__ == '__main__':
    main()