import sys
from PyQt5.QtCore import QRect, QMetaObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont


class SmartMirrorForm(QMainWindow):
    def __init__(self, parent=None):

        super(SmartMirrorForm, self).__init__(parent)
        self.widgetsList = []
        self.mainWindow = QMainWindow()
        desktopWidget = QApplication.desktop()
        numScreens = desktopWidget.screenCount()
        screenQRect = desktopWidget.screenGeometry(numScreens - 1)
        self.mainWindow.move(screenQRect.left(), screenQRect.top())
        self.mainWindow.resize(screenQRect.width(), screenQRect.height())
        self.mainWindow.showFullScreen()

        self.centralWidget = QWidget(self.mainWindow)
        self.centralWidget.setStyleSheet('background-color:black')
        self.centralWidget.resize(self.mainWindow.width(), self.mainWindow.height())
       
        self.mainWindow.setCentralWidget(self.centralWidget)
        QMetaObject.connectSlotsByName(self.mainWindow)

        self.create_time_widget()
        self.create_news_widget()
        self.create_weather_widget()

    def create_time_widget(self):

        self.timeWidget = QWidget(self.centralWidget)
        self.timeWidgetLocation = 'topLeft'
        self.timeWidget.setObjectName('timeWidget')
        self.widgetsList.append(self.timeWidget)
        self.timeWidget.setGeometry(QRect(0, 0, self.centralWidget.width()/2, (self.centralWidget.width()/2)/2.7))
        self.timeLabel = QLabel(self.timeWidget)
        self.timeLabel.setGeometry(QRect(0, 0, self.timeWidget.width(), (self.timeWidget.height()/3)*2))
        self.timeLabel.setStyleSheet("color:rgb(255, 255, 255); font-family:Century Gothic,arial,sans-serif; font-weight: bold;")
        timeLabelFont = self.timeLabel.font()
        timeLabelFont.setPixelSize(((self.timeWidget.height()/3)*2)-5)
        self.timeLabel.setFont(timeLabelFont)
        self.timeLabel.setText('17:53:59')
        
        self.dayLabel = QLabel(self.timeWidget)
        self.dayLabel.setGeometry(QRect(0, (self.timeWidget.height()/3)*2, self.timeWidget.width(), (self.timeWidget.height()/3)))
        self.dayLabel.setStyleSheet("color:rgb(255, 255, 255); font-family:Century Gothic,arial,sans-serif;")
        dayLabelFont = self.dayLabel.font()
        dayLabelFont.setPixelSize((self.timeWidget.height()/3)-5)
        self.dayLabel.setFont(dayLabelFont)
        self.dayLabel.setText('Mon, 08 Apr')

    def create_news_widget(self):

        self.newsWidget = QWidget(self.centralWidget)
        self.newsWidgetLocation = 'topLeft'
        self.newsWidget.setObjectName('newsWidget')
        self.widgetsList.append(self.newsWidget)
        self.newsWidget.setGeometry(QRect(0, 0, self.centralWidget.width() / 2, (self.centralWidget.width()/2) / 2.5))
        self.newsWidget.setStyleSheet("color:rgb(255, 255, 255); font-family:Century Gothic,arial,sans-serif;")

        self.newsHeader = QLabel(self.newsWidget)
        self.newsHeader.setStyleSheet("font-size: 30px; font-weight: bold;")
        self.newsHeader.setGeometry(QRect(0,0,self.centralWidget.width() / 2,30))

        self.newsItem1Header = QLabel(self.newsWidget)
        self.newsItem1Header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.newsItem1Header.setGeometry(QRect(0,40,self.centralWidget.width() / 2,24))

        self.newsItem2Header = QLabel(self.newsWidget)
        self.newsItem2Header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.newsItem2Header.setGeometry(QRect(0,70,self.centralWidget.width() / 2,24))

        self.newsItem3Header = QLabel(self.newsWidget)
        self.newsItem3Header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.newsItem3Header.setGeometry(QRect(0,100,self.centralWidget.width() / 2,24))

        self.newsItem4Header = QLabel(self.newsWidget)
        self.newsItem4Header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.newsItem4Header.setGeometry(QRect(0,130,self.centralWidget.width() / 2,24))

        self.newsItem5Header = QLabel(self.newsWidget)
        self.newsItem5Header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.newsItem5Header.setGeometry(QRect(0,160,self.centralWidget.width() / 2,24))
    
    def create_weather_widget(self):
        
        self.weatherWidget = QWidget(self.centralWidget)
        self.weatherWidgetLocation = 0
        self.weatherWidget.setObjectName('weatherWidget')
        self.widgetsList.append(self.weatherWidget)
        self.weatherWidget.setGeometry(QRect(0, 0, self.centralWidget.width() / 2, 181))
        self.weatherWidget.setStyleSheet("color:rgb(255, 255, 255); font-family:Century Gothic,arial,sans-serif;")

        # Forecast 1
        self.forecast1WeatherTitle = QLabel(self.weatherWidget)
        self.forecast1WeatherTitle.setStyleSheet("font-size: 22px; font-weight: bold; text-align: centre;")
        self.forecast1WeatherTitle.setGeometry(QRect(0,0,90,40))
        self.forecast1WeatherIcon = QLabel(self.weatherWidget)
        self.forecast1WeatherIcon.setGeometry(QRect(0,41,90,100))
        self.forecast1WeatherTemp = QLabel(self.weatherWidget)
        self.forecast1WeatherTemp.setStyleSheet("font-size: 20px; text-align: centre;")
        self.forecast1WeatherTemp.setGeometry(QRect(0,142,90,30))

        # Forecast 2
        self.forecast2WeatherTitle = QLabel(self.weatherWidget)
        self.forecast2WeatherTitle.setStyleSheet("font-size: 22px; font-weight: bold; text-align: centre;")
        self.forecast2WeatherTitle.setGeometry(QRect((self.weatherWidget.width() / 5) * 1,0,100,40))
        self.forecast2WeatherIcon = QLabel(self.weatherWidget)
        self.forecast2WeatherIcon.setGeometry(QRect((self.weatherWidget.width() / 5) * 1,41,90,100))
        self.forecast2WeatherTemp = QLabel(self.weatherWidget)
        self.forecast2WeatherTemp.setStyleSheet("font-size: 20px; text-align: centre;")
        self.forecast2WeatherTemp.setGeometry(QRect((self.weatherWidget.width() / 5) * 1,142,90,30))

        # Forecast 3
        self.forecast3WeatherTitle = QLabel(self.weatherWidget)
        self.forecast3WeatherTitle.setStyleSheet("font-size: 22px; font-weight: bold; text-align: centre;")
        self.forecast3WeatherTitle.setGeometry(QRect((self.weatherWidget.width() / 5) * 2,0,90,40))
        self.forecast3WeatherIcon = QLabel(self.weatherWidget)
        self.forecast3WeatherIcon.setGeometry(QRect((self.weatherWidget.width() / 5) * 2,41,90,100))
        self.forecast3WeatherTemp = QLabel(self.weatherWidget)
        self.forecast3WeatherTemp.setStyleSheet("font-size: 20px; text-align: centre;")
        self.forecast3WeatherTemp.setGeometry(QRect((self.weatherWidget.width() / 5) * 2,142,90,30))

        # Forecast 4
        self.forecast4WeatherTitle = QLabel(self.weatherWidget)
        self.forecast4WeatherTitle.setStyleSheet("font-size: 22px; font-weight: bold; text-align: centre;")
        self.forecast4WeatherTitle.setGeometry(QRect((self.weatherWidget.width() / 5) * 3, 0,90,40))
        self.forecast4WeatherIcon = QLabel(self.weatherWidget)
        self.forecast4WeatherIcon.setGeometry(QRect((self.weatherWidget.width() / 5) * 3 ,41,90,100))
        self.forecast4WeatherTemp = QLabel(self.weatherWidget)
        self.forecast4WeatherTemp.setStyleSheet("font-size: 20px; text-align: centre;")
        self.forecast4WeatherTemp.setGeometry(QRect((self.weatherWidget.width() / 5) * 3, 142,90,30))
        # Forecast 5
        self.forecast5WeatherTitle = QLabel(self.weatherWidget)
        self.forecast5WeatherTitle.setStyleSheet("font-size: 22px; font-weight: bold; text-align: centre;")
        self.forecast5WeatherTitle.setGeometry(QRect((self.weatherWidget.width() / 5) * 4,0,90,40))
        self.forecast5WeatherIcon = QLabel(self.weatherWidget)
        self.forecast5WeatherIcon.setGeometry(QRect((self.weatherWidget.width() / 5) * 4,41,90,100))
        self.forecast5WeatherTemp = QLabel(self.weatherWidget)
        self.forecast5WeatherTemp.setStyleSheet("font-size: 20px; text-align: centre;")
        self.forecast5WeatherTemp.setGeometry(QRect((self.weatherWidget.width() / 5) * 4,142,90,30))
        
    def move_top_left(self, widget):
        widget.setGeometry(QRect(0, 0, widget.width(), widget.height()))
        widget.setParent(self.centralWidget)

    def move_top_right(self, widget):
        widget.setGeometry(QRect(self.centralWidget.width()/2, 0, widget.width(), widget.height()))
        widget.setParent(self.centralWidget)

    def move_bottom_left(self, widget):
        widget.setGeometry(QRect(0, self.centralWidget.height() - widget.height(), widget.width(), widget.height()))
        widget.setParent(self.centralWidget)

    def move_bottom_right(self, widget):
        widget.setGeometry(QRect(self.centralWidget.width()/2, self.centralWidget.height() - widget.height(), widget.width(), widget.height()))
        widget.setParent(self.centralWidget)

    def toggle_visibility(self, widget):
        if widget.isVisible():
            widget.setVisible(False)
        else:
            widget.setVisible(True)