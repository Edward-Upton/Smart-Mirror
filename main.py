from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
import sys, time, requests, threading
from datetime import datetime
from newsapi.newsapi_client import NewsApiClient
from flask import Flask, render_template, request, redirect

from SmartMirrorForm import SmartMirrorForm

NEWSAPI_KEY = 'a151e158d26740219c7d611284d01989'
WEATHERAPI_KEY = '49831b5dbeb1aa231811dcfb0de29888'
WEATHERAPI_LOCATION = 'Newcastle Emlyn'

FLASK_APP = Flask(__name__)
FLASK_APP.config.from_object(__name__)

@FLASK_APP.route('/', methods=['GET', 'POST'])
def index():
    return render_template('edit-smart-mirror.html')

@FLASK_APP.route('/control-widget-update', methods=['GET', 'POST'])
def control_update():
    print(request.form)
    for widget in qtApplication.qtForm.widgetsList:
        if widget.objectName() in request.form:
            if request.form[widget.objectName()] == '0':
                qtApplication.qtForm.move_top_left(widget)
            elif request.form[widget.objectName()] == '1':
                qtApplication.qtForm.move_top_right(widget)
            elif request.form[widget.objectName()] == '2':
                qtApplication.qtForm.move_bottom_left(widget)
            elif request.form[widget.objectName()] == '3':
                qtApplication.qtForm.move_bottom_right(widget)
            elif request.form[widget.objectName()] == '4':
                qtApplication.qtForm.toggle_visibility(widget)

    return redirect('/')



class Application():
    def __init__(self):
        self.qtApp = QApplication(sys.argv)
        self.qtForm = SmartMirrorForm()
        self.setup_timers()
        self.qtForm.move_top_right(self.qtForm.timeWidget)
        # self.qtForm.move_top_right(self.qtForm.weatherWidget)
        self.qtForm.move_bottom_right(self.qtForm.newsWidget)
    
    def setup_timers(self):
        self.timeWidgetTimer = QTimer()
        self.timeWidgetTimer.timeout.connect(lambda: self.update_time_widget())
        self.timeWidgetTimer.start(500)

        self.newsapi = NewsApiClient(api_key=NEWSAPI_KEY)
        self.update_news_widget()
        self.newsWeatherTimer = QTimer()
        self.newsWeatherTimer.timeout.connect(lambda: self.update_news_widget())
        self.newsWeatherTimer.start(180000)

        self.update_weather_widget()
        self.weatherWidgetTimer = QTimer()
        self.weatherWidgetTimer.timeout.connect(lambda: self.update_weather_widget())
        self.weatherWidgetTimer.start(60000)


    def run_app(self):
        self.qtApp.exec_()

    def update_time_widget(self):
        curTime = time.strftime("%H:%M:%S")
        self.qtForm.timeLabel.setText(curTime)
        curDay = time.strftime("%a, %d %b")
        self.qtForm.dayLabel.setText(curDay)

    def update_news_widget(self):
        newsWidgetElements = [[self.qtForm.newsItem1Header],
                    [self.qtForm.newsItem2Header],
                    [self.qtForm.newsItem3Header],
                    [self.qtForm.newsItem4Header],
                    [self.qtForm.newsItem5Header]]

        topHeadlines = self.newsapi.get_top_headlines(sources='bbc-news')
        self.qtForm.newsHeader.setText("BBC News")

        i = 0
        for iter in newsWidgetElements:
            iter[0].setText(topHeadlines["articles"][i]["title"])
            i = i + 1

    def update_weather_widget(self):
        param = {"APPID": WEATHERAPI_KEY, "q":WEATHERAPI_LOCATION, "mode":"json"}
        weatherRequest = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=param)
        weatherWidgetElements = [[self.qtForm.forecast1WeatherTitle, self.qtForm.forecast1WeatherIcon, self.qtForm.forecast1WeatherTemp],
                            [self.qtForm.forecast2WeatherTitle, self.qtForm.forecast2WeatherIcon, self.qtForm.forecast2WeatherTemp],
                            [self.qtForm.forecast3WeatherTitle, self.qtForm.forecast3WeatherIcon, self.qtForm.forecast3WeatherTemp],
                            [self.qtForm.forecast4WeatherTitle, self.qtForm.forecast4WeatherIcon, self.qtForm.forecast4WeatherTemp],
                            [self.qtForm.forecast5WeatherTitle, self.qtForm.forecast5WeatherIcon, self.qtForm.forecast5WeatherTemp]]
        weatherDict = weatherRequest.json()
        for iter in range(len(weatherWidgetElements)):
            forecastDayTime = weatherDict["list"][iter]
            forecastTime = datetime.utcfromtimestamp(forecastDayTime["dt"]).strftime('%a@%H')
            weatherWidgetElements[iter][0].setText(forecastTime)

            weatherImageFilename = forecastDayTime["weather"][0]["icon"] + ".png"
            weatherPixmap = QPixmap("MirrorFiles/WeatherIcons/%s" % weatherImageFilename).scaled(90, 90, Qt.KeepAspectRatio)
            
            weatherWidgetElements[iter][1].setPixmap(weatherPixmap)

            temperatureText = "%s / %s" % (str(round(forecastDayTime["main"]["temp_max"] - 273.15)), str(round(forecastDayTime["main"]["temp_min"] - 273.15)))
            weatherWidgetElements[iter][2].setText(temperatureText)

def run_flask():
    FLASK_APP.run(host='0.0.0.0', port=80, debug=False, use_reloader=False)

if __name__ == '__main__':
    threading._start_new_thread(run_flask, ())
    qtApplication = Application()
    qtApplication.run_app()