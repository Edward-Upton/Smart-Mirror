import requests
import json
from datetime import datetime
from PIL import Image
param = {"APPID":"49831b5dbeb1aa231811dcfb0de29888", "q":"Newcastle Emlyn", "mode":"json"}

weatherRequest = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=param)

with open("weatherTempData.json", "w") as f:
    f.write(json.dumps(weatherRequest.json()))
    weatherDict = weatherRequest.json()
forecastList = weatherDict["list"]

for forecast in forecastList:
    print(datetime.utcfromtimestamp(forecast["dt"]).strftime('%a-%d-Hour:%H'))
    print(round(forecast["main"]["temp"] - 273.15))
    print(forecast["weather"][0]["main"])
    with open("MirrorFiles/WeatherIcons/" + forecast["weather"][0]["icon"] + ".png", "rb") as iconFile:
        icon = Image.open(iconFile)
        icon.show()
