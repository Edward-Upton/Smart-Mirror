import requests
import json

param = {"APPID":"49831b5dbeb1aa231811dcfb0de29888", "q":"Newcastle Emlyn", "mode":"json"}

weatherRequest = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=param)

with open("weatherTempData.json", "w") as f:
    f.write(json.dumps(weatherRequest.json()))