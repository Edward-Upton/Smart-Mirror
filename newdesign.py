from PyQt5 import QtCore, QtSvg
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QGridLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
import sys
import time
from weather import Weather, Unit
from newsapi import NewsApiClient
import json
import flask

DEBUG = True
APP = flask.Flask(__name__)
APP.config.from_object(__name__)

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
        self.centralGridLayout.addWidget(self.TopLeft, 0, 0, 1, 1)
        self.centralGridLayout.addWidget(self.TopRight, 0, 1, 1, 1)
        self.centralGridLayout.addWidget(self.BottomLeft, 1, 0, 1, 1)
        self.centralGridLayout.addWidget(self.BottomRight, 1, 1, 1, 1)

        # Final Setup Steps
        self.mainWindow.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)
        pDesktop = QApplication.desktop()
        rectScreen2 = pDesktop.screenGeometry(2)

        self.mainWindow.move(rectScreen2.left(), rectScreen2.top())
        self.mainWindow.resize(rectScreen2.width(), rectScreen2.height())

    def create_news_widget(self):
        self.newsWidget = QWidget()
        self.newsWidget.setGeometry(QRect(0,0,500,200))
        self.newsWidget.setStyleSheet("color:rgb(255, 255, 255); font-family:Century Gothic,arial,sans-serif;")

        self.newsHeader = QLabel()
        self.newsHeader.setStyleSheet("font-size: 30px; font-weight: bold;")
        self.newsHeader.setGeometry(QRect(0,0,500,30))
        self.newsHeader.setParent(self.newsWidget)

        self.newsItem1Header = QLabel()
        self.newsItem1Header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.newsItem1Header.setGeometry(QRect(0,40,500,24))
        self.newsItem1Header.setParent(self.newsWidget)

        self.newsItem2Header = QLabel()
        self.newsItem2Header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.newsItem2Header.setGeometry(QRect(0,70,500,24))
        self.newsItem2Header.setParent(self.newsWidget)

        self.newsItem3Header = QLabel()
        self.newsItem3Header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.newsItem3Header.setGeometry(QRect(0,100,500,24))
        self.newsItem3Header.setParent(self.newsWidget)

        self.newsItem4Header = QLabel()
        self.newsItem4Header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.newsItem4Header.setGeometry(QRect(0,130,500,24))
        self.newsItem4Header.setParent(self.newsWidget)

        self.newsItem5Header = QLabel()
        self.newsItem5Header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.newsItem5Header.setGeometry(QRect(0,160,500,24))
        self.newsItem5Header.setParent(self.newsWidget)

    def create_time_widget(self):
        self.timeWidget = QWidget()
        self.timeWidget.setGeometry(QRect(0,0,410,150))
        self.timeLabel = QLabel()
        self.timeLabel.setStyleSheet("color:rgb(255, 255, 255); font-family:Century Gothic,arial,sans-serif; font-size: 100px; font-weight: bold;")
        self.timeLabel.setGeometry(QRect(0,0,400,100))
        self.timeLabel.setParent(self.timeWidget)
        self.dayLabel = QLabel()
        self.dayLabel.setStyleSheet("color:rgb(255, 255, 255); font-family:Century Gothic,arial,sans-serif; font-size: 50px;")
        self.dayLabel.setGeometry(QRect(0,100,400,50))
        self.dayLabel.setParent(self.timeWidget)
    
    def create_weather_widget(self):
        self.weatherWidget = QWidget()
        self.weatherWidget.setGeometry(QRect(0,0,512,181))
        self.weatherWidget.setStyleSheet("color:rgb(255, 255, 255); font-family:Century Gothic,arial,sans-serif;")

        # Forecast 1
        self.forecast1WeatherTitle = QLabel()
        self.forecast1WeatherTitle.setStyleSheet("font-size: 25px; font-weight: bold; text-align: centre;")
        self.forecast1WeatherTitle.setGeometry(QRect(0,0,90,40))
        self.forecast1WeatherTitle.setParent(self.weatherWidget)
        self.forecast1WeatherIcon = QLabel()
        self.forecast1WeatherIcon.setGeometry(QRect(0,41,90,100))
        self.forecast1WeatherIcon.setParent(self.weatherWidget)
        self.forecast1WeatherTemp = QLabel()
        self.forecast1WeatherTemp.setStyleSheet("font-size: 20px; text-align: centre;")
        self.forecast1WeatherTemp.setGeometry(QRect(0,142,90,30))
        self.forecast1WeatherTemp.setParent(self.weatherWidget)

        # Forecast 2
        self.forecast2WeatherTitle = QLabel()
        self.forecast2WeatherTitle.setStyleSheet("font-size: 25px; font-weight: bold; text-align: centre;")
        self.forecast2WeatherTitle.setGeometry(QRect(101,0,100,40))
        self.forecast2WeatherTitle.setParent(self.weatherWidget)
        self.forecast2WeatherIcon = QLabel()
        self.forecast2WeatherIcon.setGeometry(QRect(101,41,90,100))
        self.forecast2WeatherIcon.setParent(self.weatherWidget)
        self.forecast2WeatherTemp = QLabel()
        self.forecast2WeatherTemp.setStyleSheet("font-size: 20px; text-align: centre;")
        self.forecast2WeatherTemp.setGeometry(QRect(101,142,90,30))
        self.forecast2WeatherTemp.setParent(self.weatherWidget)

        # Forecast 3
        self.forecast3WeatherTitle = QLabel()
        self.forecast3WeatherTitle.setStyleSheet("font-size: 25px; font-weight: bold; text-align: centre;")
        self.forecast3WeatherTitle.setGeometry(QRect(202,0,90,40))
        self.forecast3WeatherTitle.setParent(self.weatherWidget)
        self.forecast3WeatherIcon = QLabel()
        self.forecast3WeatherIcon.setGeometry(QRect(202,41,90,100))
        self.forecast3WeatherIcon.setParent(self.weatherWidget)
        self.forecast3WeatherTemp = QLabel()
        self.forecast3WeatherTemp.setStyleSheet("font-size: 20px; text-align: centre;")
        self.forecast3WeatherTemp.setGeometry(QRect(202,142,90,30))
        self.forecast3WeatherTemp.setParent(self.weatherWidget)

        # Forecast 4
        self.forecast4WeatherTitle = QLabel()
        self.forecast4WeatherTitle.setStyleSheet("font-size: 25px; font-weight: bold; text-align: centre;")
        self.forecast4WeatherTitle.setGeometry(QRect(303,0,90,40))
        self.forecast4WeatherTitle.setParent(self.weatherWidget)
        self.forecast4WeatherIcon = QLabel()
        self.forecast4WeatherIcon.setGeometry(QRect(303,41,90,100))
        self.forecast4WeatherIcon.setParent(self.weatherWidget)
        self.forecast4WeatherTemp = QLabel()
        self.forecast4WeatherTemp.setStyleSheet("font-size: 20px; text-align: centre;")
        self.forecast4WeatherTemp.setGeometry(QRect(303,142,90,30))
        self.forecast4WeatherTemp.setParent(self.weatherWidget)

        # Forecast 5
        self.forecast5WeatherTitle = QLabel()
        self.forecast5WeatherTitle.setStyleSheet("font-size: 25px; font-weight: bold; text-align: centre;")
        self.forecast5WeatherTitle.setGeometry(QRect(404,0,90,40))
        self.forecast5WeatherTitle.setParent(self.weatherWidget)
        self.forecast5WeatherIcon = QLabel()
        self.forecast5WeatherIcon.setGeometry(QRect(404,41,90,100))
        self.forecast5WeatherIcon.setParent(self.weatherWidget)
        self.forecast5WeatherTemp = QLabel()
        self.forecast5WeatherTemp.setStyleSheet("font-size: 20px; text-align: centre;")
        self.forecast5WeatherTemp.setGeometry(QRect(404,142,90,30))
        self.forecast5WeatherTemp.setParent(self.weatherWidget)
        


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

def update_time_label(form):
    curTime = time.strftime("%H:%M:%S")
    form.timeLabel.setText(curTime)
    
    curDay = time.strftime("%a, %d %b")
    form.dayLabel.setText(curDay)

def forecast_weather_update(form, weatherDict):

    weatherWidgetElements = [[form.forecast1WeatherTitle, form.forecast1WeatherIcon, form.forecast1WeatherTemp],
                            [form.forecast2WeatherTitle, form.forecast2WeatherIcon, form.forecast2WeatherTemp],
                            [form.forecast3WeatherTitle, form.forecast3WeatherIcon, form.forecast3WeatherTemp],
                            [form.forecast4WeatherTitle, form.forecast4WeatherIcon, form.forecast4WeatherTemp],
                            [form.forecast5WeatherTitle, form.forecast5WeatherIcon, form.forecast5WeatherTemp]]
    i = 0
    for iter in weatherWidgetElements:
        forecastDayDict = weatherDict["item"]["forecast"][i]
        # Day
        if i == 0:
            forecastDay = "Today"
        else:
            forecastDay = "%s-%s" % (forecastDayDict["day"], forecastDayDict["date"][0:2])
        iter[0].setText(forecastDay)
        # Icon
        weatherImageFilename = WEATHER_DISPLAY_DICT["images"][forecastDayDict["code"]] + ".png"
        weatherPixmap = QPixmap("MirrorFiles/WeatherIcons/%s" % weatherImageFilename).scaled(90,90, QtCore.Qt.KeepAspectRatio)
        iter[1].setPixmap(weatherPixmap)
        # Temperature
        temperatureText = "%s° / %s°" % (forecastDayDict["high"], forecastDayDict["low"])
        iter[2].setText(temperatureText)

        i = i + 1


def update_weather_widget(form, weather):
    WeatherInfo = weather.lookup(30076)
    weatherDict = WeatherInfo.print_obj
    forecast_weather_update(form, weatherDict)
    with open("weatherTempData.json", "w") as fp:
        json.dump(weatherDict, fp)

def update_news_widget(form, newsapi):
    newsWidgetElements = [[form.newsItem1Header],
                        [form.newsItem2Header],
                        [form.newsItem3Header],
                        [form.newsItem4Header],
                        [form.newsItem5Header]]
    topHeadlines = newsapi.get_top_headlines(sources='bbc-news')

    form.newsHeader.setText("BBC News")

    i = 0
    for iter in newsWidgetElements:
        iter[0].setText(topHeadlines["articles"][i]["title"])
        i = i + 1

    with open("newsTempData.json", "w") as fp:
        json.dump(topHeadlines, fp)

def main():
    app = QApplication(sys.argv)
    form = SmartMirrorApp()

    form.create_time_widget()
    move_top_right(form.timeWidget, form)
    timeUpdateTimer = QtCore.QTimer()
    timeUpdateTimer.timeout.connect(lambda: update_time_label(form))
    timeUpdateTimer.start(500)

    weather = Weather(unit=Unit.CELSIUS)
    form.create_weather_widget()
    move_top_left(form.weatherWidget, form)
    update_weather_widget(form, weather)
    weatherUpdateTimer = QtCore.QTimer()
    weatherUpdateTimer.timeout.connect(lambda: update_weather_widget(form, weather))
    weatherUpdateTimer.start(60000)

    newsapi = NewsApiClient(api_key='a151e158d26740219c7d611284d01989')
    form.create_news_widget()
    move_bottom_right(form.newsWidget, form)
    update_news_widget(form, newsapi)
    newsUpdateTimer = QtCore.QTimer()
    newsUpdateTimer.timeout.connect(lambda: update_news_widget(form, newsapi))
    newsUpdateTimer.start(180000)

    APP.run(host="0.0.0.0", port=80, debug=DEBUG)
    app.exec_()

if __name__ == '__main__':
    main()